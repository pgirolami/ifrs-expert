"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

# Reduce noise from HuggingFace/sentence-transformers
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def main() -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="IFRS Expert CLI - Document ingestion and management"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Chunk command
    chunk_parser = subparsers.add_parser(
        "chunk",
        help="Parse a PDF file into chunks and output as JSON",
    )
    chunk_parser.add_argument(
        "pdf",
        help="Path to the PDF file to chunk",
    )

    # Store command
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

    # List command
    list_parser = subparsers.add_parser(
        "list",
        help="List documents or chunks in the database",
    )
    list_parser.add_argument(
        "--doc-uid",
        help="Show chunks for a specific document",
    )

    # Query command
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
        help="Minimum relevance score (0-1). Results below this are excluded.",
    )
    query_parser.add_argument(
        "-e",
        "--expand",
        type=int,
        default=0,
        help="Number of chunks before/after to expand with (default: 0)",
    )

    # Answer command
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
        help="Minimum relevance score (0-1). Results below this are excluded.",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    # Execute command and output result
    result = _execute_command(args)

    # Handle result
    if result.startswith("Error:"):
        logger.error(result)
        return 1

    # Output result to stdout
    sys.stdout.buffer.write(result.encode("utf-8") + b"\n")
    return 0


def _execute_command(args: argparse.Namespace) -> str:
    """Execute the appropriate command based on args."""
    from src.commands import AnswerCommand, ChunkCommand, ListCommand, QueryCommand, StoreCommand

    if args.command == "chunk":
        command = ChunkCommand(pdf_path=Path(args.pdf))
    elif args.command == "store":
        command = StoreCommand(pdf_path=Path(args.pdf), doc_uid=args.doc_uid)
    elif args.command == "list":
        command = ListCommand(doc_uid=args.doc_uid)
    elif args.command == "query":
        # Read query from stdin
        query = sys.stdin.read().strip()
        verbose = not getattr(args, "json", False)
        command = QueryCommand(
            query=query,
            k=args.k,
            min_score=args.min_score,
            verbose=verbose,
            expand=args.expand,
        )
    elif args.command == "answer":
        # Read query from stdin
        query = sys.stdin.read().strip()
        command = AnswerCommand(
            query=query,
            k=args.k,
            min_score=args.min_score,
            expand=args.expand,
        )
    else:
        return f"Error: Unknown command: {args.command}"

    return command.execute()


# Keep backward compatibility - expose query_command for tests
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
