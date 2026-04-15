"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Protocol, TypeVar

from dotenv import load_dotenv

from src.answer_artifacts import save_answer_command_result
from src.commands import (
    AnswerOptions,
    ChunkCommand,
    IngestCommand,
    ListCommand,
    QueryDocumentsOptions,
    QueryOptions,
    QueryTitlesOptions,
    RetrieveOptions,
)
from src.commands.answer import create_answer_command
from src.commands.constants import (
    DEFAULT_D,
    DEFAULT_D_FOR_IAS_DOCUMENTS,
    DEFAULT_D_FOR_IFRIC_DOCUMENTS,
    DEFAULT_D_FOR_IFRS_DOCUMENTS,
    DEFAULT_D_FOR_NAVIS_DOCUMENTS,
    DEFAULT_D_FOR_PS_DOCUMENTS,
    DEFAULT_D_FOR_SIC_DOCUMENTS,
    DEFAULT_EXPAND,
    DEFAULT_FULL_DOC_THRESHOLD,
    DEFAULT_MIN_SCORE,
    DEFAULT_MIN_SCORE_FOR_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS,
    DEFAULT_QUERY_TITLES_MIN_SCORE,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVAL_MODE,
    DEFAULT_RETRIEVE_CONTENT_MIN_SCORE,
    DEFAULT_RETRIEVE_DOCUMENT_D,
    DEFAULT_RETRIEVE_EXPAND,
    DEFAULT_RETRIEVE_EXPAND_TO_SECTION,
    DEFAULT_SCOPE,
)
from src.commands.query import create_query_command
from src.commands.query_documents import create_query_documents_command
from src.commands.query_titles import create_query_titles_command
from src.commands.retrieve import create_retrieve_command
from src.commands.store import STORE_SCOPES, create_store_command
from src.llm.client import get_client
from src.logging_config import setup_logging
from src.models.document import DOCUMENT_TYPES

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)


def _build_json_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for the shared --json flag."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")
    return parser


def _build_query_limits_parent_parser(
    *,
    k_default: int,
    k_help: str,
    min_score_default: float,
    min_score_help: str,
) -> argparse.ArgumentParser:
    """Build a parent parser for shared k/min-score arguments."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-k", "--k", type=int, default=k_default, help=k_help)
    parser.add_argument(
        "--min-score",
        type=float,
        default=min_score_default,
        help=min_score_help,
    )
    return parser


def _build_document_search_parent_parser(
    *,
    d_default: int,
    d_help: str,
    min_score_default: float,
    min_score_help: str,
) -> argparse.ArgumentParser:
    """Build a parent parser for shared document-search arguments."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", "--d", type=int, default=d_default, help=d_help)
    parser.add_argument(
        "--min-score",
        type=float,
        default=min_score_default,
        help=min_score_help,
    )
    return parser


