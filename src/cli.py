"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Protocol, TypeVar

from dotenv import load_dotenv

from src.answer_artifacts import save_answer_command_result
from src.commands.answer import AnswerOptions, create_answer_command
from src.commands.chunk import ChunkCommand
from src.commands.constants import DEFAULT_SCOPE
from src.commands.ingest import IngestCommand
from src.commands.list import ListCommand
from src.commands.query import QueryOptions, create_query_command
from src.commands.query_documents import QueryDocumentsOptions, create_query_documents_command
from src.commands.query_titles import QueryTitlesOptions, create_query_titles_command
from src.commands.retrieve import RetrieveOptions, create_retrieve_command
from src.commands.store import STORE_SCOPES, StoreCommandOptions, create_store_command
from src.llm.client import get_client
from src.logging_config import setup_logging
from src.models.document import DOCUMENT_TYPES
from src.policy import RetrievalPolicy, load_policy_catalog, resolve_retrieval_policy

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)


def _build_json_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for the shared --json flag."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--json", action="store_true", help="Output results as JSON (default is verbose text)")
    return parser


def _build_policy_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for mandatory policy configuration."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--policy-config",
        type=Path,
        required=True,
        help="Path to retrieval policy YAML file",
    )
    parser.add_argument(
        "--retrieval-policy",
        required=True,
        help="Named retrieval policy to resolve from the catalog",
    )
    return parser


def _build_answer_artifacts_parent_parser() -> argparse.ArgumentParser:
    """Build a parent parser for answer artifact options."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to save intermediate files (prompt_A, response_A, prompt_B, response_B). Artifacts are always saved when this is set.",
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


def _build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI parser."""
    parser = argparse.ArgumentParser(description="IFRS Expert CLI - Document ingestion and management", allow_abbrev=False)
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
        allow_abbrev=False,
    )
    chunk_parser.add_argument("pdf", help="Path to the PDF file to chunk")


def _add_store_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    store_parser = subparsers.add_parser(
        "store",
        help="Extract chunks from a PDF or HTML capture and store them in the database",
        parents=[_build_scope_parent_parser()],
        allow_abbrev=False,
    )
    store_parser.add_argument("source", help="Path to the source file to store (.pdf or .html)")
    store_parser.add_argument(
        "--doc-uid",
        help="Document UID to use for PDF ingestion (default: filename stem)",
    )
    store_parser.add_argument(
        "--force",
        action="store_true",
        help="Force store even when the extracted payload is unchanged",
    )


def _add_ingest_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Scan ~/Downloads/ifrs-expert/ and ingest HTML capture pairs plus PDFs",
        parents=[_build_scope_parent_parser()],
        allow_abbrev=False,
    )
    ingest_parser.add_argument(
        "--force",
        action="store_true",
        help="Force store even when the extracted payload is unchanged",
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
            _build_policy_parent_parser(),
        ],
        allow_abbrev=False,
    )


def _add_query_documents_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    query_documents_parser = subparsers.add_parser(
        "query-documents",
        help="Search for similar documents using document-level embeddings (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_policy_parent_parser(),
        ],
        allow_abbrev=False,
    )
    query_documents_parser.add_argument(
        "--document-type",
        choices=DOCUMENT_TYPES,
        required=True,
        help="Document type to search: IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG, IAS, IFRIC, SIC, PS, or NAVIS.",
    )


def _add_retrieve_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "retrieve",
        help="Run the shared retrieval pipeline without invoking the LLM (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_policy_parent_parser(),
        ],
        allow_abbrev=False,
    )


def _add_query_titles_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "query-titles",
        help="Search for similar section titles (reads query from stdin)",
        parents=[
            _build_json_parent_parser(),
            _build_policy_parent_parser(),
        ],
        allow_abbrev=False,
    )


