from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.form import FormClaimRequest
from app.schemas.workflow import ApproveRequest
from app.services.form_service import claim_form
from app.services.form_workflow_service import approve_form, request_revision, submit_form, unlock_form

router = APIRouter()


@router.post("/{form_id}/claim")
def claim_form_endpoint(form_id: str, payload: FormClaimRequest, db: Session = Depends(get_db)) -> dict:
    form = claim_form(db, form_id=form_id, user_id=payload.user_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {
        "id": str(form.id),
        "status": form.status,
        "assigned_to": str(form.assigned_to) if form.assigned_to else None,
        "locked_by": str(form.locked_by) if form.locked_by else None,
    }


@router.post("/{form_id}/submit")
def submit_form_endpoint(form_id: str, db: Session = Depends(get_db)) -> dict:
    form = submit_form(db, form_id=form_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {"id": str(form.id), "status": form.status}


@router.post("/{form_id}/approve")
def approve_form_endpoint(form_id: str, payload: ApproveRequest, db: Session = Depends(get_db)) -> dict:
    form = approve_form(db, form_id=form_id, approver_id=payload.approver_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {"id": str(form.id), "status": form.status}


@router.post("/{form_id}/revision")
def revision_form_endpoint(form_id: str, db: Session = Depends(get_db)) -> dict:
    form = request_revision(db, form_id=form_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {"id": str(form.id), "status": form.status, "revision_count": form.revision_count}


@router.post("/{form_id}/unlock")
def unlock_form_endpoint(form_id: str, db: Session = Depends(get_db)) -> dict:
    form = unlock_form(db, form_id=form_id)
    if form is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {"id": str(form.id), "status": form.status, "locked_by": None}
