"""Tests for the retrieval Promptfoo wrapper script."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType
from types import SimpleNamespace


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    return _repo_root() / "scripts" / "run_retrieve.py"


def _load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("tests_run_retrieve_script_module", _script_path())
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_run_retrieve_script_forwards_retrieval_options(monkeypatch) -> None:
    """Wrapper should forward policy and retrieval policy to src.cli retrieve."""
    module = _load_module()
    captured: dict[str, object] = {}

    def fake_run(command: list[str], **kwargs: object) -> object:
        captured["command"] = command
        captured["kwargs"] = kwargs
        return module.subprocess.CompletedProcess(args=command, returncode=0, stdout='{"document_hits": []}\n', stderr="")

    monkeypatch.setattr(module.subprocess, "run", fake_run)
    monkeypatch.setattr(
        module.sys,
        "argv",
        [
            "run_retrieve.py",
            "Question de test",
            json.dumps(
                {
                    "config": {
                        "policy-config": "config/policy.default.yaml",
                        "retrieval-policy": "standards_only_through_chunks__enriched",
                    }
                }
            ),
            "{}",
        ],
    )

    exit_code = module.main()

    assert exit_code == 0
    assert captured["command"][:4] == [sys.executable, "-m", "src.cli", "retrieve"]
    assert captured["command"][-1] == "--json"
    assert captured["kwargs"]["input"] == "Question de test"


def test_extract_options_reads_context_fallback() -> None:
    """Wrapper should read options from Promptfoo context when needed."""
    module = _load_module()

    options = module._extract_options(
        provider_options={},
        context={
            "test": {
                "options": {
                    "policy-config": "config/policy.default.yaml",
                    "retrieval-policy": "standards_only_through_chunks__enriched",
                }
            }
        },
    )

    assert options.policy_config == "config/policy.default.yaml"
    assert options.retrieval_policy == "standards_only_through_chunks__enriched"


def test_run_retrieve_script_resolves_policy_relative_to_base_path(monkeypatch, tmp_path: Path) -> None:
    """Wrapper should resolve staged policy-config relative to Promptfoo basePath."""
    module = _load_module()
    captured: dict[str, object] = {}

    def fake_run(command: list[str], **kwargs: object) -> object:
        captured["command"] = command
        return module.subprocess.CompletedProcess(args=command, returncode=0, stdout='{"document_hits": []}\n', stderr="")

    monkeypatch.setattr(module.subprocess, "run", fake_run)
    monkeypatch.setattr(
        module.sys,
        "argv",
        [
            "run_retrieve.py",
            "Question de test",
            json.dumps(
                {
                    "config": {
                        "policy-config": "./effective/policy.default.yaml",
                        "retrieval-policy": "standards_only_through_chunks__enriched",
                        "basePath": str(tmp_path),
                    }
                }
            ),
            "{}",
        ],
    )

    exit_code = module.main()

    assert exit_code == 0
    assert str(tmp_path / "effective" / "policy.default.yaml") in captured["command"]


def test_run_retrieve_script_writes_embedding_artifact(monkeypatch, tmp_path: Path) -> None:
    """Wrapper should persist the embedded query text when artifacts are enabled."""
    module = _load_module()
    captured: dict[str, object] = {}
    artifact_dir = tmp_path / "artifacts"

    def fake_run(command: list[str], **kwargs: object) -> object:
        captured["command"] = command
        return module.subprocess.CompletedProcess(args=command, returncode=0, stdout='{"document_hits": []}\n', stderr="")

    monkeypatch.setenv(module.PROMPTFOO_ARTIFACTS_DIR_ENV, str(artifact_dir))
    monkeypatch.setattr(
        module,
        "build_query_embedding_text",
        lambda question: SimpleNamespace(
            original_query=question,
            embedding_text=f"{question}\nEnglish glossary expansion",
            matched_french_terms=("terme",),
            appended_english_terms=("English glossary expansion",),
        ),
    )
    monkeypatch.setattr(module.subprocess, "run", fake_run)
    monkeypatch.setattr(
        module.sys,
        "argv",
        [
            "run_retrieve.py",
            "Question de test",
            json.dumps(
                {
                    "config": {
                        "policy-config": "config/policy.default.yaml",
                        "retrieval-policy": "standards_only_through_chunks__enriched",
                    }
                }
            ),
            json.dumps(
                {
                    "test": {
                        "metadata": {
                            "family": "Q1¤",
                            "variant": "Q1.0¤",
                            "question_path": "experiments/00_QUESTIONS/Q1/Q1.0.txt",
                        }
                    }
                }
            ),
        ],
    )

    exit_code = module.main()

    artifact_path = artifact_dir / "Q1" / "Q1.0" / "query_embedding.txt"

    assert exit_code == 0
    assert artifact_path.exists()
    artifact_text = artifact_path.read_text(encoding="utf-8")
    assert artifact_text == "Question de test\nEnglish glossary expansion\n"
