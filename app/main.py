from fastapi import FastAPI, APIRouter

from app.api import light

app = FastAPI(
    title="Light example app",
    version="0.1.0"
)

app.include_router(light.router, prefix="/light")
