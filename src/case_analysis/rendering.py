"""Rendering helpers for answer artifacts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from pydantic import BaseModel

from src.b_response_utils import MarkdownOptions, convert_json_to_faq_markdown, convert_json_to_markdown_full

if TYPE_CHECKING:
    from src.models.answer_command_result import JSONValue


@dataclass(frozen=True)
class RenderedAnswerArtifacts:
    """Markdown artifacts produced from the final applicability analysis output."""

    memo_markdown: str
    faq_markdown: str


@dataclass(frozen=True)
class AnswerRenderingAdapter:
    """Convert typed answer outputs into the historical markdown artifacts."""

    def render_applicability_analysis(
        self,
        *,
        query: str,
        retrieved_doc_uids: list[str],
        approach_identification_json: JSONValue | BaseModel,
        applicability_analysis_json: JSONValue | BaseModel,
        applicability_analysis_context: str,
    ) -> RenderedAnswerArtifacts:
        """Render the final answer memo and FAQ markdown."""
        applicability_analysis_payload = self._coerce_json_dict(applicability_analysis_json)
        if applicability_analysis_payload is None:
            msg = "Applicability analysis JSON must be a dict"
            raise TypeError(msg)

        chunk_data = self._build_chunk_data_for_markdown(applicability_analysis_context)
        applicability_analysis_doc_uids = self._extract_doc_uids_from_context(applicability_analysis_context)
        primary_accounting_issue = self._extract_primary_accounting_issue(approach_identification_json)
        options = MarkdownOptions(
            question=query,
            doc_uids=retrieved_doc_uids,
            authority_doc_uids=applicability_analysis_doc_uids,
            primary_accounting_issue=primary_accounting_issue,
            chunk_data=chunk_data,
        )
        memo_markdown = convert_json_to_markdown_full(applicability_analysis_payload, options)
        faq_markdown = convert_json_to_faq_markdown(
            applicability_analysis_payload,
            primary_accounting_issue=options.primary_accounting_issue,
        )
        return RenderedAnswerArtifacts(memo_markdown=memo_markdown, faq_markdown=faq_markdown)

    def _extract_primary_accounting_issue(self, approach_identification_json: JSONValue | BaseModel) -> str | None:
        """Return the primary accounting issue when the structured output includes one."""
        approach_identification_payload = self._coerce_json_dict(approach_identification_json)
        if approach_identification_payload is None:
            return None
        primary_accounting_issue = approach_identification_payload.get("primary_accounting_issue")
        return primary_accounting_issue if isinstance(primary_accounting_issue, str) else None

    def _extract_doc_uids_from_context(self, context: str) -> list[str]:
        """Preserve document order from the filtered applicability-analysis context."""
        doc_uids: list[str] = []
        for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
            doc_uid = match.group(1)
            if doc_uid not in doc_uids:
                doc_uids.append(doc_uid)
        return doc_uids

    def _build_chunk_data_for_markdown(self, context: str) -> dict[str, str]:
        """Index chunk text by document UID and chunk number for markdown rendering."""
        chunk_data: dict[str, str] = {}
        chunk_pattern = re.compile(
            r'<chunk id="\d+" doc_uid="([^"]*)" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
            re.DOTALL,
        )
        for match in chunk_pattern.finditer(context):
            key = f"{match.group(1)}/{match.group(2)}"
            chunk_data[key] = match.group(3)
        return chunk_data

    def _coerce_json_dict(self, value: JSONValue | BaseModel) -> dict[str, object] | None:
        """Convert typed output to a JSON-like dict when possible."""
        if isinstance(value, BaseModel):
            dumped = value.model_dump(mode="json")
            if isinstance(dumped, dict):
                return cast("dict[str, object]", dumped)
            return None
        if not isinstance(value, dict):
            return None
        return cast("dict[str, object]", value)
