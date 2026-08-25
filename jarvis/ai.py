import os
from dotenv import load_dotenv

load_dotenv()

class JarvisAI:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")

    def reply(self, message):
        return f"JARVIS: I received your message -> {message}"
