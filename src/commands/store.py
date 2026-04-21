"""Store command - extract chunks from a source file and persist them."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING

from src.commands.section_filter import filter_extraction
from src.db import ChunkStore, DocumentStore, SectionStore, init_db
from src.extraction import HtmlExtractor, PdfExtractor
from src.interfaces import (
    ChunkStoreProtocol,
    DocumentStoreProtocol,
    DocumentVectorStoreProtocol,
    SectionStoreProtocol,
    TitleVectorStoreProtocol,
    VectorStoreProtocol,
)
from src.models.document import resolve_document_kind_from_document_type, resolve_document_type_from_doc_uid
from src.retrieval.document_profile_builder import DocumentProfileBuilder
from src.vector.constants import MAX_EMBEDDING_TEXT_CHARS
from src.vector.document_store import DocumentVectorStore
from src.vector.store import VectorStore
from src.vector.title_store import TitleVectorStore

if TYPE_CHECKING:
    from src.interfaces import ExtractorProtocol
    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.extraction import ExtractedDocument
    from src.models.section import SectionRecord

logger = logging.getLogger(__name__)

STORE_SCOPES: tuple[str, ...] = ("all", "chunks", "documents", "sections")

StoreChunkStore = ChunkStoreProtocol
StoreDocumentStore = DocumentStoreProtocol
StoreSectionStore = SectionStoreProtocol
StoreVectorStore = VectorStoreProtocol
StoreTitleVectorStore = TitleVectorStoreProtocol
StoreDocumentVectorStore = DocumentVectorStoreProtocol
StoreInitDb = Callable[[], None]

_DOCUMENT_EMBEDDING_REPAIR_METRICS: dict[str, int] = {"count": 0}


def _increment_document_embedding_repair_count() -> int:
    """Increment and return the process-local repaired document embedding count."""
    _DOCUMENT_EMBEDDING_REPAIR_METRICS["count"] += 1
    return _DOCUMENT_EMBEDDING_REPAIR_METRICS["count"]


@dataclass(frozen=True)
class StoreDependencies:
    """Dependencies required by StoreCommand."""

    chunk_store: StoreChunkStore
    document_store: StoreDocumentStore
    vector_store: StoreVectorStore
    init_db_fn: StoreInitDb
    section_store: StoreSectionStore | None = None
    title_vector_store: StoreTitleVectorStore | None = None
    document_vector_store: StoreDocumentVectorStore | None = None


@dataclass(frozen=True)
class StoreCommandOptions:
    """Options that control how one source is stored."""

    explicit_doc_uid: str | None = None
    scope: str = "all"
    force_store: bool = False


@dataclass(frozen=True)
class StorePayloadSnapshot:
    """Scoped payload snapshot used for skip-if-unchanged comparisons."""

    chunks: list[Chunk]
    sections: list[SectionRecord]
    document: DocumentRecord | None


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
        options: StoreCommandOptions | None = None,
        **legacy_kwargs: object,
    ) -> None:
        """Initialize the store command with its source, extractor, and storage dependencies."""
        resolved_options = _resolve_store_command_options(options=options, legacy_kwargs=legacy_kwargs)
        self.source_path = source_path
        self._extractor = extractor
        self._dependencies = dependencies
        self._explicit_doc_uid = resolved_options.explicit_doc_uid
        self._scope = resolved_options.scope
        self._force_store = resolved_options.force_store
        self._document_profile_builder = DocumentProfileBuilder()

    def execute(self) -> str:
        """Execute the store command and return CLI-facing text."""
        return self.execute_result().to_stdout()

    def execute_result(self) -> StoreCommandResult:
        """Execute the store command and return a structured result."""
        logger.info(f"Starting store command for source_path={self.source_path}, scope={self._scope}, explicit_doc_uid={self._explicit_doc_uid}, extractor={type(self._extractor).__name__}")

        scope_error = self._get_scope_error()
        if scope_error is not None:
            logger.error(f"Store command rejected invalid scope={self._scope}: {scope_error}")
            return StoreCommandResult(
                status="failed",
                doc_uid=self._explicit_doc_uid or self.source_path.stem,
                chunk_count=0,
                embedding_count=0,
                reason=scope_error,
            )

        if not self.source_path.exists():
            logger.error(f"Store command source file does not exist: {self.source_path}")
            return StoreCommandResult(
                status="failed",
                doc_uid=self._explicit_doc_uid or self.source_path.stem,
                chunk_count=0,
                embedding_count=0,
                reason=f"Source file not found: {self.source_path}",
            )

        try:
            init_started_at = perf_counter()
            logger.info(f"Initializing database dependencies for source_path={self.source_path}")
            self._dependencies.init_db_fn()
            logger.info(f"Initialized database dependencies for source_path={self.source_path} in {_elapsed_ms(init_started_at):.2f}ms")

            extraction_started_at = perf_counter()
            logger.info(f"Starting extraction for source_path={self.source_path}")
            extracted_document = self._extractor.extract(
                source_path=self.source_path,
                explicit_doc_uid=self._explicit_doc_uid,
            )
            doc_uid = self._finalize_extracted_document(extracted_document)
            logger.info(
                f"Extraction completed for source_path={self.source_path} in {_elapsed_ms(extraction_started_at):.2f}ms; "
                f"doc_uid={doc_uid}, document_type={extracted_document.document.document_type}, "
                f"raw_chunk_count={len(extracted_document.chunks)}, raw_section_count={len(extracted_document.sections)}, "
                f"raw_closure_row_count={len(extracted_document.section_closure_rows)}"
            )

            self._truncate_oversized_chunks(extracted_document.chunks)

            filter_started_at = perf_counter()
            logger.info(f"Applying extraction filters for doc_uid={doc_uid}")
            filter_result = filter_extraction(
                chunks=extracted_document.chunks,
                sections=extracted_document.sections,
                closure_rows=extracted_document.section_closure_rows,
            )
            logger.info(
                f"Applied extraction filters for doc_uid={doc_uid} in {_elapsed_ms(filter_started_at):.2f}ms; "
                f"kept_chunks={len(filter_result.chunks)}, kept_sections={len(filter_result.sections)}, "
                f"kept_closure_rows={len(filter_result.closure_rows)}, "
                f"excluded_chunks={filter_result.excluded_chunk_count}, excluded_sections={filter_result.excluded_section_count}"
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

            profile_started_at = perf_counter()
            logger.info(f"Building document profile for doc_uid={doc_uid} from filtered chunks and sections")
            built_document_profile = self._document_profile_builder.build(
                document=extracted_document.document,
                chunks=chunks,
                sections=sections,
                section_closure_rows=closure_rows,
                toc_sections=sections,
            )
            extracted_document.document = built_document_profile.document
            logger.info(f"Built document profile for doc_uid={doc_uid} in {_elapsed_ms(profile_started_at):.2f}ms")

            # Update the extracted document with filtered data for persistence.
            extracted_document.sections = sections
            extracted_document.section_closure_rows = closure_rows
            logger.info(
                f"Document representation ready for doc_uid={doc_uid}; "
                f"background_chars={len(extracted_document.document.background_text or '')}, "
                f"issue_chars={len(extracted_document.document.issue_text or '')}, "
                f"objective_chars={len(extracted_document.document.objective_text or '')}, "
                f"scope_chars={len(extracted_document.document.scope_text or '')}, "
                f"intro_chars={len(extracted_document.document.intro_text or '')}, "
                f"toc_chars={len(extracted_document.document.toc_text or '')}, "
                f"embedding_chars={len(built_document_profile.embedding_text)}"
            )

            logger.info(f"Preparing persistence for doc_uid={doc_uid}; stores_chunks={self._stores_chunks()}, stores_sections={self._stores_sections()}, stores_documents={self._stores_documents()}")
            skip_result = self._store_chunks(
                doc_uid=doc_uid,
                chunks=chunks,
                sections=extracted_document.sections,
                document=extracted_document.document,
                document_embedding_text=built_document_profile.embedding_text,
            )
            if skip_result is not None:
                return skip_result

            persistence_started_at = perf_counter()
            embeddings_stored = self._store_selected_outputs(
                doc_uid=doc_uid,
                extracted_document=extracted_document,
                chunks=chunks,
                document_embedding_text=built_document_profile.embedding_text,
            )
            logger.info(f"Finished persistence for doc_uid={doc_uid} in {_elapsed_ms(persistence_started_at):.2f}ms; stored_chunks={len(chunks)}, stored_sections={len(extracted_document.sections)}, stored_embeddings={embeddings_stored}")

            logger.info(f"Store command completed successfully for doc_uid={doc_uid}")
            return StoreCommandResult(
                status="stored",
                doc_uid=doc_uid,
                chunk_count=len(chunks),
                embedding_count=embeddings_stored,
            )
        except (OSError, RuntimeError, ValueError) as error:
            logger.exception(f"Error storing source file: {self.source_path}")
            return StoreCommandResult(
                status="failed",
                doc_uid=self._explicit_doc_uid or self.source_path.stem,
                chunk_count=0,
                embedding_count=0,
                reason=str(error),
            )

    def _store_chunks(
        self,
        doc_uid: str,
        chunks: list[Chunk],
        sections: list[SectionRecord],
        document: DocumentRecord,
        document_embedding_text: str,
    ) -> StoreCommandResult | None:
        existing_chunks = self._get_existing_chunks(doc_uid) if self._stores_chunks() else []
        existing_sections = self._get_existing_sections(doc_uid) if self._stores_sections() else []
        existing_document = self._get_existing_document(doc_uid) if self._stores_documents() else None
        logger.info(
            f"Loaded existing persisted state for doc_uid={doc_uid}; "
            f"existing_chunks={len(existing_chunks)}, existing_sections={len(existing_sections)}, "
            f"existing_document={'yes' if existing_document is not None else 'no'}, "
            f"new_chunks={len(chunks)}, new_sections={len(sections)}, new_document=yes"
        )
        should_skip = self._should_skip(
            existing_snapshot=StorePayloadSnapshot(
                chunks=existing_chunks,
                sections=existing_sections,
                document=existing_document,
            ),
            new_snapshot=StorePayloadSnapshot(
                chunks=chunks,
                sections=sections,
                document=document,
            ),
        )
        if should_skip:
            repaired_result = self._repair_missing_document_embedding_if_needed(
                doc_uid=doc_uid,
                chunk_count=len(chunks),
                embedding_text=document_embedding_text,
            )
            if repaired_result is not None:
                return repaired_result
            logger.info(f"Skipping unchanged source for doc_uid={doc_uid}")
            return StoreCommandResult(
                status="skipped",
                doc_uid=doc_uid,
                chunk_count=len(chunks),
                embedding_count=0,
                reason="unchanged content",
            )

        logger.info(f"Detected changes for doc_uid={doc_uid}; continuing with persistence")

        if not self._stores_chunks():
            return None

        with self._dependencies.chunk_store as chunk_store:
            if existing_chunks:
                logger.info(f"Replacing {len(existing_chunks)} existing chunks for {doc_uid}")
                chunk_store.delete_chunks_by_doc(doc_uid)

            chunk_store.insert_chunks(chunks)
            logger.info(f"Stored {len(chunks)} chunks with doc_uid={doc_uid}")
        return None

    def _finalize_extracted_document(self, extracted_document: ExtractedDocument) -> str:
        """Apply late extraction normalization before persistence."""
        doc_uid = extracted_document.document.doc_uid
        if extracted_document.document.document_type is None:
            extracted_document.document.document_type = resolve_document_type_from_doc_uid(doc_uid)
        if extracted_document.document.document_type is None:
            message = f"Could not resolve exact document_type for doc_uid={doc_uid}"
            raise ValueError(message)
        if extracted_document.document.document_kind is None:
            extracted_document.document.document_kind = resolve_document_kind_from_document_type(
                extracted_document.document.document_type,
            )
        if extracted_document.document.document_kind is None:
            message = f"Could not resolve document_kind for doc_uid={doc_uid}, document_type={extracted_document.document.document_type}"
            raise ValueError(message)
        return doc_uid

    def _store_sections(self, doc_uid: str, extracted_document: ExtractedDocument) -> dict[str, int]:
        if self._dependencies.section_store is None:
            return {}
        with self._dependencies.section_store as section_store:
            deleted_sections = section_store.delete_sections_by_doc(doc_uid)
            if deleted_sections > 0:
                logger.info(f"Deleted {deleted_sections} existing sections for {doc_uid}")
            section_store.insert_sections(extracted_document.sections)
            section_store.insert_closure_rows(doc_uid=doc_uid, closure_rows=extracted_document.section_closure_rows)
            section_db_id_by_source_id = section_store.map_source_ids_to_db_ids(
                doc_uid=doc_uid,
                section_ids=[section.section_id for section in extracted_document.sections],
            )
            logger.info(f"Stored {len(extracted_document.sections)} sections with doc_uid={doc_uid}; resolved_section_db_ids={len(section_db_id_by_source_id)}")
            return section_db_id_by_source_id

    def _sync_chunk_section_links(
        self,
        doc_uid: str,
        chunks: list[Chunk],
        section_db_id_by_source_id: dict[str, int],
    ) -> None:
        if not section_db_id_by_source_id:
            return
        for chunk in chunks:
            chunk.containing_section_db_id = section_db_id_by_source_id.get(chunk.containing_section_id) if chunk.containing_section_id is not None else None
        with self._dependencies.chunk_store as chunk_store:
            updated_count = chunk_store.sync_containing_section_db_ids(
                doc_uid=doc_uid,
                section_db_id_by_source_id=section_db_id_by_source_id,
            )
        logger.info(f"Synchronized synthetic section links for {updated_count} chunk(s) in doc_uid={doc_uid}")

    def _store_selected_outputs(
        self,
        doc_uid: str,
        extracted_document: ExtractedDocument,
        chunks: list[Chunk],
        document_embedding_text: str,
    ) -> int:
        if self._stores_documents():
            with self._dependencies.document_store as document_store:
                logger.info(f"Persisting document representation fields for doc_uid={doc_uid}")
                document_store.upsert_document(extracted_document.document)
                logger.info(f"Persisted document representation fields for doc_uid={doc_uid}")

        if self._stores_sections():
            logger.info(f"Persisting sections for doc_uid={doc_uid}")
            section_db_id_by_source_id = self._store_sections(doc_uid=doc_uid, extracted_document=extracted_document)
            self._sync_chunk_section_links(
                doc_uid=doc_uid,
                chunks=chunks,
                section_db_id_by_source_id=section_db_id_by_source_id,
            )
        embeddings_stored = 0
        if self._stores_chunks():
            embeddings_stored = self._store_chunk_embeddings(doc_uid=doc_uid, chunks=chunks)
        if self._stores_sections():
            self._store_title_embeddings(doc_uid=doc_uid, sections=extracted_document.sections)
        if self._stores_documents():
            self._store_document_embeddings(doc_uid=doc_uid, embedding_text=document_embedding_text)
        return embeddings_stored

    def _store_chunk_embeddings(self, doc_uid: str, chunks: list[Chunk]) -> int:
        embeddings_stored = 0
        with self._dependencies.vector_store as vector_store:
            logger.info(f"Persisting chunk embeddings for doc_uid={doc_uid}; candidate_chunks={len(chunks)}")
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
            logger.info(f"Persisting title embeddings for doc_uid={doc_uid}; candidate_sections={len(sections)}")
            deleted_titles = title_vector_store.delete_by_doc(doc_uid)
            if deleted_titles > 0:
                logger.info(f"Deleted {deleted_titles} existing title embeddings for {doc_uid}")
            if sections:
                title_vector_store.add_embeddings(
                    doc_uid,
                    [section.section_id for section in sections],
                    [section.title for section in sections],
                )
                logger.info(f"Stored {len(sections)} title embeddings for doc_uid={doc_uid}")

    def _store_document_embeddings(self, doc_uid: str, embedding_text: str) -> None:
        if self._dependencies.document_vector_store is None:
            logger.info(f"Skipping document embeddings for doc_uid={doc_uid} because no document vector store is configured")
            return
        if not embedding_text:
            logger.warning(f"Skipping document embedding for doc_uid={doc_uid} because the embedding text is empty")
            return
        with self._dependencies.document_vector_store as document_vector_store:
            deleted_count = document_vector_store.delete_by_doc(doc_uid)
            if deleted_count > 0:
                logger.info(f"Deleted {deleted_count} existing document embeddings for {doc_uid}")
            logger.info(f"Storing document embedding for doc_uid={doc_uid} with embedding_chars={len(embedding_text)}")
            document_vector_store.add_embeddings([doc_uid], [embedding_text])
            logger.info(f"Stored 1 document embedding for doc_uid={doc_uid}")

    def _repair_missing_document_embedding_if_needed(
        self,
        doc_uid: str,
        chunk_count: int,
        embedding_text: str,
    ) -> StoreCommandResult | None:
        if not self._stores_documents() or self._dependencies.document_vector_store is None:
            return None
        with self._dependencies.document_vector_store as document_vector_store:
            if document_vector_store.has_embedding_for_doc(doc_uid):
                logger.info(f"Found existing document embedding for unchanged doc_uid={doc_uid}")
                return None
        repair_count = _increment_document_embedding_repair_count()
        logger.warning(f"Detected missing document embedding for unchanged doc_uid={doc_uid}; retrying document embedding storage; repair_count={repair_count}")
        self._store_document_embeddings(doc_uid=doc_uid, embedding_text=embedding_text)
        logger.info(f"Repaired missing document embedding for unchanged doc_uid={doc_uid}; repair_count={repair_count}")
        return StoreCommandResult(
            status="stored",
            doc_uid=doc_uid,
            chunk_count=chunk_count,
            embedding_count=0,
            reason="repaired missing document embedding",
        )

    def _truncate_oversized_chunks(self, chunks: list[Chunk]) -> None:
        truncated_count = 0
        for chunk in chunks:
            if len(chunk.text) > MAX_EMBEDDING_TEXT_CHARS:
                original_len = len(chunk.text)
                chunk.text = chunk.text[:MAX_EMBEDDING_TEXT_CHARS]
                truncated_count += 1
                logger.warning(f"Truncated chunk {chunk.chunk_number} from {original_len} to {MAX_EMBEDDING_TEXT_CHARS} chars")
        if truncated_count > 0:
            logger.info(f"Truncated {truncated_count} oversized chunk(s)")

    def _get_existing_chunks(self, doc_uid: str) -> list[Chunk]:
        with self._dependencies.chunk_store as chunk_store:
            return list(chunk_store.get_chunks_by_doc(doc_uid))

    def _get_existing_sections(self, doc_uid: str) -> list[SectionRecord]:
        if self._dependencies.section_store is None:
            return []
        with self._dependencies.section_store as section_store:
            return list(section_store.get_sections_by_doc(doc_uid))

    def _get_existing_document(self, doc_uid: str) -> DocumentRecord | None:
        with self._dependencies.document_store as document_store:
            return document_store.get_document(doc_uid)

    def _should_skip(
        self,
        existing_snapshot: StorePayloadSnapshot,
        new_snapshot: StorePayloadSnapshot,
    ) -> bool:
        if self._force_store:
            logger.info(f"Force store enabled for doc_uid={existing_snapshot.document.doc_uid if existing_snapshot.document is not None else 'unknown'}; bypassing unchanged-content skip check")
            return False
        if not self._extractor.skip_if_unchanged:
            return False
        if self._stores_chunks() and not self._payloads_match(existing_snapshot.chunks, new_snapshot.chunks):
            return False
        if self._stores_sections() and not self._section_payloads_match(existing_snapshot.sections, new_snapshot.sections):
            return False
        if not self._stores_documents():
            return True
        new_document = new_snapshot.document
        return new_document is not None and self._document_payloads_match(existing_snapshot.document, new_document)

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

    def _section_payload(self, section: SectionRecord) -> tuple[str, str | None, str]:
        return (section.section_id, section.parent_section_id, section.title)

    def _document_payloads_match(self, existing_document: DocumentRecord | None, new_document: DocumentRecord) -> bool:
        if existing_document is None:
            return False
        return self._document_payload(existing_document) == self._document_payload(new_document)

    def _document_payload(
        self,
        document: DocumentRecord,
    ) -> tuple[str, str, str | None, str | None, str | None, str | None, str | None, str | None, str | None, str | None, str | None, str | None, str | None]:
        return (
            document.source_type,
            document.source_title,
            document.source_url,
            document.canonical_url,
            document.source_domain,
            document.document_type,
            document.document_kind,
            document.background_text,
            document.issue_text,
            document.objective_text,
            document.scope_text,
            document.intro_text,
            document.toc_text,
        )

    def _get_scope_error(self) -> str | None:
        if self._scope in STORE_SCOPES:
            return None
        supported_scopes = ", ".join(STORE_SCOPES)
        return f"scope must be one of {supported_scopes}"

    def _stores_chunks(self) -> bool:
        return self._scope in {"all", "chunks"}

    def _stores_sections(self) -> bool:
        return self._scope in {"all", "sections"}

    def _stores_documents(self) -> bool:
        return self._scope in {"all", "documents"}


def _elapsed_ms(started_at: float) -> float:
    return (perf_counter() - started_at) * 1000


def build_store_dependencies() -> StoreDependencies:
    """Build the production dependencies for StoreCommand."""
    return StoreDependencies(
        chunk_store=ChunkStore(),
        document_store=DocumentStore(),
        vector_store=VectorStore(),
        init_db_fn=init_db,
        section_store=SectionStore(),
        title_vector_store=TitleVectorStore(),
        document_vector_store=DocumentVectorStore(),
    )


def _resolve_store_command_options(
    options: StoreCommandOptions | None,
    legacy_kwargs: dict[str, object],
) -> StoreCommandOptions:
    resolved_explicit_doc_uid = options.explicit_doc_uid if options is not None else None
    resolved_scope = options.scope if options is not None else "all"
    resolved_force_store = options.force_store if options is not None else False

    resolved_explicit_doc_uid = _pop_legacy_optional_string(legacy_kwargs, "doc_uid", resolved_explicit_doc_uid)
    resolved_explicit_doc_uid = _pop_legacy_optional_string(
        legacy_kwargs,
        "explicit_doc_uid",
        resolved_explicit_doc_uid,
    )
    resolved_scope = _pop_legacy_string(legacy_kwargs, "scope", resolved_scope)
    resolved_force_store = _pop_legacy_bool(legacy_kwargs, "force_store", resolved_force_store)
    resolved_force_store = _pop_legacy_bool(legacy_kwargs, "force_restore", resolved_force_store)

    return StoreCommandOptions(
        explicit_doc_uid=resolved_explicit_doc_uid,
        scope=resolved_scope,
        force_store=resolved_force_store,
    )


def _pop_legacy_optional_string(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: str | None,
) -> str | None:
    if key not in legacy_kwargs:
        return current_value
    value = legacy_kwargs.pop(key)
    if value is None:
        return None
    if not isinstance(value, str):
        message = f"{key} must be a string or None, got {type(value).__name__}"
        raise TypeError(message)
    return value


def _pop_legacy_string(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: str,
) -> str:
    if key not in legacy_kwargs:
        return current_value
    value = legacy_kwargs.pop(key)
    if not isinstance(value, str):
        message = f"{key} must be a string, got {type(value).__name__}"
        raise TypeError(message)
    return value


def _pop_legacy_bool(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: object,
) -> bool:
    if key not in legacy_kwargs:
        return bool(current_value)
    value = legacy_kwargs.pop(key)
    if not isinstance(value, bool):
        message = f"{key} must be a bool, got {type(value).__name__}"
        raise TypeError(message)
    return value


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
    extractor: ExtractorProtocol | None = None,
    dependencies: StoreDependencies | None = None,
    options: StoreCommandOptions | None = None,
    **legacy_kwargs: object,
) -> StoreCommand:
    """Create StoreCommand with real dependencies by default.

    The pdf_path keyword parameter is preserved for backward compatibility.
    """
    resolved_options = _resolve_store_command_options(options=options, legacy_kwargs=legacy_kwargs)
    pdf_path = legacy_kwargs.pop("pdf_path", None)
    if legacy_kwargs:
        unexpected_keys = ", ".join(sorted(legacy_kwargs))
        message = f"Unexpected keyword arguments: {unexpected_keys}"
        raise TypeError(message)
    if pdf_path is not None and not isinstance(pdf_path, Path):
        message = f"pdf_path must be a Path, got {type(pdf_path).__name__}"
        raise TypeError(message)

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
        options=resolved_options,
    )
