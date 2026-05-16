"""Tests for centralized Pydantic AI agent factories."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic_ai.models.test import TestModel

from src.ai.agent_factory import GenerationDeps, build_generation_instruction, build_generation_run_controls, build_structured_agent, build_text_agent
from src.ai.agent_specs import load_generation_agent_spec
from src.ai.pydantic_client import GroundedFollowUpOutput, PydanticAIApp
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput

TOutput = TypeVar("TOutput")


@dataclass
class _FakeRunResult(Generic[TOutput]):
    output: TOutput


@dataclass
class _FakeAgent(Generic[TOutput]):
    output: TOutput
    captured_prompt: str | None = None
    captured_deps: GenerationDeps | None = None
    captured_kwargs: dict[str, object] | None = None

    def run_sync(self, prompt: str, deps: GenerationDeps, **kwargs: object) -> _FakeRunResult[TOutput]:
        self.captured_prompt = prompt
        self.captured_deps = deps
        self.captured_kwargs = dict(kwargs)
        return _FakeRunResult(output=self.output)


def test_build_generation_instruction_uses_prompt_kind() -> None:
    """Instruction text should vary by prompt kind."""
    deps = GenerationDeps(task_name="structured approach_identification", prompt_kind="approach_identification")

    instruction = build_generation_instruction(deps)

    assert "structured approach_identification" in instruction
    assert "governing approach" in instruction


def test_text_app_passes_generation_deps(monkeypatch) -> None:
    """Text generation should use typed deps and a shared agent builder."""
    fake_agent = _FakeAgent(output="hello")
    monkeypatch.setattr("src.ai.pydantic_client.build_text_agent", lambda model: fake_agent)

    app = PydanticAIApp(model="openai:gpt-5.2")
    output = app.generate_text("prompt text")

    assert output == "hello"
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="free-form IFRS completion", prompt_kind="free_form_completion")
    assert fake_agent.captured_kwargs == {
        "model_settings": {"temperature": 0.0, "max_tokens": 1024, "parallel_tool_calls": False},
        "metadata": {"task_name": "free-form IFRS completion", "prompt_kind": "free_form_completion"},
        "usage_limits": build_generation_run_controls(GenerationDeps(task_name="free-form IFRS completion", prompt_kind="free_form_completion")).usage_limits,
    }


def test_app_passes_generation_deps_for_structured_outputs(monkeypatch) -> None:
    """Structured generation should also use typed deps."""
    fake_output = ApproachIdentificationOutput(status="pass")
    fake_agent = _FakeAgent(output=fake_output)
    monkeypatch.setattr("src.ai.pydantic_client.build_structured_agent", lambda model, output_type, output_retries: fake_agent)

    app = PydanticAIApp(model="openai:gpt-5.2")
    output = app.generate_approach_identification("prompt text")

    assert output == fake_output
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="structured approach_identification", prompt_kind="approach_identification")
    assert fake_agent.captured_kwargs == {
        "model_settings": {"temperature": 0.0, "max_tokens": 1024, "parallel_tool_calls": False},
        "metadata": {"task_name": "structured approach_identification", "prompt_kind": "approach_identification"},
        "usage_limits": build_generation_run_controls(GenerationDeps(task_name="structured approach_identification", prompt_kind="approach_identification")).usage_limits,
    }


def test_follow_up_generation_uses_shared_structured_app(monkeypatch) -> None:
    """Follow-up generation should use the shared structured app path."""
    fake_output = GroundedFollowUpOutput(markdown="hello", limitations=[], out_of_scope=False)
    fake_agent = _FakeAgent(output=fake_output)
    monkeypatch.setattr("src.ai.pydantic_client.build_structured_agent", lambda model, output_type, output_retries: fake_agent)

    app = PydanticAIApp(model="openai:gpt-5.2")
    output = app.generate_follow_up("prompt text")

    assert output == fake_output
    assert fake_agent.captured_prompt == "prompt text"
    assert fake_agent.captured_deps == GenerationDeps(task_name="structured grounded_follow_up", prompt_kind="grounded_follow_up")
    assert fake_agent.captured_kwargs == {
        "model_settings": {"temperature": 0.0, "max_tokens": 1024, "parallel_tool_calls": False},
        "metadata": {"task_name": "structured grounded_follow_up", "prompt_kind": "grounded_follow_up"},
        "usage_limits": build_generation_run_controls(GenerationDeps(task_name="structured grounded_follow_up", prompt_kind="grounded_follow_up")).usage_limits,
    }


def test_follow_up_text_uses_markdown_output(monkeypatch) -> None:
    """Convenience follow-up text helper should expose markdown only."""
    app = PydanticAIApp(model="openai:gpt-5.2")
    monkeypatch.setattr(PydanticAIApp, "generate_follow_up", lambda self, prompt: GroundedFollowUpOutput(markdown=f"reply:{prompt}", limitations=[], out_of_scope=False))

    assert app.generate_follow_up_text("prompt text") == "reply:prompt text"


def test_text_agent_exposes_generation_contract_tool() -> None:
    """Text agent should register the shared generation guidance tool."""
    agent = build_text_agent("openai:gpt-5.2")
    model = TestModel()

    with agent.override(model=model):
        result = agent.run_sync(
            "prompt text",
            deps=GenerationDeps(task_name="free-form IFRS completion", prompt_kind="free_form_completion"),
        )

    assert "explain_generation_contract" in result.output
    assert "task_name=free-form IFRS completion" in result.output
    assert model.last_model_request_parameters is not None
    assert [tool.name for tool in model.last_model_request_parameters.function_tools] == ["explain_generation_contract"]
    assert agent.name == "ifrs-generation-agent"
    assert agent.description == "Shared IFRS generation agent for text and structured outputs."


def test_structured_agent_exposes_generation_contract_tool() -> None:
    """Structured agent should register the same generation guidance tool."""
    agent = build_structured_agent("openai:gpt-5.2", output_type=ApproachIdentificationOutput, output_retries=2)
    model = TestModel(custom_output_args={"status": "pass"})

    with agent.override(model=model):
        result = agent.run_sync(
            "prompt text",
            deps=GenerationDeps(task_name="structured approach_identification", prompt_kind="approach_identification"),
        )

    assert isinstance(result.output, ApproachIdentificationOutput)
    assert result.output.status == "pass"
    assert model.last_model_request_parameters is not None
    assert [tool.name for tool in model.last_model_request_parameters.function_tools] == ["explain_generation_contract"]
    assert agent.name == "ifrs-generation-agent"
    assert agent.description == "Shared IFRS generation agent for text and structured outputs."


def test_generation_run_controls_use_explicit_limits() -> None:
    """Run controls should define safe, intentional defaults."""
    controls = build_generation_run_controls(GenerationDeps(task_name="structured applicability_analysis", prompt_kind="applicability_analysis"))

    assert controls.model_settings == {"temperature": 0.0, "max_tokens": 1024, "parallel_tool_calls": False}
    assert controls.metadata == {"task_name": "structured applicability_analysis", "prompt_kind": "applicability_analysis"}
    assert controls.usage_limits.request_limit == 6
    assert controls.usage_limits.tool_calls_limit == 4


def test_generation_agent_spec_uses_stable_metadata() -> None:
    """Spec should hold the stable agent metadata."""
    spec = load_generation_agent_spec()

    assert spec.name == "ifrs-generation-agent"
    assert spec.description == "Shared IFRS generation agent for text and structured outputs."
    assert spec.instructions == "You are an IFRS expert."
