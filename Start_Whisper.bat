@echo off
title Whisper Transcription Studio

cd /d D:\Whisper-Transcription

call .venv\Scripts\activate.bat

set MAX_UPLOAD_MB=2000
set MAX_MINUTES=100000

start "" http://localhost:8501

streamlit run app.py --server.headless true

pause