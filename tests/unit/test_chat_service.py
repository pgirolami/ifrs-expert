"""Tests for the Streamlit chat service."""

from __future__ import annotations

from src.models.answer_command_result import AnswerCommandResult
from src.ui.chat_service import ChatService
from src.ui.chat_state import FollowUpTurn


def test_answer_first_turn_uses_answer_command_result() -> None:
    """First turn should delegate to the grounded answer runner."""
    calls: list[str] = []

    def run_first_turn(question: str) -> AnswerCommandResult:
        calls.append(question)
        return AnswerCommandResult(query=question, success=True, prompt_b_markdown="# Grounded answer")

    service = ChatService(run_first_turn_fn=run_first_turn, generate_follow_up_fn=lambda prompt: "unused")

    result = service.answer_first_turn("What is IFRS 9?")

    assert calls == ["What is IFRS 9?"]
    assert result.prompt_b_markdown == "# Grounded answer"


def test_answer_follow_up_uses_grounded_context_and_transcript() -> None:
    """Follow-up turns should use the first grounded result plus transcript context."""
    prompts: list[str] = []

    def generate_follow_up(prompt: str) -> str:
        prompts.append(prompt)
        return "## Follow-up answer"

    service = ChatService(
        run_first_turn_fn=lambda question: AnswerCommandResult(query=question, success=True),
        generate_follow_up_fn=generate_follow_up,
    )
    first_turn_result = AnswerCommandResult(
        query="Can we apply hedge accounting?",
        success=True,
        prompt_b_markdown="# Grounded first answer",
    )
    follow_up_turns = [FollowUpTurn(user_question="Under which conditions?", assistant_answer="Conditions answer")]

    answer = service.answer_follow_up(first_turn_result, follow_up_turns, "What about consolidation?")

    assert answer == "## Follow-up answer"
    assert prompts
    assert "# Grounded first answer" in prompts[0]
    assert "Under which conditions?" in prompts[0]
    assert "Conditions answer" in prompts[0]
    assert "What about consolidation?" in prompts[0]
