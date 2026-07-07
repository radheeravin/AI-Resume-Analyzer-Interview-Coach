import whisper
import os

def transcribe_audio(filename: str) -> str:
    """Transcribe an audio file using OpenAI Whisper."""
    if not os.path.exists(filename):
        return ""
    try:
        # Using the base model for faster local transcription
        model = whisper.load_model("base")
        result = model.transcribe(filename)
        return result.get("text", "")
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Error transcribing audio."
