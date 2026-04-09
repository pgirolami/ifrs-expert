"""Tests for the Q1 retrieve chunk-stats experiment script."""

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
    return (
        _repo_root()
        / "experiments"
        / "22_manual_experiment_on_document_routing"
        / "run_q1_retrieve_chunk_stats.py"
    )


def _load_module() -> ModuleType:
    """Load the experiment script as a module for unit tests."""
    spec = importlib.util.spec_from_file_location(
        "tests_run_q1_retrieve_chunk_stats_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        error_message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(error_message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_q1_retrieve_chunk_stats_module"
    sys.modules["tests_run_q1_retrieve_chunk_stats_module"] = module
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


def test_run_builds_chunk_metric_cells_and_orders_columns_by_average_sum(tmp_path: Path) -> None:
    """Columns should be ordered by average score sum per question and cells should show all chunk stats."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (question_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")

    payload_by_question = {
        "Question 0": {
            "chunks": [
                {"doc_uid": "ifrs9", "score": 0.9, "text": "abcdefghij"},
                {"doc_uid": "ifrs9", "score": 0.7, "text": "abcd"},
                {"doc_uid": "ifric16", "score": 0.8, "text": "abcdefgh"},
            ]
        },
        "Question 1": {
            "chunks": [
                {"doc_uid": "ifrs9", "score": 0.6, "text": "abcdef"},
                {"doc_uid": "ifric17", "score": 0.95, "text": "abcdefghijkl"},
                {"doc_uid": "ifric17", "score": 0.5, "text": "abcde"},
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
    experiment = module.RetrieveChunkStatsExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        artifacts=module.ExperimentArtifacts(
            markdown_path=tmp_path / "result.md",
            json_path=tmp_path / "result.json",
        ),
        retrieve_command=("uv", "run", "python"),
        command_preview="printf '<question>' | uv run python",
    )

    _, columns, markdown = experiment.run()

    if [column.doc_uid for column in columns] != ["ifrs9", "ifric17", "ifric16"]:
        error_message = f"Unexpected column order: {[column.doc_uid for column in columns]!r}"
        raise AssertionError(error_message)

    expected_fragments = (
        "| Question | Context size | ifrs9 | ifric17 | ifric16 |",
        "| Q1.0 | 0.022 | 2<br>1.6000<br>0.7000<br>0.9000<br>0.8000<br>0.8000<br>7.0 |",
        "2<br>1.4500<br>0.5000<br>0.9500<br>0.7250<br>0.7250<br>8.5",
        "Avg sum/question |  | 1.1000 | 0.7250 | 0.4000 |",
        "**Avg chars**",
        "Average |  | 6.5 | 8.5 | 8.0 |",
    )
    for fragment in expected_fragments:
        if fragment not in markdown:
            error_message = f"Expected markdown fragment not found: {fragment}"
            raise AssertionError(error_message)


def test_run_persists_chunk_statistics_in_json(tmp_path: Path) -> None:
    """JSON artifacts should persist the aggregated chunk statistics per document."""
    module = _load_module()
    question_dir = tmp_path / "questions"
    question_dir.mkdir()
    (question_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")

    def fake_run(*_args: object, **_kwargs: object) -> object:
        return _build_completed_process(
            module,
            {
                "chunks": [
                    {"doc_uid": "ifrs9", "score": 0.9, "text": "abcdefghij"},
                    {"doc_uid": "ifrs9", "score": 0.7, "text": "abcd"},
                    {"doc_uid": "ifric16", "score": 0.8, "text": "abcdefgh"},
                ]
            },
        )

    module.subprocess.run = fake_run
    experiment = module.RetrieveChunkStatsExperiment(
        repo_root=tmp_path,
        question_dir=question_dir,
        artifacts=module.ExperimentArtifacts(
            markdown_path=tmp_path / "result.md",
            json_path=tmp_path / "result.json",
        ),
        retrieve_command=("uv", "run", "python"),
        command_preview="printf '<question>' | uv run python",
    )

    experiment.run()

    payload = json.loads((tmp_path / "result.json").read_text(encoding="utf-8"))
    expected_context_size_kb = 0.022
    if payload["results"][0]["context_size_kb"] != expected_context_size_kb:
        error_message = f"Unexpected context size: {payload['results'][0]['context_size_kb']!r}"
        raise AssertionError(error_message)

    stats_by_doc_uid = {
        item["doc_uid"]: item
        for item in payload["results"][0]["documents"]
    }

    expected_ifrs9 = {
        "doc_uid": "ifrs9",
        "chunk_count": 2,
        "score_sum": 1.6,
        "score_min": 0.7,
        "score_max": 0.9,
        "score_avg": 0.8,
        "score_median": 0.8,
        "avg_char_count": 7.0,
    }
    if stats_by_doc_uid["ifrs9"] != expected_ifrs9:
        error_message = f"Unexpected IFRS 9 stats: {stats_by_doc_uid['ifrs9']!r}"
        raise AssertionError(error_message)

    expected_ifric16 = {
        "doc_uid": "ifric16",
        "chunk_count": 1,
        "score_sum": 0.8,
        "score_min": 0.8,
        "score_max": 0.8,
        "score_avg": 0.8,
        "score_median": 0.8,
        "avg_char_count": 8.0,
    }
    if stats_by_doc_uid["ifric16"] != expected_ifric16:
        error_message = f"Unexpected IFRIC 16 stats: {stats_by_doc_uid['ifric16']!r}"
        raise AssertionError(error_message)
