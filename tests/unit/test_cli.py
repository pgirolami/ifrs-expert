"""Tests for CLI commands."""

from __future__ import annotations

import argparse
import io
from pathlib import Path

import pytest

from src import cli
from src.cli import _answer_stdout_text, _build_parser, _execute_answer_command, _execute_command, _save_answer_command_result, query_command
from src.models.answer_command_result import AnswerCommandResult, RetrievedChunkHit, RetrievedDocumentHit
from src.models.provenance import Provenance

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
        document_hits=[RetrievedDocumentHit(doc_uid="ifrs-9", score=0.91, document_type="ifrs")],
        chunk_hits=[
            RetrievedChunkHit(
                doc_uid="ifrs-9",
                chunk_number="6.3.1",
                chunk_id="IFRS9_6.3.1",
                score=0.82,
                document_type="ifrs",
                provenance=Provenance.EXPAND_TO_REFERENCED_CHUNK,
            )
        ],
        prompt_a_text="Prompt A content",
        prompt_a_raw_response='{"status": "pass", "approaches": []}',
        prompt_b_text="Prompt B content",
        prompt_b_raw_response=VALID_PROMPT_B_RESPONSE,
        prompt_b_json={
            "assumptions_fr": ["Hypothèse de test"],
            "recommendation": {"answer": "oui", "justification": "Justification de test"},
            "approaches": [],
        },
        prompt_b_memo_markdown="# Markdown answer",
    )

    _save_answer_command_result(result, tmp_path)

    assert (tmp_path / "A-prompt.txt").read_text(encoding="utf-8") == "Prompt A content"
    assert (tmp_path / "A-response.json").read_text(encoding="utf-8") == '{"status": "pass", "approaches": []}'
    assert (tmp_path / "B-prompt.txt").read_text(encoding="utf-8") == "Prompt B content"
    assert '"answer": "oui"' in (tmp_path / "B-response.json").read_text(encoding="utf-8")
    assert (tmp_path / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"
    assert '"document_hits"' in (tmp_path / "document_routing.json").read_text(encoding="utf-8")
    target_chunk_json = (tmp_path / "target_chunk_retrieval.json").read_text(encoding="utf-8")
    assert '"chunks"' in target_chunk_json
    assert f'"provenance": "{Provenance.EXPAND_TO_REFERENCED_CHUNK.value}"' in target_chunk_json


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
        prompt_b_memo_markdown="# Markdown answer",
    )

    monkeypatch.setattr("src.cli.create_answer_command", lambda query, options: FakeAnswerCommand(result))
    monkeypatch.setattr("sys.stdin", io.StringIO("What is IFRS?"))

    args = argparse.Namespace(
        command="answer",
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        k=5,
        d=25,
        min_score=None,
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
        prompt_b_memo_markdown="# Markdown answer",
    )
    output_dir = tmp_path / "new-output-dir"

    monkeypatch.setattr("src.cli.create_answer_command", lambda query, options: FakeAnswerCommand(result))
    monkeypatch.setattr("sys.stdin", io.StringIO("What is IFRS?"))

    args = argparse.Namespace(
        command="answer",
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        k=5,
        d=25,
        min_score=None,
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
        retrieval_mode="text",
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert (output_dir / "B-response.md").read_text(encoding="utf-8") == "# Markdown answer"


def test_execute_answer_command_passes_policy_and_output_options(monkeypatch: pytest.MonkeyPatch) -> None:
    """Answer CLI should pass the policy and output options to AnswerCommand."""
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
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        json=False,
        output_dir=None,
    )

    output = _execute_answer_command(args)

    assert output == VALID_PROMPT_B_RESPONSE
    assert len(captured_options) == 1
    options = captured_options[0]
    assert hasattr(options, "policy")
    assert options.policy is not None
    assert options.verbose is True
    assert options.output_dir is None


def test_execute_command_dispatches_store_with_scope(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should pass the store scope and force flag through to the store command factory."""
    captured_kwargs: list[tuple[str, bool]] = []

    def _create_store_command(**kwargs: object) -> FakeTextCommand:
        options = kwargs["options"]
        captured_kwargs.append((str(options.scope), bool(options.force_store)))
        return FakeTextCommand("store output")

    monkeypatch.setattr("src.cli.create_store_command", _create_store_command)

    args = argparse.Namespace(
        command="store",
        source="/tmp/test.html",
        doc_uid=None,
        scope="documents",
        force=True,
    )

    output = _execute_command(args)

    assert output == "store output"
    assert captured_kwargs == [("documents", True)]


def test_execute_command_dispatches_ingest_with_scope(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should construct IngestCommand with the requested scope and force flag."""
    captured_args: list[tuple[str, bool]] = []

    class FakeIngestCommand:
        def __init__(self, store_options: object) -> None:
            captured_args.append((str(store_options.scope), bool(store_options.force_store)))

        def execute(self) -> str:
            return "ingest output"

    monkeypatch.setattr("src.cli.IngestCommand", FakeIngestCommand)

    args = argparse.Namespace(
        command="ingest",
        scope="sections",
        force=True,
    )

    output = _execute_command(args)

    assert output == "ingest output"
    assert captured_args == [("sections", True)]


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
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        k=5,
        min_score=None,
        json=True,
    )

    output = _execute_command(args)

    assert output == "title output"


