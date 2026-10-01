from flask import Flask, render_template, request, jsonify
from audio_processing import speech_to_text, extract_audio_features
from text_analysis import analyze_text
from scoring import calculate_scores
from explainability import generate_report
from adaptive_engine import get_next_question
from question_bank import QUESTION_BANK
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.units import cm
import io
import os
import uuid
import json
from datetime import datetime

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

AUDIO_DIR    = "../data/audio_samples"
HISTORY_FILE = "../data/session_history.json"
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs("../data", exist_ok=True)

interview_data        = []
latest_audio_path     = None
current_expected_answer = None
asked_questions       = set()
expected_answers      = {}           # maps question string -> expected answer


# =====================================================
# SESSION HISTORY HELPERS
# =====================================================
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(session):
    history = load_history()
    history.append(session)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


# =====================================================
# GET QUESTION
# =====================================================
@app.route("/get_question", methods=["POST"])
def get_question_route():
    global current_expected_answer

    data = request.get_json()
    domain = data.get("domain")
    q_type = data.get("type", "theory")
    current_level = data.get("current_level", "easy")

    if not domain:
        return jsonify({"error": "Domain not provided"}), 400

    result = get_next_question(domain, 60, current_level, q_type, asked=asked_questions)
    q_str = result.get("question", "")
    current_expected_answer = result.get("expected_answer")
    expected_answers[q_str] = result.get("expected_answer", "")
    asked_questions.add(q_str)

    return jsonify(result)


# =====================================================
# AUDIO UPLOAD
# =====================================================
@app.route("/upload_audio", methods=["POST"])
def upload_audio():
    global latest_audio_path

    audio = request.files.get("audio")
    if not audio:
        return jsonify({"error": "No audio uploaded"}), 400

    filename = f"{uuid.uuid4()}.wav"
    path = os.path.join(AUDIO_DIR, filename)
    audio.save(path)

    latest_audio_path = path
    return jsonify({"status": "audio saved"})


# =====================================================
# ANALYZE ANSWER
# =====================================================
@app.route("/analyze", methods=["POST"])
def analyze():
    global latest_audio_path
    global current_expected_answer

    if not latest_audio_path:
        return jsonify({"error": "No audio recorded"}), 400

    transcript     = speech_to_text(latest_audio_path)
    audio_features = extract_audio_features(latest_audio_path)
    text_features  = analyze_text(transcript, current_expected_answer)

    scores      = calculate_scores(audio_features, text_features)
    safe_scores = {k: float(v) for k, v in scores.items()}

    interview_data.append({
        "transcript": transcript,
        "scores":     safe_scores
    })

    question_text   = request.form.get("question", "")
    looked_up       = expected_answers.get(question_text, current_expected_answer)
    report = generate_report(
        transcript, audio_features, text_features, safe_scores,
        expected_answer=looked_up
    )

    if isinstance(report, dict):
        overview              = report.get("overview", "Good attempt.")
        suggestions           = report.get("suggestions", [])
        expected_answer_hint  = report.get("expected_answer_hint", None)
    else:
        overview              = str(report)
        suggestions           = []
        expected_answer_hint  = None

    domain        = request.form.get("domain")
    q_type        = request.form.get("type", "theory")
    current_level = request.form.get("current_level", "easy")
    next_question = None

    if domain:
        next_question = get_next_question(
            domain,
            scores.get("overall", 60),
            current_level,
            q_type,
            asked=asked_questions
        )
        current_expected_answer = next_question.get("expected_answer")
        asked_questions.add(next_question.get("question", ""))

    return jsonify({
        "scores":               safe_scores,
        "transcript":           transcript,
        "overview":             overview,
        "suggestions":          suggestions,
        "expected_answer_hint": expected_answer_hint,
        "next_question":        next_question
    })


