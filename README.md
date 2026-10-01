# HireLens — AI-Powered Interview Simulator

An AI-driven mock interview platform that simulates real technical interviews
across 9 computer science domains (DSA, DBMS, OS, Computer Networks, ML, OOP,
Web Development, System Design, HR), evaluates spoken answers with
speech-to-text (Faster-Whisper) and NLP scoring, and generates detailed PDF
performance reports.

**How it works:** pick a domain → get a question → answer by voice →
get transcribed, scored on content, confidence and fluency → download a
full PDF report.

**Stack:** Python · Flask · Faster-Whisper (Whisper tiny, CTranslate2) · librosa · scikit-learn (TF-IDF) · ReportLab · HTML/CSS/JS · Docker

Built by [Ojasvi Tanwar](https://github.com/OjasviTanwar) — B.Tech CSE,
MSIT New Delhi. Source:
[AI_Interview_Assessment](https://github.com/OjasviTanwar/AI_Interview_Assessment)
