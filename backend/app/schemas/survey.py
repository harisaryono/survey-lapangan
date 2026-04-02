from datetime import date

from pydantic import BaseModel


class SurveyCreate(BaseModel):
    survey_code: str
    title: str
    applicant_name: str
    business_name: str | None = None
    location_text: str
    survey_date: date
    chairperson_id: str
    description: str | None = None


class SurveyResponse(BaseModel):
    id: str
    survey_code: str
    title: str
    applicant_name: str
    business_name: str | None = None
    location_text: str
    survey_date: date
    chairperson_id: str
    status: str
    description: str | None = None
