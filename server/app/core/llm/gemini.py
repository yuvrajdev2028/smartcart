from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models import BaseChatModel
from app.core.llm.base import LLMProvider


class GeminiLLMProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        self._chat_model = ChatGoogleGenerativeAI(
            api_key=api_key,
            model=model,
            temperature=0.7,
        )

    def get_chat_model(self) -> BaseChatModel:
        return self._chat_model
