"""Prompt assembly helpers for grounded follow-up chat."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult, JSONValue
    from src.ui.chat_state import FollowUpTurn

logger = logging.getLogger(__name__)

FOLLOW_UP_PROMPT_HEADER = (
    "You are continuing an IFRS accounting discussion. Use the grounded first answer as the base context. If the follow-up goes beyond that context, answer cautiously and state the limitation explicitly. Format the answer in Markdown."
)


@dataclass(frozen=True)
class GroundedFollowUpPromptContext:
    """Typed context used to assemble a grounded follow-up prompt."""

    grounded_context: str
    grounded_context_source: str
    transcript_text: str
    current_question: str
    first_question: str
    prior_turn_count: int
    prior_user_chars: int
    prior_assistant_chars: int


@dataclass(frozen=True)
class GroundedFollowUpPromptBuilder:
    """Build grounded follow-up prompts from typed first-turn artifacts."""

    def build(self, result: AnswerCommandResult, follow_up_turns: list[FollowUpTurn], current_question: str) -> tuple[GroundedFollowUpPromptContext, str]:
        """Build the prompt context and final prompt text for a follow-up turn."""
        grounded_context, grounded_context_source = self.build_grounded_context(result)
        transcript_lines: list[str] = []
        prior_user_chars = 0
        prior_assistant_chars = 0
        for turn in follow_up_turns:
            transcript_lines.append(f"User: {turn.user_question}")
            transcript_lines.append(f"Assistant: {turn.assistant_answer}")
            prior_user_chars += len(turn.user_question)
            prior_assistant_chars += len(turn.assistant_answer)

        transcript_text = "\n".join(transcript_lines) if transcript_lines else "(none)"
        context = GroundedFollowUpPromptContext(
            grounded_context=grounded_context,
            grounded_context_source=grounded_context_source,
            transcript_text=transcript_text,
            current_question=current_question,
            first_question=result.query,
            prior_turn_count=len(follow_up_turns),
            prior_user_chars=prior_user_chars,
            prior_assistant_chars=prior_assistant_chars,
        )
        prompt = self._build_prompt(context)
        return context, prompt

    def build_grounded_context(self, result: AnswerCommandResult) -> tuple[str, str]:
        """Pick the richest first-turn artifact available for grounding."""
        if result.applicability_analysis_memo_markdown:
            logger.info("ChatService: using grounded markdown context for follow-up prompt")
            return result.applicability_analysis_memo_markdown, "markdown"
        if result.applicability_analysis_json is not None:
            logger.info("ChatService: using grounded JSON context for follow-up prompt")
            return _serialize_json_value(result.applicability_analysis_json), "json"
        if result.applicability_analysis_raw_response:
            logger.info("ChatService: using grounded raw response context for follow-up prompt")
            return result.applicability_analysis_raw_response, "raw_response"
        logger.warning("ChatService: grounded context missing, using fallback placeholder")
        return "No grounded answer is available.", "fallback"

    def _build_prompt(self, context: GroundedFollowUpPromptContext) -> str:
        """Render the grounded follow-up prompt text."""
        return (
            f"{FOLLOW_UP_PROMPT_HEADER}\n\n"
            f"Original grounded question:\n{context.first_question}\n\n"
            f"Grounded first-turn answer:\n{context.grounded_context}\n\n"
            f"Conversation so far:\n{context.transcript_text}\n\n"
            f"Current question:\n{context.current_question}"
        )


def _serialize_json_value(value: JSONValue) -> str:
    """Serialize a JSON value for prompt use."""
    return json.dumps(value, indent=2, ensure_ascii=False)


__all__ = ["FOLLOW_UP_PROMPT_HEADER", "GroundedFollowUpPromptBuilder", "GroundedFollowUpPromptContext"]
