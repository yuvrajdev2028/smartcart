from app.core.llm.base import LLMProvider
from app.core.rag.retriever import Retriever
from app.utils.prompt_builder import build_system_prompt


class RAGEngine:
    def __init__(self, llm_provider: LLMProvider, retriever: Retriever):
        self._llm = llm_provider
        self._retriever = retriever

    async def query(
        self,
        tenant_id: str,
        message: str,
        conversation_history: list[dict] | None = None,
        filters: dict | None = None,
        top_k: int = 8,
    ) -> dict:
        """Full RAG pipeline: retrieve → build prompt → generate response."""
        relevant_docs = self._retriever.retrieve(
            tenant_id=tenant_id,
            query=message,
            top_k=top_k,
            filters=filters,
        )

        system_prompt = build_system_prompt(relevant_docs)

        reply = await self._llm.generate(
            system_prompt=system_prompt,
            user_message=message,
            history=conversation_history,
        )

        products = []
        for doc in relevant_docs:
            meta = doc.metadata
            products.append(
                {
                    "id": meta.get("product_id", ""),
                    "name": meta.get("name", ""),
                    "price": meta.get("price", 0),
                    "currency": meta.get("currency", "USD"),
                    "brand": meta.get("brand", ""),
                    "category": meta.get("category", ""),
                    "image_url": meta.get("image_url", ""),
                    "stock": meta.get("stock", 0),
                }
            )

        return {
            "reply": reply,
            "products": products,
        }
