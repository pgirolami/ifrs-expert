"""Store command - extract chunks from a PDF and store in database and vector index."""

import logging
from pathlib import Path

from src.db import ChunkStore, init_db
from src.pdf import extract_chunks
from src.vector import VectorStore

logger = logging.getLogger(__name__)

MAX_CHUNK_CHARS = 2000


class StoreCommand:
    """Extract chunks from a PDF and store in the database and vector index."""

    def __init__(self, pdf_path: Path, doc_uid: str | None = None) -> None:
        """Initialize the store command."""
        self.pdf_path = pdf_path
        self.doc_uid = doc_uid or pdf_path.stem

    def execute(self) -> str:
        """Execute the store command - extract and store chunks."""
        if not self.pdf_path.exists():
            return f"Error: PDF file not found: {self.pdf_path}"

        try:
            # Initialize database if needed
            init_db()

            # Extract chunks from PDF
            logger.info(f"Extracting chunks from {self.pdf_path}")
            chunks = extract_chunks(self.pdf_path)
            logger.info(f"Extracted {len(chunks)} chunks")

            # Set doc_uid on all chunks (PDF extraction may return empty doc_uid)
            for chunk in chunks:
                chunk.doc_uid = self.doc_uid

            # Truncate oversized chunks
            truncated_count = 0
            for chunk in chunks:
                if len(chunk.text) > MAX_CHUNK_CHARS:
                    original_len = len(chunk.text)
                    chunk.text = chunk.text[:MAX_CHUNK_CHARS]
                    truncated_count += 1
                    logger.warning(f"Truncated chunk {chunk.section_path} from {original_len} to {MAX_CHUNK_CHARS} chars")
            if truncated_count > 0:
                logger.info(f"Truncated {truncated_count} oversized chunk(s)")

            # Store in database
            with ChunkStore() as store:
                # Delete existing chunks for this document if any
                existing = store.get_chunks_by_doc(self.doc_uid)
                if existing:
                    logger.info(f"Replacing {len(existing)} existing chunks for {self.doc_uid}")
                    store.delete_chunks_by_doc(self.doc_uid)

                # Insert new chunks
                ids = store.insert_chunks(chunks)
                logger.info(f"Stored {len(ids)} chunks with doc_uid={self.doc_uid}")

            # Store embeddings in vector index
            embeddings_stored = 0
            with VectorStore() as vector_store:
                # Delete existing embeddings for this document
                deleted = vector_store.delete_by_doc(self.doc_uid)
                if deleted > 0:
                    logger.info(f"Deleted {deleted} existing embeddings for {self.doc_uid}")

                # Add embeddings (only for chunks with valid IDs)
                chunks_with_ids = [c for c in chunks if c.chunk_id is not None]
                if chunks_with_ids:
                    chunk_ids = [c.chunk_id for c in chunks_with_ids]
                    texts = [c.text for c in chunks_with_ids]
                    vector_store.add_embeddings(self.doc_uid, chunk_ids, texts)
                    embeddings_stored = len(texts)
                    logger.info(f"Stored {embeddings_stored} embeddings for doc_uid={self.doc_uid}")

            return f"Stored {len(chunks)} chunks and {embeddings_stored} embeddings for doc_uid={self.doc_uid}"
        except Exception as e:
            logger.exception("Error storing chunks")
            return f"Error: {e}"
