"""Tests for authority sufficiency and citation verification stages."""

from __future__ import annotations

from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, CitationVerificationResult
from src.case_analysis.stages import AuthoritySufficiencyStage, VerifyCitationsStage


def test_authority_sufficiency_stage_continues_for_pass_payload() -> None:
    """A normal approach-identification pass payload should continue to applicability analysis."""
    stage = AuthoritySufficiencyStage()
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

    result = stage.execute(approach_identification)

    assert result is None


def test_authority_sufficiency_stage_stops_for_clarification_payload() -> None:
    """A clarification status should route to a controlled failure."""
    stage = AuthoritySufficiencyStage()
    approach_identification = ApproachIdentificationOutput.model_validate(
        {
            "status": "needs_clarification",
            "questions": ["Missing fact?"],
        }
    )

    result = stage.execute(approach_identification)

    assert result is not None
    assert result.error_stage == "authority_sufficiency"
    assert result.reason == "needs_clarification"


def test_verify_citations_stage_passes_when_excerpt_matches_context() -> None:
    """Citation verifier should pass when each cited excerpt is in retrieved source text."""
    stage = VerifyCitationsStage()

    analysis_output = ApplicabilityAnalysisOutput.model_validate(
        {
            "status": "pass",
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": ""},
            "approaches": [
                {
                    "id": "a",
                    "normalized_label": "a",
                    "label_fr": "A",
                    "applicability": "oui",
                    "reasoning_fr": "",
                    "conditions_fr": [],
                    "practical_implication_fr": "",
                    "references": [{"document": "ifrs", "section": "1.1", "excerpt": "matching words"}],
                }
            ],
        }
    )
    result = stage.execute(analysis_output=analysis_output, chunk_data={"ifrs/1.1": "This chunk contains matching words for the test."})

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "pass"
    assert result.unsupported_references == []


def test_verify_citations_stage_fails_when_excerpt_is_not_in_context() -> None:
    """Citation verifier should flag cited text that is absent from retrieved source text."""
    stage = VerifyCitationsStage()

    analysis_output = ApplicabilityAnalysisOutput.model_validate(
        {
            "status": "pass",
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": ""},
            "approaches": [
                {
                    "id": "a",
                    "normalized_label": "a",
                    "label_fr": "A",
                    "applicability": "oui",
                    "reasoning_fr": "",
                    "conditions_fr": [],
                    "practical_implication_fr": "",
                    "references": [{"document": "ifrs", "section": "1.1", "excerpt": "missing words"}],
                }
            ],
        }
    )
    result = stage.execute(analysis_output=analysis_output, chunk_data={"ifrs/1.1": "This chunk contains different text."})

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "fail"
    assert result.unsupported_references == ["1.1: missing words"]


def test_verify_citations_stage_warns_when_no_references_are_present() -> None:
    """Citation verifier should warn, not fail, when no references are present."""
    stage = VerifyCitationsStage()

    analysis_output = ApplicabilityAnalysisOutput.model_validate({"status": "pass", "assumptions_fr": [], "recommendation": {"answer": "oui", "justification": ""}, "approaches": []})
    result = stage.execute(analysis_output=analysis_output, chunk_data={})

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "warn"
    assert result.missing_references == ["No references found in applicability analysis."]
