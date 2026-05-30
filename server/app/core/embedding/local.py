from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings
from app.core.embedding.base import BaseEmbedder


class LocalEmbedder(BaseEmbedder):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self._model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def get_embedding_model(self) -> Embeddings:
        return self._model