def test_execute_command_dispatches_retrieve(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the retrieve subcommand."""
    captured_policies: list[object] = []

    def _create_retrieve_command(query: str, options: object) -> FakeTextCommand:
        del query
        captured_policies.append(options.policy)
        return FakeTextCommand("retrieve output")

    monkeypatch.setattr("src.cli.create_retrieve_command", _create_retrieve_command)
    monkeypatch.setattr("sys.stdin", io.StringIO("Find lease guidance"))

    args = argparse.Namespace(
        command="retrieve",
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        json=True,
    )

    output = _execute_command(args)

    assert output == "retrieve output"
    assert len(captured_policies) == 1
    assert captured_policies[0] is not None


def test_execute_command_dispatches_query_documents(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the query-documents subcommand."""
    captured_document_types: list[str] = []

    def _create_query_documents_command(query: str, options: object) -> FakeTextCommand:
        del query
        captured_document_types.append(options.document_type)
        return FakeTextCommand("document output")

    monkeypatch.setattr("src.cli.create_query_documents_command", _create_query_documents_command)
    monkeypatch.setattr("sys.stdin", io.StringIO("Find hedge guidance"))

    args = argparse.Namespace(
        command="query-documents",
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        document_type="IFRIC",
        d=3,
        min_score=None,
        json=True,
    )

    output = _execute_command(args)

    assert output == "document output"
    assert captured_document_types == ["IFRIC"]


def test_execute_command_dispatches_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should dispatch the llm subcommand and pass raw stdin prompt."""

    class _FakeTextGenerator:
        def generate_text(self, prompt: str) -> str:
            return f"reply:{prompt}"

    monkeypatch.setattr("src.cli.create_default_text_generator", lambda: _FakeTextGenerator())
    monkeypatch.setattr("sys.stdin", io.StringIO("Raw prompt"))

    output = _execute_command(argparse.Namespace(command="llm"))

    assert output == "reply:Raw prompt"


def test_answer_stdout_text_prefers_raw_response() -> None:
    """CLI stdout should use the raw response when available."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        prompt_b_raw_response="raw response",
        prompt_b_memo_markdown="markdown response",
    )

    assert _answer_stdout_text(result) == "raw response"


def test_answer_stdout_text_uses_markdown_when_raw_missing() -> None:
    """CLI stdout should fall back to markdown when raw response is absent."""
    result = AnswerCommandResult(query="test", success=True, prompt_b_memo_markdown="markdown response")
    assert _answer_stdout_text(result) == "markdown response"


def test_answer_stdout_text_returns_empty_string_when_no_payload() -> None:
    """CLI stdout should be empty when no answer payload is present."""
    result = AnswerCommandResult(query="test", success=False)
    assert _answer_stdout_text(result) == ""


def test_execute_command_returns_unknown_command_error() -> None:
    """CLI dispatcher should return explicit error for unsupported commands."""
    output = _execute_command(argparse.Namespace(command="nope"))
    assert output == "Error: Unknown command: nope"


def test_execute_answer_command_returns_policy_load_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """Answer execution should fail fast when policy loading fails."""
    monkeypatch.setattr("src.cli._build_answer_options", lambda args, policy: (_ for _ in ()).throw(ValueError("bad policy")))
    monkeypatch.setattr("src.cli._read_stdin_text", lambda: "What is IFRS?")

    args = argparse.Namespace(
        command="answer",
        policy_config=Path("config/policy.default.yaml"),
        retrieval_policy="standards_only_through_chunks__enriched",
        output_dir=None,
    )

    output = _execute_answer_command(args)

    assert output == "Error: bad policy"


def test_retrieve_parser_requires_policy_config_and_no_inline_defaults() -> None:
    """Retrieve parser should require policy config and leave inline overrides unset."""
    parser = _build_parser()

    args = parser.parse_args(["retrieve", "--policy-config", "config/policy.default.yaml", "--retrieval-policy", "documents2_through_chunks__enriched"])

    assert args.policy_config == Path("config/policy.default.yaml")
    assert args.retrieval_policy == "documents2_through_chunks__enriched"
    assert args.json is False
    assert not hasattr(args, "d")
    assert not hasattr(args, "ifrs_d")
    assert not hasattr(args, "content_min_score")


def test_answer_parser_requires_policy_config_and_no_inline_defaults() -> None:
    """Answer parser should require policy config and leave inline overrides unset."""
    parser = _build_parser()

    args = parser.parse_args(["answer", "--policy-config", "config/policy.default.yaml", "--retrieval-policy", "documents2_through_chunks__enriched"])

    assert args.policy_config == Path("config/policy.default.yaml")
    assert args.retrieval_policy == "documents2_through_chunks__enriched"
    assert args.output_dir is None
    assert not hasattr(args, "d")
    assert not hasattr(args, "ifrs_d")
    assert not hasattr(args, "content_min_score")


def test_store_parser_accepts_force_flag() -> None:
    """Store parser should expose the force flag for unchanged payloads."""
    parser = _build_parser()

    args = parser.parse_args(["store", "--force", "./doc.html"])

    assert args.force is True
    assert args.scope == "all"


def test_ingest_parser_accepts_force_flag() -> None:
    """Ingest parser should expose the force flag for unchanged payloads."""
    parser = _build_parser()

    args = parser.parse_args(["ingest", "--force"])

    assert args.force is True
    assert args.scope == "all"


def test_query_command_returns_error_exit_code(monkeypatch: pytest.MonkeyPatch) -> None:
    """query_command should return non-zero when command output is an error."""
    monkeypatch.setattr("src.cli._execute_command", lambda args: "Error: failed")
    exit_code = query_command(argparse.Namespace(command="query"))
    assert exit_code == 1


def test_query_command_writes_utf8_output(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    """query_command should write UTF-8 output when execution succeeds."""
    monkeypatch.setattr("src.cli._execute_command", lambda args: "succès")
    exit_code = query_command(argparse.Namespace(command="query"))
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "succès" in captured.out
