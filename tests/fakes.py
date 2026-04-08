"""In-memory fakes for testing."""

from __future__ import annotations

from dataclasses import replace
from typing import Self

from src.interfaces import ChunkStoreProtocol, DocumentStoreProtocol, SearchResult, VectorStoreProtocol
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.section import SectionClosureRow, SectionRecord


class InMemoryChunkStore(ChunkStoreProtocol):
    """In-memory implementation of chunk storage for testing."""

    def __init__(self) -> None:
        self._chunks: list[Chunk] = []
        self._next_id = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        ids: list[int] = []
        for chunk in chunks:
            row_id = chunk.id if chunk.id is not None else self._next_id
            self._next_id = max(self._next_id, row_id + 1)
            stored_chunk = replace(chunk, id=row_id)
            chunk.id = row_id
            self._chunks.append(stored_chunk)
            ids.append(row_id)
        return ids

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        return [replace(chunk) for chunk in self._chunks if chunk.doc_uid == doc_uid]

    def get_all_docs(self) -> list[str]:
        return sorted({chunk.doc_uid for chunk in self._chunks})

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        original_count = len(self._chunks)
        self._chunks = [chunk for chunk in self._chunks if chunk.doc_uid != doc_uid]
        return original_count - len(self._chunks)

    def clear(self) -> None:
        self._chunks.clear()
        self._next_id = 1


class InMemorySectionStore:
    """In-memory implementation of section storage for testing."""

    def __init__(self) -> None:
        self._sections: dict[str, SectionRecord] = {}
        self._descendants: dict[str, list[str]] = {}
        self._closure_rows: list[SectionClosureRow] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def insert_sections(self, sections: list[SectionRecord]) -> None:
        for section in sections:
            self._sections[section.section_id] = replace(section)

    def insert_closure_rows(self, closure_rows: list[SectionClosureRow]) -> None:
        for row in closure_rows:
            self._closure_rows.append(row)
            self._descendants.setdefault(row.ancestor_section_id, [])
            if row.descendant_section_id not in self._descendants[row.ancestor_section_id]:
                self._descendants[row.ancestor_section_id].append(row.descendant_section_id)

    def get_sections_by_doc(self, doc_uid: str) -> list[SectionRecord]:
        sections = [section for section in self._sections.values() if section.doc_uid == doc_uid]
        return sorted(sections, key=lambda section: section.position)

    def get_descendant_section_ids(self, section_id: str) -> list[str]:
        return list(self._descendants.get(section_id, [section_id]))

    def delete_sections_by_doc(self, doc_uid: str) -> int:
        section_ids = [section.section_id for section in self._sections.values() if section.doc_uid == doc_uid]
        for section_id in section_ids:
            self._sections.pop(section_id, None)
            self._descendants.pop(section_id, None)
        return len(section_ids)

    def add_descendant_mapping(self, section_id: str, descendant_ids: list[str]) -> None:
        self._descendants[section_id] = list(descendant_ids)


class InMemoryDocumentStore(DocumentStoreProtocol):
    """In-memory implementation of document storage for testing."""

    def __init__(self) -> None:
        self._documents: dict[str, DocumentRecord] = {}

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def upsert_document(self, document: DocumentRecord) -> None:
        self._documents[document.doc_uid] = replace(document)

    def get_document(self, doc_uid: str) -> DocumentRecord | None:
        document = self._documents.get(doc_uid)
        if document is None:
            return None
        return replace(document)


class RecordingVectorStore(VectorStoreProtocol):
    """Vector store fake that records operations for assertions."""

    def __init__(self) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[str, list[int], list[str]]] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        return []

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        return 0

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uid, chunk_ids, texts))


class RecordingTitleVectorStore:
    """Title vector store fake that records section embedding operations."""

    def __init__(self) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[str, list[str], list[str]]] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return []

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        return 0

    def add_embeddings(self, doc_uid: str, section_ids: list[str], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uid, section_ids, texts))


class RecordingDocumentVectorStore:
    """Document vector store fake that records document embedding operations."""

    def __init__(self) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[list[str], list[str]]] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return []

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        return 0

    def add_embeddings(self, doc_uids: list[str], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uids, texts))
