"""Minimax LLM client implementation."""

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

from src.llm.openai_client import OpenAIClient

MINIMAX_BASE_URL = "https://api.minimax.io/v1"


class MinimaxClient(OpenAIClient):
    """Minimax API client, extending OpenAIClient with Minimax-specific base URL."""

    def __init__(self, api_key: str, model: str) -> None:
        """Initialize the Minimax client.

        Args:
            api_key: Minimax API key
            model: Model identifier
        """
        self._model = model
        self._client = OpenAI(api_key=api_key, base_url=MINIMAX_BASE_URL)

    def _create_text_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a text completion with thinking disabled."""
        return self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            extra_body={"thinking_type": "disabled"},
        )

    def _create_json_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a JSON completion with thinking disabled."""
        return self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            response_format={"type": "json_object"},
            extra_body={"thinking_type": "disabled"},
        )
