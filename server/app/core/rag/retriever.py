from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class Retriever:
    def __init__(self, embeddings: Embeddings, persist_dir: str):
        self._embeddings = embeddings
        self._persist_dir = persist_dir

    def _get_store(self, tenant_id: str) -> Chroma:
        return Chroma(
            collection_name=f"inventory_{tenant_id}",
            embedding_function=self._embeddings,
            persist_directory=self._persist_dir,
        )

    def retrieve(
        self,
        tenant_id: str,
        query: str,
        top_k: int = 8,
        filters: dict | None = None,
    ) -> list[Document]:
        """Retrieve relevant products via semantic search with optional metadata filters."""
        store = self._get_store(tenant_id)

        where_filter = self._build_where_filter(filters)
        search_kwargs = {"k": top_k}
        if where_filter:
            search_kwargs["filter"] = where_filter

        results = store.similarity_search(query, **search_kwargs)
        return results

    @staticmethod
    def _build_where_filter(filters: dict | None) -> dict | None:
        if not filters:
            return None

        conditions = []

        # Always exclude out-of-stock
        conditions.append({"stock": {"$gt": 0}})

        if "category" in filters:
            conditions.append({"category": {"$eq": filters["category"]}})
        if "max_price" in filters:
            conditions.append({"price": {"$lte": filters["max_price"]}})
        if "min_price" in filters:
            conditions.append({"price": {"$gte": filters["min_price"]}})
        if "brand" in filters:
            conditions.append({"brand": {"$eq": filters["brand"]}})

        if len(conditions) == 1:
            return conditions[0]
        return {"$and": conditions}
