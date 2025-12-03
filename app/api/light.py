from fastapi import APIRouter

from app.models import State

router = APIRouter()

@router.get("/state", status_code=200)
async def state() -> State:
    return State(state="OK")
