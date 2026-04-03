from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest
from app.services.auth_service import login_user

router = APIRouter()


@router.post("/login")
def login_endpoint(payload: LoginRequest, db: Session = Depends(get_db)) -> dict:
    result = login_user(db, payload.username, payload.password)
    if result is None:
        raise HTTPException(status_code=401, detail="Username atau password salah.")
    return result.model_dump()
