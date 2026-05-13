"""Tests for authority sufficiency and citation verification stages."""

from __future__ import annotations

from src.case_analysis.models import AuthoritySufficiencyResult, CitationVerificationResult
from src.case_analysis.stages import AuthoritySufficiencyStage, VerifyCitationsStage


def test_authority_sufficiency_stage_continues_for_pass_payload() -> None:
    """A normal Prompt A pass payload should continue to applicability analysis."""
    stage = AuthoritySufficiencyStage()

    result = stage.execute({"status": "pass", "approaches": []})

    assert isinstance(result, AuthoritySufficiencyResult)
    assert result.status == "pass"
    assert result.should_continue is True


def test_authority_sufficiency_stage_stops_for_clarification_payload() -> None:
    """An explicit clarification status should route to a controlled failure."""
    stage = AuthoritySufficiencyStage()

    result = stage.execute({"status": "needs_clarification", "clarification_payload": {"questions": ["Missing fact?"]}})

    assert isinstance(result, AuthoritySufficiencyResult)
    assert result.status == "needs_clarification"
    assert result.should_continue is False
    assert result.reason == "needs_clarification"


def test_verify_citations_stage_passes_when_excerpt_matches_context() -> None:
    """Citation verifier should pass when each cited excerpt is in retrieved source text."""
    stage = VerifyCitationsStage()

    result = stage.execute(
        analysis_payload={"approaches": [{"references": [{"section": "1.1", "excerpt": "matching words"}]}]},
        chunk_data={"ifrs/doc/1.1": "This chunk contains matching words for the test."},
    )

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "pass"
    assert result.unsupported_references == []


def test_verify_citations_stage_fails_when_excerpt_is_not_in_context() -> None:
    """Citation verifier should flag cited text that is absent from retrieved source text."""
    stage = VerifyCitationsStage()

    result = stage.execute(
        analysis_payload={"approaches": [{"references": [{"section": "1.1", "excerpt": "missing words"}]}]},
        chunk_data={"ifrs/doc/1.1": "This chunk contains different text."},
    )

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "fail"
    assert result.unsupported_references == ["1.1: missing words"]


def test_verify_citations_stage_warns_when_no_references_are_present() -> None:
    """Citation verifier should warn, not fail, when no references are present."""
    stage = VerifyCitationsStage()

    result = stage.execute(analysis_payload={"recommendation": {"answer": "oui"}}, chunk_data={})

    assert isinstance(result, CitationVerificationResult)
    assert result.status == "warn"
    assert result.missing_references == ["No references found in applicability analysis."]
