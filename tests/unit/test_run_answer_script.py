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
    """Return repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return Promptfoo wrapper path."""
    return _repo_root() / "scripts" / "run_answer.py"


def _load_run_answer_module() -> ModuleType:
    """Load scripts/run_answer.py as module for unit tests."""
    spec = importlib.util.spec_from_file_location("tests_run_answer_script_module", _script_path())
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_answer_script_module"
    sys.modules["tests_run_answer_script_module"] = module
    spec.loader.exec_module(module)
    return module


def test_run_answer_script_supports_direct_execution_from_repo_root() -> None:
    """Wrapper should run as direct script from repository root."""
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


def test_extract_mode_defaults_to_live_when_missing() -> None:
    """Wrapper should default to live mode when Promptfoo does not pass one."""
    run_answer = _load_run_answer_module()
    assert run_answer._extract_mode({}) == "live"


def test_extract_options_requires_policy_config() -> None:
    """Wrapper should fail fast when policy-config missing."""
    run_answer = _load_run_answer_module()

    with pytest.raises(ValueError, match="policy-config"):
        run_answer._extract_options(provider_options={}, context={})


def test_extract_options_reads_policy_config_and_artifact_flags() -> None:
    """Wrapper should parse policy-config and artifact options."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={
            "config": {
                "policy-config": "../../../../config/policy.default.yaml",
                "output-dir": "artifacts/promptfoo",
                "save-all": True,
            }
        },
        context={},
    )

    assert options.policy_config == "../../../../config/policy.default.yaml"
    assert options.output_dir == "artifacts/promptfoo"
    assert options.config_kv["policy-config"] == "../../../../config/policy.default.yaml"


def test_apply_llm_provider_override_updates_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Wrapper should set LLM_PROVIDER before executing live pipeline."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv("LLM_PROVIDER", "openai")

    run_answer._apply_llm_provider_override("anthropic")

    assert os.environ["LLM_PROVIDER"] == "anthropic"


def test_run_live_passes_policy_to_answer_command(monkeypatch: pytest.MonkeyPatch) -> None:
    """Wrapper should load policy and forward it into AnswerOptions."""
    run_answer = _load_run_answer_module()
    captured: dict[str, object] = {}

    class _FakeCommand:
        def execute(self) -> AnswerCommandResult:
            return AnswerCommandResult(query="Question?", success=True, prompt_b_raw_response='{"ok": true}')

    def _fake_create_answer_command(query: str, options: object) -> _FakeCommand:
        captured["query"] = query
        captured["options"] = options
        return _FakeCommand()

    loaded_retrieval_policy = object()

    class _FakePolicyConfig:
        retrieval = loaded_retrieval_policy

    monkeypatch.setattr(run_answer, "create_answer_command", _fake_create_answer_command)
    monkeypatch.setattr(run_answer, "load_policy_config", lambda path: _FakePolicyConfig())
    monkeypatch.setattr(run_answer, "setup_logging", lambda: None)
    monkeypatch.setattr(run_answer, "load_dotenv", lambda: None)

    exit_code, payload = run_answer._run_live(
        question="Question?",
        llm_provider=None,
        context={},
        options=run_answer.ExtractionOptions(
            policy_config="../../../../config/policy.default.yaml",
            output_dir="tmp/promptfoo",
        ),
    )

    assert exit_code == 0
    assert payload == '{"ok": true}'
    assert captured["query"] == "Question?"
    answer_options = captured["options"]
    assert isinstance(answer_options, run_answer.AnswerOptions)
    assert answer_options.policy is loaded_retrieval_policy
    assert answer_options.output_dir == Path("tmp/promptfoo")