# =====================================================
# AUTOMATED CODING TEST CASE EVALUATION
# =====================================================
def _find_coding_question(domain, question_text):
    domain_data = QUESTION_BANK.get(domain, {})
    for level in ("easy", "medium", "hard"):
        for q in domain_data.get(level, {}).get("coding", []):
            if isinstance(q, dict) and q.get("question", "").lower() in question_text.lower():
                return q
    return None


def _run_auto_tests(func, test_cases):
    passed  = 0
    details = []
    for case in test_cases:
        inp      = case["input"]
        expected = case["expected"]
        try:
            output = func(*inp) if isinstance(inp, tuple) else func(inp)
            if expected is None:
                ok = True
            elif isinstance(expected, list):
                ok = (list(output) == expected)
            elif isinstance(expected, float):
                ok = abs(float(output) - expected) < 1e-6
            else:
                ok = (output == expected)
            if ok:
                passed += 1
            details.append({"input": str(inp), "expected": str(expected), "got": str(output), "passed": ok})
        except Exception as e:
            details.append({"input": str(inp), "expected": str(expected), "got": f"Error: {e}", "passed": False})
    return passed, len(test_cases), details


def _run_keyword_check(code, keywords):
    code_lower = code.lower()
    matched    = [kw for kw in keywords if kw.lower() in code_lower]
    return len(matched), len(keywords), matched


@app.route("/check_code", methods=["POST"])
def check_code():
    data          = request.get_json()
    domain        = data.get("domain", "").lower()
    question_text = data.get("question", "").lower()
    code          = data.get("code", "")

    q_def = _find_coding_question(domain, question_text)

    if not q_def:
        try:
            compile(code, "<string>", "exec")
            return jsonify({"score": 50, "result": "⚠ Question not found in bank. Code compiled without syntax errors.", "details": []})
        except SyntaxError as e:
            return jsonify({"score": 0, "result": f"❌ Syntax Error: {e}", "details": []})

    eval_type = q_def.get("eval_type", "manual")

    if eval_type == "manual":
        return jsonify({"score": 70, "result": "⚠ This question requires manual review (frontend/visual output).", "details": []})

    if eval_type == "keyword":
        keywords                    = q_def.get("keywords", [])
        matched_count, total, matched = _run_keyword_check(code, keywords)
        score  = round((matched_count / total) * 100, 2) if total else 50
        result = (f"✅ {matched_count}/{total} required keywords found: {matched}"
                  if matched_count == total else f"⚠ {matched_count}/{total} keywords found: {matched}")
        return jsonify({"score": score, "result": result, "details": []})

    if eval_type == "auto":
        test_cases = q_def.get("test_cases", [])
        if not test_cases:
            return jsonify({"score": 50, "result": "⚠ No test cases defined for this question.", "details": []})
        try:
            local_env = {}
            exec(code, {}, local_env)
            func = next((v for v in local_env.values() if callable(v)), None)
            if not func:
                return jsonify({"score": 0, "result": "❌ No function detected in submitted code.", "details": []})
            passed, total, details = _run_auto_tests(func, test_cases)
            score  = round((passed / total) * 100, 2)
            result = (f"✅ Passed {passed}/{total} test cases."
                      if passed == total else f"⚠ Passed {passed}/{total} test cases.")
            return jsonify({"score": score, "result": result, "details": details})
        except Exception as e:
            return jsonify({"score": 0, "result": f"❌ Runtime Error: {str(e)}", "details": []})

    return jsonify({"score": 0, "result": "❌ Unknown eval_type.", "details": []})


