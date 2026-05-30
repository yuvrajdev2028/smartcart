from abc import ABC, abstractmethod
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


class LLMProvider(ABC):
    @abstractmethod
    def get_chat_model(self) -> BaseChatModel:
        ...

    async def generate(
        self, system_prompt: str, user_message: str, history: list[dict] | None = None
    ) -> str:
        messages = [SystemMessage(content=system_prompt)]

        for msg in history or []:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))

        messages.append(HumanMessage(content=user_message))
        response = await self.get_chat_model().ainvoke(messages)
        return str(response.content)
