"""In-memory fakes for testing."""

from typing import Self

from src.interfaces import ChunkStoreProtocol
from src.models.chunk import Chunk


class InMemoryChunkStore(ChunkStoreProtocol):
    """In-memory implementation of chunk storage for testing."""

    def __init__(self) -> None:
        self._chunks: list[Chunk] = []
        self._next_id: int = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        pass

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        ids: list[int] = []
        for chunk in chunks:
            # Preserve existing chunk_id if set, otherwise assign new one
            chunk_id = chunk.chunk_id if chunk.chunk_id is not None else self._next_id
            if chunk.chunk_id is None:
                self._next_id += 1
            chunk.chunk_id = chunk_id
            ids.append(chunk_id)
            self._chunks.append(chunk)
        return ids

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        return [c for c in self._chunks if c.doc_uid == doc_uid]

    def get_all_docs(self) -> list[str]:
        return sorted(set(c.doc_uid for c in self._chunks))

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        original_count = len(self._chunks)
        self._chunks = [c for c in self._chunks if c.doc_uid != doc_uid]
        return original_count - len(self._chunks)

    def clear(self) -> None:
        self._chunks.clear()
        self._next_id = 1