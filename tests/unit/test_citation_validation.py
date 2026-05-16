"""Tests for citation validation."""

from __future__ import annotations

from src.case_analysis.citation_validation import CitationValidationService
from src.case_analysis.models import ApplicabilityAnalysisOutput


class TestCitationValidationService:
    """Behavior tests for citation validation service."""

    def test_builds_chunk_data_for_markdown(self) -> None:
        service = CitationValidationService()
        context = (
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n'
            '<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\n'
            "Revenue is recognised.\n"
            "</chunk>\n"
            "</Document>"
        )

        chunk_data = service.build_chunk_data_for_markdown(context)

        assert chunk_data == {"ifrs15/5.1": "Revenue is recognised."}

    def test_validates_pass_output_references(self) -> None:
        service = CitationValidationService()
        analysis_output = ApplicabilityAnalysisOutput.model_validate(
            {
                "status": "pass",
                "assumptions_fr": ["Hypothèse"],
                "recommendation": {"answer": "oui", "justification": "Justification"},
                "approaches": [
                    {
                        "id": "approach_1",
                        "normalized_label": "revenue_recognition",
                        "label_fr": "Comptabilisation",
                        "applicability": "oui",
                        "reasoning_fr": "Raison",
                        "conditions_fr": [],
                        "practical_implication_fr": "Implication",
                        "references": [{"document": "ifrs15", "section": "5.1", "excerpt": "Revenue is recognised."}],
                    }
                ],
            }
        )

        result = service.validate_applicability_analysis(
            analysis_output,
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\nRevenue is recognised.\n</chunk>\n</Document>',
        )

        assert result.status == "pass"
