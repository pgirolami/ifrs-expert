"""Abstract interfaces for store dependencies and extraction."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, Self, TypedDict

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.extraction import ExtractedDocument
    from src.models.section import SectionClosureRow, SectionRecord


class SearchResult(TypedDict):
    """Vector-search result for paragraph chunks."""

    doc_uid: str
    chunk_id: int
    score: float


class TitleSearchResult(TypedDict):
    """Vector-search result for indexed section titles."""

    doc_uid: str
    section_id: str
    score: float


class DocumentSearchResult(TypedDict):
    """Vector-search result for document-level retrieval."""

    doc_uid: str
    score: float


class ReadChunkStoreProtocol(Protocol):
    """Protocol for chunk-store reads used by query/answer flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        """Get all chunks for a document."""


class ChunkStoreProtocol(ReadChunkStoreProtocol, Protocol):
    """Protocol for full chunk storage operations."""

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        """Insert chunks into the store."""

    def get_all_docs(self) -> list[str]:
        """Get all document UIDs."""

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        """Delete all chunks for a document."""


class ReadSectionStoreProtocol(Protocol):
    """Protocol for section-store reads used by title retrieval flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def get_sections_by_doc(self, doc_uid: str) -> list[SectionRecord]:
        """Get indexed sections for a document."""

    def get_descendant_section_ids(self, section_id: str) -> list[str]:
        """Get descendant section ids including the matched section itself."""


class SectionStoreProtocol(ReadSectionStoreProtocol, Protocol):
    """Protocol for full section storage operations."""

    def insert_sections(self, sections: list[SectionRecord]) -> None:
        """Insert sections into the store."""

    def insert_closure_rows(self, closure_rows: list[SectionClosureRow]) -> None:
        """Insert section closure rows into the store."""

    def delete_sections_by_doc(self, doc_uid: str) -> int:
        """Delete all sections for a document."""


class DocumentStoreProtocol(Protocol):
    """Protocol for document metadata storage."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def upsert_document(self, document: DocumentRecord) -> None:
        """Insert or update a document record."""

    def get_document(self, doc_uid: str) -> DocumentRecord | None:
        """Fetch a document record by UID."""


class SearchVectorStoreProtocol(Protocol):
    """Protocol for vector-store searches used by paragraph retrieval flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def search_all(self, query: str) -> list[SearchResult]:
        """Search for similar chunks."""


class SearchTitleVectorStoreProtocol(Protocol):
    """Protocol for vector-store searches used by title retrieval flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def search_all(self, query: str) -> list[TitleSearchResult]:
        """Search for similar section titles."""


class SearchDocumentVectorStoreProtocol(Protocol):
    """Protocol for vector-store searches used by document retrieval flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def search_all(self, query: str) -> list[DocumentSearchResult]:
        """Search for similar documents."""


class VectorStoreProtocol(SearchVectorStoreProtocol, Protocol):
    """Protocol for full vector-store operations."""

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document."""

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        """Add embeddings for chunks."""


class TitleVectorStoreProtocol(SearchTitleVectorStoreProtocol, Protocol):
    """Protocol for full title-vector-store operations."""

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document."""

    def add_embeddings(self, doc_uid: str, section_ids: list[str], texts: list[str]) -> None:
        """Add embeddings for section titles."""


class DocumentVectorStoreProtocol(SearchDocumentVectorStoreProtocol, Protocol):
    """Protocol for full document-vector-store operations."""

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document."""

    def add_embeddings(self, doc_uids: list[str], texts: list[str]) -> None:
        """Add embeddings for documents."""


class ExtractorProtocol(Protocol):
    """Protocol for source extractors used by StoreCommand."""

    source_type: str
    skip_if_unchanged: bool

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        """Extract one source file into structured metadata and chunks."""
