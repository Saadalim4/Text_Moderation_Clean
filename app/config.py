import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "mixtral-8x7b-32768"  # or llama3-8b if preferred
SUPPORTED_LANGUAGES = ["en", "es"]
SENSITIVITY_LEVELS = {"strict": 0.2, "moderate": 0.5, "lenient": 0.8}