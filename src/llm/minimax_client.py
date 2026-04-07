"""Minimax LLM client implementation."""

import re

from openai import OpenAI

from src.llm.openai_client import OpenAIClient

MINIMAX_BASE_URL = "https://api.minimax.io/v1"
THINKING_PATTERN = re.compile(r"<think>.*?</think>", re.DOTALL)


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

    def _clean_response(self, content: str) -> str:
        """Remove thinking blocks from the response.

        Minimax returns thinking in <think>...</think> tags.
        """
        return THINKING_PATTERN.sub("", content).strip()
