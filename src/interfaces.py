"""Abstract interfaces for store dependencies and extraction."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, Self, TypedDict

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.extraction import ExtractedDocument


class SearchResult(TypedDict):
    """Vector-search result."""

    doc_uid: str
    chunk_id: int
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
    """Protocol for vector-store searches used by query/answer flows."""

    def __enter__(self) -> Self:
        """Enter context manager."""

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit context manager."""

    def search_all(self, query: str) -> list[SearchResult]:
        """Search for similar chunks."""


class VectorStoreProtocol(SearchVectorStoreProtocol, Protocol):
    """Protocol for full vector-store operations."""

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document."""

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        """Add embeddings for chunks."""


class ExtractorProtocol(Protocol):
    """Protocol for source extractors used by StoreCommand."""

    source_type: str
    skip_if_unchanged: bool

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        """Extract one source file into structured metadata and chunks."""
