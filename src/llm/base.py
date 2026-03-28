"""LLM client base classes and shared constants."""

from abc import ABC, abstractmethod

# Error messages
MISSING_API_KEY_MESSAGE = "API key environment variable is required for this provider. Set it in your environment or .env file."
UNKNOWN_PROVIDER_MESSAGE = "Provider not supported."

AUTH_FAILED_MESSAGES = {
    "openai": "OpenAI API authentication failed. Please check your OPENAI_API_KEY in .env file.",
    "anthropic": "Anthropic API authentication failed. Please check your ANTHROPIC_API_KEY in .env file.",
    "mistral": "Mistral API authentication failed. Please check your MISTRAL_API_KEY in .env file.",
}

EMPTY_RESPONSE_MESSAGES = {
    "openai": "OpenAI returned empty response",
    "anthropic": "Anthropic returned empty response",
    "mistral": "Mistral returned empty response",
}

JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"


class LLMClient(ABC):
    """Abstract base class for LLM clients."""

    @abstractmethod
    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Raw text response from the LLM
        """

    @abstractmethod
    def generate_json(self, prompt: str, system: str | None = None) -> dict:
        """Generate and parse JSON from a prompt.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Parsed JSON response from the LLM
        """
