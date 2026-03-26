"""Abstract interfaces for store dependencies."""

from typing import Protocol

from src.models.chunk import Chunk


class ChunkStoreProtocol(Protocol):
    """Protocol for chunk storage operations."""

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        """Insert chunks into the store."""

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        """Get all chunks for a document."""

    def get_all_docs(self) -> list[str]:
        """Get all document UIDs."""

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        """Delete all chunks for a document."""


class VectorStoreProtocol(Protocol):
    """Protocol for vector store operations."""

    def search_all(self, query: str) -> list[dict]:
        """Search for similar chunks."""

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document."""

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        """Add embeddings for chunks."""
