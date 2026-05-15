"""Pydantic AI app boundary and provider/model resolution."""

from __future__ import annotations

import os
from dataclasses import dataclass

MISSING_MODEL_MESSAGE = "Model environment variable is required for this provider. Set it in your environment or .env file."
SUPPORTED_PROVIDERS: tuple[str, ...] = ("openai", "anthropic", "mistral", "ollama")


@dataclass(frozen=True)
class PydanticAIRuntime:
    """Canonical Pydantic AI app boundary for provider and model configuration."""

    provider: str
    model: str

    @property
    def model_name(self) -> str:
        """Return the provider-prefixed Pydantic AI model name."""
        return f"{self.provider}:{self.model}"


def resolve_pydantic_ai_runtime() -> PydanticAIRuntime:
    """Resolve configured provider/model into one app-level runtime object."""
    provider = os.getenv("LLM_PROVIDER")
    if not provider:
        msg = "LLM_PROVIDER environment variable is required. Set it to a Pydantic AI supported provider such as openai, anthropic, mistral, or ollama"
        raise ValueError(msg)

    normalized_provider = provider.lower()
    if normalized_provider not in SUPPORTED_PROVIDERS:
        msg = f"Unknown Pydantic AI provider: {provider}. Supported providers: {', '.join(SUPPORTED_PROVIDERS)}"
        raise ValueError(msg)

    model_env_var = f"{normalized_provider.upper()}_MODEL"
    model = os.getenv(model_env_var)
    if not model:
        msg = f"{model_env_var} {MISSING_MODEL_MESSAGE}"
        raise ValueError(msg)

    return PydanticAIRuntime(provider=normalized_provider, model=model)


__all__ = ["SUPPORTED_PROVIDERS", "PydanticAIRuntime", "resolve_pydantic_ai_runtime"]
