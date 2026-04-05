"""Tests for LLM client factory configuration."""

from __future__ import annotations

import pytest

from src.llm.client import get_client


@pytest.mark.parametrize(
    ("provider", "api_key_var", "model_var"),
    [
        ("openai", "OPENAI_API_KEY", "OPENAI_MODEL"),
        ("anthropic", "ANTHROPIC_API_KEY", "ANTHROPIC_MODEL"),
        ("mistral", "MISTRAL_API_KEY", "MISTRAL_MODEL"),
    ],
)
def test_get_client_requires_model_env_var(
    monkeypatch: pytest.MonkeyPatch,
    provider: str,
    api_key_var: str,
    model_var: str,
) -> None:
    """The configured provider should fail when its model env var is missing."""
    monkeypatch.setenv("LLM_PROVIDER", provider)
    monkeypatch.setenv(api_key_var, "test-api-key")
    monkeypatch.delenv(model_var, raising=False)

    with pytest.raises(ValueError, match=model_var):
        get_client()
