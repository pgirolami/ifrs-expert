"""Regression tests for the Promptfoo wrapper script."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest

from src.models.answer_command_result import AnswerCommandResult


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


def test_run_answer_script_logs_policy_load_failures(tmp_path: Path) -> None:
    """Wrapper should write startup failures to the run log file."""
    project_root = _repo_root()
    default_policy_text = (project_root / "config" / "policy.default.yaml").read_text(encoding="utf-8")
    invalid_policy_text = re.sub(
        r"(NAVIS:\n\s+d: 2\n\s+)min_score: 0\.8(\n\s+expand_to_section: true)",
        r"\1min_score: 2\2",
        default_policy_text,
        count=1,
    )
    policy_path = tmp_path / "policy.invalid.yaml"
    policy_path.write_text(invalid_policy_text, encoding="utf-8")

    provider_options = json.dumps(
        {
            "config": {
                "policy-config": str(policy_path),
                "retrieval-policy": "standards_only_through_chunks__enriched",
            }
        },
        ensure_ascii=False,
    )

    result = subprocess.run(
        [sys.executable, str(_script_path()), "Question de test", provider_options, "{}"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1, result.stderr

    log_path = tmp_path / "logs" / "app.log"
    assert log_path.exists(), "Expected the wrapper to create a run log file"
    log_text = log_path.read_text(encoding="utf-8")
    assert "Promptfoo answer wrapper failed" in log_text
    assert "must be a number between 0.0 and 1.0" in log_text


def test_extract_mode_defaults_to_live_when_missing() -> None:
    """Wrapper should default to live mode when Promptfoo does not pass one."""
    run_answer = _load_run_answer_module()
    assert run_answer._extract_mode({}) == "live"


def test_extract_options_requires_policy_config() -> None:
    """Wrapper should fail fast when policy-config missing."""
    run_answer = _load_run_answer_module()

    with pytest.raises(ValueError, match="policy-config"):
        run_answer._extract_options(provider_options={}, context={})


def test_extract_options_requires_retrieval_policy() -> None:
    """Wrapper should fail fast when retrieval-policy missing."""
    run_answer = _load_run_answer_module()

    with pytest.raises(ValueError, match="retrieval-policy"):
        run_answer._extract_options(
            provider_options={"config": {"policy-config": "../../../../config/policy.default.yaml"}},
            context={},
        )


def test_extract_options_reads_policy_config_and_artifact_flags() -> None:
    """Wrapper should parse policy-config and artifact options."""
    run_answer = _load_run_answer_module()
    base_path = Path("/tmp/promptfoo-run")

    options = run_answer._extract_options(
        provider_options={
            "config": {
                "policy-config": "../../../../config/policy.default.yaml",
                "retrieval-policy": "standards_only_through_chunks__enriched",
                "output-dir": "artifacts/promptfoo",
                "basePath": str(base_path),
                "save-all": True,
            }
        },
        context={},
    )

    assert options.policy_config == "../../../../config/policy.default.yaml"
    assert options.retrieval_policy == "standards_only_through_chunks__enriched"
    assert options.output_dir == "artifacts/promptfoo"
    assert options.base_path == base_path
    assert options.config_kv["policy-config"] == "../../../../config/policy.default.yaml"
    assert options.config_kv["retrieval-policy"] == "standards_only_through_chunks__enriched"


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

    class _FakePolicyCatalog:
        pass

    monkeypatch.setattr(run_answer, "create_answer_command", _fake_create_answer_command)
    monkeypatch.setattr(run_answer, "load_policy_catalog", lambda _path: _FakePolicyCatalog())
    monkeypatch.setattr(run_answer, "resolve_retrieval_policy", lambda _catalog, _policy_name: loaded_retrieval_policy)
    monkeypatch.setattr(run_answer, "setup_logging", lambda: None)
    monkeypatch.setattr(run_answer, "load_dotenv", lambda: None)

    exit_code, payload = run_answer._run_live(
        question="Question?",
        llm_provider=None,
        context={},
        options=run_answer.ExtractionOptions(
            policy_config="../../../../config/policy.default.yaml",
            retrieval_policy="standards_only_through_chunks__enriched",
            output_dir="tmp/promptfoo",
        ),
    )

    assert exit_code == 0
    assert payload == '{"ok": true}'
    assert captured["query"] == "Question?"
    answer_options = captured["options"]
    assert isinstance(answer_options, run_answer.AnswerOptions)
    assert answer_options.policy is loaded_retrieval_policy
    assert answer_options.output_dir == run_answer.PROJECT_ROOT / "tmp" / "promptfoo"


def test_run_live_resolves_promptfoo_relative_paths_against_base_path(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Wrapper should resolve Promptfoo staged paths relative to basePath."""
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

    class _FakePolicyCatalog:
        pass

    def _fake_load_policy_catalog(path: Path) -> _FakePolicyCatalog:
        captured["policy_path"] = path
        return _FakePolicyCatalog()

    def _fake_resolve_retrieval_policy(catalog: object, policy_name: str) -> object:
        captured["policy_catalog"] = catalog
        captured["policy_name"] = policy_name
        return loaded_retrieval_policy

    monkeypatch.setattr(run_answer, "create_answer_command", _fake_create_answer_command)
    monkeypatch.setattr(run_answer, "load_policy_catalog", _fake_load_policy_catalog)
    monkeypatch.setattr(run_answer, "resolve_retrieval_policy", _fake_resolve_retrieval_policy)
    monkeypatch.setattr(run_answer, "setup_logging", lambda: None)
    monkeypatch.setattr(run_answer, "load_dotenv", lambda: None)

    exit_code, payload = run_answer._run_live(
        question="Question?",
        llm_provider=None,
        context={},
        options=run_answer.ExtractionOptions(
            policy_config="./effective/policy.default.yaml",
            retrieval_policy="standards_only_through_chunks__enriched",
            output_dir="artifacts/promptfoo",
            base_path=tmp_path,
        ),
    )

    assert exit_code == 0
    assert payload == '{"ok": true}'
    assert captured["policy_path"] == tmp_path / "effective" / "policy.default.yaml"
    assert captured["policy_name"] == "standards_only_through_chunks__enriched"
    answer_options = captured["options"]
    assert isinstance(answer_options, run_answer.AnswerOptions)
    assert answer_options.output_dir == tmp_path / "artifacts" / "promptfoo"
