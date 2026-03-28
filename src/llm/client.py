"""LLM client factory."""

import logging
import os

from src.llm.anthropic_client import AnthropicClient
from src.llm.base import MISSING_API_KEY_MESSAGE, LLMClient
from src.llm.mistral_client import MistralClient
from src.llm.openai_client import OpenAIClient

logger = logging.getLogger(__name__)


def get_client() -> LLMClient:
    """Create an LLM client based on environment configuration.

    Reads LLM_PROVIDER from environment (default: 'openai').

    Returns:
        LLMClient instance for the configured provider

    Raises:
        ValueError: If provider is unknown or required API key is missing
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            error_msg = f"OPENAI_API_KEY {MISSING_API_KEY_MESSAGE}"
            raise ValueError(error_msg)
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return OpenAIClient(api_key=api_key, model=model)

    if provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            error_msg = f"ANTHROPIC_API_KEY {MISSING_API_KEY_MESSAGE}"
            raise ValueError(error_msg)
        model = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
        return AnthropicClient(api_key=api_key, model=model)

    if provider == "mistral":
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            error_msg = f"MISTRAL_API_KEY {MISSING_API_KEY_MESSAGE}"
            raise ValueError(error_msg)
        model = os.getenv("MISTRAL_MODEL", "mistral-small-latest")
        return MistralClient(api_key=api_key, model=model)

    error_msg = f"Unknown LLM provider: {provider}. Supported providers: openai, anthropic, mistral"
    raise ValueError(error_msg)
