"""Rendering helpers for answer artifacts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.applicability_markdown_utils import MarkdownOptions, convert_json_to_faq_markdown, convert_json_to_markdown_full

if TYPE_CHECKING:
    from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput


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
        approach_identification: ApproachIdentificationOutput,
        applicability_analysis: ApplicabilityAnalysisOutput,
        applicability_analysis_context: str,
    ) -> RenderedAnswerArtifacts:
        """Render the final answer memo and FAQ markdown."""
        applicability_analysis_payload = applicability_analysis.model_dump(mode="json")
        chunk_data = self._build_chunk_data_for_markdown(applicability_analysis_context)
        applicability_analysis_doc_uids = self._extract_doc_uids_from_context(applicability_analysis_context)
        primary_accounting_issue = self._extract_primary_accounting_issue(approach_identification)
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

    def _extract_primary_accounting_issue(self, approach_identification: ApproachIdentificationOutput) -> str | None:
        """Return the primary accounting issue when the structured output includes one."""
        if approach_identification.status != "pass":
            return None
        return approach_identification.primary_accounting_issue

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
