import os
import json
import tempfile
import subprocess
import threading
from pathlib import Path

import streamlit as st
from faster_whisper import WhisperModel

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Whisper Transcription Studio",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "100"))
MAX_MINUTES = int(os.getenv("MAX_MINUTES", "15"))

MODEL_LOCK = threading.Lock()

# --------------------------------------------------
# ANIMATED NEON UI
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #28105d 0%, transparent 35%),
        radial-gradient(ellipse at 90% 20%, #071e59 0%, transparent 35%),
        radial-gradient(ellipse at 50% 100%, #250b55 0%, transparent 45%),
        #050b22;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: rgba(5, 11, 34, 0.8);
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Animated background glow */

.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: -50%;
    width: 200%;
    height: 100%;
    pointer-events: none;
    background: linear-gradient(
        115deg,
        transparent 35%,
        rgba(125, 35, 255, 0.07),
        rgba(0, 210, 255, 0.07),
        transparent 65%
    );
    animation: backgroundMove 12s linear infinite;
    z-index: 0;
}

@keyframes backgroundMove {
    0% { transform: translateX(-15%); }
    100% { transform: translateX(15%); }
}

@keyframes glowPulse {
    0%, 100% {
        box-shadow: 0 0 12px rgba(139, 52, 255, 0.25);
    }
    50% {
        box-shadow: 0 0 28px rgba(0, 210, 255, 0.4);
    }
}

@keyframes waveMove {
    0%, 100% { transform: scaleY(0.65); }
    50% { transform: scaleY(1.25); }
}

/* Main heading */

.hero-title {
    text-align: center;
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 8px;
    background: linear-gradient(
        90deg,
        #ffffff,
        #bd8aff,
        #00e5ff,
        #ffffff
    );
    background-size: 250% auto;
    color: transparent;
    -webkit-background-clip: text;
    animation: titleGradient 6s linear infinite;
}

@keyframes titleGradient {
    to { background-position: 250% center; }
}

.hero-subtitle {
    text-align: center;
    color: #c5d7ff;
    font-size: 16px;
    margin-bottom: 8px;
}

.creator-card {
    border: 1px solid #9b48ff;
    border-radius: 16px;
    padding: 14px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(74, 30, 150, 0.35),
        rgba(0, 190, 255, 0.12)
    );
    box-shadow: 0 0 20px rgba(145, 48, 255, 0.2);
}

.creator-name {
    color: #ffd34e;
    font-size: 18px;
    font-weight: 800;
}

.creator-role {
    color: #d8b5ff;
    font-size: 13px;
    font-weight: 600;
}

/* Feature badges */

.feature {
    text-align: center;
    padding: 12px 8px;
    border: 1px solid rgba(125, 105, 255, 0.7);
    border-radius: 25px;
    background: rgba(25, 40, 90, 0.75);
    color: #ffffff;
    font-weight: 700;
    font-size: 13px;
    animation: glowPulse 4s infinite;
}

/* Main glass panels */

.glass-panel {
    background: linear-gradient(
        145deg,
        rgba(31, 48, 105, 0.92),
        rgba(12, 22, 59, 0.94)
    );
    border: 1px solid rgba(116, 111, 255, 0.75);
    border-radius: 22px;
    padding: 22px;
    box-shadow:
        0 0 25px rgba(88, 49, 255, 0.22),
        inset 0 0 20px rgba(80, 140, 255, 0.05);
}

.section-heading {
    color: #43eaff;
    font-size: 23px;
    font-weight: 800;
    border-bottom: 2px solid #4b66ff;
    padding-bottom: 12px;
    margin-bottom: 15px;
}

.panel-heading {
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
    margin-bottom: 18px;
}

.format-card {
    background: linear-gradient(
        120deg,
        rgba(85, 67, 180, 0.48),
        rgba(22, 53, 110, 0.8)
    );
    border: 1px solid rgba(118, 125, 255, 0.6);
    border-radius: 13px;
    padding: 13px;
    margin-bottom: 12px;
    color: white;
    font-weight: 700;
}

.format-description {
    color: #c6d4ff;
    font-size: 12px;
    font-weight: 400;
}

/* File uploader */

[data-testid="stFileUploaderDropzone"] {
    background: rgba(31, 44, 99, 0.75);
    border: 2px dashed #42dcff;
    border-radius: 17px;
    min-height: 150px;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #c17aff;
    box-shadow: 0 0 22px rgba(0, 210, 255, 0.25);
}

/* Select boxes */

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(36, 51, 105, 0.95);
    border: 1px solid #6779db;
    border-radius: 12px;
    color: white;
}

/* Buttons */

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(
        100deg,
        #a22bff,
        #405dff,
        #00c9e8
    );
    color: white;
    border: 0;
    border-radius: 30px;
    font-weight: 800;
    min-height: 45px;
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 25px rgba(0, 210, 255, 0.55);
    border: 1px solid #ffffff;
    color: white;
}

/* Labels and text */

label, p, li {
    color: #e4eaff !important;
}

