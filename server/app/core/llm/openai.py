from langchain_openai import ChatOpenAI
from langchain_core.language_models import BaseChatModel
from app.core.llm.base import LLMProvider


class OpenAILLMProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self._chat_model = ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=0.7,
        )

    def get_chat_model(self) -> BaseChatModel:
        return self._chat_model
