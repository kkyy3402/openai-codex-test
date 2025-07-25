from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
import httpx

# 주식 관련 라우터
router = APIRouter()

class Stock(BaseModel):
    """주식 기본 정보"""

    symbol: str
    name: str

async def fetch_stocks(term: str, strategy: str) -> List[Stock]:
    """KIS API에서 주식 목록을 가져옵니다 (예제)."""
    # TODO: 실제 KIS API 호출로 교체하세요
    await httpx.AsyncClient().get("https://example.com")
    return [Stock(symbol="000000", name="Placeholder Corp")]

@router.get("")
async def get_stocks(term: str, strategy: str):
    stocks = await fetch_stocks(term, strategy)
    return {"term": term, "strategy": strategy, "data": [s.dict() for s in stocks]}