def _add_answer_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser(
        "answer",
        help="Search for chunks and embed them into a prompt template (reads query from stdin)",
        parents=[
            _build_policy_parent_parser(),
            _build_answer_artifacts_parent_parser(),
        ],
        allow_abbrev=False,
    )


def _add_llm_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    subparsers.add_parser("llm", help="Send a raw prompt directly to the LLM (reads prompt from stdin)", allow_abbrev=False)


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
    options_factory: Callable[[argparse.Namespace, RetrievalPolicy], OptionsT],
) -> str:
    """Execute a stdin-driven command that returns text."""
    input_text = _read_stdin_text()
    try:
        policy = _load_policy(args)
        options = options_factory(args, policy)
    except (FileNotFoundError, ValueError) as error:
        return f"Error: {error}"
    command = command_factory(input_text, options)
    return command.execute()


def _load_policy(args: argparse.Namespace) -> RetrievalPolicy:
    """Load and resolve the selected retrieval policy from CLI args."""
    policy_path = Path(args.policy_config)
    retrieval_policy = str(args.retrieval_policy)
    catalog = load_policy_catalog(policy_path)
    return resolve_retrieval_policy(catalog, retrieval_policy)


def _build_query_options(args: argparse.Namespace, policy: RetrievalPolicy) -> QueryOptions:
    """Build QueryOptions from CLI args."""
    return QueryOptions(
        policy=policy,
        verbose=_is_verbose(args),
    )


def _build_query_documents_options(args: argparse.Namespace, policy: RetrievalPolicy) -> QueryDocumentsOptions:
    """Build QueryDocumentsOptions from CLI args."""
    return QueryDocumentsOptions(
        policy=policy,
        document_type=args.document_type,
        verbose=_is_verbose(args),
    )


def _build_query_titles_options(args: argparse.Namespace, policy: RetrievalPolicy) -> QueryTitlesOptions:
    """Build QueryTitlesOptions from CLI args."""
    return QueryTitlesOptions(
        policy=policy,
        verbose=_is_verbose(args),
    )


def _build_retrieve_options(args: argparse.Namespace, policy: RetrievalPolicy) -> RetrieveOptions:
    """Build RetrieveOptions from CLI args."""
    return RetrieveOptions(
        policy=policy,
        verbose=_is_verbose(args),
    )


def _build_answer_options(args: argparse.Namespace, policy: RetrievalPolicy) -> AnswerOptions:
    """Build AnswerOptions from CLI args."""
    return AnswerOptions(
        policy=policy,
        verbose=_is_verbose(args),
        output_dir=args.output_dir,
    )


def _execute_chunk_command(args: argparse.Namespace) -> str:
    """Execute the chunk command."""
    return ChunkCommand(pdf_path=Path(args.pdf)).execute()


def _execute_store_command(args: argparse.Namespace) -> str:
    """Execute the store command."""
    return create_store_command(
        source_path=Path(args.source),
        options=StoreCommandOptions(
            explicit_doc_uid=args.doc_uid,
            scope=args.scope,
            force_store=getattr(args, "force", False),
        ),
    ).execute()


def _execute_ingest_command(args: argparse.Namespace) -> str:
    """Execute the ingest command."""
    return IngestCommand(
        store_options=StoreCommandOptions(
            scope=args.scope,
            force_store=getattr(args, "force", False),
        ),
    ).execute()


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
    client = get_client()
    return client.generate_text(prompt=prompt)


def _execute_answer_command(args: argparse.Namespace) -> str:
    """Execute the answer command while keeping CLI behavior unchanged."""
    query = _read_stdin_text()
    try:
        policy = _load_policy(args)
        options = _build_answer_options(args, policy)
    except (FileNotFoundError, ValueError) as error:
        return f"Error: {error}"
    command = create_answer_command(query=query, options=options)
    result = command.execute()

    if args.output_dir is not None:
        _save_answer_command_result(result, args.output_dir)

    if result.error:
        return result.error

    return _answer_stdout_text(result)


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