# =====================================================
# FINAL REPORT — saves session to history
# =====================================================
@app.route("/final_report")
def final_report():
    if not interview_data:
        return jsonify({"error": "No interview data"}), 400

    n = len(interview_data)

    avg_conf = sum(i["scores"].get("confidence",    0) for i in interview_data) / n
    avg_comm = sum(i["scores"].get("communication", 0) for i in interview_data) / n
    avg_flu  = sum(i["scores"].get("fluency",       0) for i in interview_data) / n
    avg_tech = sum(i["scores"].get("technical",     0) for i in interview_data) / n

    final_score = round((avg_conf + avg_comm + avg_flu + avg_tech) / 4, 2)

    if final_score >= 80:
        level = "Excellent"
    elif final_score >= 65:
        level = "Good"
    elif final_score >= 50:
        level = "Average"
    else:
        level = "Needs Improvement"

    result = {
        "questions_answered": n,
        "avg_confidence":     round(avg_conf, 2),
        "avg_communication":  round(avg_comm, 2),
        "avg_fluency":        round(avg_flu,  2),
        "avg_technical":      round(avg_tech, 2),
        "final_score":        final_score,
        "level":              level
    }

    # Save to history file
    save_history({
        "date":               datetime.now().strftime("%Y-%m-%d %H:%M"),
        "questions_answered": n,
        "avg_confidence":     round(avg_conf, 2),
        "avg_communication":  round(avg_comm, 2),
        "avg_fluency":        round(avg_flu,  2),
        "avg_technical":      round(avg_tech, 2),
        "final_score":        final_score,
        "level":              level
    })

    return jsonify(result)


# =====================================================
# SESSION HISTORY — returns all past sessions
# =====================================================
@app.route("/history")
def history():
    return jsonify(load_history())


# =====================================================
# RESET
# =====================================================
@app.route("/reset", methods=["POST"])
def reset():
    interview_data.clear()
    asked_questions.clear()
    expected_answers.clear()
    global latest_audio_path
    latest_audio_path = None
    return jsonify({"status": "reset successful"})

