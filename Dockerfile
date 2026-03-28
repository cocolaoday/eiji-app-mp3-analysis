FROM python:3.11-slim

WORKDIR /app

# 1. 修正路徑：直接去 app 目錄抓清單
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. 複製所有檔案
COPY . .

# 3. 啟動指令：明確指定 app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
