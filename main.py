from jarvis.ai import JarvisAI
from jarvis.voice import speak, listen
from jarvis.system import system_info


def main():
    print("=" * 40)
    print("        FIZAN JARVIS AI")
    print("        SYSTEM READY")
    print("=" * 40)

    info = system_info()

    print(f"Platform : {info['platform']}")
    print(f"Machine  : {info['machine']}")
    print(f"Python   : {info['python']}")
    print(f"Free Disk: {info['disk_free_gb']} GB")
    print()

    assistant = JarvisAI()

    speak("Hello FIZAN. JARVIS is ready.")

    while True:
        message = listen()

        if not message:
            continue

        command = message.lower().strip()

        if command in {"exit", "quit", "shutdown", "bye"}:
            speak("Goodbye FIZAN.")
            break

        response = assistant.reply(message)
        speak(response)


if __name__ == "__main__":
    main()
