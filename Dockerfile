# 使用輕量級 Python 映像檔
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 先複製零件清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製倉庫內所有檔案 (包含 main.py)
COPY . .

# 開啟 8080 端口
EXPOSE 8080

# 啟動指令：直接執行根目錄的 main.py 裡的 app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
