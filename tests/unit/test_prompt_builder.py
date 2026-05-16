"""Tests for prompt construction."""

from __future__ import annotations

from src.case_analysis.models import ApproachIdentificationOutput
from src.case_analysis.prompt_builder import PromptBuilder


class TestPromptBuilder:
    """Behavior tests for prompt builder."""

    def test_builds_approach_identification_prompt(self) -> None:
        builder = PromptBuilder()
        template = "Question: {{QUERY}}\n\nChunks:\n{{CHUNKS}}"

        prompt = builder.build_approach_identification(template, "Q", ["chunk-1", "chunk-2"], "summary")

        assert "summary" in prompt
        assert "Question: Q" in prompt
        assert "chunk-1" in prompt
        assert "chunk-2" in prompt

    def test_builds_applicability_analysis_prompt(self) -> None:
        builder = PromptBuilder()
        template = "Question: {{QUERY}}\n\nChunks:\n{{CHUNKS}}\n\nApproaches:\n{{APPROACHES_JSON}}"
        approach_identification = ApproachIdentificationOutput.model_validate(
            {
                "status": "pass",
                "primary_accounting_issue": "Issue",
                "authority_resolution": {
                    "candidate_governing_documents": [],
                    "selected_primary_document": None,
                    "selection_reason": None,
                    "discarded_due_to_overlap": [],
                    "residual_uncertainty": None,
                },
                "authority_classification": {"primary_authority": [], "supporting_authority": [], "peripheral_authority": []},
                "treatment_families": [],
                "approaches": [],
            }
        )

        prompt = builder.build_applicability_analysis(template, "Q", "context", approach_identification)

        assert "Question: Q" in prompt
        assert "context" in prompt
        assert '"status": "pass"' in prompt
