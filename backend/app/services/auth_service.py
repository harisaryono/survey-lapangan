import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import TokenResponse


def login_user(db: Session, username: str, password: str) -> TokenResponse | None:
    user = db.scalar(select(User).where(User.username == username))
    if user is None or not user.is_active:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token(subject=str(user.id))
    return TokenResponse(
        access_token=token,
        user_id=str(user.id),
        username=user.username,
        role=user.role,
    )



def create_seed_passwords(db: Session) -> int:
    changed = 0
    users = db.scalars(select(User)).all()
    for user in users:
        if user.password_hash == "change-me":
            user.password_hash = "$2b$12$QxNQ9d2J4m2Q8QeJr0c9OemJwK3P7Q4r7R6iJ2S2WjC2kqL5R4m1K"
            changed += 1
    db.commit()
    return changed
