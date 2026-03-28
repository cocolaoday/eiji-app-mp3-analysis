from fastapi import FastAPI, UploadFile, File, Query, HTTPException
from fastapi.responses import JSONResponse
import logging

# 初始化日誌系統
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RedEye_API")

app = FastAPI(title="Red-Eye_Audio_Analysis_v2")

# 1. 強制通車檢查點 (讓 Zeabur 知道你活著，不報 502)
@app.get("/")
@app.get("/health")
async def health_check():
    logger.info("📡 Heartbeat confirmed.")
    return {
        "status": "online",
        "system": "Red-Eye Heavy Industries",
        "msg": "主公，引擎已淨化，正式通車。",
        "bypass": "True"
    }

# 2. 音頻分析接口 (暴力測試版：確認上傳路徑通暢)
@app.post("/analyze")
async def analyze_audio(
    file: UploadFile = File(...),
    model: str = Query("flash", regex="^(pro|flash)$")
):
    try:
        if not file.content_type.startswith("audio/"):
            return JSONResponse(status_code=400, content={"error": "上傳的不是音訊檔案"})
        
        logger.info(f"📊 Received: {file.filename}")
        
        return {
            "status": "received",
            "filename": file.filename,
            "content_type": file.content_type,
            "model": f"gemini-1.5-{model}",
            "message": "連線測試成功！檔案已送達，等待下一步 AI 焊接指令。"
        }
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
