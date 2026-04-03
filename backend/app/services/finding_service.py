import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.form_finding import FormFinding
from app.models.survey_form import SurveyForm


def upsert_finding(
    db: Session,
    form_id: str,
    condition_summary: str | None,
    compliance_status: str | None,
    recommendation: str | None,
    general_note: str | None,
    filled_by: str | None,
) -> FormFinding | None:
    form = db.scalar(select(SurveyForm).where(SurveyForm.id == uuid.UUID(form_id)))
    if form is None:
        return None

    finding = db.scalar(select(FormFinding).where(FormFinding.form_id == uuid.UUID(form_id)))
    if finding is None:
        finding = FormFinding(
            form_id=uuid.UUID(form_id),
            filled_by=uuid.UUID(filled_by) if filled_by else None,
            condition_summary=condition_summary,
            compliance_status=compliance_status,
            recommendation=recommendation,
            general_note=general_note,
        )
        db.add(finding)
    else:
        finding.condition_summary = condition_summary
        finding.compliance_status = compliance_status
        finding.recommendation = recommendation
        finding.general_note = general_note
        finding.filled_by = uuid.UUID(filled_by) if filled_by else None
        finding.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(finding)
    return finding


def get_finding_by_form(db: Session, form_id: str) -> FormFinding | None:
    return db.scalar(select(FormFinding).where(FormFinding.form_id == uuid.UUID(form_id)))
