from fastapi import APIRouter, HTTPException
from app.dependencies import get_rag_engine
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    engine = get_rag_engine()

    try:
        result = await engine.query(
            tenant_id=request.tenant_id,
            message=request.message,
            conversation_history=request.conversation_history,
        )
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
