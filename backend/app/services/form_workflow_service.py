import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.survey_form import SurveyForm


def get_form_or_none(db: Session, form_id: str) -> SurveyForm | None:
    return db.scalar(select(SurveyForm).where(SurveyForm.id == uuid.UUID(form_id)))



def submit_form(db: Session, form_id: str) -> SurveyForm | None:
    form = get_form_or_none(db, form_id)
    if form is None:
        return None
    form.status = "submitted"
    form.submitted_at = datetime.utcnow()
    db.commit()
    db.refresh(form)
    return form



def approve_form(db: Session, form_id: str, approver_id: str) -> SurveyForm | None:
    form = get_form_or_none(db, form_id)
    if form is None:
        return None
    form.status = "approved"
    form.approved_at = datetime.utcnow()
    form.approved_by = uuid.UUID(approver_id)
    db.commit()
    db.refresh(form)
    return form



def request_revision(db: Session, form_id: str) -> SurveyForm | None:
    form = get_form_or_none(db, form_id)
    if form is None:
        return None
    form.status = "needs_revision"
    form.revision_count += 1
    db.commit()
    db.refresh(form)
    return form



def unlock_form(db: Session, form_id: str) -> SurveyForm | None:
    form = get_form_or_none(db, form_id)
    if form is None:
        return None
    form.locked_by = None
    form.locked_at = None
    if form.status == "in_progress":
        form.status = "assigned" if form.assigned_to else "unclaimed"
    db.commit()
    db.refresh(form)
    return form
