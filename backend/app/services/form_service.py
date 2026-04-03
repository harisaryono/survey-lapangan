import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.survey_form import SurveyForm


def claim_form(db: Session, form_id: str, user_id: str) -> SurveyForm | None:
    form = db.scalar(select(SurveyForm).where(SurveyForm.id == uuid.UUID(form_id)))
    if form is None:
        return None

    if form.status not in {"unclaimed", "assigned"}:
        return form

    form.assigned_to = uuid.UUID(user_id)
    form.locked_by = uuid.UUID(user_id)
    form.locked_at = datetime.utcnow()
    form.status = "in_progress"
    db.commit()
    db.refresh(form)
    return form
