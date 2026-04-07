"""LLM client factory."""

import logging
import os

from src.llm.anthropic_client import AnthropicClient
from src.llm.base import MISSING_API_KEY_MESSAGE, MISSING_MODEL_MESSAGE, LLMClient
from src.llm.codex_auth import CodexAuthLoader
from src.llm.minimax_client import MinimaxClient
from src.llm.mistral_client import MistralClient
from src.llm.openai_client import OpenAIClient
from src.llm.openai_codex_client import OpenAICodexClient

logger = logging.getLogger(__name__)


def get_client() -> LLMClient:
    """Create an LLM client based on environment configuration.

    Reads LLM_PROVIDER from environment (default: 'openai').

    Returns:
        LLMClient instance for the configured provider

    Raises:
        ValueError: If provider is unknown or required API key/model is missing
    """
    provider = os.getenv("LLM_PROVIDER")
    if not provider:
        msg = "LLM_PROVIDER environment variable is required. Set it to: openai, openai-codex, anthropic, or mistral"
        raise ValueError(msg)
    provider = provider.lower()

    if provider == "openai":
        api_key = _require_env_var("OPENAI_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("OPENAI_MODEL", MISSING_MODEL_MESSAGE)
        return OpenAIClient(api_key=api_key, model=model)

    if provider == "openai-codex":
        model = _require_env_var("OPENAI_CODEX_MODEL", MISSING_MODEL_MESSAGE)
        auth_context = CodexAuthLoader().load()
        return OpenAICodexClient(model=model, auth_context=auth_context)

    if provider == "anthropic":
        api_key = _require_env_var("ANTHROPIC_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("ANTHROPIC_MODEL", MISSING_MODEL_MESSAGE)
        return AnthropicClient(api_key=api_key, model=model)

    if provider == "mistral":
        api_key = _require_env_var("MISTRAL_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("MISTRAL_MODEL", MISSING_MODEL_MESSAGE)
        return MistralClient(api_key=api_key, model=model)

    if provider == "minimax":
        api_key = _require_env_var("MINIMAX_API_KEY", MISSING_API_KEY_MESSAGE)
        model = _require_env_var("MINIMAX_MODEL", MISSING_MODEL_MESSAGE)
        return MinimaxClient(api_key=api_key, model=model)

    error_msg = f"Unknown LLM provider: {provider}. Supported providers: openai, openai-codex, anthropic, mistral, minimax"
    raise ValueError(error_msg)


def _require_env_var(var_name: str, missing_message: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(var_name)
    if not value:
        error_msg = f"{var_name} {missing_message}"
        raise ValueError(error_msg)
    return value
