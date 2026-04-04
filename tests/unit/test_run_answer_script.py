"""Regression tests for the Promptfoo wrapper script."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from types import ModuleType

from src.models.answer_command_result import AnswerCommandResult

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


def test_extract_mode_defaults_to_live_when_missing() -> None:
    """The wrapper should default to live mode when Promptfoo does not pass one."""
    run_answer = _load_run_answer_module()

    mode = run_answer._extract_mode({})

    assert mode == "live"


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


def test_promptfoo_artifact_output_dir_uses_family_variant_and_provider(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Promptfoo artifact paths should group files by family, variant, and provider."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv(run_answer.PROMPTFOO_ARTIFACTS_DIR_ENV, str(tmp_path))

    output_dir = run_answer._artifact_output_dir(
        context={"test": {"metadata": {"family": "Q1", "variant": "Q1.0"}}},
        llm_provider="Mistral Large 3",
    )

    assert output_dir == tmp_path / "Q1" / "Q1.0" / "mistral-large-3"


def test_write_promptfoo_artifacts_persists_historical_answer_files(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """The wrapper should save the usual prompt and response files when Promptfoo artifact archiving is enabled."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv(run_answer.PROMPTFOO_ARTIFACTS_DIR_ENV, str(tmp_path))
    result = AnswerCommandResult(
        query="Test query",
        success=True,
        prompt_a_text="Prompt A",
        prompt_a_raw_response='{"status": "pass"}',
        prompt_b_text="Prompt B",
        prompt_b_raw_response='{"answer": "oui"}',
        prompt_b_json={"answer": "oui"},
        prompt_b_markdown="# Markdown",
    )

    run_answer._write_promptfoo_artifacts(
        result=result,
        context={"test": {"metadata": {"family": "Q1", "variant": "Q1.0"}}},
        llm_provider="Mistral Large 3",
    )

    artifact_dir = tmp_path / "Q1" / "Q1.0" / "mistral-large-3"
    assert (artifact_dir / "A-prompt.txt").read_text(encoding="utf-8") == "Prompt A"
    assert (artifact_dir / "A-response.json").read_text(encoding="utf-8") == '{"status": "pass"}'
    assert (artifact_dir / "B-prompt.txt").read_text(encoding="utf-8") == "Prompt B"
    assert '"answer": "oui"' in (artifact_dir / "B-response.json").read_text(encoding="utf-8")
    assert (artifact_dir / "B-response.md").read_text(encoding="utf-8") == "# Markdown"


def test_apply_llm_provider_override_updates_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """The wrapper should set LLM_PROVIDER before executing the live pipeline."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv("LLM_PROVIDER", "openai")

    run_answer._apply_llm_provider_override("anthropic")

    assert os.environ["LLM_PROVIDER"] == "anthropic"
