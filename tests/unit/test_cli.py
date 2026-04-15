"""Tests for CLI commands."""

from __future__ import annotations

import argparse
import io
from pathlib import Path

import pytest

import src.cli as cli
from src.cli import _answer_stdout_text, _build_parser, _execute_answer_command, _execute_command, _save_answer_command_result
from src.models.answer_command_result import AnswerCommandResult

VALID_PROMPT_B_RESPONSE = """{
  "assumptions_fr": ["Hypothèse de test"],
  "recommendation": {
    "answer": "oui",
    "justification": "Justification de test"
  },
  "approaches": [],
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


def test_execute_answer_command_saves_artifacts_when_output_dir_is_provided(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Answer CLI should save artifacts whenever output_dir is provided."""
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
        d=25,
        min_score=None,
        doc_min_score=None,
        content_min_score=0.53,
        ifrs_d=4,
        ias_d=4,
        ifric_d=6,
        sic_d=6,
        ps_d=1,
        navis_d=2,
        ifrs_min_score=0.53,
        ias_min_score=0.4,
        ifric_min_score=0.48,
        sic_min_score=0.4,
        ps_min_score=0.4,
        navis_min_score=0.6,
        expand=0,
        expand_to_section=True,
        full_doc_threshold=0,
        output_dir=tmp_path,
        save_all=False,
        retrieval_mode="documents",
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert (tmp_path / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"


def test_execute_answer_command_creates_missing_output_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Answer CLI should create output directories when saving artifacts."""
    result = AnswerCommandResult(
        query="What is IFRS?",
        success=True,
        prompt_b_raw_response=VALID_PROMPT_B_RESPONSE,
        prompt_b_markdown="# Markdown answer",
    )
    output_dir = tmp_path / "new-output-dir"

    monkeypatch.setattr("src.cli.create_answer_command", lambda query, options: FakeAnswerCommand(result))
    monkeypatch.setattr("sys.stdin", io.StringIO("What is IFRS?"))

    args = argparse.Namespace(
        command="answer",
        k=5,
        d=25,
        min_score=None,
        doc_min_score=None,
        content_min_score=None,
        ifrs_d=4,
        ias_d=100,
        ifric_d=6,
        sic_d=100,
        ps_d=100,
        navis_d=2,
        ifrs_min_score=0.53,
        ias_min_score=0.0,
        ifric_min_score=0.48,
        sic_min_score=0.0,
        ps_min_score=0.0,
        navis_min_score=0.6,
        expand=0,
        expand_to_section=True,
        full_doc_threshold=0,
        output_dir=output_dir,
        save_all=False,
        retrieval_mode="text",
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert (output_dir / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"


def test_execute_answer_command_requires_output_dir_for_save_all() -> None:
    """Answer CLI should reject --save-all without --output-dir."""
    args = argparse.Namespace(
        command="answer",
        k=5,
        d=25,
        min_score=None,
        doc_min_score=None,
        content_min_score=0.53,
        ifrs_d=4,
        ias_d=4,
        ifric_d=6,
        sic_d=6,
        ps_d=1,
        navis_d=2,
        ifrs_min_score=0.53,
        ias_min_score=0.4,
        ifric_min_score=0.48,
        sic_min_score=0.4,
        ps_min_score=0.4,
        navis_min_score=0.6,
        expand=0,
        expand_to_section=True,
        full_doc_threshold=0,
        output_dir=None,
        save_all=True,
        retrieval_mode="documents",
    )

    output = _execute_answer_command(args)

    assert output == "Error: --save-all requires --output-dir to be specified"


def test_execute_answer_command_passes_retrieve_style_options(monkeypatch: pytest.MonkeyPatch) -> None:
    """Answer CLI should pass retrieval options through to AnswerOptions."""
    result = AnswerCommandResult(
        query="What is IFRS?",
        success=True,
        prompt_b_raw_response=VALID_PROMPT_B_RESPONSE,
    )
    captured_options: list[object] = []

    def _create_answer_command(query: str, options: object) -> FakeAnswerCommand:
        del query
        captured_options.append(options)
        return FakeAnswerCommand(result)

    monkeypatch.setattr("src.cli.create_answer_command", _create_answer_command)
    monkeypatch.setattr("sys.stdin", io.StringIO("What is IFRS?"))

    args = argparse.Namespace(
        command="answer",
        k=3,
        d=9,
        min_score=0.4,
        doc_min_score=0.2,
        content_min_score=0.1,
        ifrs_d=7,
        ias_d=6,
        ifric_d=4,
        sic_d=3,
        ps_d=2,
        navis_d=1,
        ifrs_min_score=0.61,
        ias_min_score=0.54,
        ifric_min_score=0.50,
        sic_min_score=0.49,
        ps_min_score=0.48,
        navis_min_score=0.47,
        expand=1,
        expand_to_section=True,
        full_doc_threshold=2000,
        output_dir=None,
        save_all=False,
        retrieval_mode="documents",
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert len(captured_options) == 1
    options = captured_options[0]
    assert getattr(options, "k") == 3
    assert getattr(options, "d") == 9
    assert getattr(options, "doc_min_score") == 0.2
    assert getattr(options, "content_min_score") == 0.1
    assert getattr(options, "ifrs_d") == 7
    assert getattr(options, "ias_d") == 6
    assert getattr(options, "ifric_d") == 4
    assert getattr(options, "sic_d") == 3
    assert getattr(options, "ps_d") == 2
    assert getattr(options, "ifrs_min_score") == 0.61
    assert getattr(options, "ias_min_score") == 0.54
    assert getattr(options, "ifric_min_score") == 0.50
    assert getattr(options, "sic_min_score") == 0.49
    assert getattr(options, "ps_min_score") == 0.48
    assert getattr(options, "navis_d") == 1
    assert getattr(options, "navis_min_score") == 0.47
    assert getattr(options, "expand_to_section") is True
    assert getattr(options, "expand") == 1
    assert getattr(options, "full_doc_threshold") == 2000
    assert getattr(options, "retrieval_mode") == "documents"


def test_execute_command_dispatches_store_with_scope(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should pass the store scope through to the store command factory."""
    captured_scopes: list[str] = []

    def _create_store_command(**kwargs: object) -> FakeTextCommand:
        captured_scopes.append(str(kwargs["scope"]))
        return FakeTextCommand("store output")

    monkeypatch.setattr("src.cli.create_store_command", _create_store_command)

    args = argparse.Namespace(
        command="store",
        source="/tmp/test.html",
        doc_uid=None,
        scope="documents",
    )

    output = _execute_command(args)

    assert output == "store output"
    assert captured_scopes == ["documents"]


def test_execute_command_dispatches_ingest_with_scope(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should construct IngestCommand with the requested scope."""
    captured_scopes: list[str] = []

    class FakeIngestCommand:
        def __init__(self, scope: str) -> None:
            captured_scopes.append(scope)

        def execute(self) -> str:
            return "ingest output"

    monkeypatch.setattr("src.cli.IngestCommand", FakeIngestCommand)

    args = argparse.Namespace(
        command="ingest",
        scope="sections",
    )

    output = _execute_command(args)

    assert output == "ingest output"
    assert captured_scopes == ["sections"]


def test_main_logs_and_reraises_unhandled_command_exceptions(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should log unexpected command exceptions before re-raising them."""
    captured_messages: list[str] = []

    class FakeParser:
        def parse_args(self) -> argparse.Namespace:
            return argparse.Namespace(command="ingest")

        def print_help(self) -> None:
            return None

    def _raise_command_error(args: argparse.Namespace) -> str:
        del args
        raise RuntimeError("boom")

    def _capture_exception(message: str, *args: object, **kwargs: object) -> None:
        del args, kwargs
        captured_messages.append(message)

    monkeypatch.setattr(cli, "load_dotenv", lambda: None)
    monkeypatch.setattr(cli, "setup_logging", lambda: None)
    monkeypatch.setattr(cli, "_build_parser", lambda: FakeParser())
    monkeypatch.setattr(cli, "_execute_command", _raise_command_error)
    monkeypatch.setattr(cli.logger, "exception", _capture_exception)

    with pytest.raises(RuntimeError, match="boom"):
        cli.main()

    assert captured_messages == ["CLI command failed: ingest"]


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


def test_execute_command_dispatches_retrieve(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the retrieve subcommand."""
    captured_modes: list[str] = []
    captured_ifrs_ds: list[int] = []
    captured_ifrs_min_scores: list[float] = []
    captured_expand_to_section: list[bool] = []

    def _create_retrieve_command(query: str, options: object) -> FakeTextCommand:
        del query
        captured_modes.append(getattr(options, "retrieval_mode"))
        captured_ifrs_ds.append(getattr(options, "ifrs_d"))
        captured_ifrs_min_scores.append(getattr(options, "ifrs_min_score"))
        captured_expand_to_section.append(getattr(options, "expand_to_section"))
        return FakeTextCommand("retrieve output")

    monkeypatch.setattr("src.cli.create_retrieve_command", _create_retrieve_command)
    monkeypatch.setattr("sys.stdin", io.StringIO("Find lease guidance"))

    args = argparse.Namespace(
        command="retrieve",
        k=3,
        d=2,
        doc_min_score=None,
        content_min_score=None,
        ifrs_d=7,
        ias_d=5,
        ifric_d=5,
        sic_d=5,
        ps_d=5,
        navis_d=3,
        ifrs_min_score=0.61,
        ias_min_score=0.55,
        ifric_min_score=0.51,
        sic_min_score=0.51,
        ps_min_score=0.50,
        navis_min_score=0.49,
        expand_to_section=True,
        expand=0,
        full_doc_threshold=0,
        retrieval_mode="documents",
        json=True,
    )

    output = _execute_command(args)

    assert output == "retrieve output"
    assert captured_modes == ["documents"]
    assert captured_ifrs_ds == [7]
    assert captured_ifrs_min_scores == [0.61]
    assert captured_expand_to_section == [True]


def test_execute_command_dispatches_query_documents(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the query-documents subcommand."""
    captured_document_types: list[str] = []

    def _create_query_documents_command(query: str, options: object) -> FakeTextCommand:
        del query
        captured_document_types.append(getattr(options, "document_type"))
        return FakeTextCommand("document output")

    monkeypatch.setattr("src.cli.create_query_documents_command", _create_query_documents_command)
    monkeypatch.setattr("sys.stdin", io.StringIO("Find hedge guidance"))

    args = argparse.Namespace(
        command="query-documents",
        document_type="IFRIC",
        d=3,
        min_score=None,
        json=True,
    )

    output = _execute_command(args)

    assert output == "document output"
    assert captured_document_types == ["IFRIC"]


def test_answer_stdout_text_prefers_raw_response() -> None:
    """CLI stdout should use the raw response when available."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        prompt_b_raw_response="raw response",
        prompt_b_markdown="markdown response",
    )

    assert _answer_stdout_text(result) == "raw response"


def test_retrieve_parser_uses_tuned_document_retrieval_defaults() -> None:
    """Retrieve parser should expose the tuned document-retrieval defaults."""
    parser = _build_parser()

    args = parser.parse_args(["retrieve"])

    assert args.d == 25
    assert args.ifrs_d == 4
    assert args.ias_d == 4
    assert args.ifric_d == 6
    assert args.sic_d == 6
    assert args.ps_d == 1
    assert args.navis_d == 2
    assert args.ifrs_min_score == 0.53
    assert args.ias_min_score == 0.4
    assert args.ifric_min_score == 0.48
    assert args.sic_min_score == 0.4
    assert args.ps_min_score == 0.4
    assert args.navis_min_score == 0.6
    assert args.content_min_score == 0.53


def test_answer_parser_uses_tuned_document_retrieval_defaults() -> None:
    """Answer parser should expose the tuned document-retrieval defaults."""
    parser = _build_parser()

    args = parser.parse_args(["answer"])

    assert args.d == 25
    assert args.ifrs_d == 4
    assert args.ias_d == 4
    assert args.ifric_d == 6
    assert args.sic_d == 6
    assert args.ps_d == 1
    assert args.navis_d == 2
    assert args.ifrs_min_score == 0.53
    assert args.ias_min_score == 0.4
    assert args.ifric_min_score == 0.48
    assert args.sic_min_score == 0.4
    assert args.ps_min_score == 0.4
    assert args.navis_min_score == 0.6
    assert args.content_min_score == 0.53
