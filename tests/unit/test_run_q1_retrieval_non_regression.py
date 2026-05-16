"""Tests for the Q1 retrieval non-regression analysis script."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    return _repo_root() / "experiments" / "analysis" / "run_q1_retrieval_non_regression.py"


def _load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("tests_run_q1_retrieval_non_regression_module", _script_path())
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_non_regression_summary_writes_artifacts_and_passes(tmp_path: Path, monkeypatch) -> None:
    """The summary script should compute metrics and write summaries."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (question_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")
    (question_dir / "family.yaml").write_text(
        """
family_id: Q1
assert_retrieve:
  required_documents:
    - ifrs9
    - ias39
    - ifric16
  required_section_ranges:
    - document: ifrs9
      start: "6.3.1"
      end: "6.3.6"
    - document: ifrs9
      start: "6.5.1"
      end: "6.5.1"
    - document: ifric16
      start: "10"
      end: "13"
""".lstrip(),
        encoding="utf-8",
    )

    fixture_path = tmp_path / "fixture.yaml"
    fixture_path.write_text(
        f"""
family_id: Q1
common:
  question_dir: {question_dir.as_posix()}
scenarios:
  authority_gate:
    label: enriched
    policy_config: config/policy.default.yaml
    retrieval_policy: standards_only_through_chunks__enriched
  glossary_sentinel:
    baseline:
      label: raw
      policy_config: config/policy.default.yaml
      retrieval_policy: documents2_through_chunks__raw
    candidate:
      label: enriched
      policy_config: config/policy.default.yaml
      retrieval_policy: documents2_through_chunks__enriched
""".lstrip(),
        encoding="utf-8",
    )

    payloads = {
        ("policy.default.yaml", "standards_only_through_chunks__enriched", "Question 0"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.99},
                {"doc_uid": "ias39", "document_type": "IAS-S", "score": 0.88},
                {"doc_uid": "ifric16", "document_type": "IFRIC", "score": 0.77},
            ]
        },
        ("policy.default.yaml", "standards_only_through_chunks__enriched", "Question 1"): {
            "document_hits": [
                {"doc_uid": "ifric16", "document_type": "IFRIC", "score": 0.98},
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.91},
                {"doc_uid": "ias39", "document_type": "IAS-S", "score": 0.81},
            ]
        },
        ("policy.default.yaml", "documents2_through_chunks__raw", "Question 0"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.89},
                {"doc_uid": "ifric16", "document_type": "IFRIC", "score": 0.50},
            ]
        },
        ("policy.default.yaml", "documents2_through_chunks__raw", "Question 1"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.80},
            ]
        },
        ("policy.default.yaml", "documents2_through_chunks__enriched", "Question 0"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.90},
                {"doc_uid": "ias39", "document_type": "IAS-S", "score": 0.85},
                {"doc_uid": "ifric16", "document_type": "IFRIC", "score": 0.75},
            ]
        },
        ("policy.default.yaml", "documents2_through_chunks__enriched", "Question 1"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "document_type": "IFRS-S", "score": 0.88},
                {"doc_uid": "ifric16", "document_type": "IFRIC", "score": 0.87},
                {"doc_uid": "ias39", "document_type": "IAS-S", "score": 0.82},
            ]
        },
    }

    def fake_run(command: list[str], **kwargs: object) -> object:
        policy_index = command.index("--policy-config") + 1
        policy_name = Path(command[policy_index]).name
        retrieval_index = command.index("--retrieval-policy") + 1
        retrieval_policy = command[retrieval_index]
        question_text = kwargs["input"]
        if not isinstance(question_text, str):
            raise TypeError(f"Expected string input, got: {question_text!r}")
        key = (policy_name, retrieval_policy, question_text)
        payload = payloads.get(key)
        if payload is None:
            raise AssertionError(f"Unexpected retrieve invocation: {key!r}")
        return module.subprocess.CompletedProcess(
            args=command,
            returncode=0,
            stdout=json.dumps(payload),
            stderr="",
        )

    monkeypatch.setattr(module.subprocess, "run", fake_run)
    output_dir = tmp_path / "out"
    exit_code = module.main(["--fixture", str(fixture_path), "--output-dir", str(output_dir), "--max-workers", "2"])

    assert exit_code == 0
    report = json.loads((output_dir / "summary.json").read_text(encoding="utf-8"))
    assert report["scenarios"][0]["passed"] is True
    assert report["scenarios"][1]["passed"] is True
    assert "authority_gate" in (output_dir / "summary.md").read_text(encoding="utf-8")
    assert (output_dir / "authority_gate" / "enriched" / "Q1.0.retrieve.json").exists()
    assert (output_dir / "glossary_sentinel" / "raw" / "Q1.1.retrieve.json").exists()
