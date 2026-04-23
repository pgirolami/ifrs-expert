"""Tests for the Q1 retrieve target matrix analysis script."""

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
    """Return the analysis script path."""
    return _repo_root() / "experiments" / "analysis" / "run_q1_retrieve_target_matrix.py"


def _load_module() -> ModuleType:
    """Load the analysis script as a module."""
    spec = importlib.util.spec_from_file_location(
        "tests_run_q1_retrieve_target_matrix_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_q1_retrieve_target_matrix_module"
    sys.modules["tests_run_q1_retrieve_target_matrix_module"] = module
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


def test_run_builds_frequency_sorted_matrix_with_totals(tmp_path: Path) -> None:
    """The matrix should sort columns by coverage and include totals/ranges."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (question_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")
    (question_dir / "Q1.2.txt").write_text("Question 2", encoding="utf-8")

    payload_by_question = {
        "Question 0": {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.91},
                {"doc_uid": "ifric16", "score": 0.73},
                {"doc_uid": "ias39", "score": 0.65},
            ]
        },
        "Question 1": {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.87},
                {"doc_uid": "ifric16", "score": 0.95},
                {"doc_uid": "ifrs15", "score": 0.60},
            ]
        },
        "Question 2": {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.90},
                {"doc_uid": "ifrs10", "score": 0.70},
            ]
        },
    }

    def fake_run(*_args: object, **kwargs: object) -> object:
        query_text = kwargs["input"]
        if not isinstance(query_text, str):
            message = f"Expected string input, got: {query_text!r}"
            raise TypeError(message)
        return _build_completed_process(module, payload_by_question[query_text])

    module.subprocess.run = fake_run
    output_path = tmp_path / "result.md"
    experiment = module.Q1RetrieveTargetMatrixExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        output_path=output_path,
        retrieve_command=(
            "uv",
            "run",
            "python",
            "-m",
            "src.cli",
            "retrieve",
            "--policy-config",
            "config/policy.default.yaml",
            "--json",
        ),
    )

    markdown = experiment.run()

    if output_path.read_text(encoding="utf-8") != markdown:
        message = "Expected markdown artifact to match returned markdown"
        raise AssertionError(message)
    if "| Total | Question | IFRS 9 | IFRIC 16 | IAS 39 | IFRS 10 | IFRS 15 |" not in markdown:
        message = "Expected header order not found in markdown"
        raise AssertionError(message)
    if '<span style="display:block; background-color: #d4edda; padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">0.91 / <strong>1</strong></span>' not in markdown:
        message = "Expected green top-ranked cell not found in markdown"
        raise AssertionError(message)
    if '<span style="display:block; background-color: #e6e2da; padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">0.95 / <strong>2</strong></span>' not in markdown:
        message = "Expected mid-ranked cell not found in markdown"
        raise AssertionError(message)
    if '<span style="display:block; background-color: #f8d7da; padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">0.65 / <strong>3</strong></span>' not in markdown:
        message = "Expected red lowest-ranked cell not found in markdown"
        raise AssertionError(message)
    if "| Total |  | 3 (0.87-0.91) | 2 (0.73-0.95) | 1 (0.65-0.65) | 1 (0.70-0.70) | 1 (0.60-0.60) |" not in markdown:
        message = "Expected totals row not found in markdown"
        raise AssertionError(message)


def test_run_places_requested_documents_first_in_lexicographic_order(tmp_path: Path) -> None:
    """Requested document UIDs should be moved to the front and sorted."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (question_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")

    payload_by_question = {
        "Question 0": {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.91},
                {"doc_uid": "ifric16", "score": 0.73},
                {"doc_uid": "ias39", "score": 0.65},
            ]
        },
        "Question 1": {
            "document_hits": [
                {"doc_uid": "ifric16", "score": 0.95},
                {"doc_uid": "ifrs9", "score": 0.87},
                {"doc_uid": "ifrs15", "score": 0.60},
            ]
        },
    }

    def fake_run(*_args: object, **kwargs: object) -> object:
        query_text = kwargs["input"]
        if not isinstance(query_text, str):
            message = f"Expected string input, got: {query_text!r}"
            raise TypeError(message)
        return _build_completed_process(module, payload_by_question[query_text])

    module.subprocess.run = fake_run
    experiment = module.Q1RetrieveTargetMatrixExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        output_path=tmp_path / "result.md",
        retrieve_command=(
            "uv",
            "run",
            "python",
            "-m",
            "src.cli",
            "retrieve",
            "--policy-config",
            "config/policy.default.yaml",
            "--json",
        ),
        priority_doc_uids=("ifrs15", "ifric16"),
    )

    markdown = experiment.run()

    if "| Total | Question | IFRS 15 | IFRIC 16 | IFRS 9 | IAS 39 |" not in markdown:
        message = "Expected prioritized columns first in the supplied priority order"
        raise AssertionError(message)


def test_humanize_doc_uid_formats_standard_document_labels() -> None:
    """Document UIDs should be converted to human-readable labels."""
    module = _load_module()

    if module.humanize_doc_uid("ifric16") != "IFRIC 16":
        message = "Expected ifric16 to humanize to IFRIC 16"
        raise AssertionError(message)
    if module.humanize_doc_uid("ifrs9") != "IFRS 9":
        message = "Expected ifrs9 to humanize to IFRS 9"
        raise AssertionError(message)
    if module.humanize_doc_uid("ias39") != "IAS 39":
        message = "Expected ias39 to humanize to IAS 39"
        raise AssertionError(message)
    if module.humanize_doc_uid("unknown") != "unknown":
        message = "Expected unknown to remain unchanged"
        raise AssertionError(message)
