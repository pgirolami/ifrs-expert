"""Tests for Pydantic AI model resolution."""

from __future__ import annotations

import pytest

from src.ai.pydantic_client import infer_answer_prompt_kind, resolve_pydantic_ai_model_name


def test_resolve_pydantic_ai_model_name_openai(monkeypatch: pytest.MonkeyPatch) -> None:
    """OpenAI env settings should map to a Pydantic AI model name."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-5.2")

    assert resolve_pydantic_ai_model_name() == "openai:gpt-5.2"


def test_resolve_pydantic_ai_model_name_anthropic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Anthropic env settings should map to a Pydantic AI model name."""
    monkeypatch.setenv("LLM_PROVIDER", "anthropic")
    monkeypatch.setenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")

    assert resolve_pydantic_ai_model_name() == "anthropic:claude-sonnet-4-6"


def test_resolve_pydantic_ai_model_name_requires_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    """The resolver should fail clearly when no provider is configured."""
    monkeypatch.delenv("LLM_PROVIDER", raising=False)

    with pytest.raises(ValueError, match="LLM_PROVIDER environment variable is required"):
        resolve_pydantic_ai_model_name()


def test_resolve_pydantic_ai_model_name_rejects_unsupported_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unsupported legacy providers should not remain as runtime modes."""
    monkeypatch.setenv("LLM_PROVIDER", "minimax")
    monkeypatch.setenv("MINIMAX_MODEL", "MiniMax-M1")

    with pytest.raises(ValueError, match="Unknown Pydantic AI provider: minimax"):
        resolve_pydantic_ai_model_name()


def test_resolve_pydantic_ai_model_name_requires_model(monkeypatch: pytest.MonkeyPatch) -> None:
    """The resolver should fail clearly when the provider model is missing."""
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)

    with pytest.raises(ValueError, match="OLLAMA_MODEL"):
        resolve_pydantic_ai_model_name()


def test_infer_answer_prompt_kind_detects_applicability_analysis_marker() -> None:
    """Applicability analysis contains the identified approaches marker."""
    assert infer_answer_prompt_kind("<identified_approaches>{}</identified_approaches>") == "applicability_analysis"


def test_infer_answer_prompt_kind_defaults_to_approach_identification() -> None:
    """Approach identification has no identified approaches marker."""
    assert infer_answer_prompt_kind("You are an IFRS expert") == "approach_identification"
