"""Ollama LLM client implementation."""

from src.llm.openai_client import OpenAIClient, ReasoningLevel

OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_API_KEY_PLACEHOLDER = "ollama"


class OllamaClient(OpenAIClient):
    """Ollama OpenAI-compatible API client."""

    def __init__(
        self,
        model: str,
        api_key: str = OLLAMA_API_KEY_PLACEHOLDER,
        reasoning_effort: ReasoningLevel = "high",
        base_url: str = OLLAMA_BASE_URL,
    ) -> None:
        """Initialize the Ollama client.

        Args:
            model: Model identifier
            api_key: API key passed to the OpenAI SDK. Ollama ignores it, but the SDK requires one.
            reasoning_effort: Optional reasoning effort ("none", "low", "medium", "high").
            base_url: Base URL for the Ollama OpenAI-compatible API.
        """
        super().__init__(
            api_key=api_key,
            model=model,
            reasoning_effort=reasoning_effort,
            base_url=base_url,
        )
