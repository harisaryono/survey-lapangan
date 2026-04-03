import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.survey import Survey


def list_surveys(db: Session) -> list[Survey]:
    return list(db.scalars(select(Survey).order_by(Survey.created_at.desc())).all())



def get_survey(db: Session, survey_id: str) -> Survey | None:
    return db.scalar(select(Survey).where(Survey.id == uuid.UUID(survey_id)))
