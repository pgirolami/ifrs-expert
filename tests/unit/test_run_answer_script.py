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
    # Set __name__ so that dataclass decorators on classes in this module
    # can resolve cls.__module__ in sys.modules (required by Python 3.11+).
    module.__name__ = "tests_run_answer_script_module"
    sys.modules["tests_run_answer_script_module"] = module
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


def test_promptfoo_artifact_output_dir_uses_family_variant_and_config_kv(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Artifact paths should group files by family, variant, and config key-value pairs."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv(run_answer.PROMPTFOO_ARTIFACTS_DIR_ENV, str(tmp_path))

    output_dir = run_answer._artifact_output_dir(
        context={"test": {"metadata": {"family": "Q1", "variant": "Q1.0¤"}}},
        config_kv={"llm_provider": "openai", "k": "5", "min-score": "0.5"},
    )

    assert output_dir == tmp_path / "Q1" / "Q1.0" / "k=5__llm_provider=openai__min-score=0.5"


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
        context={"test": {"metadata": {"family": "Q1", "variant": "Q1.0¤"}}},
        config_kv={"llm_provider": "openai", "k": "5", "min-score": "0.5"},
    )

    artifact_dir = tmp_path / "Q1" / "Q1.0" / "k=5__llm_provider=openai__min-score=0.5"
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


def test_extract_options_reads_k_min_score_expand_and_retrieval_mode_from_config(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """ExtractionOptions should pull answer options from provider config."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={
            "config": {
                "llm_provider": "openai",
                "k": 10,
                "min-score": 0.7,
                "expand": 3,
                "retrieval-mode": "titles",
            }
        },
        context={},
    )

    assert options.k == 10
    assert options.min_score == 0.7
    assert options.expand == 3
    assert options.retrieval_mode == "titles"
    assert "k" in options.config_kv
    assert "min-score" in options.config_kv
    assert "llm_provider" in options.config_kv
    assert options.config_kv["retrieval-mode"] == "titles"


def test_extract_options_supports_e_key_for_expand() -> None:
    """The 'e' key should be accepted as an alias for expand."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={"config": {"e": 7}},
        context={},
    )

    assert options.expand == 7


def test_extract_options_prefers_e_over_expand_when_both_present() -> None:
    """When both 'e' and 'expand' are present, 'e' should take precedence."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={"config": {"e": 7, "expand": 2}},
        context={},
    )

    assert options.expand == 7


def test_extract_options_merges_config_kv_from_multiple_mappings() -> None:
    """Config key-values should accumulate across provider_options and context mappings."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={"config": {"llm_provider": "openai"}},
        context={"test": {"options": {"k": 10}}},
    )

    assert options.config_kv.get("llm_provider") == "openai"
    assert options.config_kv.get("k") == "10"


def test_extract_options_defaults_when_no_overrides() -> None:
    """ExtractionOptions should use defaults when no config overrides are provided."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(provider_options={}, context={})

    assert options.k == run_answer.DEFAULT_K
    assert options.min_score == run_answer.DEFAULT_MIN_SCORE
    assert options.expand == run_answer.DEFAULT_EXPAND
    assert options.retrieval_mode == run_answer.DEFAULT_RETRIEVAL_MODE


def test_build_config_dirname_from_kv_pairs() -> None:
    """The config directory name should be key=value pairs joined by __."""
    run_answer = _load_run_answer_module()

    dirname = run_answer._build_config_dirname({"llm_provider": "openai", "k": "5", "min-score": "0.5"})

    assert dirname == "k=5__llm_provider=openai__min-score=0.5"


def test_build_config_dirname_falls_back_to_llm_provider_env_when_empty(monkeypatch: pytest.MonkeyPatch) -> None:
    """When config_kv is empty, the directory should use the LLM_PROVIDER env var."""
    run_answer = _load_run_answer_module()
    monkeypatch.setenv("LLM_PROVIDER", "anthropic")

    dirname = run_answer._build_config_dirname({})

    assert dirname == "anthropic"


def test_extract_options_accepts_retrieval_mode_alias() -> None:
    """The wrapper should accept retrieval_mode as well as retrieval-mode."""
    run_answer = _load_run_answer_module()

    options = run_answer._extract_options(
        provider_options={"config": {"retrieval_mode": "titles"}},
        context={},
    )

    assert options.retrieval_mode == "titles"


def test_build_config_kv_excludes_nested_dicts() -> None:
    """_build_config_kv should only include scalar and primitive values, not nested dicts."""
    run_answer = _load_run_answer_module()

    kv = run_answer._build_config_kv({"llm_provider": "openai", "nested": {"should": "skip"}})

    assert "llm_provider" in kv
    assert "nested" not in kv


def test_merge_config_kv_overlay_wins() -> None:
    """Later mappings should override earlier ones in _merge_config_kv."""
    run_answer = _load_run_answer_module()

    merged = run_answer._merge_config_kv({"k": "5"}, {"k": "10"})

    assert merged["k"] == "10"


def test_extract_int_from_mapping_accepts_float_values() -> None:
    """Integer extraction should accept int or float and return int."""
    run_answer = _load_run_answer_module()

    assert run_answer._extract_int_from_mapping({"k": 5.0}, "k", 99) == 5
    assert run_answer._extract_int_from_mapping({"k": 5}, "k", 99) == 5


def test_extract_float_from_mapping_validates_range() -> None:
    """Float extraction should only accept values between 0.0 and 1.0."""
    run_answer = _load_run_answer_module()

    assert run_answer._extract_float_from_mapping({"min-score": 0.75}, "min-score", 0.55) == 0.75
    assert run_answer._extract_float_from_mapping({"min-score": 1.5}, "min-score", 0.55) == 0.55  # Out of range, uses fallback


def test_run_live_passes_retrieval_mode_to_answer_command(monkeypatch: pytest.MonkeyPatch) -> None:
    """The Promptfoo wrapper should forward retrieval mode into the answer pipeline."""
    run_answer = _load_run_answer_module()
    captured: dict[str, object] = {}

    class _FakeCommand:
        def execute(self) -> AnswerCommandResult:
            return AnswerCommandResult(query="Question?", success=True, prompt_b_raw_response='{"ok": true}')

    def _fake_create_answer_command(query: str, options: object) -> _FakeCommand:
        captured["query"] = query
        captured["options"] = options
        return _FakeCommand()

    monkeypatch.setattr(run_answer, "create_answer_command", _fake_create_answer_command)
    monkeypatch.setattr(run_answer, "setup_logging", lambda: None)
    monkeypatch.setattr(run_answer, "load_dotenv", lambda: None)

    exit_code, payload = run_answer._run_live(
        question="Question?",
        llm_provider=None,
        context={},
        options=run_answer.ExtractionOptions(k=7, min_score=0.4, expand=2, retrieval_mode="titles"),
    )

    assert exit_code == 0
    assert payload == '{"ok": true}'
    assert captured["query"] == "Question?"
    answer_options = captured["options"]
    assert isinstance(answer_options, run_answer.AnswerOptions)
    assert answer_options.k == 7
    assert answer_options.min_score == 0.4
    assert answer_options.expand == 2
    assert answer_options.retrieval_mode == "titles"
