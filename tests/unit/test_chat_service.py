"""Tests for the Streamlit chat service."""

from __future__ import annotations

from src.models.answer_command_result import AnswerCommandResult
from src.policy import RetrievalPolicy
from src.ui.chat_service import (
    ChatService,
    _build_grounded_context,
    _serialize_json_value,
    create_chat_service,
)
from src.ui.chat_state import FollowUpTurn
from tests.policy import make_retrieval_policy


def test_answer_first_turn_uses_answer_command_result() -> None:
    """First turn should delegate to the grounded answer runner."""
    calls: list[str] = []

    def run_first_turn(question: str) -> AnswerCommandResult:
        calls.append(question)
        return AnswerCommandResult(query=question, success=True, prompt_b_memo_markdown="# Grounded answer")

    service = ChatService(run_first_turn_fn=run_first_turn, generate_follow_up_fn=lambda prompt: "unused")

    result = service.answer_first_turn("What is IFRS 9?")

    assert calls == ["What is IFRS 9?"]
    assert result.prompt_b_memo_markdown == "# Grounded answer"


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
        prompt_b_memo_markdown="# Grounded first answer",
    )
    follow_up_turns = [FollowUpTurn(user_question="Under which conditions?", assistant_answer="Conditions answer")]

    answer = service.answer_follow_up(first_turn_result, follow_up_turns, "What about consolidation?")

    assert answer == "## Follow-up answer"
    assert prompts
    assert "# Grounded first answer" in prompts[0]
    assert "Under which conditions?" in prompts[0]
    assert "Conditions answer" in prompts[0]
    assert "What about consolidation?" in prompts[0]


def test_build_grounded_context_prefers_markdown_then_json_then_raw() -> None:
    """Grounded context should follow markdown > json > raw fallback order."""
    markdown_context, markdown_source = _build_grounded_context(AnswerCommandResult(query="q", success=True, prompt_b_memo_markdown="# memo"))
    assert markdown_context == "# memo"
    assert markdown_source == "markdown"

    json_context, json_source = _build_grounded_context(AnswerCommandResult(query="q", success=True, prompt_b_json={"x": 1}))
    assert '"x": 1' in json_context
    assert json_source == "json"

    raw_context, raw_source = _build_grounded_context(AnswerCommandResult(query="q", success=True, prompt_b_raw_response="raw"))
    assert raw_context == "raw"
    assert raw_source == "raw_response"


def test_build_grounded_context_uses_fallback_when_empty() -> None:
    """Grounded context should use explicit fallback when no payload is available."""
    context, source = _build_grounded_context(AnswerCommandResult(query="q", success=False))
    assert context == "No grounded answer is available."
    assert source == "fallback"


def test_serialize_json_value_returns_pretty_json() -> None:
    """JSON serializer should format values for readable prompts."""
    serialized = _serialize_json_value({"clé": [1, 2]})
    assert "\n" in serialized
    assert '"clé"' in serialized


def test_create_chat_service_uses_provided_options(monkeypatch) -> None:
    """Factory should use caller-provided options without loading default policy."""
    captured: dict[str, object] = {}

    class _FakeAnswerCommand:
        def execute(self) -> AnswerCommandResult:
            return AnswerCommandResult(query="Q", success=True)

    class _FakeFollowUpGenerator:
        def generate_follow_up(self, prompt: str) -> object:
            captured["prompt"] = prompt
            return type("_FollowUpOutput", (), {"markdown": "follow-up", "limitations": [], "out_of_scope": False})()

    class _Options:
        pass

    options = _Options()
    monkeypatch.setattr("src.ui.chat_service.create_answer_command", lambda query, options: _FakeAnswerCommand())
    monkeypatch.setattr("src.ui.chat_service.create_default_follow_up_generator", lambda: _FakeFollowUpGenerator())

    service = create_chat_service(answer_options=options)  # type: ignore[arg-type]
    first = service.answer_first_turn("Q")
    follow = service.answer_follow_up(first, [], "Next?")

    assert first.success is True
    assert follow == "follow-up"
    assert "Current question:\nNext?" in captured["prompt"]


def test_create_chat_service_loads_default_policy_when_missing_options(monkeypatch) -> None:
    """Factory should load default policy and build AnswerOptions when options absent."""
    captured: dict[str, object] = {}

    class _FakeAnswerCommand:
        def execute(self) -> AnswerCommandResult:
            return AnswerCommandResult(query="Q", success=True)

    class _FakeFollowUpGenerator:
        def generate_follow_up(self, prompt: str) -> object:
            captured["prompt"] = prompt
            return type("_FollowUpOutput", (), {"markdown": "follow-up", "limitations": [], "out_of_scope": False})()

    fake_retrieval_policy = make_retrieval_policy()

    class _FakePolicyCatalog:
        pass

    monkeypatch.setattr("src.ui.chat_service.load_policy_catalog", lambda path: _FakePolicyCatalog())
    monkeypatch.setattr("src.ui.chat_service.resolve_retrieval_policy", lambda catalog, policy_name: fake_retrieval_policy)

    def _fake_create_answer_command(query: str, options: object) -> _FakeAnswerCommand:
        captured["query"] = query
        captured["options"] = options
        return _FakeAnswerCommand()

    monkeypatch.setattr("src.ui.chat_service.create_answer_command", _fake_create_answer_command)
    monkeypatch.setattr("src.ui.chat_service.create_default_follow_up_generator", lambda: _FakeFollowUpGenerator())

    service = create_chat_service(answer_options=None)
    result = service.answer_first_turn("Question?")

    assert result.success is True
    assert captured["query"] == "Question?"
    options = captured["options"]
    assert hasattr(options, "policy")
    policy_value = options.policy
    assert isinstance(policy_value, RetrievalPolicy)
    assert policy_value.k == fake_retrieval_policy.k
