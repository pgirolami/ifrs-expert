"""Tests for typed prompt stages in case-analysis workflow."""

from __future__ import annotations

import json

from src.case_analysis.models import ApplicabilityAnalysisResult, AuthorityClassificationResult, PromptAPassOutput, PromptBPassOutput, ValidationFailure
from src.case_analysis.stages import ClassifyAuthorityStage, EvaluateApplicabilityStage


def _prompt_a_payload() -> dict[str, object]:
    return {
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


def _prompt_b_payload() -> dict[str, object]:
    return {
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


def test_classify_authority_stage_returns_typed_result() -> None:
    """Prompt A stage should parse and validate the Pydantic authority result."""
    raw_response = json.dumps(_prompt_a_payload())
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: raw_response)

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, AuthorityClassificationResult)
    assert isinstance(result.output, PromptAPassOutput)
    assert result.raw_response == raw_response
    assert result.payload["status"] == "pass"
    assert result.payload["approaches"] == [
        {
            "id": "approach_1",
            "label": "Revenue recognition",
            "normalized_label": "revenue_recognition",
            "rationale_for_inclusion": "The standard provides the governing model.",
        }
    ]


def test_classify_authority_stage_rejects_invalid_json() -> None:
    """Prompt A stage should return a structured failure for invalid JSON."""
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: "not json")

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "prompt_a_parse"
    assert result.reason == "invalid_json"
    assert "LLM returned invalid JSON" in result.message


def test_classify_authority_stage_rejects_non_object_json() -> None:
    """Prompt A stage should reject JSON arrays because the contract is an object."""
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: "[]")

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "prompt_a_parse"
    assert result.reason == "invalid_contract"


def test_classify_authority_stage_rejects_missing_required_prompt_a_fields() -> None:
    """Prompt A stage should reject pass responses that omit required contract fields."""
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: '{"status": "pass", "approaches": []}')

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "prompt_a_parse"
    assert result.reason == "invalid_contract"
    assert "primary_accounting_issue" in result.message


def test_classify_authority_stage_accepts_clarification_contract() -> None:
    """Prompt A stage should accept the compact clarification output contract."""
    raw_response = '{"status": "needs_clarification", "questions": ["Which contract terms apply?"]}'
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: raw_response)

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, AuthorityClassificationResult)
    assert result.payload == {"status": "needs_clarification", "questions": ["Which contract terms apply?"]}


def test_evaluate_applicability_stage_returns_typed_result() -> None:
    """Prompt B stage should parse and validate the Pydantic applicability result."""
    raw_response = json.dumps(_prompt_b_payload())
    stage = EvaluateApplicabilityStage(send_to_llm_fn=lambda prompt: raw_response)

    result = stage.execute(prompt_text="Prompt B text")

    assert isinstance(result, ApplicabilityAnalysisResult)
    assert isinstance(result.output, PromptBPassOutput)
    assert result.raw_response == raw_response
    assert result.payload["recommendation"] == {"answer": "oui", "justification": "Le modèle IFRS 15 s'applique aux faits décrits."}


def test_evaluate_applicability_stage_rejects_missing_required_prompt_b_fields() -> None:
    """Prompt B stage should reject recommendation-only JSON without approach analysis."""
    stage = EvaluateApplicabilityStage(send_to_llm_fn=lambda prompt: '{"recommendation": {"answer": "oui"}}')

    result = stage.execute(prompt_text="Prompt B text")

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "prompt_b_parse"
    assert result.reason == "invalid_contract"
    assert "approaches" in result.message


def test_evaluate_applicability_stage_returns_call_failure() -> None:
    """Prompt B stage should turn LLM runtime errors into structured failures."""

    def failing_send_to_llm(prompt: str) -> str:
        del prompt
        raise RuntimeError("provider down")

    stage = EvaluateApplicabilityStage(send_to_llm_fn=failing_send_to_llm)

    result = stage.execute(prompt_text="Prompt B text")

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "prompt_b"
    assert result.reason == "llm_call_failed"
    assert "provider down" in result.message
