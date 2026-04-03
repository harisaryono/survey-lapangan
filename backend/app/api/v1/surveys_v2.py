from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.survey import SurveyCreate
from app.services.survey_query_service import get_survey, list_surveys
from app.services.survey_service import create_survey

router = APIRouter()


@router.get("")
def list_surveys_endpoint(db: Session = Depends(get_db)) -> dict:
    items = list_surveys(db)
    return {
        "items": [
            {
                "id": str(item.id),
                "survey_code": item.survey_code,
                "title": item.title,
                "applicant_name": item.applicant_name,
                "survey_date": str(item.survey_date),
                "status": item.status,
            }
            for item in items
        ]
    }


@router.get("/{survey_id}")
def get_survey_endpoint(survey_id: str, db: Session = Depends(get_db)) -> dict:
    survey = get_survey(db, survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survei tidak ditemukan.")
    return {
        "id": str(survey.id),
        "survey_code": survey.survey_code,
        "title": survey.title,
        "applicant_name": survey.applicant_name,
        "business_name": survey.business_name,
        "location_text": survey.location_text,
        "survey_date": str(survey.survey_date),
        "chairperson_id": str(survey.chairperson_id),
        "status": survey.status,
        "description": survey.description,
    }


@router.post("")
def create_survey_endpoint(payload: SurveyCreate, db: Session = Depends(get_db)) -> dict:
    survey = create_survey(db, payload)
    return {
        "id": str(survey.id),
        "survey_code": survey.survey_code,
        "title": survey.title,
        "status": survey.status,
        "message": "Survei berhasil dibuat beserta form default.",
    }
