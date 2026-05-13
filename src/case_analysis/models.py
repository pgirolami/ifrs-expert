"""Typed models shared by case-analysis workflow stages."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, cast

from pydantic import BaseModel

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


class AuthorityClassificationResult(BaseModel):
    """Typed Prompt A result after JSON/object contract validation."""

    raw_response: str
    payload: dict[str, object]


class ApplicabilityAnalysisResult(BaseModel):
    """Typed Prompt B result after JSON/object contract validation."""

    raw_response: str
    payload: dict[str, object]


class AuthoritySufficiencyResult(BaseModel):
    """Decision from the authority sufficiency gate after Prompt A."""

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


StageOutcome = ValidatedQuestion | RetrievedSourcePackage | AuthorityClassificationResult | ApplicabilityAnalysisResult | ValidationFailure
RouteDecision = Literal["continue", "fail"]
