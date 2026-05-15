"""Prompt template assembly helpers for answer generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.case_analysis.models import ApproachIdentificationOutput


@dataclass(frozen=True)
class PromptBuilder:
    """Assemble Approach identification and Applicability analysis text from templates and context."""

    def build_approach_identification(self, template: str, question: str, chunks: list[str], chunk_summary: str) -> str:
        """Build the Approach identification text with the retrieved chunk summary prepended."""
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", question)
        return f"{chunk_summary}\n\n{prompt}"

    def build_applicability_analysis(self, template: str, question: str, context: str, approach_identification: ApproachIdentificationOutput) -> str:
        """Build the Applicability analysis text with the filtered applicability context."""
        approaches_json = approach_identification.model_dump_json(indent=2)
        return template.replace("{{CHUNKS}}", context).replace("{{QUERY}}", question).replace("{{APPROACHES_JSON}}", approaches_json)
