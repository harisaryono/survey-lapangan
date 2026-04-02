from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_surveys() -> dict:
    return {
        "items": [],
        "message": "Daftar survei masih kosong. Endpoint ini siap dihubungkan ke PostgreSQL.",
    }
