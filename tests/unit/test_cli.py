"""Tests for CLI."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest


class TestCli:
    """Tests for CLI commands."""

    @pytest.fixture
    def ifrs16_pdf(self) -> Path:
        """Path to IFRS 16 test PDF."""
        return Path(__file__).parent.parent.parent / "examples" / "ifrs-16-leases_38-39.pdf"

    def test_chunk_command_output(self, ifrs16_pdf, capsys):
        """Test chunk command outputs JSON."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        from src.cli import chunk_command

        # Create a mock args namespace
        class Args:
            pdf = str(ifrs16_pdf)

        result = chunk_command(Args())

        assert result == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert isinstance(data, list)
        assert len(data) > 0

    def test_chunk_command_nonexistent_file(self, capsys):
        """Test chunk command with non-existent file."""
        from src.cli import chunk_command

        class Args:
            pdf = "/nonexistent/file.pdf"

        result = chunk_command(Args())

        assert result == 1

    @patch("src.cli.VectorStore")
    @patch("src.cli.ChunkStore")
    @patch("src.cli.init_db")
    def test_store_command(self, mock_init_db, mock_chunk_store_cls, mock_vector_store_cls, ifrs16_pdf, capsys):
        """Test store command stores chunks and embeddings."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        # Setup mocks
        mock_chunk_store = mock_chunk_store_cls.return_value.__enter__.return_value
        mock_chunk_store.get_chunks_by_doc.return_value = []
        mock_chunk_store.insert_chunks.return_value = [1, 2, 3]

        mock_vector_store = mock_vector_store_cls.return_value.__enter__.return_value
        mock_vector_store.delete_by_doc.return_value = 0
        mock_vector_store.add_embeddings.return_value = None

        from src.cli import store_command

        class Args:
            pdf = str(ifrs16_pdf)
            doc_uid = "test-doc"

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("src.db.connection.DB_PATH", Path(tmpdir) / "test.db"):
                with patch("src.vector.store.INDEX_PATH", Path(tmpdir) / "faiss.index"):
                    result = store_command(Args())

        assert result == 0
        mock_chunk_store.insert_chunks.assert_called_once()

    @patch("src.cli.VectorStore")
    @patch("src.cli.ChunkStore")
    @patch("src.cli.init_db")
    def test_store_command_nonexistent_file(self, mock_init_db, mock_chunk_store_cls, mock_vector_store_cls, capsys):
        """Test store command with non-existent file."""
        from src.cli import store_command

        class Args:
            pdf = "/nonexistent/file.pdf"
            doc_uid = None

        result = store_command(Args())

        assert result == 1

    @patch("src.cli.ChunkStore")
    @patch("src.cli.init_db")
    def test_list_command_docs(self, mock_init_db, mock_chunk_store_cls, capsys):
        """Test list command shows all documents."""
        mock_chunk_store = mock_chunk_store_cls.return_value.__enter__.return_value
        mock_chunk_store.get_all_docs.return_value = ["doc1", "doc2"]

        from src.cli import list_command

        class Args:
            doc_uid = None

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("src.db.connection.DB_PATH", Path(tmpdir) / "test.db"):
                result = list_command(Args())

        assert result == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data == ["doc1", "doc2"]

    @patch("src.cli.ChunkStore")
    @patch("src.cli.init_db")
    def test_list_command_chunks(self, mock_init_db, mock_chunk_store_cls, capsys):
        """Test list command shows chunks for a specific document."""
        mock_chunk_store = mock_chunk_store_cls.return_value.__enter__.return_value
        mock_chunk_store.get_chunks_by_doc.return_value = [
            type("Chunk", (), {"chunk_id": 1, "doc_uid": "doc1", "section_path": "B43", "page_start": "A1", "page_end": "A1", "text": "test"})()
        ]

        from src.cli import list_command

        class Args:
            doc_uid = "doc1"

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("src.db.connection.DB_PATH", Path(tmpdir) / "test.db"):
                result = list_command(Args())

        assert result == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert len(data) == 1
        assert data[0]["section_path"] == "B43"

    def test_main_no_command(self):
        """Test main function with no command."""
        from src.cli import main
        import sys
        from io import StringIO

        with patch("sys.argv", ["cli"]), patch("sys.stdout", StringIO()):
            with patch("sys.stdin", StringIO()):
                result = main()

        assert result == 1

    def test_main_with_help(self):
        """Test main function with --help."""
        from src.cli import main
        import sys
        from io import StringIO

        old_stdout = sys.stdout
        old_argv = sys.argv
        try:
            sys.argv = ["cli", "--help"]
            sys.stdout = StringIO()
            result = main()
        except SystemExit:
            pass
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
