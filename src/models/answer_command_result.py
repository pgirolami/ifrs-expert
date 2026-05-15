"""Answer command result models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, TypeAlias, TypeVar, cast

if TYPE_CHECKING:
    from src.models.provenance import Provenance

JSONScalar: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONScalar | list["JSONValue"] | dict[str, "JSONValue"]
T = TypeVar("T")


def _prefer(primary: T | None, fallback: T | None) -> T | None:
    """Prefer a primary value when it is not None."""
    return primary if primary is not None else fallback


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


@dataclass(init=False)
class AnswerCommandResult:
    """Artifacts produced by one AnswerCommand execution."""

    query: str
    success: bool
    retrieved_doc_uids: list[str] = field(default_factory=list)
    document_hits: list[RetrievedDocumentHit] = field(default_factory=list)
    chunk_hits: list[RetrievedChunkHit] = field(default_factory=list)
    approach_identification_text: str | None = None
    approach_identification_raw_response: str | None = None
    approach_identification_json: JSONValue | None = None
    authority_sufficiency_json: JSONValue | None = None
    applicability_analysis_text: str | None = None
    applicability_analysis_raw_response: str | None = None
    applicability_analysis_json: JSONValue | None = None
    citation_verification_json: JSONValue | None = None
    applicability_analysis_memo_markdown: str | None = None
    applicability_analysis_faq_markdown: str | None = None
    error: str | None = None
    error_stage: str | None = None

    def __init__(self, query: str, *, success: bool = False, **kwargs: object) -> None:
        """Initialize the result while accepting legacy prompt field names."""
        self.query = query
        self.success = success

        retrieved_doc_uids_value = cast("list[str] | None", kwargs.pop("retrieved_doc_uids", None))
        document_hits_value = cast("list[RetrievedDocumentHit] | None", kwargs.pop("document_hits", None))
        chunk_hits_value = cast("list[RetrievedChunkHit] | None", kwargs.pop("chunk_hits", None))

        prompt_a_text = cast("str | None", kwargs.pop("prompt_a_text", None))
        prompt_a_raw_response = cast("str | None", kwargs.pop("prompt_a_raw_response", None))
        prompt_a_json = cast("JSONValue | None", kwargs.pop("prompt_a_json", None))
        prompt_b_text = cast("str | None", kwargs.pop("prompt_b_text", None))
        prompt_b_raw_response = cast("str | None", kwargs.pop("prompt_b_raw_response", None))
        prompt_b_json = cast("JSONValue | None", kwargs.pop("prompt_b_json", None))
        prompt_b_memo_markdown = cast("str | None", kwargs.pop("prompt_b_memo_markdown", None))
        prompt_b_faq_markdown = cast("str | None", kwargs.pop("prompt_b_faq_markdown", None))

        self.retrieved_doc_uids = retrieved_doc_uids_value or []
        self.document_hits = document_hits_value or []
        self.chunk_hits = chunk_hits_value or []
        self.approach_identification_text = _prefer(
            cast("str | None", kwargs.pop("approach_identification_text", None)),
            prompt_a_text,
        )
        self.approach_identification_raw_response = _prefer(
            cast("str | None", kwargs.pop("approach_identification_raw_response", None)),
            prompt_a_raw_response,
        )
        self.approach_identification_json = _prefer(
            cast("JSONValue | None", kwargs.pop("approach_identification_json", None)),
            prompt_a_json,
        )
        self.authority_sufficiency_json = cast("JSONValue | None", kwargs.pop("authority_sufficiency_json", None))
        self.applicability_analysis_text = _prefer(
            cast("str | None", kwargs.pop("applicability_analysis_text", None)),
            prompt_b_text,
        )
        self.applicability_analysis_raw_response = _prefer(
            cast("str | None", kwargs.pop("applicability_analysis_raw_response", None)),
            prompt_b_raw_response,
        )
        self.applicability_analysis_json = _prefer(
            cast("JSONValue | None", kwargs.pop("applicability_analysis_json", None)),
            prompt_b_json,
        )
        self.citation_verification_json = cast("JSONValue | None", kwargs.pop("citation_verification_json", None))
        self.applicability_analysis_memo_markdown = _prefer(
            cast("str | None", kwargs.pop("applicability_analysis_memo_markdown", None)),
            prompt_b_memo_markdown,
        )
        self.applicability_analysis_faq_markdown = _prefer(
            cast("str | None", kwargs.pop("applicability_analysis_faq_markdown", None)),
            prompt_b_faq_markdown,
        )
        self.error = cast("str | None", kwargs.pop("error", None))
        self.error_stage = cast("str | None", kwargs.pop("error_stage", None))

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

    @property
    def prompt_a_text(self) -> str | None:
        """Legacy alias for approach_identification_text."""
        return self.approach_identification_text

    @prompt_a_text.setter
    def prompt_a_text(self, value: str | None) -> None:
        """Legacy alias for approach_identification_text."""
        self.approach_identification_text = value

    @property
    def prompt_a_raw_response(self) -> str | None:
        """Legacy alias for approach_identification_raw_response."""
        return self.approach_identification_raw_response

    @prompt_a_raw_response.setter
    def prompt_a_raw_response(self, value: str | None) -> None:
        """Legacy alias for approach_identification_raw_response."""
        self.approach_identification_raw_response = value

    @property
    def prompt_a_json(self) -> JSONValue | None:
        """Legacy alias for approach_identification_json."""
        return self.approach_identification_json

    @prompt_a_json.setter
    def prompt_a_json(self, value: JSONValue | None) -> None:
        """Legacy alias for approach_identification_json."""
        self.approach_identification_json = value

    @property
    def prompt_b_text(self) -> str | None:
        """Legacy alias for applicability_analysis_text."""
        return self.applicability_analysis_text

    @prompt_b_text.setter
    def prompt_b_text(self, value: str | None) -> None:
        """Legacy alias for applicability_analysis_text."""
        self.applicability_analysis_text = value

    @property
    def prompt_b_raw_response(self) -> str | None:
        """Legacy alias for applicability_analysis_raw_response."""
        return self.applicability_analysis_raw_response

    @prompt_b_raw_response.setter
    def prompt_b_raw_response(self, value: str | None) -> None:
        """Legacy alias for applicability_analysis_raw_response."""
        self.applicability_analysis_raw_response = value

    @property
    def prompt_b_json(self) -> JSONValue | None:
        """Legacy alias for applicability_analysis_json."""
        return self.applicability_analysis_json

    @prompt_b_json.setter
    def prompt_b_json(self, value: JSONValue | None) -> None:
        """Legacy alias for applicability_analysis_json."""
        self.applicability_analysis_json = value

    @property
    def prompt_b_memo_markdown(self) -> str | None:
        """Legacy alias for applicability_analysis_memo_markdown."""
        return self.applicability_analysis_memo_markdown

    @prompt_b_memo_markdown.setter
    def prompt_b_memo_markdown(self, value: str | None) -> None:
        """Legacy alias for applicability_analysis_memo_markdown."""
        self.applicability_analysis_memo_markdown = value

    @property
    def prompt_b_faq_markdown(self) -> str | None:
        """Legacy alias for applicability_analysis_faq_markdown."""
        return self.applicability_analysis_faq_markdown

    @prompt_b_faq_markdown.setter
    def prompt_b_faq_markdown(self, value: str | None) -> None:
        """Legacy alias for applicability_analysis_faq_markdown."""
        self.applicability_analysis_faq_markdown = value
