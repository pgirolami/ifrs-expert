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


def test_retrieve_documents_mode_applies_per_type_thresholds_and_overall_cap() -> None:
    """Documents mode should apply per-type thresholds before the overall document cap."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifric16", chunk_number="1.1", page_start="A1", page_end="A1", text="ifric chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="2.1", page_start="B1", page_end="B1", text="ifrs chunk"),
                Chunk(id=3, doc_uid="ias21", chunk_number="3.1", page_start="C1", page_end="C1", text="ias chunk"),
                Chunk(id=4, doc_uid="sic25", chunk_number="4.1", page_start="D1", page_end="D1", text="sic chunk"),
                Chunk(id=5, doc_uid="ps1", chunk_number="5.1", page_start="E1", page_end="E1", text="ps chunk"),
            ]
        )

    command = RetrieveCommand(
        query="foreign currency",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifric16", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.95},
                    {"doc_uid": "ias21", "chunk_id": 3, "score": 0.94},
                    {"doc_uid": "sic25", "chunk_id": 4, "score": 0.93},
                    {"doc_uid": "ps1", "chunk_id": 5, "score": 0.92},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.60},
                    {"doc_uid": "ifrs9", "score": 0.595},
                    {"doc_uid": "ias21", "score": 0.56},
                    {"doc_uid": "sic25", "score": 0.52},
                    {"doc_uid": "ps1", "score": 0.49},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            retrieval_mode="documents",
            k=5,
            d=3,
            content_min_score=0.5,
            verbose=False,
            expand=0,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["retrieval_mode"] == "documents"
    assert data["document_hits"] == [
        {"doc_uid": "ifric16", "score": 0.6},
        {"doc_uid": "ifrs9", "score": 0.595},
        {"doc_uid": "ias21", "score": 0.56},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifric16", "ifrs9", "ias21"]
    assert [chunk["text"] for chunk in data["chunks"]] == ["ifric chunk", "ifrs chunk", "ias chunk"]


def test_retrieve_documents_mode_respects_per_type_document_caps() -> None:
    """Documents mode should respect per-type document caps before chunk retrieval."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifric16", chunk_number="1.1", page_start="A1", page_end="A1", text="ifric 16 chunk"),
                Chunk(id=2, doc_uid="ifric17", chunk_number="1.2", page_start="A2", page_end="A2", text="ifric 17 chunk"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="2.1", page_start="B1", page_end="B1", text="ifrs chunk"),
            ]
        )

    command = RetrieveCommand(
        query="foreign currency",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifric16", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ifric17", "chunk_id": 2, "score": 0.95},
                    {"doc_uid": "ifrs9", "chunk_id": 3, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.60},
                    {"doc_uid": "ifric17", "score": 0.59},
                    {"doc_uid": "ifrs9", "score": 0.595},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            retrieval_mode="documents",
            k=5,
            d=5,
            ifric_d=1,
            content_min_score=0.5,
            verbose=False,
            expand=0,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["document_hits"] == [
        {"doc_uid": "ifric16", "score": 0.6},
        {"doc_uid": "ifrs9", "score": 0.595},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifric16", "ifrs9"]


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

    assert result.startswith("RetrieveOptions(k=5, d=5, doc_min_score=None, ifrs_d=5")
    assert "Retrieved chunks:" in result
    assert "Document: ifrs9" in result
