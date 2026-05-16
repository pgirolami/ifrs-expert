"""Tests for grounded follow-up generation wiring."""

from __future__ import annotations

from src.ai.pydantic_client import GroundedFollowUpOutput, PydanticAIApp


def test_pydantic_ai_app_follow_up_text_returns_markdown(monkeypatch) -> None:
    """The app should expose grounded follow-up markdown directly."""
    monkeypatch.setattr(
        PydanticAIApp,
        "generate_follow_up",
        lambda self, prompt: GroundedFollowUpOutput(markdown=f"reply:{prompt}", limitations=[], out_of_scope=False),
    )

    app = PydanticAIApp(model="openai:gpt-5.2")

    assert app.generate_follow_up_text("prompt") == "reply:prompt"
