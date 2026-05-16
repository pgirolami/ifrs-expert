"""Tests for centralized Pydantic AI agent factories."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from src.ai.agent_factory import GenerationDeps
from src.ai.pydantic_client import PydanticAIAnswerGenerator, PydanticAITextGenerator
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, Recommendation
from src.ui.follow_up_agent import GroundedFollowUpOutput, PydanticAIGroundedFollowUpGenerator

TOutput = TypeVar("TOutput")


@dataclass
class _FakeRunResult(Generic[TOutput]):
    output: TOutput


@dataclass
class _FakeAgent(Generic[TOutput]):
    output: TOutput
    captured_prompt: str | None = None
    captured_deps: GenerationDeps | None = None

    def run_sync(self, prompt: str, deps: GenerationDeps) -> _FakeRunResult[TOutput]:
        self.captured_prompt = prompt
        self.captured_deps = deps
        return _FakeRunResult(output=self.output)


def test_text_generator_passes_generation_deps(monkeypatch) -> None:
    """Text generation should use typed deps and a shared agent builder."""
    fake_agent = _FakeAgent(output="hello")
    monkeypatch.setattr("src.ai.pydantic_client.build_text_agent", lambda model: fake_agent)

    generator = PydanticAITextGenerator(model="openai:gpt-5.2")
    output = generator.generate_text("prompt text")

    assert output == "hello"
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="free-form IFRS completion", prompt_kind="free_form_completion")


def test_answer_generator_passes_generation_deps(monkeypatch) -> None:
    """Structured answer generation should also use typed deps."""
    fake_output = ApproachIdentificationOutput(status="pass")
    fake_agent = _FakeAgent(output=fake_output)
    monkeypatch.setattr("src.ai.pydantic_client.build_structured_agent", lambda model, output_type, output_retries: fake_agent)

    generator = PydanticAIAnswerGenerator(model="openai:gpt-5.2")
    output = generator.generate_approach_identification("prompt text")

    assert output == fake_output
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="structured approach_identification", prompt_kind="approach_identification")


def test_follow_up_generator_passes_generation_deps(monkeypatch) -> None:
    """Follow-up generation should use the shared structured agent builder."""
    fake_output = GroundedFollowUpOutput(markdown="hello", limitations=[], out_of_scope=False)
    fake_agent = _FakeAgent(output=fake_output)
    monkeypatch.setattr("src.ui.follow_up_agent.build_structured_agent", lambda model, output_type, output_retries: fake_agent)

    generator = PydanticAIGroundedFollowUpGenerator(model="openai:gpt-5.2")
    output = generator.generate_follow_up("prompt text")

    assert output == fake_output
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="grounded follow-up", prompt_kind="grounded_follow_up")
