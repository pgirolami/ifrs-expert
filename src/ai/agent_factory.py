"""Shared Pydantic AI agent builders."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, cast

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.capabilities import Toolset
from pydantic_ai.toolsets import FunctionToolset

TOutput = TypeVar("TOutput", bound=BaseModel)


@dataclass(frozen=True)
class GenerationDeps:
    """Runtime context passed into Pydantic AI agent instructions."""

    task_name: str
    prompt_kind: str


_PROMPT_KIND_GUIDANCE: dict[str, str] = {
    "free_form_completion": "Answer the user directly and keep the response concise.",
    "approach_identification": ("Extract the governing approach, authority classification, and any clarification needed. Return only the structured result the schema asks for."),
    "applicability_analysis": ("Assess the identified approaches for applicability, preserve the structured schema, and do not add any extra wrapper text."),
    "grounded_follow_up": ("Produce grounded markdown only. Clearly call out limitations and out-of-scope cases when relevant."),
}


def build_generation_instruction(deps: GenerationDeps) -> str:
    """Build the runtime instruction text for one agent run."""
    guidance = _PROMPT_KIND_GUIDANCE.get(deps.prompt_kind, "Follow the task instructions carefully.")
    return f"Task: {deps.task_name}. {guidance}"


def _explain_generation_contract(ctx: RunContext[GenerationDeps]) -> str:
    """Return the active generation contract for tool-assisted self-checks."""
    guidance = build_generation_instruction(ctx.deps)
    return f"task_name={ctx.deps.task_name}; prompt_kind={ctx.deps.prompt_kind}; {guidance}"


def _generation_toolset() -> Toolset[GenerationDeps]:
    """Build the reusable generation guidance toolset capability."""
    return Toolset(
        FunctionToolset(
            [
                Tool(
                    _explain_generation_contract,
                    name="explain_generation_contract",
                    description="Return the active generation contract for this run.",
                ),
            ],
            instructions="Use explain_generation_contract when you need a compact reminder of the current task contract.",
        ),
    )


def build_text_agent(model: str) -> Agent[GenerationDeps, str]:
    """Build a text-generation agent with typed dependencies and instructions."""
    agent: Agent[GenerationDeps, str] = Agent(
        model,
        deps_type=GenerationDeps,
        output_type=str,
        system_prompt="You are an IFRS expert.",
        capabilities=[_generation_toolset()],
    )

    @agent.instructions
    def _task_instructions(ctx: RunContext[GenerationDeps]) -> str:
        return build_generation_instruction(ctx.deps)

    return agent


def build_structured_agent(model: str, output_type: type[TOutput], output_retries: int) -> Agent[GenerationDeps, TOutput]:
    """Build a structured-output agent with typed dependencies and instructions."""
    agent = cast(
        "Agent[GenerationDeps, TOutput]",
        Agent(
            model,
            deps_type=GenerationDeps,
            output_type=output_type,
            output_retries=output_retries,
            system_prompt="You are an IFRS expert.",
            capabilities=[_generation_toolset()],
        ),
    )

    @agent.instructions
    def _task_instructions(ctx: RunContext[GenerationDeps]) -> str:
        return build_generation_instruction(ctx.deps)

    return agent


__all__ = [
    "GenerationDeps",
    "build_generation_instruction",
    "build_structured_agent",
    "build_text_agent",
]
