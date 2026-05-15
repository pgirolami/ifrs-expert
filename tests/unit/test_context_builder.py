"""Tests for the answer-generation context builder."""

from __future__ import annotations

from src.case_analysis.context_builder import ContextBuilder


class TestContextBuilder:
    """Behavior tests for ContextBuilder."""

    def test_filters_applicability_context_to_authority_references(self) -> None:
        """Only the referenced authority chunks should remain in the context."""
        builder = ContextBuilder()
        formatted_chunks = [
            '<Document name="ifrs15" document_type="ifrs" document_kind="standard">\n<chunk id="1" doc_uid="ifrs15" paragraph="5.1" score="0.9000">\nprimary\n</chunk>\n\n<chunk id="2" doc_uid="ifrs15" paragraph="5.2" score="0.8500">\nexcluded\n</chunk>\n</Document>',
            '<Document name="ias21" document_type="ias" document_kind="standard">\n<chunk id="3" doc_uid="ias21" paragraph="8.2" score="0.8100">\nsupporting\n</chunk>\n</Document>',
        ]
        approach_identification_json = {
            "authority_classification": {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1"]}],
                "supporting_authority": [{"document": "ias21", "references": ["8.2"]}],
            }
        }

        context = builder.build_applicability_analysis_context(formatted_chunks, approach_identification_json)

        assert "primary" in context
        assert "supporting" in context
        assert "excluded" not in context

    def test_uses_all_chunks_when_authority_classification_missing(self) -> None:
        """Missing authority classification should keep the full chunk context."""
        builder = ContextBuilder()
        formatted_chunks = ["chunk-a", "chunk-b"]

        context = builder.build_applicability_analysis_context(formatted_chunks, {"status": "pass"})

        assert context == "chunk-a\n\nchunk-b"

    def test_falls_back_to_all_chunks_when_no_authority_matches(self) -> None:
        """When nothing matches, the builder should preserve the original context."""
        builder = ContextBuilder()
        formatted_chunks = [
            '<Document name="doc1" document_type="ifrs" document_kind="standard">\n<chunk id="1" doc_uid="doc1" paragraph="1.1" score="0.5000">\ncontent\n</chunk>\n</Document>',
        ]
        approach_identification_json = {
            "authority_classification": {
                "primary_authority": [{"document": "other", "references": ["9.9"]}],
                "supporting_authority": [],
            }
        }

        context = builder.build_applicability_analysis_context(formatted_chunks, approach_identification_json)

        assert context == formatted_chunks[0]
