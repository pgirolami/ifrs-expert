"""Tests for the answer-generation context builder."""

from __future__ import annotations

from src.case_analysis.context_builder import ContextBuilder
from src.case_analysis.models import ApproachIdentificationOutput


def _make_approach_output(authority_classification: dict[str, object], status: str = "pass") -> ApproachIdentificationOutput:
    return ApproachIdentificationOutput.model_validate(
        {
            "status": status,
            "primary_accounting_issue": "Issue",
            "authority_resolution": {
                "candidate_governing_documents": ["ifrs15"],
                "selected_primary_document": "ifrs15",
                "selection_reason": "reason",
                "discarded_due_to_overlap": [],
                "residual_uncertainty": "low",
            },
            "authority_classification": authority_classification,
            "treatment_families": [],
            "approaches": [],
        }
    )


class TestContextBuilder:
    """Behavior tests for ContextBuilder."""

    def test_filters_applicability_context_to_authority_references(self) -> None:
        builder = ContextBuilder()
        formatted_chunks = [
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\nprimary\n</chunk>\n\n<chunk id="2" doc_uid="ifrs15" paragraph="5.2" score="0.8500">\nexcluded\n</chunk>\n</Document>',
            '<Document name="ias21" document_type="ias" document_kind="standard">\n<chunk id="3" doc_uid="ias21" paragraph="8.2" score="0.8100">\nsupporting\n</chunk>\n</Document>',
        ]
        approach_identification_output = _make_approach_output(
            {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1"]}],
                "supporting_authority": [{"document": "ias21", "references": ["8.2"]}],
                "peripheral_authority": [],
            }
        )

        context = builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert "primary" in context
        assert "supporting" in context
        assert "excluded" not in context

    def test_uses_all_chunks_when_authority_classification_empty(self) -> None:
        builder = ContextBuilder()
        formatted_chunks = ["chunk-a", "chunk-b"]
        approach_identification_output = _make_approach_output(
            {
                "primary_authority": [],
                "supporting_authority": [],
                "peripheral_authority": [],
            }
        )

        context = builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert context == "chunk-a\n\nchunk-b"

    def test_falls_back_to_all_chunks_when_no_authority_matches(self) -> None:
        builder = ContextBuilder()
        formatted_chunks = [
            '<Document name="doc1" document_type="ifrs" document_kind="standard">\n<chunk id="1" doc_uid="doc1" paragraph="1.1" score="0.5000">\ncontent\n</chunk>\n</Document>',
        ]
        approach_identification_output = _make_approach_output(
            {
                "primary_authority": [{"document": "other", "references": ["9.9"]}],
                "supporting_authority": [],
                "peripheral_authority": [],
            }
        )

        context = builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert context == formatted_chunks[0]
