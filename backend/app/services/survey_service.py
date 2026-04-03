import uuid

from sqlalchemy.orm import Session

from app.models.survey import Survey
from app.models.survey_form import SurveyForm
from app.schemas.survey import SurveyCreate

DEFAULT_INSPECTION_POINTS = [
    ("PERIZINAN", "Kelengkapan Perizinan"),
    ("SAMPAH_PADAT", "Pengelolaan Sampah Padat"),
    ("LIMBAH_CAIR", "Pengelolaan Limbah Cair"),
    ("LIMBAH_B3", "Pengelolaan Limbah B3"),
    ("RTH", "Pengelolaan RTH"),
    ("RESAPAN_AIR_HUJAN", "Pengelolaan Resapan Air Hujan"),
    ("BAHAYA_KEBAKARAN", "Pengelolaan Bahaya Kebakaran"),
]


def create_survey(db: Session, payload: SurveyCreate) -> Survey:
    survey = Survey(
        survey_code=payload.survey_code,
        title=payload.title,
        applicant_name=payload.applicant_name,
        business_name=payload.business_name,
        location_text=payload.location_text,
        survey_date=payload.survey_date,
        chairperson_id=uuid.UUID(payload.chairperson_id),
        description=payload.description,
        status="draft",
    )
    db.add(survey)
    db.flush()

    for code, name in DEFAULT_INSPECTION_POINTS:
        db.add(
            SurveyForm(
                survey_id=survey.id,
                inspection_point_code=code,
                inspection_point_name=name,
                status="unclaimed",
            )
        )

    db.commit()
    db.refresh(survey)
    return survey
