"""Prompt template assembly helpers for answer generation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PromptBuilder:
    """Assemble Prompt A and Prompt B text from templates and context."""

    def build_prompt_a(self, template: str, question: str, chunks: list[str], chunk_summary: str) -> str:
        """Build the Prompt A text with the retrieved chunk summary prepended."""
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", question)
        return f"{chunk_summary}\n\n{prompt}"

    def build_prompt_b(self, template: str, question: str, context: str, approaches_json: str) -> str:
        """Build the Prompt B text with the filtered applicability context."""
        return template.replace("{{CHUNKS}}", context).replace("{{QUERY}}", question).replace("{{APPROACHES_JSON}}", approaches_json)
