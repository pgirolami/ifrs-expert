"""Tests for prompt template assembly."""

from __future__ import annotations

import pytest

from src.case_analysis.prompt_builder import PromptBuilder


class TestPromptBuilder:
    """Behavior tests for PromptBuilder."""

    def test_build_approach_identification_includes_chunk_summary_query_and_chunks(self) -> None:
        """Approach identification should splice chunks and question into the template."""
        builder = PromptBuilder()
        template = "Header\n{{CHUNKS}}\nQuestion: {{QUERY}}"

        prompt = builder.build_approach_identification(template, "What happened?", ["chunk-one", "chunk-two"], "Summary")

        if "Summary" not in prompt:
            pytest.fail("Expected chunk summary in approach identification prompt")
        if "chunk-one" not in prompt or "chunk-two" not in prompt:
            pytest.fail("Expected chunks in approach identification prompt")
        if "What happened?" not in prompt:
            pytest.fail("Expected query in approach identification prompt")

    def test_build_applicability_analysis_includes_context_query_and_approaches(self) -> None:
        """Applicability analysis should splice filtered context, question, and approaches JSON."""
        builder = PromptBuilder()
        template = "Header\n{{CHUNKS}}\nQuestion: {{QUERY}}\n{{APPROACHES_JSON}}"

        prompt = builder.build_applicability_analysis(template, "Why?", "context text", '{"approaches": []}')

        if "context text" not in prompt:
            pytest.fail("Expected context in applicability analysis prompt")
        if "Why?" not in prompt:
            pytest.fail("Expected query in applicability analysis prompt")
        if '"approaches": []' not in prompt:
            pytest.fail("Expected approaches JSON in applicability analysis prompt")
