"""Streamlit app for IFRS Expert."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, cast

import streamlit as st
from dotenv import load_dotenv

from src.logging_config import setup_logging
from src.ui.chat_service import ChatService, create_chat_service
from src.ui.chat_state import (
    FIRST_TURN_RESULT_KEY,
    LAST_ERROR_KEY,
    SessionStateProtocol,
    append_follow_up_turn,
    append_message,
    clear_pending_prompt,
    clear_session_state,
    get_first_turn_result,
    get_follow_up_turns,
    get_messages,
    get_pending_prompt,
    initialize_session_state,
    set_pending_prompt,
)

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)


@st.cache_resource
def get_chat_service() -> ChatService:
    """Create the cached chat service."""
    logger.info("Streamlit UI: creating cached chat service")
    return create_chat_service()


def main() -> None:
    """Render the Streamlit chat app."""
    load_dotenv()
    setup_logging()
    st.set_page_config(page_title="IFRS Expert")

    session_state = cast("SessionStateProtocol", st.session_state)
    initialize_session_state(session_state)
    service = get_chat_service()

    messages = get_messages(session_state)
    first_turn_result = get_first_turn_result(session_state)
    follow_up_turns = get_follow_up_turns(session_state)
    has_grounded_result = first_turn_result is not None
    logger.info(f"Streamlit UI: rerun start messages={len(messages)} has_grounded_result={has_grounded_result} follow_up_turns={len(follow_up_turns)}")

    if messages and st.button("Clear chat"):
        logger.info(f"Streamlit UI: clear chat requested messages_before={len(messages)} follow_up_turns_before={len(follow_up_turns)}")
        clear_session_state(session_state)
        logger.info("Streamlit UI: chat cleared, rerunning app")
        st.rerun()

    logger.info(f"Streamlit UI: rendering transcript messages={len(messages)}")
    for message in messages:
        with st.chat_message(message.role):
            if message.format_type == "markdown":
                st.markdown(message.content)
            else:
                st.write(message.content)

    prompt = st.chat_input("Ask a question")
    if prompt:
        logger.info(f"Streamlit UI: prompt received chars={len(prompt)} question='{prompt[:80]}' has_grounded_result={has_grounded_result}")
        append_message(session_state, role="user", content=prompt, format_type="text")
        set_pending_prompt(session_state, prompt)
        logger.info(f"Streamlit UI: user message appended and pending prompt stored transcript_messages={len(get_messages(session_state))}")
        st.rerun()

    pending_prompt = get_pending_prompt(session_state)
    if pending_prompt is None:
        logger.info("Streamlit UI: no pending prompt to process on this rerun")
        return

    logger.info(f"Streamlit UI: processing pending prompt chars={len(pending_prompt)} question='{pending_prompt[:80]}'")
    clear_pending_prompt(session_state)

    with st.chat_message("assistant"), st.spinner("Thinking..."):
        first_turn_result = get_first_turn_result(session_state)
        if first_turn_result is None:
            logger.info("Streamlit UI: routing pending prompt through grounded first-turn flow")
            _handle_first_turn(service, session_state, pending_prompt)
        else:
            logger.info("Streamlit UI: routing pending prompt through follow-up flow")
            _handle_follow_up_turn(service, session_state, first_turn_result, pending_prompt)


def _handle_first_turn(service: ChatService, session_state: SessionStateProtocol, prompt: str) -> None:
    """Handle the first grounded turn."""
    logger.info(f"Streamlit UI: first turn start question='{prompt[:80]}'")
    result = service.answer_first_turn(prompt)

    if result.error:
        logger.error(f"Streamlit UI: first turn failed error={result.error}")
        session_state[LAST_ERROR_KEY] = result.error
        st.write(result.error)
        append_message(session_state, role="assistant", content=result.error, format_type="text")
        logger.info("Streamlit UI: first-turn error rendered to transcript")
        return

    assistant_content = _get_assistant_display_text(result)
    assistant_format = "markdown" if result.prompt_b_markdown else "text"
    prompt_a_chars = len(result.prompt_a_text) if result.prompt_a_text else 0
    prompt_b_chars = len(result.prompt_b_text) if result.prompt_b_text else 0
    assistant_chars = len(assistant_content)
    logger.info(f"Streamlit UI: first turn succeeded docs={len(result.retrieved_doc_uids)} prompt_a_chars={prompt_a_chars} prompt_b_chars={prompt_b_chars} assistant_chars={assistant_chars} format={assistant_format}")

    session_state[FIRST_TURN_RESULT_KEY] = result
    session_state[LAST_ERROR_KEY] = None
    logger.info("Streamlit UI: stored grounded first-turn result in session state")

    if assistant_format == "markdown":
        st.markdown(assistant_content)
    else:
        st.write(assistant_content)

    append_message(session_state, role="assistant", content=assistant_content, format_type=assistant_format)
    logger.info(f"Streamlit UI: grounded assistant message appended transcript_messages={len(get_messages(session_state))}")


def _handle_follow_up_turn(
    service: ChatService,
    session_state: SessionStateProtocol,
    first_turn_result: AnswerCommandResult,
    prompt: str,
) -> None:
    """Handle a later conversational follow-up turn."""
    follow_up_turns = get_follow_up_turns(session_state)
    logger.info(f"Streamlit UI: follow-up start prior_turns={len(follow_up_turns)} question='{prompt[:80]}'")

    try:
        assistant_answer = service.answer_follow_up(first_turn_result, follow_up_turns, prompt)
    except RuntimeError as e:
        error_message = f"Error: LLM call failed: {e}"
        logger.exception(f"Streamlit UI: follow-up failed error={error_message}")
        session_state[LAST_ERROR_KEY] = error_message
        st.write(error_message)
        append_message(session_state, role="assistant", content=error_message, format_type="text")
        logger.info("Streamlit UI: follow-up error rendered to transcript")
        return

    session_state[LAST_ERROR_KEY] = None
    st.markdown(assistant_answer)
    append_follow_up_turn(session_state, user_question=prompt, assistant_answer=assistant_answer)
    append_message(session_state, role="assistant", content=assistant_answer, format_type="markdown")
    logger.info(f"Streamlit UI: follow-up succeeded answer_chars={len(assistant_answer)} prior_turns_after={len(get_follow_up_turns(session_state))} transcript_messages={len(get_messages(session_state))}")


def _get_assistant_display_text(result: AnswerCommandResult) -> str:
    """Return the text displayed for the grounded first-turn answer."""
    if result.prompt_b_markdown:
        logger.info("Streamlit UI: displaying grounded markdown answer")
        return result.prompt_b_markdown
    if result.prompt_b_raw_response:
        logger.info("Streamlit UI: displaying grounded raw response")
        return result.prompt_b_raw_response
    logger.warning("Streamlit UI: grounded result had no displayable answer content")
    return "No answer returned."
