"""Regression tests for the Promptfoo wrapper script."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest


def _repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return the Promptfoo wrapper path."""
    return _repo_root() / "scripts" / "run_answer.py"


def _load_run_answer_module() -> ModuleType:
    """Load scripts/run_answer.py as a module for unit tests."""
    spec = importlib.util.spec_from_file_location("tests_run_answer_script_module", _script_path())
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_run_answer_script_supports_direct_execution_from_repo_root() -> None:
    """The Promptfoo wrapper should run as a direct script from the repo root."""
    context = json.dumps({"test": {"options": {"mode": "canned"}}}, ensure_ascii=False)

    result = subprocess.run(
        [sys.executable, str(_script_path()), "Question de test", "{}", context],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    payload = json.loads(result.stdout)
    assert payload["recommendation"]["answer"] == "oui_sous_conditions"
    assert len(payload["approaches"]) == 3


def test_extract_llm_provider_prefers_provider_options_over_context() -> None:
    """Provider-level Promptfoo config should take precedence over test options."""
    run_answer = _load_run_answer_module()

    provider = run_answer._extract_llm_provider(
        provider_options={"config": {"llm_provider": "anthropic"}},
        context={"test": {"options": {"llm_provider": "openai"}}},
    )

    assert provider == "anthropic"


def test_extract_llm_provider_falls_back_to_test_options() -> None:
    """Test options should still work when no provider override is configured."""
    run_answer = _load_run_answer_module()

    provider = run_answer._extract_llm_provider(
        provider_options={},
        context={"test": {"options": {"llm_provider": "mistral"}}},
    )

    assert provider == "mistral"


def test_apply_llm_provider_override_updates_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """The wrapper should set LLM_PROVIDER before executing the live pipeline."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv("LLM_PROVIDER", "openai")

    run_answer._apply_llm_provider_override("anthropic")

    assert os.environ["LLM_PROVIDER"] == "anthropic"
