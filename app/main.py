from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.moderation import moderate_text

app = FastAPI()

class ModerationRequest(BaseModel):
    texts: List[str]
    language: str
    sensitivity: str

@app.post("/moderate")
async def moderate(request: ModerationRequest):
    results = [
        moderate_text(text, request.language, request.sensitivity)
        for text in request.texts
    ]
    return {"results": results}
