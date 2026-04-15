"""Services for the Streamlit chat interface."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.answer import AnswerOptions, create_answer_command
from src.llm import get_client

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.models.answer_command_result import AnswerCommandResult, JSONValue
    from src.ui.chat_state import FollowUpTurn

logger = logging.getLogger(__name__)

FOLLOW_UP_PROMPT_HEADER = (
    "You are continuing an IFRS accounting discussion. Use the grounded first answer as the base context. If the follow-up goes beyond that context, answer cautiously and state the limitation explicitly. Format the answer in Markdown."
)


@dataclass
class ChatService:
    """Orchestrates first-turn and follow-up chat flows."""

    run_first_turn_fn: Callable[[str], AnswerCommandResult]
    generate_follow_up_fn: Callable[[str], str]

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
        grounded_context, grounded_context_source = _build_grounded_context(first_turn_result)
        transcript_lines: list[str] = []
        prior_user_chars = 0
        prior_assistant_chars = 0
        for turn in follow_up_turns:
            transcript_lines.append(f"User: {turn.user_question}")
            transcript_lines.append(f"Assistant: {turn.assistant_answer}")
            prior_user_chars += len(turn.user_question)
            prior_assistant_chars += len(turn.assistant_answer)

        transcript_text = "\n".join(transcript_lines) if transcript_lines else "(none)"
        logger.info(
            f"ChatService: follow-up context includes sources="
            f"original_first_question,grounded_{grounded_context_source},prior_follow_up_pairs,current_question "
            f"prior_pairs={len(follow_up_turns)} prior_user_chars={prior_user_chars} "
            f"prior_assistant_chars={prior_assistant_chars} grounded_context_chars={len(grounded_context)} "
            f"transcript_chars={len(transcript_text)} current_question_chars={len(current_question)}"
        )

        return f"{FOLLOW_UP_PROMPT_HEADER}\n\nOriginal grounded question:\n{first_turn_result.query}\n\nGrounded first-turn answer:\n{grounded_context}\n\nConversation so far:\n{transcript_text}\n\nCurrent question:\n{current_question}"

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
        logger.info("ChatService: no options provided, using base.yaml defaults")
        effective_options = AnswerOptions(
            k=5,
            min_score=0.53,
            d=25,
            doc_min_score=None,
            ifrs_d=4,
            ias_d=4,
            ifric_d=6,
            sic_d=6,
            ps_d=1,
            ifrs_min_score=0.53,
            ias_min_score=0.4,
            ifric_min_score=0.48,
            sic_min_score=0.4,
            ps_min_score=0.4,
            content_min_score=0.53,
            expand_to_section=True,
            expand=0,
            full_doc_threshold=0,
            retrieval_mode="documents",
        )

    def run_first_turn(question: str) -> AnswerCommandResult:
        logger.info(f"ChatService: creating AnswerCommand for question='{question[:80]}'")
        command = create_answer_command(query=question, options=effective_options)
        return command.execute()

    def generate_follow_up(prompt: str) -> str:
        logger.info(f"ChatService: requesting follow-up completion chars={len(prompt)}")
        client = get_client()
        logger.info(f"ChatService: using follow-up provider={type(client).__name__}")
        return client.generate_text(prompt)

    return ChatService(run_first_turn_fn=run_first_turn, generate_follow_up_fn=generate_follow_up)


def _build_grounded_context(result: AnswerCommandResult) -> tuple[str, str]:
    """Build later-turn context from the grounded first answer."""
    if result.prompt_b_memo_markdown:
        logger.info("ChatService: using grounded markdown context for follow-up prompt")
        return result.prompt_b_memo_markdown, "markdown"
    if result.prompt_b_json is not None:
        logger.info("ChatService: using grounded JSON context for follow-up prompt")
        return _serialize_json_value(result.prompt_b_json), "json"
    if result.prompt_b_raw_response:
        logger.info("ChatService: using grounded raw response context for follow-up prompt")
        return result.prompt_b_raw_response, "raw_response"
    logger.warning("ChatService: grounded context missing, using fallback placeholder")
    return "No grounded answer is available.", "fallback"


def _serialize_json_value(value: JSONValue) -> str:
    """Serialize a JSON value for prompt use."""
    return json.dumps(value, indent=2, ensure_ascii=False)
