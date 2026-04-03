from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(payload: LoginRequest) -> dict:
    return {
        "message": "Login endpoint belum terhubung ke database.",
        "username": payload.username,
    }
