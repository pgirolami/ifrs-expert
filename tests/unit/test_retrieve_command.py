"""Tests for the retrieve command."""

from __future__ import annotations

import json
from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore, InMemorySectionStore


class MockVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for chunk vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | int | float]]) -> None:
        self._search_results = cast(list[SearchResult], search_results)

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return self._search_results


class MockDocumentVectorStore(SearchDocumentVectorStoreProtocol):
    """Minimal mock for document vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | float]]) -> None:
        self._search_results = cast(list[DocumentSearchResult], search_results)

    def __enter__(self) -> "MockDocumentVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[DocumentSearchResult]:
        del query
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


def test_retrieve_documents_mode_filters_chunks_to_selected_documents() -> None:
    """Documents mode should preselect documents before chunk filtering."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk"),
                Chunk(id=2, doc_uid="ias21", chunk_number="2.1", page_start="B1", page_end="B1", text="ias chunk"),
            ]
        )

    command = RetrieveCommand(
        query="foreign currency",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ias21", "chunk_id": 2, "score": 0.95},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ias21", "score": 0.92},
                    {"doc_uid": "ifrs9", "score": 0.91},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            retrieval_mode="documents",
            k=5,
            d=1,
            doc_min_score=0.5,
            content_min_score=0.5,
            verbose=False,
            expand=0,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["retrieval_mode"] == "documents"
    assert data["document_hits"] == [{"doc_uid": "ias21", "score": 0.92}]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ias21"]
    assert data["chunks"][0]["text"] == "ias chunk"


def test_retrieve_verbose_output_starts_with_options() -> None:
    """Verbose retrieve output should start with the options object."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk"),
            ]
        )

    command = RetrieveCommand(
        query="leases",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(retrieval_mode="text", k=5, verbose=True, expand=0),
    )

    result = command.execute()

    assert result.startswith("RetrieveOptions(k=5, d=5, doc_min_score=0.5, content_min_score=0.55, verbose=True, expand=0, full_doc_threshold=0, retrieval_mode='text')")
    assert "Retrieved chunks:" in result
    assert "Document: ifrs9" in result
