import os
import requests

from dotenv import load_dotenv

load_dotenv()


class JarvisAI:
    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")

    def reply(self, message: str) -> str:
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
                                "Answer clearly and concisely.\n\n"
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

            return data["candidates"][0]["content"]["parts"][0]["text"]

        except requests.RequestException as exc:
            return f"JARVIS connection error: {exc}"

        except (KeyError, IndexError, TypeError):
            return "JARVIS received an unexpected response from Gemini."
