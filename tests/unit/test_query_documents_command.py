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


def test_query_documents_returns_top_d_documents_for_selected_type_as_json() -> None:
    """The command should return the top matching documents for the selected document type."""
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
                document_type="IFRIC",
                background_text="Background text",
                issue_text="Issue text",
                scope_text="Scope text",
                toc_text="Background\nIssue\nScope",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric17",
                source_type="html",
                source_title="IFRIC 17",
                source_url="https://www.ifrs.org/ifric17.html",
                canonical_url="https://www.ifrs.org/ifric17.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRIC",
                objective_text="Objective text",
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
                document_type="IFRS",
                intro_text="IFRS intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ias21",
                source_type="html",
                source_title="IAS 21",
                source_url="https://www.ifrs.org/ias21.html",
                canonical_url="https://www.ifrs.org/ias21.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IAS",
                intro_text="IAS intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="sic25",
                source_type="html",
                source_title="SIC 25",
                source_url="https://www.ifrs.org/sic25.html",
                canonical_url="https://www.ifrs.org/sic25.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="SIC",
                intro_text="SIC intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ps1",
                source_type="html",
                source_title="PS 1",
                source_url="https://www.ifrs.org/ps1.html",
                canonical_url="https://www.ifrs.org/ps1.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="PS",
                intro_text="PS intro",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.97},
                    {"doc_uid": "ifrs9", "score": 0.96},
                    {"doc_uid": "ifric17", "score": 0.95},
                    {"doc_uid": "ias21", "score": 0.94},
                    {"doc_uid": "sic25", "score": 0.93},
                    {"doc_uid": "ps1", "score": 0.92},
                ]
            ),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(document_type="IFRIC", d=2, min_score=0.6, verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert [item["doc_uid"] for item in data] == ["ifric16", "ifric17"]
    assert data[0]["document_type"] == "IFRIC"
    assert data[0]["background_text"] == "Background text"
    assert data[0]["issue_text"] == "Issue text"
    assert data[0]["TOC"] == "Background\nIssue\nScope"
    assert data[0]["score"] == 0.97


def test_query_documents_returns_error_for_unsupported_document_type() -> None:
    """The command should reject document types outside the supported set."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    command = QueryDocumentsCommand(
        query="scope",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([]),
            document_store=InMemoryDocumentStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(document_type="CUSTOM", d=5, min_score=0.6, verbose=False),
    )

    result = command.execute()

    assert result == "Error: document_type must be one of IFRS, IAS, IFRIC, SIC, PS"


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
        options=QueryDocumentsOptions(document_type="IFRS", d=5, min_score=0.6, verbose=False),
    )

    result = command.execute()

    assert result == "Error: No document index found. Please run 'store' command first."


def test_query_documents_verbose_output_starts_with_options() -> None:
    """Verbose document-query output should start with options and truncated representation details."""
    from src.commands.query_documents import (
        QueryDocumentsCommand,
        QueryDocumentsConfig,
        QueryDocumentsOptions,
        VERBOSE_TEXT_PREVIEW_CHARS,
    )

    long_background_text = "B" * (VERBOSE_TEXT_PREVIEW_CHARS + 10)
    long_scope_text = "S" * (VERBOSE_TEXT_PREVIEW_CHARS + 15)

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
                document_type="IFRIC",
                background_text=long_background_text,
                scope_text=long_scope_text,
                toc_text="Background\nIssue\nScope",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([{"doc_uid": "ifric16", "score": 0.97}]),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(document_type="IFRIC", d=5, min_score=None, verbose=True),
    )

    result = command.execute()

    expected_background_preview = ("B" * VERBOSE_TEXT_PREVIEW_CHARS) + "..."
    expected_scope_preview = ("S" * VERBOSE_TEXT_PREVIEW_CHARS) + "..."

    assert result.startswith("QueryDocumentsOptions(document_type='IFRIC', d=5, min_score=None, verbose=True)")
    assert f"Snippet: {expected_background_preview}" in result
    assert "Type: IFRIC" in result
    assert "Document representation:" in result
    assert f"- Background: {expected_background_preview}" in result
    assert f"- Scope: {expected_scope_preview}" in result
    assert "- TOC: Background Issue Scope" in result
