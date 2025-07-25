from pydantic import BaseSettings

class Settings(BaseSettings):
    # KIS API 키를 환경 변수에서 불러옵니다
    kis_api_key: str = ""

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
