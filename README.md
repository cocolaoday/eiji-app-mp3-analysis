# Audio Analysis API

FastAPI application for audio file analysis using Google Gemini LLM.

## Features

- Upload audio files for analysis
- Use Google Gemini 1.5 Pro or Flash models
- Store analysis results in PostgreSQL
- Retrieve analysis history

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Configure environment variables in `.env`:
   - DATABASE_URL: PostgreSQL connection string
   - REDIS_URL: Redis connection string
   - GOOGLE_API_KEY: Your Google API key

3. Run the application:
   uvicorn main:app --reload

## API Endpoints

- POST /analyze: Upload and analyze audio file
  Query parameters: model (pro or flash, default: flash)

- GET /analyses: Retrieve all analysis results

## Deployment

Deploy to Zeabur using the provided Dockerfile.