[data-testid="stMetric"] {
    background: rgba(31, 49, 105, 0.7);
    border: 1px solid #5969c7;
    padding: 12px;
    border-radius: 12px;
}

.stTextArea textarea {
    background: #0d183c;
    color: #ffffff;
    border: 1px solid #6379dc;
    border-radius: 12px;
}

/* Footer */

.footer {
    text-align: center;
    border: 1px solid #9348ff;
    border-radius: 30px;
    padding: 13px;
    margin-top: 28px;
    background: rgba(37, 24, 83, 0.8);
    color: #e4eaff;
    font-size: 13px;
}

.footer span {
    color: #ffd34e;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# MODEL
# --------------------------------------------------

@st.cache_resource
def load_model(model_name):
    return WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8"
    )


# --------------------------------------------------
# AUDIO CONVERSION
# --------------------------------------------------

def convert_media(input_path, output_path):

    command = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-c:a", "pcm_s16le",
        str(output_path)
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr[-2000:])


def get_duration(audio_path):

    command = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(audio_path)
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    try:
        return float(result.stdout.strip())
    except ValueError:
        return None


# --------------------------------------------------
# TRANSCRIPT FORMATTING
# --------------------------------------------------

def timestamp(seconds, separator=","):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60

    return (
        f"{hours:02}:{minutes:02}:"
        f"{secs:06.3f}".replace(".", separator)
    )


def create_outputs(segments):

    plain_text = []
    srt = []
    vtt = ["WEBVTT\n"]
    json_segments = []

    for index, segment in enumerate(segments, start=1):

        text = segment.text.strip()
        plain_text.append(text)

        srt.append(
            f"{index}\n"
            f"{timestamp(segment.start, ',')} --> "
            f"{timestamp(segment.end, ',')}\n"
            f"{text}\n"
        )

        vtt.append(
            f"{timestamp(segment.start, '.')} --> "
            f"{timestamp(segment.end, '.')}\n"
            f"{text}\n"
        )

        json_segments.append({
            "start": segment.start,
            "end": segment.end,
            "text": text
        })

    return {
        "txt": "\n".join(plain_text),
        "srt": "\n".join(srt),
        "vtt": "\n".join(vtt),
        "json": json_segments
    }


# --------------------------------------------------
# HEADER
# --------------------------------------------------

header_left, header_center, header_right = st.columns(
    [1.1, 4.5, 1.5]
)

