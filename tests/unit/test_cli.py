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
