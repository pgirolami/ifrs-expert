"""Grounded follow-up answer orchestration for chat."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Protocol

from src.ui.follow_up_prompt_builder import GroundedFollowUpPromptBuilder, GroundedFollowUpPromptContext

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult
    from src.ui.chat_state import FollowUpTurn


class GenerateFollowUpFn(Protocol):
    """Callable contract for grounded follow-up generation."""

    def __call__(self, prompt: str) -> str:
        """Generate a grounded follow-up answer from the prompt."""
        ...


@dataclass(frozen=True)
class GroundedFollowUpService:
    """Build prompts and request grounded follow-up completions."""

    generate_follow_up_fn: GenerateFollowUpFn
    prompt_builder: GroundedFollowUpPromptBuilder = field(default_factory=GroundedFollowUpPromptBuilder)

    def build_prompt(
        self,
        first_turn_result: AnswerCommandResult,
        follow_up_turns: list[FollowUpTurn],
        current_question: str,
    ) -> tuple[GroundedFollowUpPromptContext, str]:
        """Build the context and prompt for one follow-up turn."""
        return self.prompt_builder.build(first_turn_result, follow_up_turns, current_question)

    def answer(
        self,
        first_turn_result: AnswerCommandResult,
        follow_up_turns: list[FollowUpTurn],
        current_question: str,
    ) -> tuple[GroundedFollowUpPromptContext, str, str]:
        """Build the prompt and request a grounded follow-up completion."""
        context, prompt = self.build_prompt(first_turn_result, follow_up_turns, current_question)
        answer = self.generate_follow_up_fn(prompt)
        return context, prompt, answer


__all__ = ["GenerateFollowUpFn", "GroundedFollowUpService"]
