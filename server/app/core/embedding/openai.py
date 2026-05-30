from langchain_openai import OpenAIEmbeddings
from langchain_core.embeddings import Embeddings
from app.core.embedding.base import BaseEmbedder


class OpenAIEmbedder(BaseEmbedder):
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self._model = OpenAIEmbeddings(api_key=api_key, model=model)

    def get_embedding_model(self) -> Embeddings:
        return self._model
