"""Answer command result models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, CitationVerificationResult
    from src.models.provenance import Provenance


@dataclass
class RetrievedDocumentHit:
    """One retrieved document candidate selected during answer generation."""

    doc_uid: str
    score: float
    document_type: str | None = None
    document_kind: str | None = None


@dataclass
class RetrievedChunkHit:
    """One retrieved chunk selected during answer generation."""

    doc_uid: str
    chunk_number: str
    chunk_id: str
    score: float
    document_type: str | None = None
    document_kind: str | None = None
    containing_section_id: str | None = None
    containing_section_db_id: int | None = None
    page_start: str | None = None
    page_end: str | None = None
    text: str | None = None
    provenance: Provenance | None = None


@dataclass
class AnswerCommandResult:
    """Artifacts produced by one AnswerCommand execution."""

    query: str
    success: bool = False
    retrieved_doc_uids: list[str] = field(default_factory=list)
    document_hits: list[RetrievedDocumentHit] = field(default_factory=list)
    chunk_hits: list[RetrievedChunkHit] = field(default_factory=list)
    approach_identification_text: str | None = None
    approach_identification_output: ApproachIdentificationOutput | None = None
    applicability_analysis_text: str | None = None
    applicability_analysis_output: ApplicabilityAnalysisOutput | None = None
    citation_verification_result: CitationVerificationResult | None = None
    applicability_analysis_memo_markdown: str | None = None
    applicability_analysis_faq_markdown: str | None = None
    error: str | None = None
    error_stage: str | None = None

    @classmethod
    def failure(
        cls,
        query: str,
        error: str,
        error_stage: str | None = None,
    ) -> AnswerCommandResult:
        """Build a failed result."""
        return cls(query=query, success=False, error=error, error_stage=error_stage)

    def mark_success(self) -> None:
        """Mark the result as successful."""
        self.success = True
        self.error = None
        self.error_stage = None
