"""Tests for CLI commands."""

from __future__ import annotations

import argparse
import io
from pathlib import Path

import pytest

from src.cli import _answer_stdout_text, _execute_answer_command, _execute_command, _save_answer_command_result
from src.models.answer_command_result import AnswerCommandResult

VALID_PROMPT_B_RESPONSE = """{
  "assumptions_fr": ["Hypothèse de test"],
  "recommendation": {
    "answer": "oui",
    "justification": "Justification de test"
  },
  "approaches": [],
  "operational_points_fr": []
}"""


class FakeAnswerCommand:
    """Fake answer command for CLI testing."""

    def __init__(self, result: AnswerCommandResult) -> None:
        self._result = result

    def execute(self) -> AnswerCommandResult:
        return self._result


def test_save_answer_command_result_writes_expected_files(tmp_path: Path) -> None:
    """CLI writer should persist the historical artifact set."""
    result = AnswerCommandResult(
        query="What is IFRS?",
        success=True,
        retrieved_doc_uids=["ifrs-9"],
        prompt_a_text="Prompt A content",
        prompt_a_raw_response='{"status": "pass", "approaches": []}',
        prompt_b_text="Prompt B content",
        prompt_b_raw_response=VALID_PROMPT_B_RESPONSE,
        prompt_b_json={
            "assumptions_fr": ["Hypothèse de test"],
            "recommendation": {"answer": "oui", "justification": "Justification de test"},
            "approaches": [],
            "operational_points_fr": [],
        },
        prompt_b_markdown="# Markdown answer",
    )

    _save_answer_command_result(result, tmp_path)

    assert (tmp_path / "A-prompt.txt").read_text(encoding="utf-8") == "Prompt A content"
    assert (tmp_path / "A-response.json").read_text(encoding="utf-8") == '{"status": "pass", "approaches": []}'
    assert (tmp_path / "B-prompt.txt").read_text(encoding="utf-8") == "Prompt B content"
    assert '"answer": "oui"' in (tmp_path / "B-response.json").read_text(encoding="utf-8")
    assert (tmp_path / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"


class FakeTextCommand:
    """Fake text command for CLI testing."""

    def __init__(self, output: str) -> None:
        self._output = output

    def execute(self) -> str:
        return self._output


def test_execute_answer_command_returns_raw_response_and_preserves_save_all(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Answer CLI should keep stdout behavior unchanged while saving artifacts."""
    result = AnswerCommandResult(
        query="What is IFRS?",
        success=True,
        prompt_b_raw_response=VALID_PROMPT_B_RESPONSE,
        prompt_b_markdown="# Markdown answer",
    )

    monkeypatch.setattr("src.cli.create_answer_command", lambda query, options: FakeAnswerCommand(result))
    monkeypatch.setattr("sys.stdin", io.StringIO("What is IFRS?"))

    args = argparse.Namespace(
        command="answer",
        k=5,
        min_score=None,
        expand=0,
        full_doc_threshold=0,
        output_dir=tmp_path,
        save_all=True,
        retrieval_mode="titles",
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert (tmp_path / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"


def test_execute_answer_command_requires_output_dir_for_save_all() -> None:
    """Answer CLI should reject --save-all without --output-dir."""
    args = argparse.Namespace(
        command="answer",
        k=5,
        min_score=None,
        expand=0,
        full_doc_threshold=0,
        output_dir=None,
        save_all=True,
        retrieval_mode="text",
    )

    output = _execute_answer_command(args)

    assert output == "Error: --save-all requires --output-dir to be specified"


def test_execute_command_dispatches_query_titles(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the query-titles subcommand."""
    monkeypatch.setattr("src.cli.create_query_titles_command", lambda query, options: FakeTextCommand("title output"))
    monkeypatch.setattr("sys.stdin", io.StringIO("Find initial recognition"))

    args = argparse.Namespace(
        command="query-titles",
        k=5,
        min_score=None,
        json=True,
    )

    output = _execute_command(args)

    assert output == "title output"


def test_answer_stdout_text_prefers_raw_response() -> None:
    """CLI stdout should use the raw response when available."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        prompt_b_raw_response="raw response",
        prompt_b_markdown="markdown response",
    )

    assert _answer_stdout_text(result) == "raw response"
