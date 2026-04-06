"""Tests for LLM client factory configuration."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.llm.client import get_client
from src.llm.openai_codex_client import OpenAICodexClient


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


def test_get_client_openai_codex_requires_model_env_var(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """The Codex provider should fail when OPENAI_CODEX_MODEL is missing."""
    auth_path = tmp_path / "auth.json"
    auth_path.write_text(json.dumps({"tokens": {"access_token": "token", "account_id": "account-123"}}))

    monkeypatch.setenv("LLM_PROVIDER", "openai-codex")
    monkeypatch.setenv("CODEX_AUTH_FILE", str(auth_path))
    monkeypatch.delenv("OPENAI_CODEX_MODEL", raising=False)

    with pytest.raises(ValueError, match="OPENAI_CODEX_MODEL"):
        get_client()


def test_get_client_openai_codex_does_not_require_openai_api_key(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """The Codex provider should construct without OPENAI_API_KEY."""
    auth_path = tmp_path / "auth.json"
    auth_path.write_text(json.dumps({"tokens": {"access_token": "token", "account_id": "account-123"}}))

    monkeypatch.setenv("LLM_PROVIDER", "openai-codex")
    monkeypatch.setenv("OPENAI_CODEX_MODEL", "gpt-5.1")
    monkeypatch.setenv("CODEX_AUTH_FILE", str(auth_path))
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    client = get_client()

    assert isinstance(client, OpenAICodexClient)


def test_get_client_unknown_provider_lists_openai_codex(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unknown provider errors should advertise the Codex provider too."""
    monkeypatch.setenv("LLM_PROVIDER", "unknown-provider")

    with pytest.raises(ValueError, match="openai-codex"):
        get_client()