@app.route("/download_report")
def download_report():
    if not interview_data:
        return jsonify({"error": "No session data"}), 400

    scores_list   = [d.get("scores", {})   for d in interview_data]
    transcripts   = [d.get("transcript", "") for d in interview_data]
    suggestions   = [d.get("suggestions", []) for d in interview_data]

    avg_conf  = sum(s.get("confidence",    0) for s in scores_list) / max(len(scores_list), 1)
    avg_comm  = sum(s.get("communication", 0) for s in scores_list) / max(len(scores_list), 1)
    avg_flu   = sum(s.get("fluency",       0) for s in scores_list) / max(len(scores_list), 1)
    avg_tech  = sum(s.get("technical",     0) for s in scores_list) / max(len(scores_list), 1)
    final     = round(0.30*avg_conf + 0.30*avg_comm + 0.25*avg_flu + 0.15*avg_tech, 1)

    buf = io.BytesIO()
    c   = pdf_canvas.Canvas(buf, pagesize=A4)
    W, H = A4

    def new_page():
        c.showPage()
        c.setFillColorRGB(0.008, 0.024, 0.09)
        c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── PAGE 1 ──
    c.setFillColorRGB(0.008, 0.024, 0.09)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Header bar
    c.setFillColorRGB(0.133, 0.773, 0.369)
    c.rect(0, H-70, W, 70, fill=1, stroke=0)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(2*cm, H-48, "HireLens")
    c.setFont("Helvetica", 13)
    c.drawString(2*cm, H-64, "AI Interview Simulator — Session Report")

    from datetime import datetime
    date_str = datetime.now().strftime("%d %b %Y, %I:%M %p")
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0.4, 0.9, 0.5)
    c.drawRightString(W-2*cm, H-30, date_str)

    # Final score big display
    c.setFillColorRGB(0.133, 0.773, 0.369)
    c.setFont("Helvetica-Bold", 72)
    c.drawCentredString(W/2, H-160, str(int(final)))
    c.setFont("Helvetica", 18)
    c.setFillColorRGB(0.6, 0.7, 0.8)
    c.drawCentredString(W/2, H-182, "Overall Score / 100")

    # Score boxes
    score_items = [
        ("Confidence",    avg_conf,  (0.133, 0.773, 0.369)),
        ("Communication", avg_comm,  (0.231, 0.510, 0.965)),
        ("Fluency",       avg_flu,   (0.961, 0.620, 0.043)),
        ("Technical",     avg_tech,  (0.659, 0.333, 0.969)),
    ]
    box_w = (W - 4*cm) / 4
    for i, (label, val, rgb) in enumerate(score_items):
        bx = 2*cm + i * box_w
        by = H - 280
        c.setFillColorRGB(0.051, 0.082, 0.149)
        c.roundRect(bx+4, by, box_w-8, 70, 6, fill=1, stroke=0)
        c.setFillColorRGB(*rgb)
        c.setFont("Helvetica-Bold", 26)
        c.drawCentredString(bx + box_w/2, by+38, str(int(val)))
        c.setFillColorRGB(0.6, 0.7, 0.8)
        c.setFont("Helvetica", 10)
        c.drawCentredString(bx + box_w/2, by+22, label)

    # Performance level
    if final >= 80:   level, rgb = "Excellent",          (0.133, 0.773, 0.369)
    elif final >= 65: level, rgb = "Good",               (0.231, 0.510, 0.965)
    elif final >= 50: level, rgb = "Average",            (0.961, 0.620, 0.043)
    else:             level, rgb = "Needs Improvement",  (0.937, 0.267, 0.267)

    c.setFillColorRGB(*rgb)
    c.roundRect(W/2 - 80, H-330, 160, 30, 8, fill=1, stroke=0)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(W/2, H-310, level)

    # Questions & Transcripts
    y = H - 375
    c.setFillColorRGB(0.133, 0.773, 0.369)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2*cm, y, f"Session Details  —  {len(interview_data)} Questions Answered")
    y -= 20

    for i, entry in enumerate(interview_data):
        if y < 100:
            new_page()
            y = H - 60

        q_scores = entry.get("scores", {})
        q_text   = entry.get("transcript", "No transcript")
        q_overall = q_scores.get("overall", 0)

        # Question header
        y -= 18
        c.setFillColorRGB(0.051, 0.082, 0.149)
        c.rect(2*cm, y-2, W-4*cm, 20, fill=1, stroke=0)
        c.setFillColorRGB(0.886, 0.910, 0.941)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(2.3*cm, y+4, f"Q{i+1}  —  Overall: {int(q_overall)}  |  Conf: {int(q_scores.get('confidence',0))}  |  Comm: {int(q_scores.get('communication',0))}  |  Fluency: {int(q_scores.get('fluency',0))}")
        y -= 8

        # Transcript snippet
        snippet = q_text[:220] + ("..." if len(q_text) > 220 else "")
        c.setFillColorRGB(0.58, 0.64, 0.73)
        c.setFont("Helvetica", 9)
        from reportlab.lib.utils import simpleSplit
        lines = simpleSplit(snippet, "Helvetica", 9, W - 5*cm)
        for line in lines[:3]:
            y -= 13
            if y < 80:
                new_page()
                y = H - 60
            c.drawString(2.3*cm, y, line)

        # Suggestions
        for sug in entry.get("suggestions", [])[:2]:
            y -= 13
            if y < 80:
                new_page()
                y = H - 60
            sug_lines = simpleSplit("→  " + sug, "Helvetica", 8.5, W - 5*cm)
            c.setFillColorRGB(0.4, 0.85, 0.5)
            c.setFont("Helvetica", 8.5)
            for sl in sug_lines[:2]:
                c.drawString(2.3*cm, y, sl)
                y -= 12

        y -= 6
        c.setStrokeColorRGB(0.12, 0.18, 0.28)
        c.line(2*cm, y, W-2*cm, y)

    # Footer
    c.setFillColorRGB(0.133, 0.773, 0.369)
    c.rect(0, 0, W, 28, fill=1, stroke=0)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 9)
    c.drawCentredString(W/2, 10, "Generated by HireLens AI Interview Simulator  —  MSIT New Delhi")

    c.save()
    buf.seek(0)

    from flask import send_file
    return send_file(
        buf,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=f"HireLens_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)