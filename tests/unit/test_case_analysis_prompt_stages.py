"""Tests for typed prompt stages in case-analysis workflow."""

from __future__ import annotations

from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, ValidationFailure
from src.case_analysis.stages import ApproachIdentificationStage, ApplicabilityAnalysisStage
from tests.fakes import FakeAnswerGenerator

APPROACH_IDENTIFICATION_OUTPUT = ApproachIdentificationOutput.model_validate(
    {
        "status": "pass",
        "primary_accounting_issue": "Whether the fact pattern is in scope of IFRS 15.",
        "authority_resolution": {
            "candidate_governing_documents": ["ifrs15"],
            "selected_primary_document": "ifrs15",
            "selection_reason": "IFRS 15 directly governs revenue from contracts with customers.",
            "discarded_due_to_overlap": [],
            "residual_uncertainty": "Low uncertainty because no competing standard is present.",
        },
        "authority_classification": {
            "primary_authority": [{"document": "ifrs15", "references": ["5"], "reason": "Direct scope paragraph."}],
            "supporting_authority": [],
            "peripheral_authority": [],
        },
        "treatment_families": [
            {
                "family": "Revenue recognition model",
                "authority_basis": [{"document": "ifrs15", "references": ["5"]}],
                "mapped_approaches": ["revenue_recognition"],
            }
        ],
        "approaches": [
            {
                "id": "approach_1",
                "label": "Revenue recognition",
                "normalized_label": "revenue_recognition",
                "rationale_for_inclusion": "The standard provides the governing model.",
            }
        ],
    }
)

APPLICABILITY_ANALYSIS_OUTPUT = ApplicabilityAnalysisOutput.model_validate(
    {
        "status": "pass",
        "assumptions_fr": ["Le contrat relève d'IFRS 15."],
        "recommendation": {"answer": "oui", "justification": "Le modèle IFRS 15 s'applique aux faits décrits."},
        "approaches": [
            {
                "id": "approach_1",
                "normalized_label": "revenue_recognition",
                "label_fr": "Comptabilisation du chiffre d'affaires",
                "applicability": "oui",
                "reasoning_fr": "IFRS 15.5 couvre les contrats avec des clients dans cette situation.",
                "conditions_fr": [],
                "practical_implication_fr": "Appliquer le modèle en cinq étapes.",
                "references": [{"document": "ifrs15", "section": "5", "excerpt": "IFRS 15 applies to contracts with customers."}],
            }
        ],
    }
)


class TestCaseAnalysisPromptStages:
    """Tests for typed Approach identification and Applicability analysis stages."""

    def test_classify_authority_stage_returns_typed_result(self) -> None:
        """Approach identification stage should return the typed output directly."""
        generator = FakeAnswerGenerator(approach_identification_output=APPROACH_IDENTIFICATION_OUTPUT, applicability_analysis_output=APPLICABILITY_ANALYSIS_OUTPUT)
        stage = ApproachIdentificationStage(answer_generator=generator)

        result = stage.execute(prompt_text="Approach identification text")

        assert isinstance(result, ApproachIdentificationOutput)
        assert result == APPROACH_IDENTIFICATION_OUTPUT
        assert generator.approach_identification_prompts == ["Approach identification text"]

    def test_classify_authority_stage_returns_call_failure(self) -> None:
        """Approach identification stage should turn generator runtime errors into structured failures."""
        generator = FakeAnswerGenerator(approach_identification_output=RuntimeError("provider down"), applicability_analysis_output=APPLICABILITY_ANALYSIS_OUTPUT)
        stage = ApproachIdentificationStage(answer_generator=generator)

        result = stage.execute(prompt_text="Approach identification text")

        assert isinstance(result, ValidationFailure)
        assert result.error_stage == "approach_identification"
        assert result.reason == "llm_call_failed"
        assert "provider down" in result.message

    def test_evaluate_applicability_stage_returns_typed_result(self) -> None:
        """Applicability analysis stage should return the typed output directly."""
        generator = FakeAnswerGenerator(approach_identification_output=APPROACH_IDENTIFICATION_OUTPUT, applicability_analysis_output=APPLICABILITY_ANALYSIS_OUTPUT)
        stage = ApplicabilityAnalysisStage(answer_generator=generator)

        result = stage.execute(prompt_text="Applicability analysis text")

        assert isinstance(result, ApplicabilityAnalysisOutput)
        assert result == APPLICABILITY_ANALYSIS_OUTPUT
        assert generator.applicability_analysis_prompts == ["Applicability analysis text"]

    def test_evaluate_applicability_stage_returns_call_failure(self) -> None:
        """Applicability analysis stage should turn generator runtime errors into structured failures."""
        generator = FakeAnswerGenerator(approach_identification_output=APPROACH_IDENTIFICATION_OUTPUT, applicability_analysis_output=RuntimeError("provider down"))
        stage = ApplicabilityAnalysisStage(answer_generator=generator)

        result = stage.execute(prompt_text="Applicability analysis text")

        assert isinstance(result, ValidationFailure)
        assert result.error_stage == "applicability_analysis"
        assert result.reason == "llm_call_failed"
        assert "provider down" in result.message