with header_center:

    st.markdown(
        '<div class="hero-title">🎙️ Whisper Transcription Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        '🎬 Video & Audio → 📝 Accurate Text '
        '(Tamil | English | Multilingual)'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Free AI-powered transcription using Whisper (Faster-Whisper)'
        '</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.markdown(
        '<div class="creator-card">'
        '<div>🚀 App created by</div>'
        '<div class="creator-name">Kalyanasundar</div>'
        '<div class="creator-role">Gen/AI Developer</div>'
        '</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# FEATURE BADGES
# --------------------------------------------------

st.write("")

features = st.columns(5)

feature_labels = [
    "⚡ Fast & Free",
    "🎯 High Accuracy",
    "🌐 Multi-language",
    "📥 Multiple Formats",
    "🛡️ No API Cost"
]

for column, label in zip(features, feature_labels):
    with column:
        st.markdown(
            f'<div class="feature">{label}</div>',
            unsafe_allow_html=True
        )

st.write("")


# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------

left_panel, main_panel, right_panel = st.columns(
    [1.05, 4.2, 1.25],
    gap="medium"
)


# LEFT NAVIGATION

with left_panel:

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

    st.markdown(
        '<div class="panel-heading">⚡ MENU</div>',
        unsafe_allow_html=True
    )

    st.markdown("🏠 **Transcribe**")
    st.divider()
    st.markdown("ℹ️ **How It Works**")

    with st.expander("Steps"):
        st.write("1. Upload a video or audio file.")
        st.write("2. Select the language.")
        st.write("3. Choose a Whisper model.")
        st.write("4. Start transcription.")
        st.write("5. Download your transcript.")

    st.divider()
    st.markdown("⚙️ **Settings**")

    with st.expander("Upload limits"):
        st.write(f"Maximum file size: {MAX_UPLOAD_MB} MB")
        st.write(f"Maximum duration: {MAX_MINUTES} minutes")

    st.divider()
    st.markdown("👨‍💻 **About**")

    with st.expander("Developer"):
        st.write("Created by Kalyanasundar")
        st.write("Gen/AI Developer")
        st.write("Powered by Faster-Whisper.")

    st.markdown('</div>', unsafe_allow_html=True)


# MAIN TRANSCRIPTION PANEL

with main_panel:

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">'
        '🎬 Transcribe Video or Audio'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Upload your media, choose language and model, "
        "and generate your transcript."
    )

    uploaded_file = st.file_uploader(
        "📤 Drag and drop your video or audio here",
        type=[
            "mp4", "mkv", "mov", "avi", "webm",
            "mp3", "wav", "m4a", "aac", "flac", "ogg"
        ],
        help=f"Maximum upload size: {MAX_UPLOAD_MB} MB"
    )

    language_col, model_col = st.columns(2)

    with language_col:

        language_choice = st.selectbox(
            "🌐 Transcription Language",
            [
                "Auto detect",
                "Tamil",
                "English",
                "Hindi",
                "Malayalam",
                "Telugu"
            ]
        )

    with model_col:

        model_choice = st.selectbox(
            "🧠 Whisper Model",
            ["tiny", "base", "small"],
            help="Tiny is fastest. Small may be more accurate but needs more memory."
        )

    st.write("")

    start_button = st.button(
        "🚀 Start Transcription ✨",
        type="primary",
        use_container_width=True
    )

    if uploaded_file:

        file_size_mb = len(uploaded_file.getvalue()) / (1024 * 1024)

        st.caption(
            f"Selected: {uploaded_file.name} | "
            f"File size: {file_size_mb:.2f} MB"
        )

    if start_button:

        if uploaded_file is None:
            st.warning("Please upload a video or audio file first.")

        elif file_size_mb > MAX_UPLOAD_MB:
            st.error(
                f"File exceeds the {MAX_UPLOAD_MB} MB upload limit."
            )

        else:

            with tempfile.TemporaryDirectory() as temp_dir:

                temp_dir = Path(temp_dir)

                suffix = Path(uploaded_file.name).suffix

                input_path = temp_dir / ("input" + suffix)
                audio_path = temp_dir / "converted.wav"

                input_path.write_bytes(uploaded_file.getvalue())

                progress = st.progress(0)
                status = st.empty()

                try:

                    status.info("🔄 Converting video/audio...")
                    convert_media(input_path, audio_path)
                    progress.progress(20)

                    duration = get_duration(audio_path)

                    if duration is not None:

                        duration_minutes = duration / 60

                        st.write(
                            f"⏱️ Media duration: "
                            f"{duration_minutes:.2f} minutes"
                        )

                        if duration_minutes > MAX_MINUTES:
                            st.error(
                                f"Maximum duration is "
                                f"{MAX_MINUTES} minutes."
                            )
                            st.stop()

                    status.info("🧠 Loading Whisper AI model...")
                    model = load_model(model_choice)
                    progress.progress(35)

                    language_codes = {
                        "Auto detect": None,
                        "Tamil": "ta",
                        "English": "en",
                        "Hindi": "hi",
                        "Malayalam": "ml",
                        "Telugu": "te"
                    }

                    selected_language = language_codes[
                        language_choice
                    ]

                    status.info("🎙️ Transcribing your media...")

                    with MODEL_LOCK:

                        segments_generator, info = model.transcribe(
                            str(audio_path),
                            language=selected_language,
                            beam_size=1,
                            vad_filter=True
                        )

                        segments = list(segments_generator)

                    progress.progress(90)

                    outputs = create_outputs(segments)

                    progress.progress(100)
                    status.success("✅ Transcription completed!")

                    st.success(
                        f"Detected language: {info.language} | "
                        f"Confidence: {info.language_probability:.2%}"
                    )

                    st.markdown("### 📝 Transcription Results")

                    st.text_area(
                        "Your transcript",
                        outputs["txt"],
                        height=280
                    )

                    base_name = Path(uploaded_file.name).stem

                    download_columns = st.columns(4)

                    with download_columns[0]:
                        st.download_button(
                            "📄 TXT",
                            outputs["txt"],
                            file_name=base_name + ".txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    with download_columns[1]:
                        st.download_button(
                            "🎬 SRT",
                            outputs["srt"],
                            file_name=base_name + ".srt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    with download_columns[2]:
                        st.download_button(
                            "🌐 VTT",
                            outputs["vtt"],
                            file_name=base_name + ".vtt",
                            mime="text/vtt",
                            use_container_width=True
                        )

                    with download_columns[3]:
                        st.download_button(
                            "💻 JSON",
                            json.dumps(
                                outputs["json"],
                                ensure_ascii=False,
                                indent=2
                            ),
                            file_name=base_name + ".json",
                            mime="application/json",
                            use_container_width=True
                        )

                except Exception as error:
                    status.error("Transcription failed.")
                    st.exception(error)

    st.markdown('</div>', unsafe_allow_html=True)


# RIGHT OUTPUT PANEL

with right_panel:

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

    st.markdown(
        '<div class="panel-heading">📊 Output Formats</div>',
        unsafe_allow_html=True
    )

    formats = [
        ("📄 TXT", "Plain text"),
        ("🎬 SRT", "Subtitles for video"),
        ("🌐 VTT", "Web video subtitles"),
        ("💻 JSON", "Structured data")
    ]

    for name, description in formats:

        st.markdown(
            f'<div class="format-card">'
            f'{name}<br>'
            f'<span class="format-description">{description}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Powered by Faster-Whisper (Open Source) &nbsp; | &nbsp; '
    'App created by <span>Kalyanasundar – Gen/AI Developer</span> '
    '&nbsp; 💜'
    '</div>',
    unsafe_allow_html=True
)
