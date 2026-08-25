from jarvis.ai import JarvisAI
from jarvis.voice import speak, listen
from jarvis.system import system_info


def main():
    print("=" * 40)
    print("        FIZAN JARVIS AI")
    print("        SYSTEM READY")
    print("=" * 40)

    # System information
    try:
        info = system_info()

        print(f"Platform : {info.get('platform', 'Unknown')}")
        print(f"Machine  : {info.get('machine', 'Unknown')}")
        print(f"Python   : {info.get('python', 'Unknown')}")
        print(f"Free Disk: {info.get('disk_free_gb', 'Unknown')} GB")
        print()
    except Exception as exc:
        print(f"System information error: {exc}")

    assistant = JarvisAI()

    try:
        speak("Hello FIZAN. JARVIS is ready.")
    except Exception as exc:
        print(f"Voice error: {exc}")

    while True:
        try:
            message = listen()
        except Exception as exc:
            print(f"Listening error: {exc}")
            continue

        if not message:
            continue

        message = message.strip()

        if not message:
            continue

        command = message.lower()

        if command in {"exit", "quit", "shutdown", "bye"}:
            try:
                speak("Goodbye FIZAN.")
            except Exception:
                pass
            break

        response = assistant.reply(message)

        print(f"JARVIS: {response}")

        try:
            speak(response)
        except Exception as exc:
            print(f"Voice error: {exc}")


if __name__ == "__main__":
    main()
