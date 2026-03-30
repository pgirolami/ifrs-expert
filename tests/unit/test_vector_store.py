"""Tests for vector store functionality."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import faiss
import numpy as np
import pytest

from src.vector.store import VectorStore, compute_embeddings, set_index_path


@pytest.fixture(autouse=True)
def temp_index():
    """Use a temporary index for each test."""
    with tempfile.TemporaryDirectory() as tmpdir:
        index_path = Path(tmpdir) / "faiss.index"
        set_index_path(index_path)
        yield index_path
        set_index_path(None)


class FakeSentenceTransformer:
    """Minimal embedding model stub for vector-store tests."""

    def encode(
        self,
        inputs: str | list[str],
        batch_size: int | None = None,
        show_progress_bar: bool = False,
    ) -> np.ndarray:
        """Return deterministic 3D embeddings for one or more inputs."""
        del batch_size, show_progress_bar

        if isinstance(inputs, str):
            return np.array([1.0, 0.0, 0.0], dtype="float32")

        embeddings: list[np.ndarray] = []
        for index, _text in enumerate(inputs, start=1):
            embeddings.append(np.array([float(index), 0.0, 0.0], dtype="float32"))
        return np.array(embeddings, dtype="float32")


class TestVectorStoreSearch:
    """Tests for VectorStore search functionality."""

    def test_search_returns_correct_structure(self, temp_index: Path) -> None:
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

    def test_search_handles_empty_index(self, temp_index: Path) -> None:
        """Test that search handles empty index results."""
        with VectorStore() as store:
            results = store.search("test", k=5)

        assert results == []

    def test_search_filters_by_k(self, temp_index: Path) -> None:
        """Test that search respects k parameter."""
        # Add multiple embeddings
        texts = [f"document number {i}" for i in range(10)]
        chunk_ids = list(range(10))
        with VectorStore() as store:
            store.add_embeddings("doc1", chunk_ids, texts)

        with VectorStore() as store:
            results = store.search("test query", k=3)

        assert len(results) == 3


class TestVectorStorePersistence:
    """Tests for VectorStore persistence behavior."""

    def test_exit_does_not_write_new_empty_index(self, tmp_path: Path) -> None:
        """Entering and exiting without mutations should not create index files."""
        index_path = tmp_path / "faiss.index"
        id_map_path = tmp_path / "id_map.json"
        store = VectorStore(index_path=index_path, id_map_path=id_map_path)
        store._model = FakeSentenceTransformer()

        with store:
            pass

        assert not index_path.exists(), "Expected no FAISS index file when nothing changed"
        assert not id_map_path.exists(), "Expected no ID map file when nothing changed"

    def test_exit_does_not_rewrite_unchanged_existing_index(self, tmp_path: Path) -> None:
        """Loading an existing index without mutations should not rewrite it."""
        index_path = tmp_path / "faiss.index"
        id_map_path = tmp_path / "id_map.json"

        initial_index = faiss.IndexFlatIP(3)
        faiss.write_index(initial_index, str(index_path))
        id_map_path.write_text("{}", encoding="utf-8")
        original_bytes = index_path.read_bytes()
        original_id_map = id_map_path.read_text(encoding="utf-8")

        with VectorStore(index_path=index_path, id_map_path=id_map_path):
            pass

        assert index_path.read_bytes() == original_bytes
        assert id_map_path.read_text(encoding="utf-8") == original_id_map

    def test_exit_writes_index_after_adding_embeddings(self, tmp_path: Path) -> None:
        """Adding embeddings should persist the updated index on exit."""
        index_path = tmp_path / "faiss.index"
        id_map_path = tmp_path / "id_map.json"

        faiss.write_index(faiss.IndexFlatIP(3), str(index_path))
        id_map_path.write_text("{}", encoding="utf-8")
        store = VectorStore(index_path=index_path, id_map_path=id_map_path)
        store._model = FakeSentenceTransformer()

        with store:
            store.add_embeddings("doc-1", [11], ["chunk text"])

        saved_index = faiss.read_index(str(index_path))
        saved_id_map = json.loads(id_map_path.read_text(encoding="utf-8"))

        assert saved_index.ntotal == 1
        assert saved_id_map == {"0": ["doc-1", 11]}

    def test_exit_writes_index_after_deletion(self, tmp_path: Path) -> None:
        """Deleting embeddings should persist the updated index on exit."""
        index_path = tmp_path / "faiss.index"
        id_map_path = tmp_path / "id_map.json"

        initial_index = faiss.IndexFlatIP(3)
        initial_index.add(np.array([[1.0, 0.0, 0.0]], dtype="float32"))
        faiss.write_index(initial_index, str(index_path))
        id_map_path.write_text('{"0": ["doc-1", 11]}', encoding="utf-8")

        with VectorStore(index_path=index_path, id_map_path=id_map_path) as store:
            deleted_count = store.delete_by_doc("doc-1")

        saved_index = faiss.read_index(str(index_path))
        saved_id_map = json.loads(id_map_path.read_text(encoding="utf-8"))

        assert deleted_count == 1
        assert saved_index.ntotal == 0
        assert saved_id_map == {}
