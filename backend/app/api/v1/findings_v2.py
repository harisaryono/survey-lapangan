from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.finding import FindingUpsertRequest
from app.services.finding_service import get_finding_by_form, upsert_finding

router = APIRouter()


@router.get("/forms/{form_id}")
def get_finding_endpoint(form_id: str, db: Session = Depends(get_db)) -> dict:
    finding = get_finding_by_form(db, form_id)
    if finding is None:
        return {"form_id": form_id, "finding": None}
    return {
        "form_id": form_id,
        "finding": {
            "condition_summary": finding.condition_summary,
            "compliance_status": finding.compliance_status,
            "recommendation": finding.recommendation,
            "general_note": finding.general_note,
            "filled_by": str(finding.filled_by) if finding.filled_by else None,
        },
    }


@router.put("/forms/{form_id}")
def put_finding_endpoint(form_id: str, payload: FindingUpsertRequest, db: Session = Depends(get_db)) -> dict:
    finding = upsert_finding(
        db,
        form_id=form_id,
        condition_summary=payload.condition_summary,
        compliance_status=payload.compliance_status,
        recommendation=payload.recommendation,
        general_note=payload.general_note,
        filled_by=payload.filled_by,
    )
    if finding is None:
        raise HTTPException(status_code=404, detail="Form tidak ditemukan.")
    return {
        "form_id": form_id,
        "message": "Temuan berhasil disimpan.",
        "finding_id": str(finding.id),
    }
