# 라우팅이 포함된 FastAPI 애플리케이션
from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

