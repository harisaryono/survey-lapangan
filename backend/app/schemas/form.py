from pydantic import BaseModel


class FormClaimRequest(BaseModel):
    user_id: str


class FormResponse(BaseModel):
    id: str
    survey_id: str
    inspection_point_code: str
    inspection_point_name: str
    assigned_to: str | None = None
    locked_by: str | None = None
    status: str
