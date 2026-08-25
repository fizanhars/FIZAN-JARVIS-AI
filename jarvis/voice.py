import sys


def speak(text: str) -> None:
    """
    Basic text output for JARVIS.
    A real TTS engine can be connected later.
    """
    print(f"JARVIS: {text}")


def listen() -> str:
    """
    Basic console input for now.
    Microphone speech recognition will be added later.
    """
    try:
        return input("YOU: ").strip()
    except (EOFError, KeyboardInterrupt):
        return ""


if __name__ == "__main__":
    speak("Voice system is ready.")
    message = listen()

    if message:
        speak(f"You said: {message}")
