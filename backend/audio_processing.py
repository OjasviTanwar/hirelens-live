import os
from faster_whisper import WhisperModel
import librosa
import numpy as np

# Whisper model size. "tiny" fits Render's free tier (512MB RAM) — the
# CTranslate2 engine uses far less memory than openai-whisper+torch.
# Override with WHISPER_MODEL=base (or larger) on hosts with more memory.
WHISPER_MODEL_NAME = os.environ.get("WHISPER_MODEL", "tiny")
model = WhisperModel(WHISPER_MODEL_NAME, device="cpu", compute_type="int8")


def speech_to_text(audio_path):
    # Decode with librosa (16kHz mono, like openai-whisper's load_audio) and
    # hand faster-whisper the raw array — this avoids its PyAV decode path,
    # which is broken with newer `av` releases (metadata_errors kwarg).
    y, _ = librosa.load(audio_path, sr=16000, mono=True)
    segments, _info = model.transcribe(y.astype("float32"), beam_size=5)
    return " ".join(segment.text for segment in segments).strip()


def extract_audio_features(audio_path):
    y, sr = librosa.load(audio_path)

    # =========================
    # BASIC AUDIO FEATURES
    # =========================
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    # librosa >= 0.10 returns tempo as a 1-element array, not a scalar
    tempo = float(np.atleast_1d(tempo)[0]) if np.size(tempo) else 0.0

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[pitches > 0]
    pitch_variation = np.std(pitch_values) if len(pitch_values) > 0 else 0

    # RMS energy — normalised so short/quiet recordings don't tank confidence
    rms_frames = librosa.feature.rms(y=y)[0]
    energy = float(np.mean(rms_frames))
    energy_std = float(np.std(rms_frames))   # stability: low std = steady voice

    # =========================
    # PAUSE ANALYSIS
    # top_db=25 catches natural breath pauses without being too sensitive
    # A pause is only counted if it is longer than 0.3 s (avoid mic noise)
    # =========================
    MIN_PAUSE_SEC = 0.3

    intervals = librosa.effects.split(y, top_db=25)

    total_samples  = len(y)
    total_duration = total_samples / sr

    total_speech_samples = sum((i[1] - i[0]) for i in intervals)
    speech_duration = total_speech_samples / sr

    pause_duration = total_duration - speech_duration
    pause_ratio    = pause_duration / max(total_duration, 1e-6)

    # Count only meaningful pauses (> MIN_PAUSE_SEC)
    pause_count = 0
    for i in range(len(intervals) - 1):
        gap_samples = intervals[i + 1][0] - intervals[i][1]
        if gap_samples / sr >= MIN_PAUSE_SEC:
            pause_count += 1

    # =========================
    # SPEECH RATE (WORDS PER MINUTE)
    # Use speech_duration (excludes silence) for accurate WPM
    # =========================
    transcript = speech_to_text(audio_path)
    word_count  = len(transcript.split())

    # WPM based on actual speaking time, not total recording length
    if speech_duration > 0:
        words_per_minute = (word_count / speech_duration) * 60
    elif total_duration > 0:
        words_per_minute = (word_count / total_duration) * 60
    else:
        words_per_minute = 0

    # Clamp to a sane range — whisper errors can give absurd values
    words_per_minute = float(np.clip(words_per_minute, 0, 350))

    # =========================
    # ARTICULATION RATE
    # How many syllables per second of actual speech (proxy for clarity)
    # rough syllable estimate: 1.4 syllables per word (English average)
    # =========================
    syllables_estimated = word_count * 1.4
    articulation_rate   = syllables_estimated / max(speech_duration, 1e-6)

    return {
        "tempo":             float(tempo),
        "pitch_variation":   float(pitch_variation),
        "energy":            float(energy),
        "energy_std":        float(energy_std),
        "pause_ratio":       float(pause_ratio),
        "pause_count":       int(pause_count),
        "pause_duration":    float(pause_duration),
        "speech_duration":   float(speech_duration),
        "total_duration":    float(total_duration),
        "words_per_minute":  float(words_per_minute),
        "articulation_rate": float(articulation_rate)
    }