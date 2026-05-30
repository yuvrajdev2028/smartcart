from functools import lru_cache
from app.config import get_settings
from app.core.llm.base import LLMProvider
from app.core.llm.openai import OpenAILLMProvider
from app.core.llm.gemini import GeminiLLMProvider
from app.core.embedding.base import BaseEmbedder
from app.core.embedding.local import LocalEmbedder
from app.core.embedding.openai import OpenAIEmbedder
from app.core.embedding.gemini import GeminiEmbedder
from app.core.rag.retriever import Retriever
from app.core.rag.engine import RAGEngine
from app.core.inventory.sync import InventorySyncService
from langchain_core.embeddings import Embeddings


@lru_cache
def get_embedder() -> BaseEmbedder:
    settings = get_settings()
    provider = settings.embedding_provider

    if provider == "openai":
        return OpenAIEmbedder(
            api_key=settings.llm_api_key.get_secret_value(),
            model=settings.embedding_model,
        )
    elif provider == "gemini":
        return GeminiEmbedder(
            api_key=settings.llm_api_key.get_secret_value(),
            model=settings.embedding_model,
        )
    else:
        return LocalEmbedder(model_name=settings.embedding_model)


def get_embeddings() -> Embeddings:
    return get_embedder().get_embedding_model()


@lru_cache
def get_llm_provider() -> LLMProvider:
    settings = get_settings()
    api_key = settings.llm_api_key.get_secret_value()

    if settings.llm_provider == "openai":
        return OpenAILLMProvider(api_key=api_key, model=settings.llm_model)
    else:
        return GeminiLLMProvider(api_key=api_key, model=settings.llm_model)


@lru_cache
def get_retriever() -> Retriever:
    settings = get_settings()
    return Retriever(
        embeddings=get_embeddings(),
        persist_dir=settings.chroma_persist_dir,
    )


@lru_cache
def get_rag_engine() -> RAGEngine:
    return RAGEngine(
        llm_provider=get_llm_provider(),
        retriever=get_retriever(),
    )


@lru_cache
def get_inventory_service() -> InventorySyncService:
    settings = get_settings()
    return InventorySyncService(
        embeddings=get_embeddings(),
        persist_dir=settings.chroma_persist_dir,
    )
