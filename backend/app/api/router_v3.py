from fastapi import APIRouter

from app.api.v1 import auth_v2, findings_v2, forms_v2, reports, surveys_v2

api_router_v3 = APIRouter()
api_router_v3.include_router(auth_v2.router, prefix="/auth", tags=["auth"])
api_router_v3.include_router(surveys_v2.router, prefix="/surveys", tags=["surveys"])
api_router_v3.include_router(forms_v2.router, prefix="/forms", tags=["forms"])
api_router_v3.include_router(findings_v2.router, prefix="/findings", tags=["findings"])
api_router_v3.include_router(reports.router, prefix="/reports", tags=["reports"])
