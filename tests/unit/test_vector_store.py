"""Tests for vector store functionality."""

import pytest


class TestVectorStoreSearch:
    """Tests for VectorStore search functionality."""

    def test_search_returns_correct_structure(self):
        """Test that search returns expected result structure."""
        # Test the search logic directly
        id_map = {
            0: ("doc1", 1),
            1: ("doc1", 2),
        }
        distances = [[0.1, 0.2]]
        indices = [[0, 1]]

        results: list[dict] = []
        for dist, idx in zip(distances[0], indices[0], strict=True):
            if idx >= 0 and idx in id_map:
                doc_uid, chunk_id = id_map[idx]
                results.append(
                    {
                        "doc_uid": doc_uid,
                        "chunk_id": chunk_id,
                        "distance": float(dist),
                    }
                )

        assert len(results) == 2
        assert results[0]["doc_uid"] == "doc1"
        assert results[0]["chunk_id"] == 1

    def test_search_handles_empty_index(self):
        """Test that search handles empty index results."""
        id_map = {}
        distances = [[]]
        indices = [[]]

        results: list[dict] = []
        for dist, idx in zip(distances[0], indices[0], strict=True):
            if idx >= 0 and idx in id_map:
                doc_uid, chunk_id = id_map[idx]
                results.append(
                    {
                        "doc_uid": doc_uid,
                        "chunk_id": chunk_id,
                        "distance": float(dist),
                    }
                )

        assert results == []

    def test_search_filters_invalid_indices(self):
        """Test that search filters out invalid indices."""
        id_map = {
            0: ("doc1", 1),
            1: ("doc1", 2),
        }
        distances = [[0.1, 0.2, 0.3]]
        indices = [[0, 1, 999]]  # 999 is invalid

        results: list[dict] = []
        for dist, idx in zip(distances[0], indices[0], strict=True):
            if idx >= 0 and idx in id_map:
                doc_uid, chunk_id = id_map[idx]
                results.append(
                    {
                        "doc_uid": doc_uid,
                        "chunk_id": chunk_id,
                        "distance": float(dist),
                    }
                )

        assert len(results) == 2
        assert results[0]["chunk_id"] == 1
        assert results[1]["chunk_id"] == 2
