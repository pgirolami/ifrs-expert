"""Tests for the typed grounded follow-up agent."""

from __future__ import annotations

from src.ui.follow_up_agent import GroundedFollowUpOutput, GroundedFollowUpTextGenerator


class _FakeGenerator:
    def generate_follow_up(self, prompt: str) -> GroundedFollowUpOutput:
        return GroundedFollowUpOutput(markdown=f"# {prompt}", limitations=["scope"], out_of_scope=False)


class TestGroundedFollowUpTextGenerator:
    """Behavior tests for the text adapter over structured follow-up output."""

    def test_generate_text_returns_markdown(self) -> None:
        generator = GroundedFollowUpTextGenerator(generator=_FakeGenerator())

        markdown = generator.generate_text("Follow up")

        if markdown != "# Follow up":
            raise AssertionError("Expected markdown returned from structured follow-up output")
