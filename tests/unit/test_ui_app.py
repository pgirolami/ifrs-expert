"""Tests for Streamlit app helpers."""

from __future__ import annotations

from src.case_analysis.models import ApplicabilityAnalysisOutput
from src.models.answer_command_result import AnswerCommandResult
from src.ui.app import _get_assistant_display_text


def test_get_assistant_display_text_prefers_markdown() -> None:
    """Grounded markdown should be displayed first."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        applicability_analysis_memo_markdown="# Markdown answer",
        applicability_analysis_output=ApplicabilityAnalysisOutput.model_validate({"status": "pass", "assumptions_fr": [], "recommendation": {"answer": "oui", "justification": ""}, "approaches": []}),
    )

    assert _get_assistant_display_text(result) == "# Markdown answer"


def test_get_assistant_display_text_falls_back_to_typed_output() -> None:
    """Typed output should be used when markdown is unavailable."""
    result = AnswerCommandResult(
        query="test",
        success=True,
        applicability_analysis_output=ApplicabilityAnalysisOutput.model_validate({"status": "pass", "assumptions_fr": [], "recommendation": {"answer": "oui", "justification": ""}, "approaches": []}),
    )

    assert '"status": "pass"' in _get_assistant_display_text(result)


def test_get_assistant_display_text_handles_missing_content() -> None:
    """Missing answer content should return a fallback message."""
    result = AnswerCommandResult(query="test", success=True)

    assert _get_assistant_display_text(result) == "No answer returned."
