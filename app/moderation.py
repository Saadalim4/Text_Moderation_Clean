import json
from typing import Dict, Any


def clean_json_response(raw: str) -> Dict[str, Any]:
    """Extracts JSON from a raw or malformed API response."""
    if not raw.strip():
        return {
            "classification": "error",
            "reason": "Empty response from API",
            "edited": ""
        }

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        try:
            start = raw.find('{')
            end = raw.rfind('}') + 1
            if start >= 0 and end > start:
                return json.loads(raw[start:end])
        except json.JSONDecodeError:
            pass

        return {
            "classification": "error",
            "reason": f"Failed to parse API response: {str(e)}",
            "edited": ""
        }


def moderate_text(text: str, language: str = "en", sensitivity: str = "strict") -> Dict[str, Any]:
    """
    Simulates moderation of text. This can be extended with real API logic.
    """
    # Very basic fake moderation logic
    flagged_words = ["bitch", "hate", "stupid"]
    lowered = text.lower()

    for word in flagged_words:
        if word in lowered:
            return {
                "classification": "flagged",
                "reason": f"Detected offensive language: '{word}'",
                "edited": text.replace(word, "[censored]")
            }

    return {
        "classification": "safe",
        "reason": "No issue",
        "edited": text
    }
