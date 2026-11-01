
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Hello! Introduce yourself as Bharat Brief AI Assistant in Hindi."
)

print(response.text)
