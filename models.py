from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AudioAnalysis(Base):
    __tablename__ = "audio_analyses"

    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    transcription = Column(Text)
    analysis = Column(Text)
    model_used = Column(String, default="gemini-1.5-flash")
    created_at = Column(DateTime, default=datetime.utcnow)
