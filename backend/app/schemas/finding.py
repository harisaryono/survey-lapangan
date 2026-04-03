from pydantic import BaseModel


class FindingUpsertRequest(BaseModel):
    condition_summary: str | None = None
    compliance_status: str | None = None
    recommendation: str | None = None
    general_note: str | None = None
    filled_by: str | None = None
