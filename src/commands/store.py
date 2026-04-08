"""Store command - extract chunks from a source file and persist them."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.section_filter import filter_extraction
from src.db import ChunkStore, DocumentStore, SectionStore, init_db
from src.extraction import HtmlExtractor, PdfExtractor
from src.interfaces import (
    ChunkStoreProtocol,
    DocumentStoreProtocol,
    ExtractorProtocol,
    SectionStoreProtocol,
    TitleVectorStoreProtocol,
    VectorStoreProtocol,
)
from src.vector.store import VectorStore
from src.vector.title_store import TitleVectorStore

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.chunk import Chunk
    from src.models.extraction import ExtractedDocument
    from src.models.section import SectionRecord

logger = logging.getLogger(__name__)

MAX_CHUNK_CHARS = 8000

StoreChunkStore = ChunkStoreProtocol
StoreDocumentStore = DocumentStoreProtocol
StoreSectionStore = SectionStoreProtocol
StoreVectorStore = VectorStoreProtocol
StoreTitleVectorStore = TitleVectorStoreProtocol
StoreInitDb = Callable[[], None]


@dataclass(frozen=True)
class StoreDependencies:
    """Dependencies required by StoreCommand."""

    chunk_store: StoreChunkStore
    document_store: StoreDocumentStore
    vector_store: StoreVectorStore
    init_db_fn: StoreInitDb
    section_store: StoreSectionStore | None = None
    title_vector_store: StoreTitleVectorStore | None = None


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
        dependencies: StoreDependencies,
        explicit_doc_uid: str | None = None,
    ) -> None:
        """Initialize the store command with its source, extractor, and storage dependencies."""
        self.source_path = source_path
        self._extractor = extractor
        self._dependencies = dependencies
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
            self._dependencies.init_db_fn()
            extracted_document = self._extractor.extract(
                source_path=self.source_path,
                explicit_doc_uid=self._explicit_doc_uid,
            )
            doc_uid = extracted_document.document.doc_uid

            # Apply section filtering to exclude unwanted sections and chunks
            filter_result = filter_extraction(
                chunks=extracted_document.chunks,
                sections=extracted_document.sections,
                closure_rows=extracted_document.section_closure_rows,
            )

            if filter_result.excluded_section_count > 0:
                sample_titles = filter_result.excluded_section_titles[:10]
                logger.info(f"Excluded {filter_result.excluded_section_count} section(s) based on title filters: {sample_titles}")
            if filter_result.excluded_chunk_count > 0:
                sample_ids = filter_result.excluded_chunk_ids[:10]
                logger.info(f"Excluded {filter_result.excluded_chunk_count} chunk(s) based on content filters: {sample_ids}")

            chunks = filter_result.chunks
            sections = filter_result.sections
            closure_rows = filter_result.closure_rows

            # Update the extracted document with filtered data
            extracted_document.sections = sections
            extracted_document.section_closure_rows = closure_rows

            self._truncate_oversized_chunks(chunks)

            skip_result = self._store_chunks(doc_uid=doc_uid, chunks=chunks, sections=extracted_document.sections)
            if skip_result is not None:
                return skip_result

            self._store_sections(doc_uid=doc_uid, extracted_document=extracted_document)
            with self._dependencies.document_store as document_store:
                document_store.upsert_document(extracted_document.document)

            embeddings_stored = self._store_chunk_embeddings(doc_uid=doc_uid, chunks=chunks)
            self._store_title_embeddings(doc_uid=doc_uid, sections=extracted_document.sections)

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

    def _store_chunks(self, doc_uid: str, chunks: list[Chunk], sections: list[SectionRecord]) -> StoreCommandResult | None:
        with self._dependencies.chunk_store as chunk_store:
            existing_chunks = chunk_store.get_chunks_by_doc(doc_uid)
            existing_sections = self._get_existing_sections(doc_uid)
            should_skip = self._extractor.skip_if_unchanged and self._payloads_match(existing_chunks, chunks) and self._section_payloads_match(existing_sections, sections)
            if should_skip:
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
        return None

    def _store_sections(self, doc_uid: str, extracted_document: ExtractedDocument) -> None:
        if self._dependencies.section_store is None:
            return
        with self._dependencies.section_store as section_store:
            deleted_sections = section_store.delete_sections_by_doc(doc_uid)
            if deleted_sections > 0:
                logger.info(f"Deleted {deleted_sections} existing sections for {doc_uid}")
            section_store.insert_sections(extracted_document.sections)
            section_store.insert_closure_rows(extracted_document.section_closure_rows)
            logger.info(f"Stored {len(extracted_document.sections)} sections with doc_uid={doc_uid}")

    def _store_chunk_embeddings(self, doc_uid: str, chunks: list[Chunk]) -> int:
        embeddings_stored = 0
        with self._dependencies.vector_store as vector_store:
            deleted = vector_store.delete_by_doc(doc_uid)
            if deleted > 0:
                logger.info(f"Deleted {deleted} existing embeddings for {doc_uid}")

            chunks_with_ids = [chunk for chunk in chunks if chunk.id is not None]
            if chunks_with_ids:
                chunk_ids = [chunk.id for chunk in chunks_with_ids if chunk.id is not None]
                texts = [chunk.text for chunk in chunks_with_ids]
                vector_store.add_embeddings(doc_uid, chunk_ids, texts)
                embeddings_stored = len(texts)
                logger.info(f"Stored {embeddings_stored} embeddings for doc_uid={doc_uid}")
        return embeddings_stored

    def _store_title_embeddings(self, doc_uid: str, sections: list[SectionRecord]) -> None:
        if self._dependencies.title_vector_store is None:
            return
        with self._dependencies.title_vector_store as title_vector_store:
            deleted_titles = title_vector_store.delete_by_doc(doc_uid)
            if deleted_titles > 0:
                logger.info(f"Deleted {deleted_titles} existing title embeddings for {doc_uid}")
            if sections:
                title_vector_store.add_embeddings(
                    doc_uid,
                    [section.section_id for section in sections],
                    [section.embedding_text for section in sections],
                )
                logger.info(f"Stored {len(sections)} title embeddings for doc_uid={doc_uid}")

    def _truncate_oversized_chunks(self, chunks: list[Chunk]) -> None:
        truncated_count = 0
        for chunk in chunks:
            if len(chunk.text) > MAX_CHUNK_CHARS:
                original_len = len(chunk.text)
                chunk.text = chunk.text[:MAX_CHUNK_CHARS]
                truncated_count += 1
                logger.warning(f"Truncated chunk {chunk.chunk_number} from {original_len} to {MAX_CHUNK_CHARS} chars")
        if truncated_count > 0:
            logger.info(f"Truncated {truncated_count} oversized chunk(s)")

    def _get_existing_sections(self, doc_uid: str) -> list[SectionRecord]:
        if self._dependencies.section_store is None:
            return []
        with self._dependencies.section_store as section_store:
            return list(section_store.get_sections_by_doc(doc_uid))

    def _payloads_match(self, existing_chunks: list[Chunk], new_chunks: list[Chunk]) -> bool:
        return [self._payload(chunk) for chunk in existing_chunks] == [self._payload(chunk) for chunk in new_chunks]

    def _payload(self, chunk: Chunk) -> tuple[str, str, str, str, str, str | None]:
        return (
            chunk.chunk_number,
            chunk.page_start,
            chunk.page_end,
            chunk.chunk_id,
            chunk.text,
            chunk.containing_section_id,
        )

    def _section_payloads_match(self, existing_sections: list[SectionRecord], new_sections: list[SectionRecord]) -> bool:
        return [self._section_payload(section) for section in existing_sections] == [self._section_payload(section) for section in new_sections]

    def _section_payload(self, section: SectionRecord) -> tuple[str, str | None, str, str]:
        return (section.section_id, section.parent_section_id, section.title, section.embedding_text)


def build_store_dependencies() -> StoreDependencies:
    """Build the production dependencies for StoreCommand."""
    return StoreDependencies(
        chunk_store=ChunkStore(),
        document_store=DocumentStore(),
        vector_store=VectorStore(),
        init_db_fn=init_db,
        section_store=SectionStore(),
        title_vector_store=TitleVectorStore(),
    )


def _default_extractor_for_source(source_path: Path) -> ExtractorProtocol:
    """Select the default extractor for a source path based on its file suffix."""
    suffix = source_path.suffix.lower()
    if suffix == ".pdf":
        return PdfExtractor()
    if suffix == ".html":
        return HtmlExtractor(sidecar_path=source_path.with_suffix(".json"))

    message = f"Unsupported source type: {source_path}"
    raise ValueError(message)


def create_store_command(
    source_path: Path | None = None,
    doc_uid: str | None = None,
    extractor: ExtractorProtocol | None = None,
    dependencies: StoreDependencies | None = None,
    pdf_path: Path | None = None,
) -> StoreCommand:
    """Create StoreCommand with real dependencies by default.

    The pdf_path parameter is preserved for backward compatibility.
    """
    resolved_source_path = source_path or pdf_path
    if resolved_source_path is None:
        message = "create_store_command() requires source_path or pdf_path"
        raise TypeError(message)

    resolved_dependencies = dependencies or build_store_dependencies()
    resolved_extractor = extractor or _default_extractor_for_source(resolved_source_path)
    return StoreCommand(
        source_path=resolved_source_path,
        extractor=resolved_extractor,
        dependencies=resolved_dependencies,
        explicit_doc_uid=doc_uid,
    )
