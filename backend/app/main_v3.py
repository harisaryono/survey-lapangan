from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router_v3 import api_router_v3
from app.core.config import settings

app = FastAPI(title=settings.app_name, debug=settings.app_debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(api_router_v3, prefix=settings.api_v1_prefix)
