"""Tests for Pydantic AI runtime resolution and prompt-kind inference."""

from __future__ import annotations

import pytest

from src.ai.pydantic_client import infer_answer_prompt_kind, resolve_pydantic_ai_runtime


def test_infer_answer_prompt_kind_detects_applicability_analysis_marker() -> None:
    """Applicability analysis contains the identified approaches marker."""
    assert infer_answer_prompt_kind("<identified_approaches>{}</identified_approaches>") == "applicability_analysis"


def test_infer_answer_prompt_kind_defaults_to_approach_identification() -> None:
    """Approach identification has no identified approaches marker."""
    assert infer_answer_prompt_kind("You are an IFRS expert") == "approach_identification"


def test_resolve_pydantic_ai_runtime_openai(monkeypatch: pytest.MonkeyPatch) -> None:
    """Runtime config should bundle provider and model in one app boundary."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-5.2")

    runtime = resolve_pydantic_ai_runtime()

    assert runtime.provider == "openai"
    assert runtime.model == "gpt-5.2"
    assert runtime.model_name == "openai:gpt-5.2"

