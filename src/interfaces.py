"""Abstract interfaces for store dependencies."""

from typing import Protocol, Self, TypedDict

from src.models.chunk import Chunk


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
