"""Tests for grounded follow-up generation wiring."""

from __future__ import annotations

from dataclasses import dataclass

from src.ui.follow_up_agent import GroundedFollowUpOutput, GroundedFollowUpTextGenerator


@dataclass(frozen=True)
class _FakeFollowUpGenerator:
    output: GroundedFollowUpOutput

    def generate_follow_up(self, prompt: str) -> GroundedFollowUpOutput:
        del prompt
        return self.output


def test_grounded_follow_up_text_generator_returns_markdown() -> None:
    """Text adapter should expose markdown from structured follow-up output."""
    generator = GroundedFollowUpTextGenerator(
        generator=_FakeFollowUpGenerator(
            output=GroundedFollowUpOutput(markdown="hello", limitations=["limit"], out_of_scope=False),
        ),
    )

    assert generator.generate_text("prompt") == "hello"
