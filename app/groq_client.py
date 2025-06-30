import json  # Add this import at the top
import openai
from app.config import GROQ_API_KEY, GROQ_MODEL

openai.api_key = GROQ_API_KEY
openai.api_base = "https://api.groq.com/openai/v1"

def call_groq(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"}  # Explicitly request JSON
        )
        content = response["choices"][0]["message"]["content"].strip()
        # Ensure the response starts with {
        if not content.startswith('{'):
            content = '{' + content.split('{', 1)[-1]
        return content
    except Exception as e:
        # Use properly formatted JSON fallback
        return json.dumps({
            "classification": "error",
            "reason": str(e),
            "edited": ""
        })