def _build_expansion_parent_parser(
    *,
    expand_default: int,
    expand_help: str,
    full_doc_threshold_default: int,
) -> argparse.ArgumentParser:
    """Build a parent parser for shared expansion arguments."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--expand-to-section",
        action="store_true",
        default=DEFAULT_RETRIEVE_EXPAND_TO_SECTION,
        help=(f"Expand each selected chunk to its containing section subtree before neighbor/full-doc expansion (default={DEFAULT_RETRIEVE_EXPAND_TO_SECTION})."),
    )
    parser.add_argument(
        "-e",
        "--expand",
        type=int,
        default=expand_default,
        help=expand_help,
    )
    parser.add_argument(
        "-f",
        "--full-doc-threshold",
        type=int,
        default=full_doc_threshold_default,
        help=(f"Include the full document during expansion when its total chunk text size is below this threshold (default: {full_doc_threshold_default})"),
    )
    return parser


def _build_scope_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for shared ingestion scope arguments."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--scope",
        choices=STORE_SCOPES,
        default=DEFAULT_SCOPE,
        help=f"Ingestion scope: all, chunks, sections, or documents (default: {DEFAULT_SCOPE})",
    )
    return parser


def _build_retrieval_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for shared retrieval arguments."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-k",
        "--k",
        type=int,
        default=DEFAULT_RETRIEVAL_K,
        help=f"Number of chunks to retrieve per document (default: {DEFAULT_RETRIEVAL_K})",
    )
    parser.add_argument(
        "-d",
        "--d",
        type=int,
        default=DEFAULT_RETRIEVE_DOCUMENT_D,
        help=(f"Number of documents to preselect in documents mode (default: {DEFAULT_RETRIEVE_DOCUMENT_D})"),
    )
    parser.add_argument(
        "--doc-min-score",
        type=float,
        default=None,
        help="Legacy override for all document-stage score thresholds in documents mode.",
    )
    parser.add_argument(
        "--ifrs-d",
        type=int,
        default=DEFAULT_D_FOR_IFRS_DOCUMENTS,
        help=(f"Maximum IFRS documents to keep before overall capping (default: {DEFAULT_D_FOR_IFRS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ias-d",
        type=int,
        default=DEFAULT_D_FOR_IAS_DOCUMENTS,
        help=(f"Maximum IAS documents to keep before overall capping (default: {DEFAULT_D_FOR_IAS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ifric-d",
        type=int,
        default=DEFAULT_D_FOR_IFRIC_DOCUMENTS,
        help=(f"Maximum IFRIC documents to keep before overall capping (default: {DEFAULT_D_FOR_IFRIC_DOCUMENTS})"),
    )
    parser.add_argument(
        "--sic-d",
        type=int,
        default=DEFAULT_D_FOR_SIC_DOCUMENTS,
        help=(f"Maximum SIC documents to keep before overall capping (default: {DEFAULT_D_FOR_SIC_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ps-d",
        type=int,
        default=DEFAULT_D_FOR_PS_DOCUMENTS,
        help=(f"Maximum PS documents to keep before overall capping (default: {DEFAULT_D_FOR_PS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--navis-d",
        type=int,
        default=DEFAULT_D_FOR_NAVIS_DOCUMENTS,
        help=(f"Maximum NAVIS documents to keep before overall capping (default: {DEFAULT_D_FOR_NAVIS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ifrs-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS,
        help=(f"Minimum IFRS document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ias-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS,
        help=(f"Minimum IAS document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ifric-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS,
        help=(f"Minimum IFRIC document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS})"),
    )
    parser.add_argument(
        "--sic-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS,
        help=(f"Minimum SIC document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS})"),
    )
    parser.add_argument(
        "--ps-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS,
        help=(f"Minimum PS document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--navis-min-score",
        type=float,
        default=DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS,
        help=(f"Minimum NAVIS document score before overall capping (default: {DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS})"),
    )
    parser.add_argument(
        "--content-min-score",
        type=float,
        default=DEFAULT_RETRIEVE_CONTENT_MIN_SCORE,
        help=(f"Minimum chunk/title-stage score. Default: {DEFAULT_RETRIEVE_CONTENT_MIN_SCORE}."),
    )
    parser.add_argument(
        "--retrieval-mode",
        choices=["text", "titles", "documents"],
        default=DEFAULT_RETRIEVAL_MODE,
        help=f"Retrieval mode to use (default: {DEFAULT_RETRIEVAL_MODE})",
    )
    return parser


def _build_answer_min_score_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for the answer-specific min-score alias."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--min-score",
        type=float,
        default=DEFAULT_RETRIEVE_CONTENT_MIN_SCORE,
        help=(f"Legacy alias for the content-stage minimum score. Results below this are excluded. Default: {DEFAULT_RETRIEVE_CONTENT_MIN_SCORE}."),
    )
    return parser


def _build_answer_artifacts_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for answer artifact options."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to save intermediate files (prompt_A, response_A, prompt_B, response_B)",
    )
    parser.add_argument(
        "--save-all",
        action="store_true",
        help="Save all intermediate prompts and responses to output-dir",
    )
    return parser


def _build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI parser."""
    parser = argparse.ArgumentParser(description="IFRS Expert CLI - Document ingestion and management")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    _add_chunk_parser(subparsers)
    _add_store_parser(subparsers)
    _add_ingest_parser(subparsers)
    _add_list_parser(subparsers)
    _add_query_parser(subparsers)
    _add_query_documents_parser(subparsers)
    _add_retrieve_parser(subparsers)
    _add_query_titles_parser(subparsers)
    _add_answer_parser(subparsers)
    _add_llm_parser(subparsers)
    return parser


def _add_chunk_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    chunk_parser = subparsers.add_parser(
        "chunk",
        help="Parse a PDF file into chunks and output as JSON",
    )
    chunk_parser.add_argument("pdf", help="Path to the PDF file to chunk")


def _add_store_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    store_parser = subparsers.add_parser(
        "store",
        help="Extract chunks from a PDF or HTML capture and store them in the database",
        parents=[_build_scope_parent_parser()],
    )
    store_parser.add_argument("source", help="Path to the source file to store (.pdf or .html)")
    store_parser.add_argument(
        "--doc-uid",
        help="Document UID to use for PDF ingestion (default: filename stem)",
    )


