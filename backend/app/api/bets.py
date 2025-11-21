from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_bets():
    return {"bets": []}
