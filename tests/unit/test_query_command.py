"""Tests for query command."""

import json
from unittest.mock import MagicMock, patch

from src.commands import QueryCommand, QueryOptions
from src.db.chunks import Chunk


class TestQueryCommand:
    """Tests for query command."""

    def test_query_no_index(self):
        """Test query command when no index exists."""
        with patch("src.commands.query.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = False

            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=None))
            result = command.execute()

            assert result.startswith("Error:")
            assert "No index found" in result

    def test_query_with_results(self):
        """Test query returns matching chunks."""
        # Mock VectorStore search results (using score instead of distance)
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        # Mock chunks returned from database
        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            # Setup path mock
            mock_path.return_value.exists.return_value = True

            # Setup VectorStore mock
            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Setup ChunkStore mock
            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test query", options=QueryOptions(k=5, min_score=None, verbose=False))
            result = command.execute()

            # Verify search was called
            mock_vs.search_all.assert_called_once_with("test query")
            # Verify chunks were retrieved (called once per unique doc_uid)
            assert mock_cs.get_chunks_by_doc.call_count == 1
            # Verify results
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

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.side_effect = [doc1_chunks, doc2_chunks]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test query", options=QueryOptions(k=2, min_score=None, verbose=False))
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
        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = []
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=None, verbose=False))
            result = command.execute()

            assert result == "Error: No chunks retrieved"

    def test_query_exception_handling(self):
        """Test query command exception handling."""
        with patch("src.commands.query.get_index_path") as mock_path:
            # Make exists() raise an exception
            mock_path.return_value.exists.side_effect = RuntimeError("Test error")

            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=None, verbose=False))
            result = command.execute()

            assert result.startswith("Error:")
            assert "Test error" in result

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

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:

            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Query with min_score of 0.5 should filter out chunk 2
            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=0.5, verbose=False))
            result = command.execute()

            mock_vs.search_all.assert_called_once_with("test")

            data = json.loads(result)
            assert len(data) == 1
            assert data[0]["id"] == 1

    def test_query_verbose_output(self):
        """Test query verbose output includes relevance."""
        # Mock search results with different scores
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},  # High
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.2},  # Low
        ]

        # Mock chunks returned from database
        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:

            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Test verbose output (both results are above threshold)
            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=None, verbose=True))
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

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test", options=QueryOptions(k=5, min_score=None, verbose=False, expand=1))
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

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(
                query="test",
                options=QueryOptions(
                    k=5,
                    min_score=None,
                    verbose=False,
                    expand=0,
                    full_doc_threshold=10,
                ),
            )
            result = command.execute()

            data = json.loads(result)
            assert [item["id"] for item in data] == [1, 2, 3]
            assert data[1]["score"] == 0.9
            assert data[0]["score"] == 0.0
            assert data[2]["score"] == 0.0