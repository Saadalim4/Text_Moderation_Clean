from pydantic import BaseModel
from typing import List

class ModerationRequest(BaseModel):
    texts: List[str]
    language: str = "en"
    sensitivity: str = "moderate"

class ModerationResult(BaseModel):
    original: str
    flagged: bool
    reason: str
    edited: str