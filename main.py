from fastapi import FastAPI, UploadFile, File, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from config import settings
from database import get_db, init_db
from models import AudioAnalysis
import google.generativeai as genai
import os

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()
    genai.configure(api_key=settings.GOOGLE_API_KEY)

@app.post("/analyze")
async def analyze_audio(
    file: UploadFile = File(...),
    model: str = Query("flash", regex="^(pro^|flash^)$"),
    db: Session = Depends(get_db)
):
    model_name = "gemini-1.5-pro" if model == "pro" else "gemini-1.5-flash"
ECHO 已啟動。
    content = await file.read()
ECHO 已啟動。
    audio_part = {
        "mime_type": file.content_type,
        "data": content
    }
ECHO 已啟動。
    response = genai.GenerativeModel(model_name).generate_content(
        [
            "Analyze this audio file and provide insights.",
            audio_part
        ]
    )
ECHO 已啟動。
    analysis = AudioAnalysis(
        filename=file.filename,
        analysis=response.text,
        model_used=model_name
    )
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
ECHO 已啟動。
    return {"id": analysis.id, "analysis": analysis.analysis, "model": model_name}

@app.get("/analyses")
async def get_analyses(db: Session = Depends(get_db)):
    analyses = db.query(AudioAnalysis).all()
    return analyses
