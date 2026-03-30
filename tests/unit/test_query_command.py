"""Tests for query command."""

import json
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock

import pytest

from src.commands.query import QueryCommand, QueryConfig, QueryOptions
from src.interfaces import SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore


class MockVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for VectorStore context manager."""

    def __init__(self, search_results: list[dict[str, str | int | float]]) -> None:
        self._search_results = cast(list[SearchResult], search_results)

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        pass

    def search_all(self, query: str) -> list[SearchResult]:
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


class TestQueryCommand:
    """Tests for query command using dependency injection."""

    def test_query_no_index(self):
        """Test query command when no index exists."""
        config = QueryConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False),
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "No index found" in result

    def test_query_with_results(self):
        """Test query returns matching chunks."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test query",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 2

    def test_query_retrieves_top_k_per_document(self):
        """Test query keeps up to k results per document above the relevance threshold."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.95},
            {"doc_uid": "doc2", "chunk_id": 10, "score": 0.94},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.90},
            {"doc_uid": "doc2", "chunk_id": 11, "score": 0.89},
            {"doc_uid": "doc1", "chunk_id": 3, "score": 0.88},
            {"doc_uid": "doc2", "chunk_id": 12, "score": 0.87},
            {"doc_uid": "doc1", "chunk_id": 4, "score": 0.20},
        ]

        doc1_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="doc1 text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="doc1 text 2"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="doc1 text 3"),
            Chunk(chunk_id=4, doc_uid="doc1", section_path="1.4", page_start="A4", page_end="A4", text="doc1 text 4"),
        ]
        doc2_chunks = [
            Chunk(chunk_id=10, doc_uid="doc2", section_path="2.1", page_start="B1", page_end="B1", text="doc2 text 1"),
            Chunk(chunk_id=11, doc_uid="doc2", section_path="2.2", page_start="B2", page_end="B2", text="doc2 text 2"),
            Chunk(chunk_id=12, doc_uid="doc2", section_path="2.3", page_start="B3", page_end="B3", text="doc2 text 3"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(doc1_chunks + doc2_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test query",
            config=config,
            options=QueryOptions(k=2, min_score=None, verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert [(item["doc_uid"], item["id"]) for item in data] == [
            ("doc1", 1),
            ("doc2", 10),
            ("doc1", 2),
            ("doc2", 11),
        ]

    def test_query_no_results(self):
        """Test query command with no matching results."""
        config = QueryConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False),
        )

        result = command.execute()

        assert result == "Error: No chunks retrieved"

    def test_query_exception_handling(self):
        """Test query command exception handling from search."""
        # Create a vector store that throws when search_all is called
        class FailingVectorStore(SearchVectorStoreProtocol):
            def __init__(self) -> None:
                pass

            def __enter__(self) -> "FailingVectorStore":
                return self

            def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
                pass

            def search_all(self, query: str) -> list[SearchResult]:
                raise RuntimeError("Search failed")

        config = QueryConfig(
            vector_store=FailingVectorStore(),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False),
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "Search failed" in result

    def test_query_score_threshold(self):
        """Test query command with min_score filters results."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.3},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=0.5, verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["id"] == 1

    def test_query_verbose_output(self):
        """Test query verbose output includes relevance."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},  # High
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.2},  # Low
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=True),
        )

        result = command.execute()

        # Both High-relevance chunks are in output; Low is filtered
        assert "(High)" in result
        assert "(Low)" not in result

    def test_query_expand_includes_neighboring_chunks(self):
        """Test query expansion includes surrounding chunks in document order."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="chunk 3"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False, expand=1),
        )

        result = command.execute()

        data = json.loads(result)
        assert [item["id"] for item in data] == [1, 2, 3]
        assert data[1]["score"] == 0.9
        assert data[0]["score"] == 0.0
        assert data[2]["score"] == 0.0

    def test_query_full_doc_threshold_uses_total_text_size(self):
        """Test query includes the full document when total text size is below threshold."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="aa"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="bbb"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="cccc"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        config = QueryConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(k=5, min_score=None, verbose=False, expand=0, full_doc_threshold=10),
        )

        result = command.execute()

        data = json.loads(result)
        assert [item["id"] for item in data] == [1, 2, 3]
        assert data[1]["score"] == 0.9
        assert data[0]["score"] == 0.0
        assert data[2]["score"] == 0.0
