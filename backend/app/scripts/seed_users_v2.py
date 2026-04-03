from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.user import User


def seed() -> None:
    db: Session = SessionLocal()
    try:
        samples = [
            {
                "full_name": "Admin Sistem",
                "username": "admin",
                "email": "admin@example.local",
                "password": "admin123",
                "role": "admin",
            },
            {
                "full_name": "Ketua Tim",
                "username": "ketua",
                "email": "ketua@example.local",
                "password": "ketua123",
                "role": "chairperson",
            },
        ]
        for item in samples:
            exists = db.query(User).filter(User.username == item["username"]).first()
            if not exists:
                db.add(
                    User(
                        full_name=item["full_name"],
                        username=item["username"],
                        email=item["email"],
                        password_hash=get_password_hash(item["password"]),
                        role=item["role"],
                    )
                )
        db.commit()
        print("Seed users v2 selesai.")
        print("admin / admin123")
        print("ketua / ketua123")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
