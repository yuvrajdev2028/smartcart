from fastapi import APIRouter
from app.api.health import router as health_router
from app.api.chat import router as chat_router
from app.api.inventory import router as inventory_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router, tags=["health"])
api_router.include_router(chat_router, tags=["chat"])
api_router.include_router(inventory_router, tags=["inventory"])
