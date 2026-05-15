"""Tests for answer rendering artifacts."""

from __future__ import annotations

import pytest

from src.case_analysis.rendering import AnswerRenderingAdapter


class TestAnswerRenderingAdapter:
    """Behavior tests for the answer rendering adapter."""

    def test_renders_markdown_artifacts_from_typed_outputs(self) -> None:
        """The adapter should produce memo and FAQ markdown from typed JSON inputs."""
        adapter = AnswerRenderingAdapter()
        result = adapter.render_applicability_analysis(
            query="How should revenue be recognised?",
            retrieved_doc_uids=["ifrs15"],
            approach_identification_json={"primary_accounting_issue": "Revenue recognition under IFRS 15"},
            applicability_analysis_json={
                "assumptions_fr": ["Hypothèse de test"],
                "recommendation": {"answer": "oui", "justification": "Justification de test"},
                "approaches": [],
            },
            applicability_analysis_context=(
                '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n'
                '<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\n'
                "Revenue is recognised when control transfers.\n"
                "</chunk>\n"
                "</Document>"
            ),
        )

        if not result.memo_markdown:
            pytest.fail("Expected memo markdown")
        if not result.faq_markdown:
            pytest.fail("Expected FAQ markdown")
        if "Revenue recognition under IFRS 15" not in result.memo_markdown:
            pytest.fail("Expected primary accounting issue in memo markdown")
        if "Hypothèse de test" not in result.memo_markdown and "Hypothèse de test" not in result.faq_markdown:
            pytest.fail("Expected rendered assumptions in markdown output")
