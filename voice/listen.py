try:
    import whisper
    _WHISPER_AVAILABLE = True
except ImportError:
    _WHISPER_AVAILABLE = False

def listen():
    """
    Listens for audio input and transcribes it using Whisper.
    """
    print("Listening... (Simulated)")
    return input("Type your voice command (simulated): ")

def transcribe(audio_path):
    """
    Transcribes an audio file.
    """
    if not _WHISPER_AVAILABLE:
        raise RuntimeError("openai-whisper is not installed. Run: pip install openai-whisper")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]
