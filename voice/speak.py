import pyttsx3

def speak(text):
    """
    Converts text to speech.
    """
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")
        print(f"Agent: {text}")

if __name__ == "__main__":
    speak("Hello, I am Livion. How can I help you today?")
