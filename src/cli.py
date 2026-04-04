"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from dotenv import load_dotenv

from src.answer_artifacts import save_answer_command_result
from src.commands import AnswerOptions, ChunkCommand, ListCommand, QueryOptions
from src.commands.answer import create_answer_command
from src.commands.query import create_query_command
from src.commands.store import create_store_command
from src.logging_config import setup_logging

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)


def main() -> int:
    """Entry point for the CLI."""
    load_dotenv()
    setup_logging()

    parser = argparse.ArgumentParser(description="IFRS Expert CLI - Document ingestion and management")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    chunk_parser = subparsers.add_parser(
        "chunk",
        help="Parse a PDF file into chunks and output as JSON",
    )
    chunk_parser.add_argument(
        "pdf",
        help="Path to the PDF file to chunk",
    )

    store_parser = subparsers.add_parser(
        "store",
        help="Extract chunks from a PDF and store in the database",
    )
    store_parser.add_argument(
        "pdf",
        help="Path to the PDF file to store",
    )
    store_parser.add_argument(
        "--doc-uid",
        help="Document UID to use (default: PDF filename stem)",
    )

    list_parser = subparsers.add_parser(
        "list",
        help="List documents or chunks in the database",
    )
    list_parser.add_argument(
        "--doc-uid",
        help="Show chunks for a specific document",
    )

    query_parser = subparsers.add_parser(
        "query",
        help="Search for similar chunks using text query (reads query from stdin)",
    )
    query_parser.add_argument(
        "-k",
        "--k",
        type=int,
        default=5,
        help="Number of results to return (default: 5)",
    )
    query_parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON (default is verbose text)",
    )
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
    answer_parser.add_argument(
        "-k",
        "--k",
        type=int,
        default=5,
        help="Number of chunks to retrieve (default: 5)",
    )
    answer_parser.add_argument(
        "--min-score",
        type=float,
        default=None,
        help="Minimum relevance score (-1 to 1). Results below this are excluded. Default: 0.6.",
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
    if args.command == "chunk":
        command = ChunkCommand(pdf_path=Path(args.pdf))
        return command.execute()

    if args.command == "store":
        command = create_store_command(pdf_path=Path(args.pdf), doc_uid=args.doc_uid)
        return command.execute()

    if args.command == "list":
        command = ListCommand(doc_uid=args.doc_uid)
        return command.execute()

    if args.command == "query":
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

    if args.command == "answer":
        return _execute_answer_command(args)

    return f"Error: Unknown command: {args.command}"


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
            expand=args.expand,
            full_doc_threshold=args.full_doc_threshold,
            output_dir=args.output_dir,
            save_all=args.save_all,
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
