"""Answer command result models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeAlias

JSONScalar: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONScalar | list["JSONValue"] | dict[str, "JSONValue"]


@dataclass
class AnswerCommandResult:
    """Artifacts produced by one AnswerCommand execution."""

    query: str
    success: bool = False
    retrieved_doc_uids: list[str] = field(default_factory=list)
    prompt_a_text: str | None = None
    prompt_a_raw_response: str | None = None
    prompt_a_json: JSONValue | None = None
    prompt_b_text: str | None = None
    prompt_b_raw_response: str | None = None
    prompt_b_json: JSONValue | None = None
    prompt_b_memo_markdown: str | None = None
    prompt_b_faq_markdown: str | None = None
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
