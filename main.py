from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/health")
async def health():
    return {"status": "online", "msg": "主公，引擎已徹底淨化，夢魘終結。"}

@app.get("/test")
async def test():
    return {"message": "Hello World"}
