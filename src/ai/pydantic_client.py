"""Pydantic AI model resolution and text generation."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass

from pydantic_ai import Agent

from src.llm.base import MISSING_MODEL_MESSAGE

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PydanticAITextGenerator:
    """Thin Pydantic AI text-generation adapter used by legacy prompt builders."""

    model: str

    def generate_text(self, prompt: str) -> str:
        """Generate text through Pydantic AI and return the final output."""
        agent = Agent(self.model, output_type=str)
        result = agent.run_sync(prompt)
        output = result.output
        logger.info(f"Pydantic AI completion received model={self.model} output_chars={len(output)}")
        return output


def create_default_text_generator() -> PydanticAITextGenerator:
    """Create a Pydantic AI text generator from the existing environment variables."""
    model = resolve_pydantic_ai_model_name()
    logger.info(f"Using Pydantic AI model: {model}")
    return PydanticAITextGenerator(model=model)


def resolve_pydantic_ai_model_name() -> str:
    """Resolve the configured provider/model into a Pydantic AI model name."""
    provider = os.getenv("LLM_PROVIDER")
    if not provider:
        msg = "LLM_PROVIDER environment variable is required. Set it to a Pydantic AI supported provider such as openai, anthropic, mistral, or ollama"
        raise ValueError(msg)

    normalized_provider = provider.lower()
    if normalized_provider == "openai":
        return _provider_model_name(provider="openai", model_env_var="OPENAI_MODEL")
    if normalized_provider == "anthropic":
        return _provider_model_name(provider="anthropic", model_env_var="ANTHROPIC_MODEL")
    if normalized_provider == "mistral":
        return _provider_model_name(provider="mistral", model_env_var="MISTRAL_MODEL")
    if normalized_provider == "ollama":
        return _provider_model_name(provider="ollama", model_env_var="OLLAMA_MODEL")

    msg = f"Unknown Pydantic AI provider: {provider}. Supported providers: openai, anthropic, mistral, ollama"
    raise ValueError(msg)


def _provider_model_name(provider: str, model_env_var: str) -> str:
    """Build a Pydantic AI model name from one required model env var."""
    model = os.getenv(model_env_var)
    if not model:
        msg = f"{model_env_var} {MISSING_MODEL_MESSAGE}"
        raise ValueError(msg)
    return f"{provider}:{model}"


__all__ = [
    "PydanticAITextGenerator",
    "create_default_text_generator",
    "resolve_pydantic_ai_model_name",
]
