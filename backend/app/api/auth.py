from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {"message": "register placeholder"}

@router.post("/login")
def login():
    return {"message": "login placeholder"}
