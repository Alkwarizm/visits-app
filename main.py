import redis
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from config import get_settings


def create_application() -> FastAPI:
    app = FastAPI(title="FastAPI Application")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_application()
redis_client = redis.Redis(host=get_settings().REDIS_HOST, port=6379, db=0)
@app.get("/")
async def read_root(request: Request):
    ip = request.client.host
    user_agent = request.headers.get("User-Agent")
    visits = redis_client.incr("visits", 1)
    return {
        "visits": visits,
    }