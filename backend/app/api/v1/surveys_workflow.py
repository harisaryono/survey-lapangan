from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.survey import SurveyCreate
from app.services.survey_service import create_survey

router = APIRouter()


@router.post("")
def create_survey_workflow(payload: SurveyCreate, db: Session = Depends(get_db)) -> dict:
    survey = create_survey(db, payload)
    return {
        "id": str(survey.id),
        "survey_code": survey.survey_code,
        "title": survey.title,
        "status": survey.status,
        "message": "Survei berhasil dibuat beserta form default.",
    }
