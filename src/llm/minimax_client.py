"""Minimax LLM client implementation."""

from openai import OpenAI

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
