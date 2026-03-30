"""Chat session state models and helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol

from src.models.answer_command_result import AnswerCommandResult

MessageRole = Literal["user", "assistant"]
MessageFormat = Literal["markdown", "text"]

MESSAGES_KEY = "messages"
FIRST_TURN_RESULT_KEY = "first_turn_result"
FOLLOW_UP_TURNS_KEY = "follow_up_turns"
LAST_ERROR_KEY = "last_error"
PENDING_PROMPT_KEY = "pending_prompt"


class SessionStateProtocol(Protocol):
    """Protocol for the subset of Streamlit session-state behavior we use."""

    def setdefault(self, key: str, default: object) -> object:
        """Set a default value if the key is missing."""

    def get(self, key: str, default: object | None = None) -> object:
        """Get a value from session state."""

    def __getitem__(self, key: str) -> object:
        """Read a value from session state."""

    def __setitem__(self, key: str, value: object) -> None:
        """Store a value in session state."""


@dataclass
class ChatMessage:
    """Message shown in the Streamlit chat transcript."""

    role: MessageRole
    content: str
    format_type: MessageFormat


@dataclass
class FollowUpTurn:
    """Later-turn conversational exchange."""

    user_question: str
    assistant_answer: str


def initialize_session_state(session_state: SessionStateProtocol) -> None:
    """Initialize the Streamlit session state."""
    session_state.setdefault(MESSAGES_KEY, [])
    session_state.setdefault(FIRST_TURN_RESULT_KEY, None)
    session_state.setdefault(FOLLOW_UP_TURNS_KEY, [])
    session_state.setdefault(LAST_ERROR_KEY, None)
    session_state.setdefault(PENDING_PROMPT_KEY, None)


def clear_session_state(session_state: SessionStateProtocol) -> None:
    """Clear all chat-related state."""
    session_state[MESSAGES_KEY] = []
    session_state[FIRST_TURN_RESULT_KEY] = None
    session_state[FOLLOW_UP_TURNS_KEY] = []
    session_state[LAST_ERROR_KEY] = None
    session_state[PENDING_PROMPT_KEY] = None


def get_messages(session_state: SessionStateProtocol) -> list[ChatMessage]:
    """Return the chat transcript from session state."""
    value = session_state.get(MESSAGES_KEY)
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, ChatMessage)]


def get_first_turn_result(session_state: SessionStateProtocol) -> AnswerCommandResult | None:
    """Return the grounded first-turn result from session state."""
    value = session_state.get(FIRST_TURN_RESULT_KEY)
    return value if isinstance(value, AnswerCommandResult) else None


def get_follow_up_turns(session_state: SessionStateProtocol) -> list[FollowUpTurn]:
    """Return follow-up turns from session state."""
    value = session_state.get(FOLLOW_UP_TURNS_KEY)
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, FollowUpTurn)]


def get_pending_prompt(session_state: SessionStateProtocol) -> str | None:
    """Return the pending prompt waiting to be processed."""
    value = session_state.get(PENDING_PROMPT_KEY)
    return value if isinstance(value, str) and value else None


def set_pending_prompt(session_state: SessionStateProtocol, prompt: str) -> None:
    """Store a pending prompt for processing on the next rerun."""
    session_state[PENDING_PROMPT_KEY] = prompt


def clear_pending_prompt(session_state: SessionStateProtocol) -> None:
    """Clear the pending prompt."""
    session_state[PENDING_PROMPT_KEY] = None


def append_message(
    session_state: SessionStateProtocol,
    role: MessageRole,
    content: str,
    format_type: MessageFormat,
) -> None:
    """Append a new chat message to the transcript."""
    messages = get_messages(session_state)
    messages.append(ChatMessage(role=role, content=content, format_type=format_type))
    session_state[MESSAGES_KEY] = messages


def append_follow_up_turn(
    session_state: SessionStateProtocol,
    user_question: str,
    assistant_answer: str,
) -> None:
    """Append a follow-up turn to session state."""
    follow_up_turns = get_follow_up_turns(session_state)
    follow_up_turns.append(FollowUpTurn(user_question=user_question, assistant_answer=assistant_answer))
    session_state[FOLLOW_UP_TURNS_KEY] = follow_up_turns
