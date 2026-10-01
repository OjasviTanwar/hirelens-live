import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# SENTENCE TRANSFORMER — lazy load
# Loads only on first analyze call, not at startup.
# Flask starts instantly regardless.
# Falls back to TF-IDF if not installed:
#   pip install sentence-transformers
# =========================
try:
    from sentence_transformers import SentenceTransformer as _ST
    _USE_TRANSFORMER = True
except ImportError:
    _USE_TRANSFORMER = False

_model = None  # loaded on first call, not at import time

def _get_model():
    global _model
    if _model is None and _USE_TRANSFORMER:
        _model = _ST("paraphrase-MiniLM-L3-v2")  # only 17MB
    return _model


# =========================
# SEMANTIC SIMILARITY
# =========================
def semantic_similarity(a, b):
    """
    Semantic similarity using sentence-transformers (paraphrase-MiniLM-L3-v2).
    Understands meaning — 'gradient descent minimizes loss' and
    'optimization reduces error' will score high.
    Falls back to TF-IDF cosine similarity if library not installed.
    """

    if not a or not b:
        return 0.0

    model = _get_model()

    if model is not None:
        embeddings = model.encode([a, b], convert_to_numpy=True)
        dot   = float(np.dot(embeddings[0], embeddings[1]))
        norm  = float(np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
        score = dot / norm if norm > 0 else 0.0
        return max(0.0, min(1.0, score))

    # TF-IDF fallback
    try:
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform([a, b])
        return float(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0])
    except Exception:
        return 0.0


def analyze_text(text, expected_answer=None):

    words = text.split()
    word_count = len(words)
    sentence_count = max(1, text.count(".") + text.count("?"))

    # =========================
    # AVERAGE SENTENCE LENGTH
    # =========================
    avg_sentence_length = word_count / sentence_count

    # =========================
    # ADVANCED FILLER DETECTION
    # =========================
    fillers = [
        "um", "uh", "like", "you know",
        "basically", "actually", "literally",
        "i mean", "sort of", "kind of"
    ]

    lower_text = text.lower()
    filler_count = sum(lower_text.count(f) for f in fillers)
    filler_ratio = filler_count / max(word_count, 1)

    # =========================
    # CLARITY SCORE (0-1)
    # =========================
    clarity = max(0.0, min(1.0, 1 - filler_ratio))

    # =========================
    # COMPLEXITY SCORE (0-1)
    # =========================
    complexity = min(1.0, avg_sentence_length / 20)

    # =========================
    # COHERENCE SCORE (Lexical Diversity)
    # =========================
    unique_words = len(set(words))
    lexical_diversity = unique_words / max(word_count, 1)
    coherence = min(1.0, lexical_diversity)

    # =========================
    # SEMANTIC SIMILARITY
    # =========================
    semantic_score = 0.0
    if expected_answer:
        semantic_score = semantic_similarity(text, expected_answer)

    return {
        # ORIGINAL REQUIRED FIELDS (DO NOT REMOVE)
        "words": words,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "clarity": clarity,
        "complexity": complexity,

        # NEW FEATURES
        "filler_count": filler_count,
        "filler_ratio": filler_ratio,
        "coherence": coherence,
        "semantic_score": semantic_score
    }