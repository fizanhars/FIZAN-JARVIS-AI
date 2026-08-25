import datetime
import platform
import subprocess
import webbrowser

import pyttsx3
import speech_recognition as sr

ASSISTANT_NAME = "Jarvis"

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)
recognizer = sr.Recognizer()


def speak(text):
    print(f"{ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio, language="hi-IN")
            print("You:", text)
            return text.lower().strip()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("मुझे आपकी बात समझ नहीं आई।")
            return ""
        except sr.RequestError:
            speak("Speech service उपलब्ध नहीं है। Internet connection check करें।")
            return ""


def open_target(target):
    if target == "youtube":
        webbrowser.open("https://www.youtube.com")
        speak("YouTube खोल रहा हूँ।")
    elif target == "google":
        webbrowser.open("https://www.google.com")
        speak("Google खोल रहा हूँ।")
    elif target == "github":
        webbrowser.open("https://github.com")
        speak("GitHub खोल रहा हूँ।")
    elif target == "notepad":
        if platform.system().lower() == "windows":
            subprocess.Popen(["notepad.exe"])
            speak("Notepad खोल रहा हूँ।")
        else:
            speak("Notepad command अभी Windows के लिए configured है।")


def handle_command(command):
    if not command:
        return True

    if any(x in command for x in ["बंद हो जाओ", "exit", "quit", "stop"]):
        speak("ठीक है। फिर मिलते हैं।")
        return False

    if "समय" in command or "time" in command:
        speak("अभी समय " + datetime.datetime.now().strftime("%I:%M %p") + " है।")
    elif "तारीख" in command or "date" in command:
        speak("आज " + datetime.datetime.now().strftime("%d %B %Y") + " है।")
    elif "youtube" in command:
        open_target("youtube")
    elif "google" in command:
        open_target("google")
    elif "github" in command:
        open_target("github")
    elif "notepad" in command:
        open_target("notepad")
    elif "hello" in command or "हेलो" in command or "नमस्ते" in command:
        speak("नमस्ते Faizan! मैं तैयार हूँ।")
    else:
        speak("यह command अभी मेरे command center में नहीं है।")

    return True


def main():
    speak("Jarvis online. मैं आपकी command का इंतज़ार कर रहा हूँ।")
    while handle_command(listen()):
        pass


if __name__ == "__main__":
    main()
