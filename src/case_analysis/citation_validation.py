"""Citation validation helpers for answer generation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.case_analysis.stages import VerifyCitationsStage

if TYPE_CHECKING:
    from src.case_analysis.models import ApplicabilityAnalysisOutput, CitationVerificationResult


@dataclass(frozen=True)
class CitationValidationService:
    """Validate applicability-analysis citations against filtered context."""

    def validate_applicability_analysis(
        self,
        analysis: ApplicabilityAnalysisOutput,
        applicability_analysis_context: str,
    ) -> CitationVerificationResult:
        """Validate the final analysis output against the allowed chunk text."""
        chunk_data = self.build_chunk_data_for_markdown(applicability_analysis_context)
        return VerifyCitationsStage().execute(analysis, chunk_data)

    def build_chunk_data_for_markdown(self, context: str) -> dict[str, str]:
        """Index chunk text by document UID and chunk number for citation checks."""
        chunk_data: dict[str, str] = {}
        chunk_pattern = re.compile(
            r'<chunk id="\d+" doc_uid="([^"]*)" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
            re.DOTALL,
        )
        for match in chunk_pattern.finditer(context):
            key = f"{match.group(1)}/{match.group(2)}"
            chunk_data[key] = match.group(3)
        return chunk_data


__all__ = ["CitationValidationService"]
