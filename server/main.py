import os
import json
from datetime import date
from typing import List

import httpx
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    kis_api_key: str = ""

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
app = FastAPI(title="KIS Stock API")


class Stock(BaseModel):
    symbol: str
    name: str


async def fetch_stocks(term: str, strategy: str) -> List[Stock]:
    # TODO: Replace with real API call using settings.kis_api_key
    await httpx.AsyncClient().get("https://example.com")
    return [
        Stock(symbol="000000", name="Placeholder Corp"),
    ]


@app.get("/stocks")
async def get_stocks(term: str, strategy: str):
    stocks = await fetch_stocks(term, strategy)
    return {"term": term, "strategy": strategy, "data": [s.dict() for s in stocks]}


async def fetch_chart_data() -> None:
    """Generate placeholder chart data and save it to disk."""
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", f"chart_{date.today()}.json")
    # Simple dataset of random stock prices
    data = {
        "labels": ["AAA", "BBB", "CCC", "DDD"],
        "values": [100, 80, 120, 60],
    }
    with open(path, "w") as f:
        json.dump(data, f)


@app.post("/fetch-charts")
async def schedule_fetch_charts(background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch_chart_data)
    return {"status": "scheduled"}


@app.get("/chart")
async def get_chart():
    """Return the latest chart data."""
    path = os.path.join("data", f"chart_{date.today()}.json")
    if not os.path.exists(path):
        await fetch_chart_data()
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"labels": [], "values": []}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
