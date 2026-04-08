"""Tests for query-documents command."""

from __future__ import annotations

import json
from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol
from src.models.document import DocumentRecord
from tests.fakes import InMemoryDocumentStore


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


def test_query_documents_returns_top_d_documents_as_json() -> None:
    """The command should return the top matching documents with stored fields."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-05T10:00:00Z",
                background_text="Background text",
                issue_text="Issue text",
                scope_text="Scope text",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/ifrs9.html",
                canonical_url="https://www.ifrs.org/ifrs9.html",
                captured_at="2026-04-05T10:00:00Z",
                objective_text="Objective text",
                scope_text="Scope text",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.97},
                    {"doc_uid": "ifrs9", "score": 0.65},
                ]
            ),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(d=1, min_score=0.6, verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert len(data) == 1
    assert data[0]["doc_uid"] == "ifric16"
    assert data[0]["background_text"] == "Background text"
    assert data[0]["issue_text"] == "Issue text"
    assert data[0]["score"] == 0.97


def test_query_documents_returns_error_when_index_missing() -> None:
    """The command should fail clearly when the document index is missing."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    command = QueryDocumentsCommand(
        query="scope",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([]),
            document_store=InMemoryDocumentStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
        ),
        options=QueryDocumentsOptions(d=5, min_score=0.6, verbose=False),
    )

    result = command.execute()

    assert result == "Error: No document index found. Please run 'store' command first."
