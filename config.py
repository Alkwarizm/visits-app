import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    REDIS_HOST: str = os.getenv("REDIS_HOST", "redis-server")


def get_settings() -> Settings:
    return Settings()