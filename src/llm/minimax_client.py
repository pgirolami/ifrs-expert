"""Minimax LLM client implementation."""

import logging
import re

from src.llm.openai_client import OpenAIClient, ReasoningLevel

logger = logging.getLogger(__name__)

MINIMAX_BASE_URL = "https://api.minimax.io/v1"

THINKING_PATTERN = re.compile(r"<think>[\s\S]*?</think>", re.DOTALL)


class MinimaxClient(OpenAIClient):
    """Minimax API client, extending OpenAIClient with Minimax-specific base URL."""

    def __init__(
        self,
        api_key: str,
        model: str,
        reasoning_effort: ReasoningLevel = "high",
    ) -> None:
        """Initialize the Minimax client.

        Args:
            api_key: Minimax API key
            model: Model identifier
            reasoning_effort: Optional reasoning effort ("low", "medium", "high"). If None, uses default.
        """
        super().__init__(
            api_key=api_key,
            model=model,
            reasoning_effort=reasoning_effort,
            base_url=MINIMAX_BASE_URL,
        )

    def _clean_response(self, content: str) -> str:
        """Remove thinking blocks and code fence markers from the response.

        Minimax returns thinking in <think>...</think> tags, and sometimes
        includes code fences like ``` or ```json that should be removed.
        """
        cleaned = THINKING_PATTERN.sub("", content).strip()

        lines = cleaned.splitlines()
        filtered_lines = [line for line in lines if "```" not in line and "```json" not in line]
        return "\n".join(filtered_lines).strip()
