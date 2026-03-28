from fastapi import FastAPI, UploadFile, File, Query, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Red-Eye Audio Analysis API")

# 1. 健康檢查端點 (確保 Zeabur 偵測到心跳，告別 502)
@app.get("/")
@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "system": "Red-Eye Heavy Industries",
        "msg": "主公，引擎已點火，正式通車。",
        "version": "2.0-forced-bypass"
    }

# 2. 音頻分析接口 (暴力通車測試版)
@app.post("/analyze")
async def analyze_audio(
    file: UploadFile = File(...),
    model: str = Query("flash", regex="^(pro|flash)$")
):
    try:
        # 檢查是否為音檔
        if not file.content_type.startswith("audio/"):
            return JSONResponse(
                status_code=400, 
                content={"error": "上傳的不是音訊檔案"}
            )
        
        # 暴力出口：暫不連資料庫，確保上傳功能通暢
        return {
            "status": "received",
            "filename": file.filename,
            "content_type": file.content_type,
            "model_requested": f"gemini-1.5-{model}",
            "message": "連線測試成功！檔案已送達，等待下一步 AI 指令。"
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
