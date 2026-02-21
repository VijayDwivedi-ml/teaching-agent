import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = int(os.getenv("PORT", 8080))

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")