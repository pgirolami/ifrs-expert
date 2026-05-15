"""Services for the Streamlit chat interface."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from src.ai.pydantic_client import create_default_text_generator
from src.commands.answer import AnswerOptions, create_answer_command
from src.policy import load_policy_catalog, resolve_retrieval_policy
from src.ui.follow_up_prompt_builder import GroundedFollowUpPromptBuilder

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.models.answer_command_result import AnswerCommandResult
    from src.ui.chat_state import FollowUpTurn

logger = logging.getLogger(__name__)

CHAT_RETRIEVAL_POLICY = "standards_only_through_chunks__enriched"


@dataclass
class ChatService:
    """Orchestrates first-turn and follow-up chat flows."""

    run_first_turn_fn: Callable[[str], AnswerCommandResult]
    generate_follow_up_fn: Callable[[str], str]
    follow_up_prompt_builder: GroundedFollowUpPromptBuilder = field(default_factory=GroundedFollowUpPromptBuilder)

    def answer_first_turn(self, question: str) -> AnswerCommandResult:
        """Answer the first grounded question."""
        logger.info(f"ChatService: running grounded first turn for question='{question[:80]}'")
        result = self.run_first_turn_fn(question)
        error_text = result.error or "none"
        logger.info(f"ChatService: first turn completed success={result.success} docs={len(result.retrieved_doc_uids)} error={error_text}")
        return result

    def build_follow_up_prompt(
        self,
        first_turn_result: AnswerCommandResult,
        follow_up_turns: list[FollowUpTurn],
        current_question: str,
    ) -> str:
        """Build the prompt for a later conversational turn."""
        context, prompt = self.follow_up_prompt_builder.build(first_turn_result, follow_up_turns, current_question)
        logger.info(
            f"ChatService: follow-up context includes sources="
            f"original_first_question,grounded_{context.grounded_context_source},prior_follow_up_pairs,current_question "
            f"prior_pairs={context.prior_turn_count} prior_user_chars={context.prior_user_chars} "
            f"prior_assistant_chars={context.prior_assistant_chars} grounded_context_chars={len(context.grounded_context)} "
            f"transcript_chars={len(context.transcript_text)} current_question_chars={len(context.current_question)}"
        )
        return prompt

    def answer_follow_up(
        self,
        first_turn_result: AnswerCommandResult,
        follow_up_turns: list[FollowUpTurn],
        current_question: str,
    ) -> str:
        """Answer a follow-up question directly through the LLM."""
        logger.info(f"ChatService: running follow-up turn prior_turns={len(follow_up_turns)} question='{current_question[:80]}'")
        prompt = self.build_follow_up_prompt(first_turn_result, follow_up_turns, current_question)
        logger.info(f"ChatService: follow-up prompt built chars={len(prompt)}")
        answer = self.generate_follow_up_fn(prompt)
        logger.info(f"ChatService: follow-up answer received chars={len(answer)}")
        return answer


def create_chat_service(answer_options: AnswerOptions | None = None) -> ChatService:
    """Create the real chat service."""
    logger.info("ChatService: creating chat service")

    effective_options = answer_options
    if effective_options is None:
        logger.info("ChatService: no options provided, loading default policy")
        policy_path = Path(__file__).resolve().parents[2] / "config" / "policy.default.yaml"
        policy_catalog = load_policy_catalog(policy_path)
        retrieval_policy = resolve_retrieval_policy(policy_catalog, CHAT_RETRIEVAL_POLICY)
        effective_options = AnswerOptions(policy=retrieval_policy)

    def run_first_turn(question: str) -> AnswerCommandResult:
        logger.info(f"ChatService: creating AnswerCommand for question='{question[:80]}'")
        command = create_answer_command(query=question, options=effective_options)
        return command.execute()

    def generate_follow_up(prompt: str) -> str:
        logger.info(f"ChatService: requesting Pydantic AI follow-up completion chars={len(prompt)}")
        return create_default_text_generator().generate_text(prompt)

    return ChatService(run_first_turn_fn=run_first_turn, generate_follow_up_fn=generate_follow_up)


def _build_grounded_context(result: AnswerCommandResult) -> tuple[str, str]:
    """Build later-turn context from the grounded first answer."""
    builder = GroundedFollowUpPromptBuilder()
    return builder.build_grounded_context(result)


def _serialize_json_value(value: object) -> str:
    """Serialize a JSON-like value for prompt use."""
    return json.dumps(value, indent=2, ensure_ascii=False)
