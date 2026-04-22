"""Tests for the Q1 retrieve document routing experiment script."""

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
    """Return the experiment script path."""
    return _repo_root() / "experiments" / "22_manual_experiment_on_document_routing" / "run_q1_retrieve_document_routing.py"


def _load_module() -> ModuleType:
    """Load the experiment script as a module for unit tests."""
    spec = importlib.util.spec_from_file_location(
        "tests_run_q1_retrieve_document_routing_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        error_message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(error_message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_q1_retrieve_document_routing_module"
    sys.modules["tests_run_q1_retrieve_document_routing_module"] = module
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


def test_run_includes_document_type_rank_line_and_summary(tmp_path: Path) -> None:
    """Markdown cells should include per-type rank/total plus matching summary rows."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (question_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")

    payload_by_question = {
        "Question 0": {
            "document_hits": [
                {"doc_uid": "ifrs9", "score": 0.9},
                {"doc_uid": "ias7", "score": 0.8},
                {"doc_uid": "ifrs7", "score": 0.7},
                {"doc_uid": "ifric16", "score": 0.6},
            ]
        },
        "Question 1": {
            "document_hits": [
                {"doc_uid": "ifrs7", "score": 0.85},
                {"doc_uid": "ifrs9", "score": 0.84},
                {"doc_uid": "ifric16", "score": 0.75},
                {"doc_uid": "ias7", "score": 0.74},
            ]
        },
    }

    def fake_run(*_args: object, **kwargs: object) -> object:
        query_text = kwargs["input"]
        if not isinstance(query_text, str):
            error_message = f"Expected string input, got: {query_text!r}"
            raise TypeError(error_message)
        return _build_completed_process(module, payload_by_question[query_text])

    module.subprocess.run = fake_run
    experiment = module.RetrieveDocumentRoutingExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        artifacts=module.ExperimentArtifacts(
            markdown_path=tmp_path / "result.md",
            json_path=tmp_path / "result.json",
        ),
        config=module.ExperimentConfig(
            retrieve_command=("uv", "run", "python"),
            command_preview="printf '<question>' | uv run python",
        ),
    )

    _, _, markdown = experiment.run()

    expected_fragments = (
        "1/4<br>IFRS-S 1/2<br>0.9000",
        "2/4<br>IFRS-S 2/2<br>0.8400",
        "2/4<br>IAS-S 1/1<br>0.8000",
        "**Type rank**",
        "1.5000/2.0000",
        "1.0000/1.0000",
    )
    for fragment in expected_fragments:
        if fragment not in markdown:
            error_message = f"Expected markdown fragment not found: {fragment}"
            raise AssertionError(error_message)


def test_run_persists_type_rank_metadata_in_json(tmp_path: Path) -> None:
    """JSON artifacts should include per-hit document type and type-rank metadata."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")

    def fake_run(*_args: object, **_kwargs: object) -> object:
        return _build_completed_process(
            module,
            {
                "document_hits": [
                    {"doc_uid": "ifrs9", "score": 0.9},
                    {"doc_uid": "ias7", "score": 0.8},
                    {"doc_uid": "ifrs7", "score": 0.7},
                ]
            },
        )

    module.subprocess.run = fake_run
    experiment = module.RetrieveDocumentRoutingExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        artifacts=module.ExperimentArtifacts(
            markdown_path=tmp_path / "result.md",
            json_path=tmp_path / "result.json",
        ),
        config=module.ExperimentConfig(
            retrieve_command=("uv", "run", "python"),
            command_preview="printf '<question>' | uv run python",
        ),
    )

    experiment.run()

    payload = json.loads((tmp_path / "result.json").read_text(encoding="utf-8"))
    hits = payload["results"][0]["hits"]
    first_hit = hits[0]
    second_hit = hits[1]
    third_hit = hits[2]

    if first_hit != {
        "doc_uid": "ifrs9",
        "document_type": "IFRS-S",
        "score": 0.9,
        "global_rank": 1,
        "global_total": 3,
        "type_rank": 1,
        "type_total": 2,
    }:
        error_message = f"Unexpected first hit payload: {first_hit!r}"
        raise AssertionError(error_message)

    if second_hit != {
        "doc_uid": "ias7",
        "document_type": "IAS-S",
        "score": 0.8,
        "global_rank": 2,
        "global_total": 3,
        "type_rank": 1,
        "type_total": 1,
    }:
        error_message = f"Unexpected second hit payload: {second_hit!r}"
        raise AssertionError(error_message)

    if third_hit != {
        "doc_uid": "ifrs7",
        "document_type": "IFRS-S",
        "score": 0.7,
        "global_rank": 3,
        "global_total": 3,
        "type_rank": 2,
        "type_total": 2,
    }:
        error_message = f"Unexpected third hit payload: {third_hit!r}"
        raise AssertionError(error_message)
