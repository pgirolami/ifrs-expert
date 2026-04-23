"""Tests for query command."""

import json
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock

import unittest.mock

import pytest

from src.commands.query import QueryCommand, QueryConfig, QueryOptions
from src.interfaces import SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore
from tests.policy import load_test_policy_config, load_test_retrieval_policy, make_retrieval_policy


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

    def test_query_uses_policy_query_embedding_mode(self) -> None:
        """Query should pass the policy query embedding mode through to retrieval."""
        captured_requests: list[object] = []

        def mock_execute_retrieval(*, request: object, config: object) -> tuple[None, None]:
            del config
            captured_requests.append(request)
            return None, None

        config = QueryConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(policy=make_retrieval_policy(mode="text", query_embedding_mode="enriched"), verbose=False),
        )

        with unittest.mock.patch("src.commands.query.execute_retrieval", side_effect=mock_execute_retrieval):
            command.execute()

        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert getattr(request, "query_embedding_mode") == "enriched"

    def test_query_rejects_title_similarity_policies(self) -> None:
        """Query should reject policies configured for title similarity retrieval."""
        config = QueryConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        )
        command = QueryCommand(
            query="test",
            config=config,
            options=QueryOptions(policy=make_retrieval_policy(mode="titles"), verbose=False),
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "chunk_similarity" in result

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
            options=QueryOptions(policy=load_test_retrieval_policy(), verbose=False),
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
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="test text 2"),
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
            options=QueryOptions(policy=load_test_retrieval_policy(), verbose=False),
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
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="doc1 text 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="doc1 text 2"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="doc1 text 3"),
            Chunk(id=4, doc_uid="doc1", chunk_number="1.4", page_start="A4", page_end="A4", text="doc1 text 4"),
        ]
        doc2_chunks = [
            Chunk(id=10, doc_uid="doc2", chunk_number="2.1", page_start="B1", page_end="B1", text="doc2 text 1"),
            Chunk(id=11, doc_uid="doc2", chunk_number="2.2", page_start="B2", page_end="B2", text="doc2 text 2"),
            Chunk(id=12, doc_uid="doc2", chunk_number="2.3", page_start="B3", page_end="B3", text="doc2 text 3"),
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
            options=QueryOptions(policy=make_retrieval_policy(k=2), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert [(item["doc_uid"], item["id"]) for item in data] == [
            ("doc1", 1),
            ("doc1", 2),
            ("doc2", 10),
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
            options=QueryOptions(policy=load_test_retrieval_policy(), verbose=False),
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
            options=QueryOptions(policy=load_test_retrieval_policy(), verbose=False),
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
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="test text 2"),
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
            options=QueryOptions(policy=make_retrieval_policy(chunk_min_score=0.5), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["id"] == 1

    def test_query_chunk_expansion(self):
        """Test query command chunk expansion."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="chunk 3"),
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
            options=QueryOptions(policy=make_retrieval_policy(expand=1), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert [chunk["id"] for chunk in data] == [1, 2, 3]

    def test_query_expand_to_section(self):
        """Test query command expand to section."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="chunk 1", containing_section_id="sec1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="chunk 2", containing_section_id="sec1"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="chunk 3", containing_section_id="sec2"),
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
            options=QueryOptions(policy=make_retrieval_policy(expand=0, expand_to_section=True), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert [chunk["id"] for chunk in data] == [1]

    def test_query_full_doc_threshold(self):
        """Test query command full document threshold."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="short"),
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
            options=QueryOptions(policy=make_retrieval_policy(expand=0, full_doc_threshold=100), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["id"] == 1

    def test_query_json_output_includes_metadata(self):
        """Test query command JSON output includes metadata."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="test text"),
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
            options=QueryOptions(policy=make_retrieval_policy(k=1, expand=0), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["doc_uid"] == "doc1"
        assert "document_type" in data[0]

    def test_query_verbose_output_includes_context(self):
        """Test query command verbose output."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="test text"),
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
            options=QueryOptions(policy=make_retrieval_policy(k=1, expand=0), verbose=True),
        )

        result = command.execute()

        assert result.startswith("QueryOptions(")
        assert "Document: doc1" in result

    def test_query_no_expansion_when_zero(self):
        """Test query command no expansion when expand is 0."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="chunk 3"),
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
            options=QueryOptions(policy=make_retrieval_policy(expand=0), verbose=False),
        )

        result = command.execute()

        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["id"] == 2


