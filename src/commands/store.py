"""Store command - extract chunks from a PDF and store in database and vector index."""

import logging
from pathlib import Path

from src.db import ChunkStore, init_db
from src.models.chunk import Chunk
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
                db_chunks = [DbChunk.from_pdf_chunk(c, self.doc_uid) for c in chunks]
                ids = store.insert_chunks(db_chunks)
                logger.info(f"Stored {len(ids)} chunks with doc_uid={self.doc_uid}")

            # Store embeddings in vector index
            embeddings_stored = 0
            with VectorStore() as vector_store:
                # Delete existing embeddings for this document
                deleted = vector_store.delete_by_doc(self.doc_uid)
                if deleted > 0:
                    logger.info(f"Deleted {deleted} existing embeddings for {self.doc_uid}")

                # Add embeddings (only for chunks with valid IDs)
                valid_chunks = [(db_chunks[i], chunks[i]) for i in range(len(db_chunks)) if db_chunks[i].chunk_id is not None]
                if valid_chunks:
                    chunk_ids = [c[0].chunk_id for c in valid_chunks]  # type: ignore[assignment]
                    texts = [c[1].text for c in valid_chunks]
                    vector_store.add_embeddings(self.doc_uid, chunk_ids, texts)
                    embeddings_stored = len(texts)
                    logger.info(f"Stored {embeddings_stored} embeddings for doc_uid={self.doc_uid}")

            return f"Stored {len(chunks)} chunks and {embeddings_stored} embeddings for doc_uid={self.doc_uid}"
        except Exception as e:
            logger.exception("Error storing chunks")
            return f"Error: {e}"
