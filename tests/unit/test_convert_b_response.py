"""Tests for convert_b_response module."""

import json
import tempfile
from pathlib import Path

import pytest

from src.convert_b_response import (
    extract_question_from_prompt,
    extract_doc_uids_from_prompt,
    convert_file,
    convert_directory,
)


class TestExtractFunctions:
    """Tests for extraction functions."""

    def test_extract_question_from_prompt(self):
        """Test extracting question from prompt file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Some text\nQuestion: What is IFRS 9?\n\nMore text")
            f.flush()
            path = Path(f.name)

        result = extract_question_from_prompt(path)
        path.unlink()

        assert result == "What is IFRS 9?"

    def test_extract_question_not_found(self):
        """Test when question is not in prompt."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("No question here")
            f.flush()
            path = Path(f.name)

        result = extract_question_from_prompt(path)
        path.unlink()

        assert result is None

    def test_extract_doc_uids_from_prompt(self):
        """Test extracting document UIDs from prompt."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write('<Document name="ifrs-9">content</Document>')
            f.write('<Document name="ifric-16">content</Document>')
            f.write('<Document name="ifrs-9">duplicate</Document>')
            f.flush()
            path = Path(f.name)

        result = extract_doc_uids_from_prompt(path)
        path.unlink()

        # Should preserve order and remove duplicates
        assert result == ["ifrs-9", "ifric-16"]


class TestConvertFile:
    """Tests for convert_file function."""

    def test_convert_valid_json(self):
        """Test converting a valid JSON file."""
        b_json = {
            "assumptions_fr": ["Test assumption"],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "B-response.md"
            input_path.write_text(json.dumps(b_json))

            # Create a dummy A-prompt.txt
            prompt_path = Path(tmpdir) / "A-prompt.txt"
            prompt_path.write_text("Question: Test question")

            output_dir = Path(tmpdir) / "output"
            convert_file(input_path, output_dir)

            # Check output files exist
            assert (output_dir / "B-response.json").exists()
            assert (output_dir / "B-response.md").exists()

    def test_convert_invalid_json_raises(self):
        """Test that invalid JSON raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "B-response.md"
            input_path.write_text("not valid json {")

            with pytest.raises(ValueError, match="Invalid JSON"):
                convert_file(input_path, None)

    def test_convert_missing_file_raises(self):
        """Test that missing input file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            convert_file(Path("/nonexistent/file.md"), None)


class TestConvertDirectory:
    """Tests for convert_directory function."""

    def test_convert_directory_finds_files(self):
        """Test that directory conversion finds B-response.md files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create subdirectory with B-response.md
            subdir = Path(tmpdir) / "run1"
            subdir.mkdir()

            b_json = {"assumptions_fr": [], "recommendation": {"answer": "oui", "justification": "Test"}, "approaches": []}
            (subdir / "B-response.md").write_text(json.dumps(b_json))

            # Create another subdirectory with A-prompt.txt
            prompt_path = subdir / "A-prompt.txt"
            prompt_path.write_text("Question: Test?")

            convert_directory(Path(tmpdir))

            # Should create output files
            assert (subdir / "B-response.json").exists()
            assert (subdir / "B-response.md").exists()

    def test_convert_directory_no_files(self):
        """Test conversion of directory with no B-response files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Empty directory - should not raise
            convert_directory(Path(tmpdir))
