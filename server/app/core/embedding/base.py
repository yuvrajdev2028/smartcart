from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings


class BaseEmbedder(ABC):
    @abstractmethod
    def get_embedding_model(self) -> Embeddings:
        ...
