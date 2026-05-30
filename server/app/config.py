from pydantic_settings import BaseSettings
from pydantic import SecretStr
from typing import Literal
from functools import lru_cache


class Settings(BaseSettings):
    llm_provider: Literal["openai", "gemini"] = "gemini"
    llm_model: str = "gemini-2.0-flash"
    llm_api_key: SecretStr = SecretStr("")

    embedding_provider: Literal["local", "openai", "gemini"] = "local"
    embedding_model: str = "all-MiniLM-L6-v2"

    chroma_persist_dir: str = "./chroma_data"
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
