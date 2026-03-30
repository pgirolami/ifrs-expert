"""Tests for Streamlit chat state helpers."""

from __future__ import annotations

from typing import cast

from src.models.answer_command_result import AnswerCommandResult
from src.ui.chat_state import (
    FIRST_TURN_RESULT_KEY,
    FOLLOW_UP_TURNS_KEY,
    LAST_ERROR_KEY,
    MESSAGES_KEY,
    PENDING_PROMPT_KEY,
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


def test_initialize_session_state_sets_expected_defaults() -> None:
    """State initialization should seed the expected keys."""
    session_state = cast(SessionStateProtocol, {})

    initialize_session_state(session_state)

    assert session_state[MESSAGES_KEY] == []
    assert session_state[FIRST_TURN_RESULT_KEY] is None
    assert session_state[FOLLOW_UP_TURNS_KEY] == []
    assert session_state[LAST_ERROR_KEY] is None
    assert session_state[PENDING_PROMPT_KEY] is None


def test_append_helpers_store_messages_and_follow_up_turns() -> None:
    """Append helpers should update transcript and follow-up state."""
    session_state = cast(SessionStateProtocol, {})
    initialize_session_state(session_state)

    append_message(session_state, role="user", content="Hello", format_type="text")
    append_message(session_state, role="assistant", content="# Hi", format_type="markdown")
    append_follow_up_turn(session_state, user_question="Q2", assistant_answer="A2")

    messages = get_messages(session_state)
    follow_up_turns = get_follow_up_turns(session_state)

    assert len(messages) == 2
    assert messages[0].content == "Hello"
    assert messages[1].format_type == "markdown"
    assert len(follow_up_turns) == 1
    assert follow_up_turns[0].assistant_answer == "A2"


def test_pending_prompt_helpers_round_trip() -> None:
    """Pending prompt helpers should store and clear the next prompt to process."""
    session_state = cast(SessionStateProtocol, {})
    initialize_session_state(session_state)

    assert get_pending_prompt(session_state) is None

    set_pending_prompt(session_state, "What about disclosure?")

    assert get_pending_prompt(session_state) == "What about disclosure?"

    clear_pending_prompt(session_state)

    assert get_pending_prompt(session_state) is None


def test_clear_session_state_resets_values() -> None:
    """Clear helper should reset all chat state."""
    session_state = cast(SessionStateProtocol, {})
    initialize_session_state(session_state)
    session_state[FIRST_TURN_RESULT_KEY] = AnswerCommandResult(query="Q1", success=True)
    session_state[LAST_ERROR_KEY] = "boom"
    set_pending_prompt(session_state, "Pending question")
    append_message(session_state, role="user", content="Hello", format_type="text")
    append_follow_up_turn(session_state, user_question="Q2", assistant_answer="A2")

    clear_session_state(session_state)

    assert get_messages(session_state) == []
    assert get_first_turn_result(session_state) is None
    assert get_follow_up_turns(session_state) == []
    assert session_state[LAST_ERROR_KEY] is None
    assert session_state[PENDING_PROMPT_KEY] is None
