"""Context-building helpers for answer generation."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.answer_command_result import JSONValue

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ContextBuilder:
    """Build filtered prompt context from typed Prompt A output."""

    def build_applicability_analysis_context(
        self,
        formatted_chunks: list[str],
        approach_identification_json: JSONValue,
    ) -> str:
        """Prune chunks to the authority references selected during approach identification."""
        authority_refs = self.extract_authority_references(approach_identification_json)
        if authority_refs is None:
            return "\n\n".join(formatted_chunks)
        return self.filter_chunks_by_authority(formatted_chunks, authority_refs)

    def extract_authority_references(self, approach_identification_json: JSONValue) -> set[tuple[str, str]] | None:
        """Return the document/reference pairs that applicability analysis may use."""
        if not isinstance(approach_identification_json, dict):
            logger.error("approach identification JSON is not a dict; using all chunks for applicability analysis (authority filtering skipped)")
            return None

        authority_classification = approach_identification_json.get("authority_classification")
        if not isinstance(authority_classification, dict):
            logger.error("No authority_classification in approach identification response; using all chunks for applicability analysis (authority filtering skipped)")
            return None

        primary_authority = authority_classification.get("primary_authority", [])
        supporting_authority = authority_classification.get("supporting_authority", [])
        if not primary_authority and not supporting_authority:
            logger.warning("No primary or supporting authority identified; using all chunks for applicability analysis (authority filtering skipped)")
            return None

        allowed_chunks: set[tuple[str, str]] = set()
        for authority_item in (*primary_authority, *supporting_authority):
            if not isinstance(authority_item, dict):
                continue
            document = authority_item.get("document")
            references = authority_item.get("references", [])
            if not isinstance(document, str) or not isinstance(references, list):
                continue
            for ref in references:
                if isinstance(ref, str):
                    allowed_chunks.add((document, ref))

        if not allowed_chunks:
            logger.error("Could not extract authority references; using all chunks for applicability analysis (authority filtering skipped)")
            return None

        logger.info(f"Filtering applicability analysis context to {len(allowed_chunks)} authority references")
        return allowed_chunks

    def filter_chunks_by_authority(self, formatted_chunks: list[str], authority_refs: set[tuple[str, str]]) -> str:
        """Keep only chunks matching the allowed authority references."""
        chunk_pattern = re.compile(
            r'<chunk id="(\d+)" doc_uid="[^"]*" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
            re.DOTALL,
        )

        filtered_documents: list[str] = []
        for doc_xml in formatted_chunks:
            doc_match = re.search(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', doc_xml)
            if not doc_match:
                continue
            doc_uid = doc_match.group(1)
            document_type_match = re.search(r'document_type="([^"]*)"', doc_xml)
            document_kind_match = re.search(r'document_kind="([^"]*)"', doc_xml)
            document_type = document_type_match.group(1) if document_type_match else ""
            document_kind = document_kind_match.group(1) if document_kind_match else ""
            filtered_chunk_xmls = [match.group(0) for match in chunk_pattern.finditer(doc_xml) if (doc_uid, match.group(2)) in authority_refs]
            if filtered_chunk_xmls:
                joined_chunks = "\n\n".join(filtered_chunk_xmls)
                document_xml = f'<Document name="{_escape_xml(doc_uid)}" document_type="{_escape_xml(document_type)}" document_kind="{_escape_xml(document_kind)}">\n{joined_chunks}\n</Document>'
                filtered_documents.append(document_xml)

        if not filtered_documents:
            logger.error("No chunks matched authority references; falling back to all chunks (authority filtering failed)")
            return "\n\n".join(formatted_chunks)
        return "\n\n".join(filtered_documents)


def _escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")
