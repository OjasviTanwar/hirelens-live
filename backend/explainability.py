def generate_report(text, audio_features, text_features, scores, expected_answer=None):

    observations = []
    suggestions   = []

    # ---------- CONFIDENCE ----------
    if scores["confidence"] < 50:
        observations.append("Low vocal energy detected")
        suggestions.append("Practice speaking louder with a steady and confident pace")
    elif scores["confidence"] <= 75:
        observations.append("Moderate confidence level")
        suggestions.append("Improve voice projection and reduce hesitation")
    else:
        observations.append("Strong vocal confidence detected")
        suggestions.append("Maintain this confident speaking style")

    # ---------- FLUENCY ----------
    if scores["fluency"] < 50:
        observations.append("Frequent pauses and hesitation detected")
        suggestions.append("Reduce long pauses and filler words")
    elif scores["fluency"] <= 75:
        observations.append("Fairly fluent speech")
        suggestions.append("Work on smoother transitions between ideas")
    else:
        observations.append("Excellent speech fluency")
        suggestions.append("Keep maintaining this natural flow")

    # ---------- COMMUNICATION ----------
    if scores["communication"] < 50:
        observations.append("Ideas lack clear structure")
        suggestions.append("Use structured answers like STAR or point-based responses")
    elif scores["communication"] <= 75:
        observations.append("Communication is understandable but can improve")
        suggestions.append("Focus on clearer openings and concise conclusions")
    else:
        observations.append("Clear and effective communication")
        suggestions.append("Maintain this clarity in future interviews")

    # ---------- TEXT CLARITY ----------
    if text_features.get("clarity", 1) < 0.5:
        observations.append("Frequent filler words detected")
        suggestions.append("Avoid fillers like um, uh, basically, you know")

    # ---------- SEMANTIC SCORE (answer correctness) ----------
    semantic_score = text_features.get("semantic_score", 0)

    if semantic_score < 0.30:
        observations.append("Your answer did not match the expected concepts closely")
        suggestions.append("Study the core concepts for this topic before your next attempt")
    elif semantic_score < 0.55:
        observations.append("Your answer partially covered the expected concepts")
        suggestions.append("Try to include more key technical terms and complete explanations")
    else:
        observations.append("Your answer covered the expected concepts well")

    # ---------- EXPECTED ANSWER HINT ----------
    # Show model answer when overall score is below 60 or semantic score is low
    expected_answer_hint = None
    if expected_answer and (scores.get("overall", 100) < 60 or semantic_score < 0.40):
        expected_answer_hint = expected_answer

    # ---------- OVERALL FEEDBACK ----------
    overall = scores["overall"]

    if overall < 50:
        suggestions.append("Practice mock interviews regularly to improve overall performance")
    elif overall <= 75:
        suggestions.append("You are close to interview-ready — refine weaker areas")
    else:
        suggestions.append("Excellent interview performance — keep practicing")

    # ---------- OVERVIEW SUMMARY ----------
    if overall < 50:
        overview = "Your performance needs improvement. Focus on clarity and confidence."
    elif overall <= 75:
        overview = "Good performance overall, but there are areas that can be refined."
    else:
        overview = "Great performance."

    return {
        "overview":               overview,
        "observations":           observations,
        "suggestions":            suggestions,
        "expected_answer_hint":   expected_answer_hint
    }