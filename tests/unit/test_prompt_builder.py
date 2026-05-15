"""Tests for prompt template assembly."""

from __future__ import annotations

import pytest

from src.case_analysis.prompt_builder import PromptBuilder


class TestPromptBuilder:
    """Behavior tests for PromptBuilder."""

    def test_build_prompt_a_includes_chunk_summary_query_and_chunks(self) -> None:
        """Prompt A should splice chunks and question into the template."""
        builder = PromptBuilder()
        template = "Header\n{{CHUNKS}}\nQuestion: {{QUERY}}"

        prompt = builder.build_prompt_a(template, "What happened?", ["chunk-one", "chunk-two"], "Summary")

        if "Summary" not in prompt:
            pytest.fail("Expected chunk summary in prompt A")
        if "chunk-one" not in prompt or "chunk-two" not in prompt:
            pytest.fail("Expected chunks in prompt A")
        if "What happened?" not in prompt:
            pytest.fail("Expected query in prompt A")

    def test_build_prompt_b_includes_context_query_and_approaches(self) -> None:
        """Prompt B should splice filtered context, question, and approaches JSON."""
        builder = PromptBuilder()
        template = "Header\n{{CHUNKS}}\nQuestion: {{QUERY}}\n{{APPROACHES_JSON}}"

        prompt = builder.build_prompt_b(template, "Why?", "context text", '{"approaches": []}')

        if "context text" not in prompt:
            pytest.fail("Expected context in prompt B")
        if "Why?" not in prompt:
            pytest.fail("Expected query in prompt B")
        if '"approaches": []' not in prompt:
            pytest.fail("Expected approaches JSON in prompt B")