def _add_ingest_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "ingest",
        help="Scan ~/Downloads/ifrs-expert/ and ingest HTML capture pairs plus PDFs",
        parents=[_build_scope_parent_parser()],
    )


def _add_list_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    list_parser = subparsers.add_parser("list", help="List documents or chunks in the database")
    list_parser.add_argument("--doc-uid", help="Show chunks for a specific document")


def _add_query_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "query",
        help="Search for similar chunks using text query (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_query_limits_parent_parser(
                k_default=DEFAULT_RETRIEVAL_K,
                k_help=f"Number of results to return (default: {DEFAULT_RETRIEVAL_K})",
                min_score_default=DEFAULT_MIN_SCORE,
                min_score_help=(f"Minimum relevance score (0-1). Results below this are excluded. Default: {DEFAULT_MIN_SCORE}."),
            ),
            _build_expansion_parent_parser(
                expand_default=DEFAULT_EXPAND,
                expand_help=f"Number of chunks before/after to expand with (default: {DEFAULT_EXPAND})",
                full_doc_threshold_default=DEFAULT_FULL_DOC_THRESHOLD,
            ),
        ],
    )


def _add_query_documents_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    query_documents_parser = subparsers.add_parser(
        "query-documents",
        help="Search for similar documents using document-level embeddings (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_document_search_parent_parser(
                d_default=DEFAULT_D,
                d_help=f"Number of documents to return for the selected document type (default: {DEFAULT_D})",
                min_score_default=DEFAULT_MIN_SCORE_FOR_DOCUMENTS,
                min_score_help=(f"Minimum relevance score (0-1). Results below this are excluded. Default: {DEFAULT_MIN_SCORE_FOR_DOCUMENTS}."),
            ),
        ],
    )
    query_documents_parser.add_argument(
        "--document-type",
        choices=DOCUMENT_TYPES,
        required=True,
        help="Document type to search: IFRS, IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG, IAS, IFRIC, SIC, PS, or NAVIS.",
    )


def _add_retrieve_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "retrieve",
        help="Run the shared retrieval pipeline without invoking the LLM (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_retrieval_parent_parser(),
            _build_expansion_parent_parser(
                expand_default=DEFAULT_RETRIEVE_EXPAND,
                expand_help=(f"Number of chunks before/after to expand with (default: {DEFAULT_RETRIEVE_EXPAND})"),
                full_doc_threshold_default=DEFAULT_FULL_DOC_THRESHOLD,
            ),
        ],
    )


def _add_query_titles_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "query-titles",
        help="Search for similar section titles (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_query_limits_parent_parser(
                k_default=DEFAULT_RETRIEVAL_K,
                k_help=f"Number of results to return (default: {DEFAULT_RETRIEVAL_K})",
                min_score_default=DEFAULT_QUERY_TITLES_MIN_SCORE,
                min_score_help=(f"Minimum relevance score (0-1). Results below this are excluded. Default: {DEFAULT_QUERY_TITLES_MIN_SCORE}."),
            ),
        ],
    )


def _add_answer_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "answer",
        help="Search for chunks and embed them into a prompt template (reads query from stdin)",
        parents=[
            _build_retrieval_parent_parser(),
            _build_expansion_parent_parser(
                expand_default=DEFAULT_RETRIEVE_EXPAND,
                expand_help=(f"Number of chunks before/after to expand with (default: {DEFAULT_RETRIEVE_EXPAND})"),
                full_doc_threshold_default=DEFAULT_FULL_DOC_THRESHOLD,
            ),
            _build_answer_min_score_parent_parser(),
            _build_answer_artifacts_parent_parser(),
        ],
    )


def _add_llm_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser("llm", help="Send a raw prompt directly to the LLM (reads prompt from stdin)")


def main() -> int:
    """Entry point for the CLI."""
    load_dotenv()
    setup_logging()

    parser = _build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    logger.info(f"CLI command received: {args.command}")
    try:
        result = _execute_command(args)
    except Exception:
        logger.exception(f"CLI command failed: {args.command}")
        raise

    if result.startswith("Error:"):
        logger.error(result)
        sys.stderr.buffer.write(f"{result}\n".encode())
        return 1

    logger.info(f"CLI command completed successfully: {args.command}")
    if not (args.command == "answer" and getattr(args, "save_all", False)):
        sys.stdout.buffer.write(result.encode("utf-8") + b"\n")
    return 0


