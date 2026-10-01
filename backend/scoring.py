def calculate_scores(audio_features, text_features):
    """
    Advanced Multimodal Weighted Scoring Model
    Combines:
    - Audio features
    - NLP features
    - Speech rate
    - Filler penalty
    - Semantic similarity
    """

    # =========================
    # -------- TEXT FEATURES --------
    # =========================
    clarity        = text_features.get("clarity", 0.5)
    complexity     = text_features.get("complexity", 0.5)
    coherence      = text_features.get("coherence", 0.5)
    semantic_score = text_features.get("semantic_score", 0.5)
    filler_ratio   = text_features.get("filler_ratio", 0.0)
    word_count     = text_features.get("word_count", 0)

    # =========================
    # -------- AUDIO FEATURES --------
    # =========================
    energy            = audio_features.get("energy", 0.05)
    energy_std        = audio_features.get("energy_std", 0.01)
    pause_ratio       = audio_features.get("pause_ratio", 0.4)
    pause_count       = audio_features.get("pause_count", 0)
    words_per_minute  = audio_features.get("words_per_minute", 120)
    speech_duration   = audio_features.get("speech_duration", 0)
    total_duration    = audio_features.get("total_duration", 1)
    articulation_rate = audio_features.get("articulation_rate", 3.5)

    # =========================
    # CONFIDENCE SCORE
    # Widened energy range from (0.01-0.12) to (0.005-0.08)
    # Most laptop/headset mics record at RMS 0.02-0.05 which was
    # scoring near the bottom of the old range even for loud speakers.
    # Added +15 calibration shift and floor of 20.
    # Steadiness weight reduced to 0.35 so low-energy speakers
    # are not double-penalised.
    # =========================
    energy_norm = min(1.0, max(0.0, (energy - 0.005) / (0.08 - 0.005)))

    # Steadiness: lower std relative to mean = more steady voice
    if energy > 0:
        steadiness = max(0.0, 1.0 - min(1.0, energy_std / energy))
    else:
        steadiness = 0.5

    # Raw confidence from audio signals
    confidence_raw = (0.65 * energy_norm + 0.35 * steadiness) * 100

    # +15 calibration shift brings average confident speech to 60-75
    # Floor at 20, cap at 95
    confidence = min(95, max(20, confidence_raw + 15))

    # =========================
    # COMMUNICATION SCORE
    # Reduced semantic_score weight from 0.30 to 0.15 because
    # TF-IDF cosine similarity punishes correct answers that use
    # different wording than the expected answer.
    # Added word_count_norm at 0.15 — longer answers score better.
    # +10 calibration shift, floor at 25.
    # =========================
    word_count_norm = min(1.0, word_count / 80)   # 80+ words = full score

    communication_raw = (
        0.40 * clarity +
        0.30 * coherence +
        0.15 * semantic_score +
        0.15 * word_count_norm
    )

    communication = min(100, max(25, communication_raw * 100 + 10))

    # =========================
    # FLUENCY SCORE
    # WPM: ideal range 120-170. Penalise both too slow and too fast.
    # Pause ratio: threshold tightened from 30% to 20% — natural
    # fluent speech has 15-20% pause ratio not 30%.
    # Pause count: threshold tightened from 8/min to 6/min.
    # Filler penalty multiplier raised from 3 to 5 — 10% filler
    # words should hurt noticeably not be almost ignored.
    # Articulation rate: normal English speech is 3.5-5.5 syllables/sec.
    # =========================

    # WPM score
    if 120 <= words_per_minute <= 170:
        wpm_score = 1.0
    elif words_per_minute < 120:
        wpm_score = max(0.0, words_per_minute / 120)
    else:
        wpm_score = max(0.0, 1.0 - (words_per_minute - 170) / 100)

    # Pause ratio score
    # Up to 20% pause is natural and gets full score
    # 20-40% pause gets linearly penalised
    # Above 40% gets heavily penalised
    if pause_ratio <= 0.25:
        pause_score = 1.0
    elif pause_ratio <= 0.40:
        pause_score = max(0.0, 1.0 - (pause_ratio - 0.20) / 0.40)
    else:
        pause_score = max(0.0, 0.5 - (pause_ratio - 0.40) / 0.40)

    # Pause count per minute of speech — more than 6/min = hesitant
    pauses_per_min = (pause_count / max(speech_duration, 1)) * 60
    if pauses_per_min <= 6:
        pause_freq_score = 1.0
    else:
        pause_freq_score = max(0.0, 1.0 - (pauses_per_min - 6) / 15)

    # Filler penalty — raised multiplier from 3 to 5
    # 20% filler words now gives 0 penalty score (was 33% before)
    filler_penalty = max(0.0, 1.0 - filler_ratio * 5)

    # Articulation rate score (3.5-5.5 syllables/sec is natural)
    if 3.5 <= articulation_rate <= 5.5:
        artic_score = 1.0
    else:
        artic_score = max(0.0, 1.0 - abs(articulation_rate - 4.5) / 4.5)

    fluency_raw = (
        0.30 * pause_score +
        0.25 * wpm_score +
        0.20 * filler_penalty +
        0.15 * pause_freq_score +
        0.10 * artic_score
    )
    fluency = min(100, max(0, fluency_raw * 100))

    # =========================
    # TECHNICAL DEPTH SCORE
    # Based on complexity + semantic similarity + word count depth
    # =========================
    depth_bonus = min(1.0, word_count / 150)

    technical = min(100, max(0, (
        0.40 * complexity +
        0.40 * semantic_score +
        0.20 * depth_bonus
    ) * 100))

    # =========================
    # MULTIMODAL WEIGHTED OVERALL SCORE
    # =========================
    overall = round(
        (0.30 * confidence) +
        (0.30 * communication) +
        (0.25 * fluency) +
        (0.15 * technical),
        2
    )

    return {
        "confidence":    float(round(confidence, 2)),
        "communication": float(round(communication, 2)),
        "fluency":       float(round(fluency, 2)),
        "technical":     float(round(technical, 2)),
        "overall":       float(overall),

        # Compatibility fields
        "clarity":           float(clarity),
        "complexity":        float(complexity),
        "semantic_score":    float(semantic_score),
        "word_count":        int(word_count),
        "words_per_minute":  float(round(words_per_minute, 2)),
        "pause_count":       int(pause_count)
    }

