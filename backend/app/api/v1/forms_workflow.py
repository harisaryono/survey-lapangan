from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.form import FormClaimRequest
from app.services.form_service import claim_form

router = APIRouter()


@router.post("/{form_id}/claim")
def claim_form_endpoint(form_id: str, payload: FormClaimRequest, db: Session = Depends(get_db)) -> dict:
    form = claim_form(db, form_id=form_id, user_id=payload.user_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")

    return {
        "id": str(form.id),
        "survey_id": str(form.survey_id),
        "inspection_point_code": form.inspection_point_code,
        "inspection_point_name": form.inspection_point_name,
        "assigned_to": str(form.assigned_to) if form.assigned_to else None,
        "locked_by": str(form.locked_by) if form.locked_by else None,
        "status": form.status,
    }
