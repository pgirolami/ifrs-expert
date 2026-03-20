"""IFRS Expert CLI - Command-line interface for document ingestion and management."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict
from pathlib import Path
from typing import TYPE_CHECKING

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.pdf import extract_chunks
from src.vector import VectorStore

if TYPE_CHECKING:
    from src.models.chunk import Chunk

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def chunk_command(args: argparse.Namespace) -> int:
    """Extract chunks from a PDF file and output as JSON.

    Args:
        args: Parsed command-line arguments containing the PDF path.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    pdf_path = Path(args.pdf)

    if not pdf_path.exists():
        logger.error(f"PDF file not found: {pdf_path}")
        return 1

    try:
        chunks: list[Chunk] = extract_chunks(pdf_path)
        # Output as JSON to stdout
        output: str = json.dumps([asdict(chunk) for chunk in chunks], indent=2, ensure_ascii=False)
        sys.stdout.buffer.write(output.encode("utf-8") + b"\n")
        return 0
    except Exception:
        logger.exception("Error extracting chunks")
        return 1


def store_command(args: argparse.Namespace) -> int:
    """Extract chunks from a PDF and store in the database and vector index.

    Args:
        args: Parsed command-line arguments containing the PDF path and doc_uid.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    pdf_path = Path(args.pdf)
    doc_uid = args.doc_uid or pdf_path.stem

    if not pdf_path.exists():
        logger.error(f"PDF file not found: {pdf_path}")
        return 1

    try:
        # Initialize database if needed
        init_db()

        # Extract chunks from PDF
        logger.info(f"Extracting chunks from {pdf_path}")
        chunks: list[Chunk] = extract_chunks(pdf_path)
        logger.info(f"Extracted {len(chunks)} chunks")

        # Store in database
        with ChunkStore() as store:
            # Delete existing chunks for this document if any
            existing = store.get_chunks_by_doc(doc_uid)
            if existing:
                logger.info(f"Replacing {len(existing)} existing chunks for {doc_uid}")
                store.delete_chunks_by_doc(doc_uid)

            # Insert new chunks
            db_chunks = [DbChunk.from_pdf_chunk(c, doc_uid) for c in chunks]
            ids = store.insert_chunks(db_chunks)
            logger.info(f"Stored {len(ids)} chunks with doc_uid={doc_uid}")

        # Store embeddings in vector index
        with VectorStore() as vector_store:
            # Delete existing embeddings for this document
            deleted = vector_store.delete_by_doc(doc_uid)
            if deleted > 0:
                logger.info(f"Deleted {deleted} existing embeddings for {doc_uid}")

            # Add embeddings (only for chunks with valid IDs)
            valid_chunks = [
                (db_chunks[i], chunks[i])
                for i in range(len(db_chunks))
                if db_chunks[i].chunk_id is not None
            ]
            if valid_chunks:
                chunk_ids: list[int] = [c[0].chunk_id for c in valid_chunks]  # type: ignore[assignment]
                texts = [c[1].text for c in valid_chunks]
                vector_store.add_embeddings(doc_uid, chunk_ids, texts)
                logger.info(f"Stored {len(texts)} embeddings for doc_uid={doc_uid}")

        return 0
    except Exception:
        logger.exception("Error storing chunks")
        return 1


def list_command(args: argparse.Namespace) -> int:
    """List all documents or chunks in the database.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        init_db()

        with ChunkStore() as store:
            if args.doc_uid:
                chunks = store.get_chunks_by_doc(args.doc_uid)
                output = json.dumps(
                    [
                        {
                            "id": c.chunk_id,
                            "doc_uid": c.doc_uid,
                            "section_path": c.section_path,
                            "page_start": c.page_start,
                            "page_end": c.page_end,
                            "text": c.text,
                        }
                        for c in chunks
                    ],
                    indent=2,
                    ensure_ascii=False,
                )
                sys.stdout.buffer.write(output.encode("utf-8") + b"\n")
            else:
                docs = store.get_all_docs()
                output = json.dumps(docs, indent=2)
                sys.stdout.buffer.write(output.encode("utf-8") + b"\n")

        return 0
    except Exception:
        logger.exception("Error listing chunks")
        return 1


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

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    if args.command == "chunk":
        return chunk_command(args)
    if args.command == "store":
        return store_command(args)
    if args.command == "list":
        return list_command(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
