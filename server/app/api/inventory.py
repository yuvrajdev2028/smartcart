from fastapi import APIRouter, HTTPException
from app.dependencies import get_inventory_service
from app.models.requests import InventorySyncRequest
from app.models.responses import InventorySyncResponse, InventoryStatusResponse

router = APIRouter(prefix="/inventory")


@router.post("/sync", response_model=InventorySyncResponse)
async def sync_inventory(request: InventorySyncRequest):
    service = get_inventory_service()
    try:
        count = service.sync_products(request.tenant_id, request.products)
        return InventorySyncResponse(status="success", products_synced=count)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{tenant_id}/{product_id}")
async def delete_product(tenant_id: str, product_id: str):
    service = get_inventory_service()
    try:
        service.delete_product(tenant_id, product_id)
        return {"status": "deleted", "product_id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{tenant_id}/status", response_model=InventoryStatusResponse)
async def inventory_status(tenant_id: str):
    service = get_inventory_service()
    try:
        count = service.get_product_count(tenant_id)
        return InventoryStatusResponse(tenant_id=tenant_id, product_count=count)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
