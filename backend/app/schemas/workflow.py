from pydantic import BaseModel


class ApproveRequest(BaseModel):
    approver_id: str
