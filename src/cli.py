"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from dotenv import load_dotenv

from src.answer_artifacts import save_answer_command_result
from src.commands import AnswerOptions, ChunkCommand, IngestCommand, ListCommand, QueryDocumentsOptions, QueryOptions, QueryTitlesOptions, RetrieveOptions
from src.commands.answer import create_answer_command
from src.commands.query import create_query_command
from src.commands.query_documents import create_query_documents_command
from src.commands.query_titles import create_query_titles_command
from src.commands.retrieve import create_retrieve_command
from src.commands.store import STORE_SCOPES, create_store_command
from src.llm.client import get_client
from src.logging_config import setup_logging
from src.models.document import DOCUMENT_TYPES

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)


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
    )
    store_parser.add_argument("source", help="Path to the source file to store (.pdf or .html)")
    store_parser.add_argument(
        "--doc-uid",
        help="Document UID to use for PDF ingestion (default: filename stem)",
    )
    store_parser.add_argument(
        "--scope",
        choices=STORE_SCOPES,
        default="all",
        help="Ingestion scope: all, chunks, sections, or documents (default: all)",
    )


def _add_ingest_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Scan ~/Downloads/ifrs-expert/ and ingest HTML capture pairs plus PDFs",
    )
    ingest_parser.add_argument(
        "--scope",
        choices=STORE_SCOPES,
        default="all",
        help="Ingestion scope: all, chunks, sections, or documents (default: all)",
    )


def _add_list_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    list_parser = subparsers.add_parser("list", help="List documents or chunks in the database")
    list_parser.add_argument("--doc-uid", help="Show chunks for a specific document")


def _add_query_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    query_parser = subparsers.add_parser(
        "query",
        help="Search for similar chunks using text query (reads query from stdin)",
    )
    query_parser.add_argument("-k", "--k", type=int, default=5, help="Number of results to return (default: 5)")
    query_parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")
    query_parser.add_argument(
        "--min-score",
        type=float,
        default=None,
        help="Minimum relevance score (0-1). Results below this are excluded. Default: 0.6.",
    )
    query_parser.add_argument(
        "-e",
        "--expand",
        type=int,
        default=0,
        help="Number of chunks before/after to expand with (default: 0)",
    )
    query_parser.add_argument(
        "-f",
        "--full-doc-threshold",
        type=int,
        default=0,
        help="Include the full document during expansion when its total chunk text size is below this threshold (default: 0)",
    )


def _add_query_documents_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    query_documents_parser = subparsers.add_parser(
        "query-documents",
        help="Search for similar documents using document-level embeddings (reads query from stdin)",
    )
    query_documents_parser.add_argument(
        "--document-type",
        choices=DOCUMENT_TYPES,
        required=True,
        help="Document type to search: IFRS, IAS, IFRIC, SIC, or PS.",
    )
    query_documents_parser.add_argument(
        "-d",
        "--d",
        type=int,
        default=5,
        help="Number of documents to return for the selected document type (default: 5)",
    )
    query_documents_parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")
    query_documents_parser.add_argument(
        "--min-score",
        type=float,
        default=None,
        help="Minimum relevance score (0-1). Results below this are excluded. Default: 0.55.",
    )


def _add_retrieve_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    retrieve_parser = subparsers.add_parser(
        "retrieve",
        help="Run the shared retrieval pipeline without invoking the LLM (reads query from stdin)",
    )
    retrieve_parser.add_argument(
        "-k",
        "--k",
        type=int,
        default=5,
        help="Number of chunks to retrieve per document (default: 5)",
    )
    retrieve_parser.add_argument(
        "-d",
        "--d",
        type=int,
        default=5,
        help="Number of documents to preselect in documents mode (default: 5)",
    )
    retrieve_parser.add_argument(
        "--doc-min-score",
        type=float,
        default=None,
        help="Minimum document-stage score in documents mode. Default: 0.5.",
    )
    retrieve_parser.add_argument(
        "--content-min-score",
        type=float,
        default=None,
        help="Minimum chunk/title-stage score. Default: 0.55.",
    )
    retrieve_parser.add_argument(
        "-e",
        "--expand",
        type=int,
        default=0,
        help="Number of chunks before/after to expand with (default: 0)",
    )
    retrieve_parser.add_argument(
        "-f",
        "--full-doc-threshold",
        type=int,
        default=0,
        help="Include the full document during expansion when its total chunk text size is below this threshold (default: 0)",
    )
    retrieve_parser.add_argument(
        "--retrieval-mode",
        choices=["text", "titles", "documents"],
        default="text",
        help="Retrieval mode to use (default: text)",
    )
    retrieve_parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")


