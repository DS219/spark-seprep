# Optional activity: Turn speech into text

**Time: 20–30 minutes, plus the first download.** Use this as a Lesson 8 fallback or do it on your own. You will run a small multilingual speech model locally, upload a short recording to a Streamlit app, and compare its transcript with what was actually said. No account or API key is needed. Your audio stays on your laptop.

## 1. Set up

You need Python 3.9 or newer, an internet connection for the first model download, and a short audio clip that you have permission to use. A quiet 10–30 second recording works best. Do not upload someone else's private speech without their permission.

Create a new folder and virtual environment. On macOS or Linux:

```bash
mkdir whisper-activity && cd whisper-activity
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install streamlit faster-whisper
```

On Windows PowerShell:

```powershell
mkdir whisper-activity
cd whisper-activity
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install streamlit faster-whisper
```

We use [`Systran/faster-whisper-tiny`](https://huggingface.co/Systran/faster-whisper-tiny), a multilingual conversion of OpenAI's 39-million-parameter Whisper Tiny model. **Do not choose `tiny.en`: that one is English-only.** The first run downloads the model from Hugging Face; later runs use the cache. Tiny trades accuracy for a small download and CPU-friendly speed. If you have more time and a better connection, try changing `"tiny"` to `"base"` in the code and compare the result.

> Correction to an easy mix-up: `distil-small.en` is English-only, not a multilingual fallback. This activity uses multilingual Whisper Tiny instead.

## 2. Build the upload app

Save this as `app.py` in `whisper-activity`:

```python
from pathlib import Path
import tempfile

import streamlit as st
from faster_whisper import WhisperModel


@st.cache_resource
def load_model():
    return WhisperModel("tiny", device="cpu", compute_type="int8")


st.title("Speech to text, on my laptop")
st.write("Upload a short recording. The model runs locally after its first download.")
audio = st.file_uploader("Audio file", type=["wav", "mp3", "m4a", "ogg", "flac"])

if audio:
    st.audio(audio)
    if st.button("Transcribe"):
        suffix = Path(audio.name).suffix.lower()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / f"recording{suffix}"
            path.write_bytes(audio.getvalue())
            with st.spinner("Transcribing..."):
                segments, info = load_model().transcribe(str(path), beam_size=1)
                transcript = " ".join(segment.text.strip() for segment in segments)
        st.write(f"Detected language: {info.language}")
        st.text_area("Transcript", transcript or "No speech detected.", height=180)
```

Run it:

```bash
python -m streamlit run app.py
```

Open the local URL Streamlit prints, usually `http://localhost:8501`. Upload your clip and select **Transcribe**. The temporary copy of the audio is deleted when transcription finishes; the model remains cached on your computer.

**Checkpoint:** show the detected language and transcript. Try one clip in a language other than English if you can. What did the model get right, and where did it guess?

## 3. Prepare a clip with FFmpeg, if needed

The app can read common audio formats without a separate FFmpeg installation because `faster-whisper` uses PyAV. [FFmpeg](https://ffmpeg.org/download.html) is **optional**, but useful for trimming or converting a file before upload. If you have it installed, this command takes the first 30 seconds and makes a mono, 16 kHz WAV file:

```bash
ffmpeg -i input.m4a -t 30 -ac 1 -ar 16000 clip.wav
```

Replace `input.m4a` with your filename. Use quotes around filenames with spaces. Keep the original recording; this creates a separate `clip.wav`. If FFmpeg says `command not found`, use your original MP3, M4A, or WAV in the app, or install FFmpeg from its official download page.

## Limits and troubleshooting

- **Slow first run:** the model is downloading. Finish setup before class if possible; subsequent runs use the local cache.
- **Weak transcript or wrong language:** use a clear, short clip with one speaker and little background noise. Tiny can miss accents, names, code-switching, or quiet words. Its output is a guess, not a reliable record.
- **File will not decode:** convert it to WAV with FFmpeg as above, then try again.
- **No speech detected:** check that the clip plays in the app and contains audible speech, then try a different recording.
- **Install error:** check `python --version` (3.9 or newer), activate `.venv`, and rerun the install command. On a managed computer, use your own laptop or pair with a classmate.

**Reflection:** Compare the transcript with the recording. How would an error matter if this were a caption, meeting note, or interview transcript? Do not treat automatic transcripts as verified quotations.

**Sources:** [Whisper Tiny model card](https://huggingface.co/openai/whisper-tiny), [faster-whisper documentation](https://github.com/SYSTRAN/faster-whisper), [FFmpeg](https://ffmpeg.org/).