class _ExecutableTextCommand(Protocol):
    """Protocol for text-producing commands."""

    def execute(self) -> str:
        """Execute the command and return text output."""
        ...


OptionsT = TypeVar("OptionsT")
TextCommandT = TypeVar("TextCommandT", bound=_ExecutableTextCommand)


def _read_stdin_text(*, strip: bool = True) -> str:
    """Read text from stdin, optionally trimming surrounding whitespace."""
    text = sys.stdin.read()
    if strip:
        return text.strip()
    return text


def _is_verbose(args: argparse.Namespace) -> bool:
    """Return whether JSON output is disabled for the current command."""
    return not getattr(args, "json", False)


def _execute_text_command(
    args: argparse.Namespace,
    *,
    command_factory: Callable[[str, OptionsT], TextCommandT],
    options_factory: Callable[[argparse.Namespace], OptionsT],
) -> str:
    """Execute a stdin-driven command that returns text."""
    input_text = _read_stdin_text()
    command = command_factory(input_text, options_factory(args))
    return command.execute()


def _build_query_options(args: argparse.Namespace) -> QueryOptions:
    """Build QueryOptions from CLI args."""
    return QueryOptions(
        k=args.k,
        min_score=args.min_score,
        verbose=_is_verbose(args),
        expand=args.expand,
        full_doc_threshold=args.full_doc_threshold,
    )


def _build_query_documents_options(args: argparse.Namespace) -> QueryDocumentsOptions:
    """Build QueryDocumentsOptions from CLI args."""
    return QueryDocumentsOptions(
        document_type=args.document_type,
        d=args.d,
        min_score=args.min_score,
        verbose=_is_verbose(args),
    )


def _build_query_titles_options(args: argparse.Namespace) -> QueryTitlesOptions:
    """Build QueryTitlesOptions from CLI args."""
    return QueryTitlesOptions(
        k=args.k,
        min_score=args.min_score,
        verbose=_is_verbose(args),
    )


def _build_retrieve_options(args: argparse.Namespace) -> RetrieveOptions:
    """Build RetrieveOptions from CLI args."""
    return RetrieveOptions(
        k=args.k,
        d=args.d,
        doc_min_score=args.doc_min_score,
        ifrs_d=args.ifrs_d,
        ias_d=args.ias_d,
        ifric_d=args.ifric_d,
        sic_d=args.sic_d,
        ps_d=args.ps_d,
        navis_d=args.navis_d,
        ifrs_min_score=args.ifrs_min_score,
        ias_min_score=args.ias_min_score,
        ifric_min_score=args.ifric_min_score,
        sic_min_score=args.sic_min_score,
        ps_min_score=args.ps_min_score,
        navis_min_score=args.navis_min_score,
        content_min_score=args.content_min_score,
        expand_to_section=args.expand_to_section,
        verbose=_is_verbose(args),
        expand=args.expand,
        full_doc_threshold=args.full_doc_threshold,
        retrieval_mode=args.retrieval_mode,
    )


def _build_answer_options(args: argparse.Namespace) -> AnswerOptions:
    """Build AnswerOptions from CLI args."""
    return AnswerOptions(
        k=args.k,
        min_score=args.min_score,
        d=getattr(args, "d", DEFAULT_RETRIEVE_DOCUMENT_D),
        doc_min_score=getattr(args, "doc_min_score", None),
        ifrs_d=getattr(args, "ifrs_d", DEFAULT_D_FOR_IFRS_DOCUMENTS),
        ias_d=getattr(args, "ias_d", DEFAULT_D_FOR_IAS_DOCUMENTS),
        ifric_d=getattr(args, "ifric_d", DEFAULT_D_FOR_IFRIC_DOCUMENTS),
        sic_d=getattr(args, "sic_d", DEFAULT_D_FOR_SIC_DOCUMENTS),
        ps_d=getattr(args, "ps_d", DEFAULT_D_FOR_PS_DOCUMENTS),
        navis_d=getattr(args, "navis_d", DEFAULT_D_FOR_NAVIS_DOCUMENTS),
        ifrs_min_score=getattr(args, "ifrs_min_score", DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS),
        ias_min_score=getattr(args, "ias_min_score", DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS),
        ifric_min_score=getattr(args, "ifric_min_score", DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS),
        sic_min_score=getattr(args, "sic_min_score", DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS),
        ps_min_score=getattr(args, "ps_min_score", DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS),
        navis_min_score=getattr(args, "navis_min_score", DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS),
        content_min_score=getattr(args, "content_min_score", DEFAULT_RETRIEVE_CONTENT_MIN_SCORE),
        expand_to_section=getattr(args, "expand_to_section", DEFAULT_RETRIEVE_EXPAND_TO_SECTION),
        expand=args.expand,
        full_doc_threshold=args.full_doc_threshold,
        output_dir=args.output_dir,
        save_all=args.save_all,
        retrieval_mode=args.retrieval_mode,
    )


