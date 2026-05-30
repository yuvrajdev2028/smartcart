from pydantic import BaseModel
from app.core.inventory.models import Product


class ChatRequest(BaseModel):
    tenant_id: str
    message: str
    conversation_history: list[dict] = []


class InventorySyncRequest(BaseModel):
    tenant_id: str
    products: list[Product]
