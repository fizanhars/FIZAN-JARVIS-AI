import os
import requests

from dotenv import load_dotenv

load_dotenv()


class JarvisAI:
    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY", "").strip()

    def reply(self, message: str) -> str:
        message = message.strip()

        if not message:
            return "Please enter a message."

        if not self.gemini_key:
            return "Gemini API key is not configured."

        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            "models/gemini-2.0-flash:generateContent"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": (
                                "You are JARVIS, a helpful AI assistant. "
                                "Answer clearly, accurately and concisely.\n\n"
                                f"User: {message}"
                            )
                        }
                    ]
                }
            ]
        }

        try:
            response = requests.post(
                url,
                params={"key": self.gemini_key},
                json=payload,
                timeout=30,
            )

            response.raise_for_status()

            data = response.json()

            candidates = data.get("candidates", [])

            if not candidates:
                return "JARVIS did not receive a response from Gemini."

            content = candidates[0].get("content", {})
            parts = content.get("parts", [])

            if not parts:
                return "JARVIS received an empty response from Gemini."

            text = parts[0].get("text", "")

            if not text:
                return "JARVIS received an empty answer."

            return text.strip()

        except requests.Timeout:
            return "JARVIS connection timed out."

        except requests.HTTPError as exc:
            return f"JARVIS API error: {exc}"

        except requests.RequestException as exc:
            return f"JARVIS connection error: {exc}"

        except (ValueError, KeyError, IndexError, TypeError):
            return "JARVIS received an unexpected response from Gemini."
