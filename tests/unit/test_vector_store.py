"""Tests for vector store functionality."""

import pytest
import tempfile
from pathlib import Path

from src.vector.store import VectorStore, set_index_path, compute_embeddings


@pytest.fixture(autouse=True)
def temp_index():
    """Use a temporary index for each test."""
    with tempfile.TemporaryDirectory() as tmpdir:
        index_path = Path(tmpdir) / "faiss.index"
        set_index_path(index_path)
        yield index_path
        set_index_path(None)


class TestVectorStoreSearch:
    """Tests for VectorStore search functionality."""

    def test_search_returns_correct_structure(self, temp_index):
        """Test that search returns expected result structure."""
        # Add embeddings
        with VectorStore() as store:
            store.add_embeddings("doc1", [1, 2], ["hello world test", "another document"])

        with VectorStore() as store:
            results = store.search("test query", k=5)

        assert len(results) >= 1
        assert "doc_uid" in results[0]
        assert "chunk_id" in results[0]
        assert "score" in results[0]

    def test_search_handles_empty_index(self, temp_index):
        """Test that search handles empty index results."""
        with VectorStore() as store:
            results = store.search("test", k=5)

        assert results == []

    def test_search_filters_by_k(self, temp_index):
        """Test that search respects k parameter."""
        # Add multiple embeddings
        texts = [f"document number {i}" for i in range(10)]
        chunk_ids = list(range(10))
        with VectorStore() as store:
            store.add_embeddings("doc1", chunk_ids, texts)

        with VectorStore() as store:
            results = store.search("test query", k=3)

        assert len(results) == 3