def _add_query_titles_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    query_titles_parser = subparsers.add_parser(
        "query-titles",
        help="Search for similar section titles (reads query from stdin)",
    )
    query_titles_parser.add_argument("-k", "--k", type=int, default=5, help="Number of results to return (default: 5)")
    query_titles_parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")
    query_titles_parser.add_argument(
        "--min-score",
        type=float,
        default=None,
        help="Minimum relevance score (0-1). Results below this are excluded. Default: 0.6.",
    )


def _add_answer_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    answer_parser = subparsers.add_parser(
        "answer",
        help="Search for chunks and embed them into a prompt template (reads query from stdin)",
    )
    answer_parser.add_argument(
        "-e",
        "--expand",
        type=int,
        default=0,
        help="Number of chunks before/after to expand with (default: 0)",
    )
    answer_parser.add_argument(
        "-f",
        "--full-doc-threshold",
        type=int,
        default=0,
        help="Include the full document during expansion when its total chunk text size is below this threshold (default: 0)",
    )
    answer_parser.add_argument("-k", "--k", type=int, default=5, help="Number of chunks to retrieve (default: 5)")
    answer_parser.add_argument(
        "--min-score",
        type=float,
        default=None,
        help="Legacy alias for the content-stage minimum score. Results below this are excluded. Default: 0.55.",
    )
    answer_parser.add_argument(
        "-d",
        "--d",
        type=int,
        default=5,
        help="Number of documents to preselect in documents mode (default: 5)",
    )
    answer_parser.add_argument(
        "--doc-min-score",
        type=float,
        default=None,
        help="Minimum document-stage score in documents mode. Default: 0.5.",
    )
    answer_parser.add_argument(
        "--content-min-score",
        type=float,
        default=None,
        help="Minimum chunk/title-stage score. Default: 0.55.",
    )
    answer_parser.add_argument(
        "--retrieval-mode",
        choices=["text", "titles", "documents"],
        default="text",
        help="Retrieval mode to use before prompting the LLM (default: text)",
    )
    answer_parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to save intermediate files (prompt_A, response_A, prompt_B, response_B)",
    )
    answer_parser.add_argument(
        "--save-all",
        action="store_true",
        help="Save all intermediate prompts and responses to output-dir",
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
    result = _execute_command(args)

    if result.startswith("Error:"):
        logger.error(result)
        sys.stderr.buffer.write(f"{result}\n".encode())
        return 1

    logger.info(f"CLI command completed successfully: {args.command}")
    if not (args.command == "answer" and getattr(args, "save_all", False)):
        sys.stdout.buffer.write(result.encode("utf-8") + b"\n")
    return 0


def _execute_command(args: argparse.Namespace) -> str:
    """Execute the appropriate command based on args."""
    handlers = {
        "chunk": lambda: ChunkCommand(pdf_path=Path(args.pdf)).execute(),
        "store": lambda: create_store_command(source_path=Path(args.source), doc_uid=args.doc_uid, scope=args.scope).execute(),
        "ingest": lambda: IngestCommand(scope=args.scope).execute(),
        "list": lambda: ListCommand(doc_uid=args.doc_uid).execute(),
        "query": lambda: _execute_query_command(args),
        "query-documents": lambda: _execute_query_documents_command(args),
        "query-titles": lambda: _execute_query_titles_command(args),
        "retrieve": lambda: _execute_retrieve_command(args),
        "answer": lambda: _execute_answer_command(args),
        "llm": _execute_llm_command,
    }
    handler = handlers.get(args.command)
    if handler is None:
        return f"Error: Unknown command: {args.command}"
    return handler()


def _execute_query_command(args: argparse.Namespace) -> str:
    """Execute the chunk-query command."""
    query = sys.stdin.read().strip()
    verbose = not getattr(args, "json", False)
    command = create_query_command(
        query=query,
        options=QueryOptions(
            k=args.k,
            min_score=args.min_score,
            verbose=verbose,
            expand=args.expand,
            full_doc_threshold=args.full_doc_threshold,
        ),
    )
    return command.execute()


def _execute_query_documents_command(args: argparse.Namespace) -> str:
    """Execute the document-query command."""
    query = sys.stdin.read().strip()
    verbose = not getattr(args, "json", False)
    command = create_query_documents_command(
        query=query,
        options=QueryDocumentsOptions(
            document_type=args.document_type,
            d=args.d,
            min_score=args.min_score,
            verbose=verbose,
        ),
    )
    return command.execute()


def _execute_retrieve_command(args: argparse.Namespace) -> str:
    """Execute the shared retrieval command."""
    query = sys.stdin.read().strip()
    verbose = not getattr(args, "json", False)
    command = create_retrieve_command(
        query=query,
        options=RetrieveOptions(
            k=args.k,
            d=args.d,
            doc_min_score=args.doc_min_score,
            content_min_score=args.content_min_score,
            verbose=verbose,
            expand=args.expand,
            full_doc_threshold=args.full_doc_threshold,
            retrieval_mode=args.retrieval_mode,
        ),
    )
    return command.execute()


def _execute_query_titles_command(args: argparse.Namespace) -> str:
    """Execute the title-query command."""
    query = sys.stdin.read().strip()
    verbose = not getattr(args, "json", False)
    command = create_query_titles_command(
        query=query,
        options=QueryTitlesOptions(
            k=args.k,
            min_score=args.min_score,
            verbose=verbose,
        ),
    )
    return command.execute()


def _execute_llm_command() -> str:
    """Execute the raw LLM command."""
    prompt = sys.stdin.read()
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

    query = sys.stdin.read().strip()
    command = create_answer_command(
        query=query,
        options=AnswerOptions(
            k=args.k,
            min_score=args.min_score,
            d=getattr(args, "d", 5),
            doc_min_score=getattr(args, "doc_min_score", None),
            content_min_score=getattr(args, "content_min_score", None),
            expand=args.expand,
            full_doc_threshold=args.full_doc_threshold,
            output_dir=args.output_dir,
            save_all=args.save_all,
            retrieval_mode=args.retrieval_mode,
        ),
    )
    result = command.execute()

    if args.save_all and args.output_dir is not None:
        _save_answer_command_result(result, args.output_dir)

    if result.error:
        return result.error

    return _answer_stdout_text(result)


def _get_answer_option_error(args: argparse.Namespace) -> str | None:
    """Validate CLI-only answer options."""
    if getattr(args, "save_all", False) and getattr(args, "output_dir", None) is None:
        return "Error: --save-all requires --output-dir to be specified"

    output_dir = getattr(args, "output_dir", None)
    if output_dir is not None and not output_dir.exists():
        return f"Error: Output directory does not exist: {output_dir}"

    return None


def _save_answer_command_result(result: AnswerCommandResult, output_dir: Path) -> None:
    """Persist answer artifacts using the historical CLI file layout."""
    save_answer_command_result(result=result, output_dir=output_dir)


def _answer_stdout_text(result: AnswerCommandResult) -> str:
    """Build the stdout payload for the answer command."""
    if result.prompt_b_raw_response is not None:
        return result.prompt_b_raw_response

    if result.prompt_b_markdown is not None:
        return result.prompt_b_markdown

    return ""


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
