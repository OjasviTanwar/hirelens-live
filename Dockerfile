# HireLens deployment — Render (Docker runtime, free tier)
FROM python:3.11-slim

# ffmpeg is required by librosa for audio decoding
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first (better layer caching).
# NOTE: no torch — faster-whisper runs on CTranslate2, which is why this
# fits Render's free 512MB tier.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

# Application code (audio samples intentionally excluded — uploaded by users at runtime)
COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY data/ ./data/

# Pre-download the Whisper tiny model at build time so the first
# interview transcription doesn't pay the download cost on cold start
RUN python -c "from faster_whisper import WhisperModel; WhisperModel('tiny', device='cpu', compute_type='int8')"

# app.py uses paths relative to backend/ (../frontend, ../data)
WORKDIR /app/backend

# Render injects $PORT (defaults to 10000). Single worker keeps RAM low;
# threads share the one loaded Whisper model. Generous timeout since
# transcription of longer answers takes a while on the free tier's CPU.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-10000} --workers 1 --threads 4 --timeout 300 app:app"]