def _execute_chunk_command(args: argparse.Namespace) -> str:
    """Execute the chunk command."""
    return ChunkCommand(pdf_path=Path(args.pdf)).execute()


def _execute_store_command(args: argparse.Namespace) -> str:
    """Execute the store command."""
    return create_store_command(
        source_path=Path(args.source),
        doc_uid=args.doc_uid,
        scope=args.scope,
    ).execute()


def _execute_ingest_command(args: argparse.Namespace) -> str:
    """Execute the ingest command."""
    return IngestCommand(scope=args.scope).execute()


def _execute_list_command(args: argparse.Namespace) -> str:
    """Execute the list command."""
    return ListCommand(doc_uid=args.doc_uid).execute()


def _execute_query_command(args: argparse.Namespace) -> str:
    """Execute the chunk-query command."""
    return _execute_text_command(
        args,
        command_factory=create_query_command,
        options_factory=_build_query_options,
    )


def _execute_query_documents_command(args: argparse.Namespace) -> str:
    """Execute the document-query command."""
    return _execute_text_command(
        args,
        command_factory=create_query_documents_command,
        options_factory=_build_query_documents_options,
    )


def _execute_retrieve_command(args: argparse.Namespace) -> str:
    """Execute the shared retrieval command."""
    return _execute_text_command(
        args,
        command_factory=create_retrieve_command,
        options_factory=_build_retrieve_options,
    )


def _execute_query_titles_command(args: argparse.Namespace) -> str:
    """Execute the title-query command."""
    return _execute_text_command(
        args,
        command_factory=create_query_titles_command,
        options_factory=_build_query_titles_options,
    )


def _execute_llm_command(args: argparse.Namespace) -> str:
    """Execute the raw LLM command."""
    del args
    prompt = _read_stdin_text(strip=False)
    try:
        client = get_client()
        return client.generate_text(prompt=prompt)
    except Exception as e:
        logger.exception("LLM command failed")
        return f"Error: {e}"


def _execute_answer_command(args: argparse.Namespace) -> str:
    """Execute the answer command while keeping CLI behavior unchanged."""
    option_error = _get_answer_option_error(args)
    if option_error:
        return option_error

    query = _read_stdin_text()
    command = create_answer_command(query=query, options=_build_answer_options(args))
    result = command.execute()

    if args.output_dir is not None:
        _save_answer_command_result(result, args.output_dir)

    if result.error:
        return result.error

    return _answer_stdout_text(result)


def _get_answer_option_error(args: argparse.Namespace) -> str | None:
    """Validate CLI-only answer options."""
    if getattr(args, "save_all", False) and getattr(args, "output_dir", None) is None:
        return "Error: --save-all requires --output-dir to be specified"

    return None


def _save_answer_command_result(result: AnswerCommandResult, output_dir: Path) -> None:
    """Persist answer artifacts using the historical CLI file layout."""
    save_answer_command_result(result=result, output_dir=output_dir)


def _answer_stdout_text(result: AnswerCommandResult) -> str:
    """Build the stdout payload for the answer command."""
    if result.prompt_b_raw_response is not None:
        return result.prompt_b_raw_response

    if result.prompt_b_memo_markdown is not None:
        return result.prompt_b_memo_markdown

    return ""


def _execute_command(args: argparse.Namespace) -> str:
    """Execute the appropriate command based on args."""
    handlers: dict[str, Callable[[argparse.Namespace], str]] = {
        "chunk": _execute_chunk_command,
        "store": _execute_store_command,
        "ingest": _execute_ingest_command,
        "list": _execute_list_command,
        "query": _execute_query_command,
        "query-documents": _execute_query_documents_command,
        "query-titles": _execute_query_titles_command,
        "retrieve": _execute_retrieve_command,
        "answer": _execute_answer_command,
        "llm": _execute_llm_command,
    }
    handler = handlers.get(args.command)
    if handler is None:
        return f"Error: Unknown command: {args.command}"
    return handler(args)


def query_command(args: argparse.Namespace) -> int:
    """Backward compatibility wrapper for tests."""
    result = _execute_command(args)
    if result.startswith("Error:"):
        logger.error(result)
        return 1
    sys.stdout.buffer.write(result.encode("utf-8") + b"\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
