from fastapi import APIRouter

router = APIRouter()


@router.get("/{form_id}")
def get_form(form_id: str) -> dict:
    return {
        "id": form_id,
        "status": "unclaimed",
        "message": "Detail form masih berupa placeholder awal.",
    }
