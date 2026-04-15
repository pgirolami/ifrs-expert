"""Tests for Streamlit app helpers."""

from __future__ import annotations

from src.models.answer_command_result import AnswerCommandResult
from src.ui.app import _get_assistant_display_text


def test_get_assistant_display_text_prefers_markdown() -> None:
    """Grounded markdown should be displayed first."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        prompt_b_memo_markdown="# Markdown answer",
        prompt_b_raw_response="raw answer",
    )

    assert _get_assistant_display_text(result) == "# Markdown answer"


def test_get_assistant_display_text_falls_back_to_raw_response() -> None:
    """Raw response should be used when markdown is unavailable."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        prompt_b_raw_response="raw answer",
    )

    assert _get_assistant_display_text(result) == "raw answer"


def test_get_assistant_display_text_handles_missing_content() -> None:
    """Missing answer content should return a fallback message."""
    result = AnswerCommandResult(query="test", success=True)

    assert _get_assistant_display_text(result) == "No answer returned."
