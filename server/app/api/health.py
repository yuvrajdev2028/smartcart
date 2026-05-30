from fastapi import APIRouter
from app.models.responses import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="healthy", version="0.1.0")
