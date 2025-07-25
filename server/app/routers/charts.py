import os
import json
from datetime import date
from fastapi import APIRouter, BackgroundTasks, HTTPException

# 차트 관련 라우터
router = APIRouter()

def chart_path(strategy: str) -> str:
    """전략별 차트 데이터 파일 경로를 생성합니다."""
    os.makedirs("data", exist_ok=True)
    return os.path.join("data", f"chart_{strategy}_{date.today()}.json")

async def fetch_chart_data(strategy: str) -> None:
    """차트 데이터를 가져와 저장합니다 (예제)."""
    # TODO: KIS API 호출로 대체하세요
    path = chart_path(strategy)
    with open(path, "w") as f:
        json.dump({"message": f"placeholder chart data for {strategy}"}, f)

@router.post("/fetch")
async def schedule_fetch_charts(strategy: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch_chart_data, strategy)
    return {"status": "scheduled", "strategy": strategy}

@router.get("")
async def get_chart(strategy: str):
    path = chart_path(strategy)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="데이터가 없습니다")
    with open(path) as f:
        return json.load(f)
