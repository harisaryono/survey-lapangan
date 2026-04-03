from fastapi import APIRouter

router = APIRouter()


@router.get("/{survey_id}/draft")
def get_report_draft(survey_id: str) -> dict:
    return {
        "survey_id": survey_id,
        "status": "not_generated",
        "content": "Draft berita acara belum digenerate.",
    }
