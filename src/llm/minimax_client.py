"""Minimax LLM client implementation."""

import re

from openai import OpenAI

from src.llm.openai_client import OpenAIClient

MINIMAX_BASE_URL = "https://api.minimax.io/v1"
THINKING_PATTERN = re.compile(r"<result>.*?</result>", re.DOTALL)


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

    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt using Minimax API.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Raw text response from the LLM, with thinking removed
        """
        content = super().generate_text(prompt, system)
        return self._strip_thinking(content)

    def _strip_thinking(self, content: str) -> str:
        """Remove thinking blocks from the response.

        Minimax returns thinking in <result>...</result> tags.
        """
        return THINKING_PATTERN.sub("", content).strip()
