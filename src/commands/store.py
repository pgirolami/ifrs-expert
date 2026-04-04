"""Store command - extract chunks from a source file and persist them."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.db import ChunkStore, DocumentStore, init_db
from src.extraction import HtmlExtractor, PdfExtractor
from src.interfaces import ChunkStoreProtocol, DocumentStoreProtocol, ExtractorProtocol, VectorStoreProtocol
from src.models.chunk import Chunk
from src.vector.store import VectorStore

logger = logging.getLogger(__name__)

MAX_CHUNK_CHARS = 8000

StoreChunkStore = ChunkStoreProtocol
StoreDocumentStore = DocumentStoreProtocol
StoreVectorStore = VectorStoreProtocol
StoreInitDb = Callable[[], None]


@dataclass
class StoreCommandResult:
    """Structured result for one store operation."""

    status: str
    doc_uid: str
    chunk_count: int
    embedding_count: int
    reason: str | None = None

    def to_stdout(self) -> str:
        """Return the historical CLI-facing text output."""
        if self.status == "failed":
            reason = self.reason or "unknown error"
            return f"Error: {reason}"
        if self.status == "skipped":
            reason = self.reason or "unchanged content"
            return f"Skipped: doc_uid={self.doc_uid} ({reason})"
        return f"Stored {self.chunk_count} chunks and {self.embedding_count} embeddings for doc_uid={self.doc_uid}"


class StoreCommand:
    """Extract chunks from a source file and store them in the database and vector index."""

    def __init__(
        self,
        source_path: Path,
        extractor: ExtractorProtocol,
        chunk_store: StoreChunkStore,
        document_store: StoreDocumentStore,
        vector_store: StoreVectorStore,
        init_db_fn: StoreInitDb,
        explicit_doc_uid: str | None = None,
    ) -> None:
        self.source_path = source_path
        self._extractor = extractor
        self._chunk_store = chunk_store
        self._document_store = document_store
        self._vector_store = vector_store
        self._init_db_fn = init_db_fn
        self._explicit_doc_uid = explicit_doc_uid

    def execute(self) -> str:
        """Execute the store command and return CLI-facing text."""
        return self.execute_result().to_stdout()

    def execute_result(self) -> StoreCommandResult:
        """Execute the store command and return a structured result."""
        if not self.source_path.exists():
            return StoreCommandResult(
                status="failed",
                doc_uid=self._explicit_doc_uid or self.source_path.stem,
                chunk_count=0,
                embedding_count=0,
                reason=f"Source file not found: {self.source_path}",
            )

        try:
            self._init_db_fn()
            extracted_document = self._extractor.extract(
                source_path=self.source_path,
                explicit_doc_uid=self._explicit_doc_uid,
            )
            doc_uid = extracted_document.document.doc_uid
            chunks = extracted_document.chunks

            self._truncate_oversized_chunks(chunks)

            with self._chunk_store as chunk_store:
                existing_chunks = chunk_store.get_chunks_by_doc(doc_uid)
                if self._extractor.skip_if_unchanged and self._payloads_match(existing_chunks, chunks):
                    logger.info(f"Skipping unchanged source for doc_uid={doc_uid}")
                    return StoreCommandResult(
                        status="skipped",
                        doc_uid=doc_uid,
                        chunk_count=len(chunks),
                        embedding_count=0,
                        reason="unchanged content",
                    )

                if existing_chunks:
                    logger.info(f"Replacing {len(existing_chunks)} existing chunks for {doc_uid}")
                    chunk_store.delete_chunks_by_doc(doc_uid)

                chunk_store.insert_chunks(chunks)
                logger.info(f"Stored {len(chunks)} chunks with doc_uid={doc_uid}")

            with self._document_store as document_store:
                document_store.upsert_document(extracted_document.document)

            embeddings_stored = 0
            with self._vector_store as vector_store:
                deleted = vector_store.delete_by_doc(doc_uid)
                if deleted > 0:
                    logger.info(f"Deleted {deleted} existing embeddings for {doc_uid}")

                chunks_with_ids = [chunk for chunk in chunks if chunk.chunk_id is not None]
                if chunks_with_ids:
                    chunk_ids = [chunk.chunk_id for chunk in chunks_with_ids if chunk.chunk_id is not None]
                    texts = [chunk.text for chunk in chunks_with_ids]
                    vector_store.add_embeddings(doc_uid, chunk_ids, texts)
                    embeddings_stored = len(texts)
                    logger.info(f"Stored {embeddings_stored} embeddings for doc_uid={doc_uid}")

            return StoreCommandResult(
                status="stored",
                doc_uid=doc_uid,
                chunk_count=len(chunks),
                embedding_count=embeddings_stored,
            )
        except Exception as error:
            logger.exception(f"Error storing source file: {self.source_path}")
            return StoreCommandResult(
                status="failed",
                doc_uid=self._explicit_doc_uid or self.source_path.stem,
                chunk_count=0,
                embedding_count=0,
                reason=str(error),
            )

    def _truncate_oversized_chunks(self, chunks: list[Chunk]) -> None:
        truncated_count = 0
        for chunk in chunks:
            if len(chunk.text) > MAX_CHUNK_CHARS:
                original_len = len(chunk.text)
                chunk.text = chunk.text[:MAX_CHUNK_CHARS]
                truncated_count += 1
                logger.warning(f"Truncated chunk {chunk.section_path} from {original_len} to {MAX_CHUNK_CHARS} chars")
        if truncated_count > 0:
            logger.info(f"Truncated {truncated_count} oversized chunk(s)")

    def _payloads_match(self, existing_chunks: list[Chunk], new_chunks: list[Chunk]) -> bool:
        if len(existing_chunks) != len(new_chunks):
            return False
        return [self._payload(chunk) for chunk in existing_chunks] == [self._payload(chunk) for chunk in new_chunks]

    def _payload(self, chunk: Chunk) -> tuple[str, str, str, str, str]:
        return (
            chunk.section_path,
            chunk.page_start,
            chunk.page_end,
            chunk.source_anchor,
            chunk.text,
        )


def _default_extractor_for_source(source_path: Path) -> ExtractorProtocol:
    suffix = source_path.suffix.lower()
    if suffix == ".pdf":
        return PdfExtractor()
    if suffix == ".html":
        return HtmlExtractor(sidecar_path=source_path.with_suffix(".json"))
    raise ValueError(f"Unsupported source type: {source_path}")


def create_store_command(
    source_path: Path | None = None,
    doc_uid: str | None = None,
    extractor: ExtractorProtocol | None = None,
    chunk_store: StoreChunkStore | None = None,
    document_store: StoreDocumentStore | None = None,
    vector_store: StoreVectorStore | None = None,
    init_db_fn: StoreInitDb = init_db,
    pdf_path: Path | None = None,
) -> StoreCommand:
    """Create StoreCommand with real dependencies by default.

    The pdf_path parameter is preserved for backward compatibility.
    """
    resolved_source_path = source_path or pdf_path
    if resolved_source_path is None:
        raise TypeError("create_store_command() requires source_path or pdf_path")

    resolved_extractor = extractor or _default_extractor_for_source(resolved_source_path)
    return StoreCommand(
        source_path=resolved_source_path,
        extractor=resolved_extractor,
        chunk_store=chunk_store or ChunkStore(),
        document_store=document_store or DocumentStore(),
        vector_store=vector_store or VectorStore(),
        init_db_fn=init_db_fn,
        explicit_doc_uid=doc_uid,
    )
