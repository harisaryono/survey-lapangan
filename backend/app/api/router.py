from fastapi import APIRouter

from app.api.v1 import auth, forms, reports, surveys

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(forms.router, prefix="/forms", tags=["forms"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
