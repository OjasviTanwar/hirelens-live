# adaptive_engine.py

import random
from question_bank import QUESTION_BANK


def get_next_difficulty(score, current_level):
    """
    Adaptive difficulty logic
    """

    if score > 75:
        if current_level == "easy":
            return "medium"
        elif current_level == "medium":
            return "hard"
        else:
            return "hard"

    elif score < 50:
        if current_level == "hard":
            return "medium"
        elif current_level == "medium":
            return "easy"
        else:
            return "easy"

    return current_level


def get_next_question(domain, score=60, current_level="easy", q_type="theory", asked=None):
    """
    Select next question based on:
    - Domain
    - Performance score
    - Current difficulty
    - Question type (theory/coding)
    - asked: set of question strings already shown to user
    """

    if asked is None:
        asked = set()

    # Validate domain
    if domain not in QUESTION_BANK:
        return {
            "difficulty": "easy",
            "question": "Invalid domain selected.",
            "expected_answer": ""
        }

    # Decide difficulty
    next_level = get_next_difficulty(score, current_level)

    # Try next_level first, then fall back to other levels if exhausted
    levels_to_try = [next_level] + [l for l in ("easy", "medium", "hard") if l != next_level]

    for level in levels_to_try:
        questions = QUESTION_BANK[domain].get(level, {}).get(q_type, [])

        # Build available list excluding already asked
        available = []
        for item in questions:
            q_str = item.get("question", "") if isinstance(item, dict) else item
            if q_str not in asked:
                available.append(item)

        if available:
            item = random.choice(available)
            if isinstance(item, dict):
                return {
                    "difficulty": level,
                    "question": item.get("question", ""),
                    "expected_answer": item.get("expected_answer", "")
                }
            return {
                "difficulty": level,
                "question": item,
                "expected_answer": ""
            }

    # All questions exhausted across all levels
    return {
        "difficulty": next_level,
        "question": "All questions completed for this domain.",
        "expected_answer": ""
    }