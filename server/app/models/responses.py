from pydantic import BaseModel


class ProductSummary(BaseModel):
    id: str
    name: str
    price: float
    currency: str = "USD"
    brand: str
    category: str
    image_url: str = ""
    stock: int = 0


class ChatResponse(BaseModel):
    reply: str
    products: list[ProductSummary] = []


class InventorySyncResponse(BaseModel):
    status: str
    products_synced: int


class InventoryStatusResponse(BaseModel):
    tenant_id: str
    product_count: int


class HealthResponse(BaseModel):
    status: str
    version: str
