"""Tests for typed prompt stages in case-analysis workflow."""

from __future__ import annotations

from src.case_analysis.models import ApplicabilityAnalysisResult, AuthorityClassificationResult, ValidationFailure
from src.case_analysis.stages import ClassifyAuthorityStage, EvaluateApplicabilityStage


def test_classify_authority_stage_returns_typed_result() -> None:
    """Prompt A stage should parse an object response into a typed authority result."""
    stage = ClassifyAuthorityStage(send_to_llm_fn=lambda prompt: '{"status": "pass", "approaches": []}')

    result = stage.execute(prompt_text="Prompt A text")

    assert isinstance(result, AuthorityClassificationResult)
    assert result.raw_response == '{"status": "pass", "approaches": []}'
    assert result.payload == {"status": "pass", "approaches": []}


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


def test_evaluate_applicability_stage_returns_typed_result() -> None:
    """Prompt B stage should parse an object response into a typed applicability result."""
    stage = EvaluateApplicabilityStage(send_to_llm_fn=lambda prompt: '{"recommendation": {"answer": "oui"}}')

    result = stage.execute(prompt_text="Prompt B text")

    assert isinstance(result, ApplicabilityAnalysisResult)
    assert result.raw_response == '{"recommendation": {"answer": "oui"}}'
    assert result.payload == {"recommendation": {"answer": "oui"}}


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
