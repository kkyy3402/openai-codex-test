from fastapi import FastAPI
from .config import get_settings
from .routers import stocks, charts

# 환경 설정을 불러옵니다
settings = get_settings()

# FastAPI 애플리케이션 생성
app = FastAPI(title="KIS Stock API")
app.include_router(stocks.router, prefix="/stocks", tags=["stocks"])
app.include_router(charts.router, prefix="/charts", tags=["charts"])

