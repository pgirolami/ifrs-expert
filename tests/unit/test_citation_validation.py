"""Tests for citation validation helpers."""

from __future__ import annotations

import pytest

from src.case_analysis.citation_validation import CitationValidationService
from src.case_analysis.models import ApplicabilityAnalysisPassOutput


class TestCitationValidationService:
    """Behavior tests for citation validation."""

    def test_build_chunk_data_for_markdown_indexes_chunk_text(self) -> None:
        """Chunk data should be indexed by document UID and section number."""
        service = CitationValidationService()
        context = (
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n'
            '<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\n'
            "Revenue is recognised when control transfers.\n"
            "</chunk>\n"
            "</Document>"
        )

        chunk_data = service.build_chunk_data_for_markdown(context)

        if chunk_data.get("ifrs15/5.1") != "Revenue is recognised when control transfers.":
            pytest.fail("Expected chunk text to be indexed for citation validation")

    def test_validate_applicability_analysis_returns_pass_for_matching_reference(self) -> None:
        """Citation validation should pass when the cited excerpt exists in context."""
        service = CitationValidationService()
        context = (
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n'
            '<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\n'
            "Revenue is recognised when control transfers.\n"
            "</chunk>\n"
            "</Document>"
        )

        analysis_output = ApplicabilityAnalysisPassOutput.model_validate(
            {
                "assumptions_fr": [],
                "recommendation": {"answer": "oui", "justification": ""},
                "approaches": [{"id": "a", "normalized_label": "a", "label_fr": "A", "applicability": "oui", "reasoning_fr": "", "conditions_fr": [], "practical_implication_fr": "", "references": [{"document": "ifrs15", "section": "5.1", "excerpt": "Revenue is recognised"}]}],
            }
        )
        result = service.validate_applicability_analysis(analysis_output, context)

        if result.status != "pass":
            pytest.fail("Expected citation validation to pass")
