"""Tests for the Q1 retrieval mode comparison analysis script."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


def _repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return the comparison analysis script path."""
    return _repo_root() / "experiments" / "analysis" / "run_q1_retrieval_mode_comparison.py"


def _load_module() -> ModuleType:
    """Load the comparison analysis script as a module."""
    spec = importlib.util.spec_from_file_location(
        "tests_run_q1_retrieval_mode_comparison_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_q1_retrieval_mode_comparison_module"
    sys.modules["tests_run_q1_retrieval_mode_comparison_module"] = module
    spec.loader.exec_module(module)
    return module


def _build_completed_process(module: ModuleType, payload: dict[str, object]) -> object:
    """Build a fake successful subprocess result."""
    return module.subprocess.CompletedProcess(
        args=["uv", "run", "python"],
        returncode=0,
        stdout=json.dumps(payload),
        stderr="",
    )


def test_run_writes_matrices_merged_report_and_summary(tmp_path: Path) -> None:
    """The comparison runner should emit all requested artifacts and merge results across runs."""
    module = _load_module()
    fr_question_dir = tmp_path / "Q1"
    en_question_dir = tmp_path / "Q1en"
    fr_question_dir.mkdir()
    en_question_dir.mkdir()
    (fr_question_dir / "Q1.0.txt").write_text("Question FR 0", encoding="utf-8")
    (fr_question_dir / "Q1.1.txt").write_text("Question FR 1", encoding="utf-8")
    (en_question_dir / "Q1.0.txt").write_text("Question EN 0", encoding="utf-8")
    (en_question_dir / "Q1.1.txt").write_text("Question EN 1", encoding="utf-8")

    payload_by_run_and_question = {
        ("policy.raw.yaml", "Question FR 0"): {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.91},
                {"doc_uid": "ifric16", "score": 0.73},
            ]
        },
        ("policy.raw.yaml", "Question FR 1"): {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.80},
            ]
        },
        ("policy.enriched.yaml", "Question FR 0"): {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.95},
                {"doc_uid": "ias39", "score": 0.89},
                {"doc_uid": "ifrs9", "score": 0.88},
            ]
        },
        ("policy.enriched.yaml", "Question FR 1"): {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.94},
                {"doc_uid": "ifrs9", "score": 0.82},
            ]
        },
        ("policy.raw.yaml", "Question EN 0"): {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.97},
                {"doc_uid": "ias39", "score": 0.96},
                {"doc_uid": "ifrs9", "score": 0.95},
            ]
        },
        ("policy.raw.yaml", "Question EN 1"): {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.96},
                {"doc_uid": "ias39", "score": 0.91},
                {"doc_uid": "ifrs9", "score": 0.90},
            ]
        },
    }

    def fake_run(*args: object, **kwargs: object) -> object:
        command = args[0]
        if not isinstance(command, tuple):
            message = f"Expected command tuple, got: {command!r}"
            raise TypeError(message)
        question_text = kwargs["input"]
        if not isinstance(question_text, str):
            message = f"Expected string input, got: {question_text!r}"
            raise TypeError(message)
        policy_index = command.index("--policy-config") + 1
        policy_name = Path(command[policy_index]).name
        key = (policy_name, question_text)
        if key not in payload_by_run_and_question:
            message = f"Unexpected retrieve invocation: {key!r}"
            raise AssertionError(message)
        return _build_completed_process(module, payload_by_run_and_question[key])

    module.subprocess.run = fake_run
    output_dir = tmp_path / "out"
    experiment = module.Q1RetrievalModeComparisonExperiment(
        repo_root=tmp_path,
        output_dir=output_dir,
        run_configs=(
            module.ComparisonRunConfig(
                run_id="fr_raw",
                label="fr_raw",
                question_dir=fr_question_dir,
                policy_config_path=output_dir / "policy.raw.yaml",
                matrix_output_path=output_dir / "generated_fr_raw_target_matrix.md",
            ),
            module.ComparisonRunConfig(
                run_id="fr_enriched",
                label="fr_enriched",
                question_dir=fr_question_dir,
                policy_config_path=output_dir / "policy.enriched.yaml",
                matrix_output_path=output_dir / "generated_fr_enriched_target_matrix.md",
            ),
            module.ComparisonRunConfig(
                run_id="en_control",
                label="en_control",
                question_dir=en_question_dir,
                policy_config_path=output_dir / "policy.raw.yaml",
                matrix_output_path=output_dir / "generated_en_control_target_matrix.md",
            ),
        ),
        priority_doc_uids=("ifric16", "ias39", "ifrs9"),
        target_doc_uids=("ifric16", "ias39", "ifrs9"),
    )

    experiment.run()

    merged_report = (output_dir / "generated_merged_delta_report.md").read_text(encoding="utf-8")
    summary = (output_dir / "generated_summary.md").read_text(encoding="utf-8")
    fr_raw_matrix = (output_dir / "generated_fr_raw_target_matrix.md").read_text(encoding="utf-8")
    fr_enriched_matrix = (output_dir / "generated_fr_enriched_target_matrix.md").read_text(encoding="utf-8")
    en_control_matrix = (output_dir / "generated_en_control_target_matrix.md").read_text(encoding="utf-8")

    assert "| Question | Document | fr_raw | fr_enriched | en_control |" in merged_report
    assert "| Q1.0 | IAS 39 |  | 0.89 / 2 | 0.96 / 2 |" in merged_report
    assert "## IFRIC 16" in summary
    assert "| fr_enriched | 2/2 (100.0%) | 2/2 (100.0%) | 2/2 (100.0%) | 2/2 (100.0%) | 1.00 | 0.94 |" in summary
    assert "| fr_raw | 2/2 (100.0%) | 1/2 (50.0%) | 2/2 (100.0%) | 2/2 (100.0%) | 1.50 | 0.77 |" in summary
    assert "| Total | Question | IFRIC 16 | IFRS 9 |" in fr_raw_matrix
    assert "| Total | Question | IFRIC 16 | IAS 39 | IFRS 9 |" in fr_enriched_matrix
    assert "| Total | Question | IFRIC 16 | IAS 39 | IFRS 9 |" in en_control_matrix
