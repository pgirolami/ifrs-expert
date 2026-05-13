"""Models and dependency contracts for document ingestion."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.interfaces import ChunkStoreProtocol, DocumentStoreProtocol, DocumentVectorStoreProtocol, ReferenceStoreProtocol, SectionStoreProtocol, TitleVectorStoreProtocol, VectorStoreProtocol

if TYPE_CHECKING:
    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.extraction import ExtractedDocument
    from src.models.reference import ContentReference
    from src.models.section import SectionRecord
    from src.retrieval.document_profile_builder import DocumentSimilarityRepresentation

STORE_SCOPES: tuple[str, ...] = ("all", "chunks", "documents", "sections")

StoreChunkStore = ChunkStoreProtocol
StoreDocumentStore = DocumentStoreProtocol
StoreSectionStore = SectionStoreProtocol
StoreVectorStore = VectorStoreProtocol
StoreTitleVectorStore = TitleVectorStoreProtocol
StoreDocumentVectorStore = DocumentVectorStoreProtocol
StoreInitDb = Callable[[], None]
StoreDocumentVectorStoreFactory = Callable[[str], StoreDocumentVectorStore]

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
    reference_store: ReferenceStoreProtocol | None = None
    title_vector_store: StoreTitleVectorStore | None = None
    document_vector_store: StoreDocumentVectorStore | None = None
    document_vector_store_factory: StoreDocumentVectorStoreFactory | None = None


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
    references: list[ContentReference]
    document: DocumentRecord | None


@dataclass(frozen=True)
class StorePreparedData:
    """Fully prepared extraction payload ready for persistence."""

    doc_uid: str
    extracted_document: ExtractedDocument
    chunks: list[Chunk]
    sections: list[SectionRecord]
    references: list[ContentReference]
    document_similarity_texts: dict[DocumentSimilarityRepresentation, str]


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
