from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from app.core.inventory.models import Product


class InventorySyncService:
    def __init__(self, embeddings: Embeddings, persist_dir: str):
        self._embeddings = embeddings
        self._persist_dir = persist_dir

    def _get_collection(self, tenant_id: str) -> Chroma:
        return Chroma(
            collection_name=f"inventory_{tenant_id}",
            embedding_function=self._embeddings,
            persist_directory=self._persist_dir,
        )

    def sync_products(self, tenant_id: str, products: list[Product]) -> int:
        """Upsert products into tenant collection. Returns count synced."""
        store = self._get_collection(tenant_id)
        documents = []
        ids = []

        for product in products:
            doc = Document(
                page_content=product.to_document_text(),
                metadata=product.to_metadata(),
            )
            documents.append(doc)
            ids.append(product.id)

        store.add_documents(documents, ids=ids)
        return len(documents)

    def delete_product(self, tenant_id: str, product_id: str) -> bool:
        store = self._get_collection(tenant_id)
        store.delete(ids=[product_id])
        return True

    def get_product_count(self, tenant_id: str) -> int:
        store = self._get_collection(tenant_id)
        collection = store._collection
        return collection.count()
