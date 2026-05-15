"""Typed models shared by case-analysis workflow stages."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, cast

from pydantic import BaseModel, ConfigDict, Field

from src.models.provenance import Provenance

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.retrieval.models import DocumentHit, RetrievalResult


class ValidationFailure(BaseModel):
    """Structured stage failure that can be converted to command errors."""

    error_stage: str
    reason: str
    message: str


class ValidatedQuestion(BaseModel):
    """Validated question text ready for workflow execution."""

    question: str


class SourceChunkResult(BaseModel):
    """Pydantic representation of one retrieved chunk hit."""

    doc_uid: str
    chunk_id: int
    score: float
    provenance: Provenance | None = None

    @classmethod
    def from_search_result(cls, result: SearchResult) -> SourceChunkResult:
        """Create a typed chunk result from the current SearchResult shape."""
        provenance_value = result.get("provenance")
        provenance = Provenance(provenance_value) if provenance_value is not None else None
        return cls(
            doc_uid=result["doc_uid"],
            chunk_id=result["chunk_id"],
            score=result["score"],
            provenance=provenance,
        )

    def to_search_result(self) -> SearchResult:
        """Convert back to the current SearchResult shape used by legacy helpers."""
        result: dict[str, str | int | float | Provenance] = {
            "doc_uid": self.doc_uid,
            "chunk_id": self.chunk_id,
            "score": self.score,
        }
        if self.provenance is not None:
            result["provenance"] = self.provenance
        return cast("SearchResult", result)


class DocumentSourceHit(BaseModel):
    """Pydantic representation of one retrieved document hit."""

    doc_uid: str
    score: float
    document_type: str

    @classmethod
    def from_document_hit(cls, hit: DocumentHit) -> DocumentSourceHit:
        """Create a typed document hit from the current retrieval result shape."""
        return cls(doc_uid=hit.doc_uid, score=hit.score, document_type=hit.document_type)


class RetrievedSourcePackage(BaseModel):
    """Retrieved material before authority classification."""

    policy_name: str
    document_routing_source: str
    document_routing_post_processing: str
    chunk_retrieval_mode: str
    document_hits: list[DocumentSourceHit]
    chunk_results: list[SourceChunkResult]
    doc_chunks: dict[str, list[object]]

    @classmethod
    def from_retrieval_result(cls, result: RetrievalResult) -> RetrievedSourcePackage:
        """Build a source package from the existing retrieval pipeline result."""
        return cls(
            policy_name=result.policy_name,
            document_routing_source=result.document_routing_source,
            document_routing_post_processing=result.document_routing_post_processing,
            chunk_retrieval_mode=result.chunk_retrieval_mode,
            document_hits=[DocumentSourceHit.from_document_hit(hit) for hit in result.document_hits],
            chunk_results=[SourceChunkResult.from_search_result(search_result) for search_result in result.chunk_results],
            doc_chunks=cast("dict[str, list[object]]", result.doc_chunks),
        )

    @property
    def retrieved_doc_uids(self) -> list[str]:
        """Return document UIDs in first-appearance order from final chunk results."""
        return list(dict.fromkeys(result.doc_uid for result in self.chunk_results))

    def to_search_results(self) -> list[SearchResult]:
        """Convert chunk results back to the current SearchResult shape."""
        return [result.to_search_result() for result in self.chunk_results]

    def to_doc_chunks(self) -> dict[str, list[Chunk]]:
        """Convert stored chunks back to the current Chunk dataclass mapping."""
        return cast("dict[str, list[Chunk]]", self.doc_chunks)


class AuthorityReference(BaseModel):
    """One document reference used in approach identification authority output."""

    model_config = ConfigDict(extra="allow")

    document: str
    references: list[str] = Field(default_factory=list)
    reason: str | None = None


class AuthorityResolution(BaseModel):
    """approach identification authority competition and selected-governing-document result."""

    model_config = ConfigDict(extra="allow")

    candidate_governing_documents: list[str] = Field(default_factory=list)
    selected_primary_document: str | None = None
    selection_reason: str | None = None
    discarded_due_to_overlap: list[str] = Field(default_factory=list)
    residual_uncertainty: str | None = None


class AuthorityClassification(BaseModel):
    """approach identification classification of retrieved documents by authority role."""

    model_config = ConfigDict(extra="allow")

    primary_authority: list[AuthorityReference] = Field(default_factory=list)
    supporting_authority: list[AuthorityReference] = Field(default_factory=list)
    peripheral_authority: list[AuthorityReference] = Field(default_factory=list)


class TreatmentAuthorityBasis(BaseModel):
    """Authority basis for a approach identification treatment family."""

    model_config = ConfigDict(extra="allow")

    document: str
    references: list[str] = Field(default_factory=list)


class TreatmentFamily(BaseModel):
    """Intermediate approach identification treatment family."""

    model_config = ConfigDict(extra="allow")

    family: str
    authority_basis: list[TreatmentAuthorityBasis] = Field(default_factory=list)
    mapped_approaches: list[str] = Field(default_factory=list)


class IdentifiedApproach(BaseModel):
    """Final peer top-level accounting approach identified by approach identification."""

    model_config = ConfigDict(extra="allow")

    id: str
    label: str
    normalized_label: str
    rationale_for_inclusion: str | None = None


class PromptAClarificationOutput(BaseModel):
    """approach identification output when retrieved context is insufficient."""

    model_config = ConfigDict(extra="allow")

    status: Literal["needs_clarification"]
    questions: list[str]


class PromptAPassOutput(BaseModel):
    """approach identification output when authority and peer approaches are identified."""

    model_config = ConfigDict(extra="allow")

    status: Literal["pass"]
    primary_accounting_issue: str
    authority_resolution: AuthorityResolution
    authority_classification: AuthorityClassification
    treatment_families: list[TreatmentFamily] = Field(default_factory=list)
    approaches: list[IdentifiedApproach]


PromptAOutput = PromptAPassOutput | PromptAClarificationOutput


class Recommendation(BaseModel):
    """applicability analysis final recommendation."""

    model_config = ConfigDict(extra="allow")

    answer: Literal["oui", "non", "oui_sous_conditions"]
    justification: str


class ApplicabilityReference(BaseModel):
    """One citation in applicability analysis output."""

    model_config = ConfigDict(extra="allow")

    document: str
    section: str
    excerpt: str


class ApproachApplicability(BaseModel):
    """applicability analysis applicability finding for one identified approach."""

    model_config = ConfigDict(extra="allow")

    id: str
    normalized_label: str
    label_fr: str
    applicability: Literal["oui", "non", "oui_sous_conditions"]
    reasoning_fr: str
    conditions_fr: list[str] = Field(default_factory=list)
    practical_implication_fr: str
    references: list[ApplicabilityReference] = Field(default_factory=list)


class PromptBClarificationOutput(BaseModel):
    """applicability analysis output when approach identification requires clarification."""

    model_config = ConfigDict(extra="allow")

    status: Literal["needs_clarification"]
    questions_fr: list[str]


class PromptBPassOutput(BaseModel):
    """applicability analysis output when applicability can be assessed."""

    model_config = ConfigDict(extra="allow")

    assumptions_fr: list[str] = Field(default_factory=list)
    recommendation: Recommendation
    approaches: list[ApproachApplicability]


PromptBOutput = PromptBPassOutput | PromptBClarificationOutput


class AuthorityClassificationResult(BaseModel):
    """Typed approach identification result after Pydantic output contract validation."""

    raw_response: str
    output: PromptAOutput
    payload: dict[str, object]


class ApplicabilityAnalysisResult(BaseModel):
    """Typed applicability analysis result after Pydantic output contract validation."""

    raw_response: str
    output: PromptBOutput
    payload: dict[str, object]


class AuthoritySufficiencyResult(BaseModel):
    """Decision from the authority sufficiency gate after approach identification."""

    status: str
    should_continue: bool
    reason: str | None = None
    details: dict[str, object] | None = None


class CitationVerificationResult(BaseModel):
    """Deterministic citation verification result for the final analysis."""

    status: Literal["pass", "warn", "fail"]
    checked_reference_count: int
    missing_references: list[str]
    unsupported_references: list[str]


class CaseEvidenceAgentInput(BaseModel):
    """Input state for bounded case-evidence gathering."""

    case_id: str
    issue_type: str
    known_facts: list[str]
    required_criteria: list[str]


class ToolCallRecord(BaseModel):
    """Audit record for one bounded-agent tool call."""

    tool_name: str
    arguments: dict[str, object]
    output: dict[str, object] | None = None
    error: str | None = None


class CaseEvidenceAgentResult(BaseModel):
    """Output from the bounded case-evidence gathering agent."""

    status: Literal["disabled", "complete"]
    tool_calls: list[ToolCallRecord]


StageOutcome = ValidatedQuestion | RetrievedSourcePackage | AuthorityClassificationResult | ApplicabilityAnalysisResult | ValidationFailure
RouteDecision = Literal["continue", "fail"]

ApproachIdentificationReference = AuthorityReference
ApproachIdentificationResolution = AuthorityResolution
ApproachIdentificationClassification = AuthorityClassification
ApproachIdentificationTreatmentBasis = TreatmentAuthorityBasis
ApproachIdentificationTreatmentFamily = TreatmentFamily
ApproachIdentification = IdentifiedApproach
ApproachIdentificationClarificationOutput = PromptAClarificationOutput
ApproachIdentificationPassOutput = PromptAPassOutput
ApproachIdentificationOutput = PromptAOutput
ApplicabilityAnalysisReference = ApplicabilityReference
ApplicabilityAnalysisFinding = ApproachApplicability
ApplicabilityAnalysisClarificationOutput = PromptBClarificationOutput
ApplicabilityAnalysisPassOutput = PromptBPassOutput
ApplicabilityAnalysisOutput = PromptBOutput
ApproachIdentificationResult = AuthorityClassificationResult
ApplicabilityAnalysisResultAlias = ApplicabilityAnalysisResult
ApproachSufficiencyResult = AuthoritySufficiencyResult
CitationValidationResult = CitationVerificationResult
