"""Shared Pydantic AI agent builders."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, cast

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

TOutput = TypeVar("TOutput", bound=BaseModel)


@dataclass(frozen=True)
class GenerationDeps:
    """Runtime context passed into Pydantic AI agent instructions."""

    task_name: str
    prompt_kind: str


def build_text_agent(model: str) -> Agent[GenerationDeps, str]:
    """Build a text-generation agent with typed dependencies and instructions."""
    agent: Agent[GenerationDeps, str] = Agent(
        model,
        deps_type=GenerationDeps,
        output_type=str,
        instructions="You are an IFRS expert. Follow the task instructions and answer directly.",
    )

    @agent.instructions
    def _task_instructions(ctx: RunContext[GenerationDeps]) -> str:
        return f"Task: {ctx.deps.task_name}. Prompt kind: {ctx.deps.prompt_kind}."

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
            instructions="You are an IFRS expert. Follow the task instructions and return valid structured output.",
        ),
    )

    @agent.instructions
    def _task_instructions(ctx: RunContext[GenerationDeps]) -> str:
        return f"Task: {ctx.deps.task_name}. Prompt kind: {ctx.deps.prompt_kind}."

    return agent
