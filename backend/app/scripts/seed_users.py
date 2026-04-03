from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User


def seed() -> None:
    db: Session = SessionLocal()
    try:
        samples = [
            User(
                full_name="Admin Sistem",
                username="admin",
                email="admin@example.local",
                password_hash="change-me",
                role="admin",
            ),
            User(
                full_name="Ketua Tim",
                username="ketua",
                email="ketua@example.local",
                password_hash="change-me",
                role="chairperson",
            ),
        ]
        for item in samples:
            exists = db.query(User).filter(User.username == item.username).first()
            if not exists:
                db.add(item)
        db.commit()
        print("Seed users selesai.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
