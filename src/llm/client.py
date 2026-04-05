"""LLM client factory."""

import logging
import os

from src.llm.anthropic_client import AnthropicClient
from src.llm.base import MISSING_API_KEY_MESSAGE, MISSING_MODEL_MESSAGE, LLMClient
from src.llm.mistral_client import MistralClient
from src.llm.openai_client import OpenAIClient

logger = logging.getLogger(__name__)


def get_client() -> LLMClient:
    """Create an LLM client based on environment configuration.

    Reads LLM_PROVIDER from environment (default: 'openai').

    Returns:
        LLMClient instance for the configured provider

    Raises:
        ValueError: If provider is unknown or required API key/model is missing
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        api_key = _require_env_var("OPENAI_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("OPENAI_MODEL", MISSING_MODEL_MESSAGE)
        return OpenAIClient(api_key=api_key, model=model)

    if provider == "anthropic":
        api_key = _require_env_var("ANTHROPIC_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("ANTHROPIC_MODEL", MISSING_MODEL_MESSAGE)
        return AnthropicClient(api_key=api_key, model=model)

    if provider == "mistral":
        api_key = _require_env_var("MISTRAL_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("MISTRAL_MODEL", MISSING_MODEL_MESSAGE)
        return MistralClient(api_key=api_key, model=model)

    error_msg = f"Unknown LLM provider: {provider}. Supported providers: openai, anthropic, mistral"
    raise ValueError(error_msg)


def _require_env_var(var_name: str, missing_message: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(var_name)
    if not value:
        error_msg = f"{var_name} {missing_message}"
        raise ValueError(error_msg)
    return value
