"""Typed grounded follow-up generation for chat."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field

from src.ai.agent_factory import GenerationDeps, build_generation_run_controls, build_structured_agent
from src.ai.runtime import resolve_pydantic_ai_runtime

logger = logging.getLogger(__name__)


class GroundedFollowUpOutput(BaseModel):
    """Structured grounded follow-up output."""

    model_config = ConfigDict(extra="allow")

    markdown: str
    limitations: list[str] = Field(default_factory=list)
    out_of_scope: bool = False


class GroundedFollowUpGeneratorProtocol(Protocol):
    """Callable contract for grounded follow-up generation."""

    def generate_follow_up(self, prompt: str) -> GroundedFollowUpOutput:
        """Generate a structured grounded follow-up answer."""
        ...


@dataclass(frozen=True)
class PydanticAIGroundedFollowUpGenerator:
    """Pydantic AI grounded follow-up generator."""

    model: str
    output_retries: int = 2

    def generate_follow_up(self, prompt: str) -> GroundedFollowUpOutput:
        """Generate a grounded follow-up completion as structured output."""
        agent = build_structured_agent(self.model, output_type=GroundedFollowUpOutput, output_retries=self.output_retries)
        generation_deps = GenerationDeps(task_name="grounded follow-up", prompt_kind="grounded_follow_up")
        run_controls = build_generation_run_controls(generation_deps)
        result = agent.run_sync(
            prompt,
            deps=generation_deps,
            model_settings=run_controls.model_settings,
            metadata=run_controls.metadata,
            usage_limits=run_controls.usage_limits,
        )
        output: GroundedFollowUpOutput = result.output
        logger.info(f"Pydantic AI grounded follow-up received model={self.model} markdown_chars={len(output.markdown)} limitations={len(output.limitations)} out_of_scope={output.out_of_scope}")
        return output


@dataclass(frozen=True)
class GroundedFollowUpTextGenerator:
    """Text-oriented adapter over the structured follow-up output."""

    generator: GroundedFollowUpGeneratorProtocol

    def generate_text(self, prompt: str) -> str:
        """Generate follow-up markdown through the structured follow-up contract."""
        output = self.generator.generate_follow_up(prompt)
        return output.markdown


def create_default_follow_up_generator() -> PydanticAIGroundedFollowUpGenerator:
    """Create the configured Pydantic AI grounded follow-up generator."""
    runtime = resolve_pydantic_ai_runtime()
    logger.info(f"Using Pydantic AI grounded follow-up model: {runtime.model_name}")
    return PydanticAIGroundedFollowUpGenerator(model=runtime.model_name)


__all__ = [
    "GroundedFollowUpGeneratorProtocol",
    "GroundedFollowUpOutput",
    "GroundedFollowUpTextGenerator",
    "PydanticAIGroundedFollowUpGenerator",
    "create_default_follow_up_generator",
]
