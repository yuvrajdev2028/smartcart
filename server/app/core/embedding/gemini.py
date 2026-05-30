from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.embeddings import Embeddings
from app.core.embedding.base import BaseEmbedder


class GeminiEmbedder(BaseEmbedder):
    def __init__(self, api_key: str, model: str = "models/embedding-001"):
        self._model = GoogleGenerativeAIEmbeddings(
            google_api_key=api_key, model=model
        )

    def get_embedding_model(self) -> Embeddings:
        return self._model
