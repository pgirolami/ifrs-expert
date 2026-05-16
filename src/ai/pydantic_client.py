"""Pydantic AI application client and runtime resolution."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TypeVar

from pydantic import BaseModel, ConfigDict, Field

from src.ai.agent_factory import GenerationDeps, build_generation_run_controls, build_structured_agent, build_text_agent
from src.ai.runtime import resolve_pydantic_ai_runtime
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput

logger = logging.getLogger(__name__)
TOutput = TypeVar("TOutput", bound=BaseModel)


class GroundedFollowUpOutput(BaseModel):
    """Structured grounded follow-up output."""

    model_config = ConfigDict(extra="allow")

    markdown: str
    limitations: list[str] = Field(default_factory=list)
    out_of_scope: bool = False


@dataclass(frozen=True)
class PydanticAIApp:
    """Canonical Pydantic AI application client for IFRS Expert."""

    model: str
    output_retries: int = 2

    def generate_text(self, prompt: str) -> str:
        """Generate free-form text through Pydantic AI."""
        return self._run_text_agent(prompt=prompt, task_name="free-form IFRS completion", prompt_kind="free_form_completion")

    def generate_approach_identification(self, prompt: str) -> ApproachIdentificationOutput:
        """Generate the typed approach-identification output."""
        return self._run_structured_agent(prompt=prompt, output_type=ApproachIdentificationOutput, prompt_kind="approach_identification")

    def generate_applicability_analysis(self, prompt: str) -> ApplicabilityAnalysisOutput:
        """Generate the typed applicability-analysis output."""
        return self._run_structured_agent(prompt=prompt, output_type=ApplicabilityAnalysisOutput, prompt_kind="applicability_analysis")

    def generate_follow_up(self, prompt: str) -> GroundedFollowUpOutput:
        """Generate a structured grounded follow-up answer."""
        return self._run_structured_agent(prompt=prompt, output_type=GroundedFollowUpOutput, prompt_kind="grounded_follow_up")

    def generate_follow_up_text(self, prompt: str) -> str:
        """Generate grounded follow-up markdown directly."""
        return self.generate_follow_up(prompt).markdown

    def _run_text_agent(self, *, prompt: str, task_name: str, prompt_kind: str) -> str:
        """Run one text-generation agent and return its output."""
        agent = build_text_agent(self.model)
        generation_deps = GenerationDeps(task_name=task_name, prompt_kind=prompt_kind)
        run_controls = build_generation_run_controls(generation_deps)
        result = agent.run_sync(
            prompt,
            deps=generation_deps,
            model_settings=run_controls.model_settings,
            metadata=run_controls.metadata,
            usage_limits=run_controls.usage_limits,
        )
        output = result.output
        logger.info(f"Pydantic AI completion received model={self.model} prompt_kind={prompt_kind} output_chars={len(output)}")
        return output

    def _run_structured_agent(
        self,
        *,
        prompt: str,
        output_type: type[TOutput],
        prompt_kind: str,
    ) -> TOutput:
        """Run one typed Pydantic AI agent and return its model output."""
        agent = build_structured_agent(self.model, output_type=output_type, output_retries=self.output_retries)
        generation_deps = GenerationDeps(task_name=f"structured {prompt_kind}", prompt_kind=prompt_kind)
        run_controls = build_generation_run_controls(generation_deps)
        result = agent.run_sync(
            prompt,
            deps=generation_deps,
            model_settings=run_controls.model_settings,
            metadata=run_controls.metadata,
            usage_limits=run_controls.usage_limits,
        )
        output: TOutput = result.output
        logger.info(f"Pydantic AI structured completion received model={self.model} prompt_kind={prompt_kind}")
        return output


def create_default_pydantic_ai_app() -> PydanticAIApp:
    """Create the configured Pydantic AI client from app runtime configuration."""
    runtime = resolve_pydantic_ai_runtime()
    logger.info(f"Using Pydantic AI model: {runtime.model_name}")
    return PydanticAIApp(model=runtime.model_name)


def infer_answer_prompt_kind(prompt: str) -> str:
    """Infer whether a prompt is approach identification or applicability analysis from stable markers."""
    if "<identified_approaches>" in prompt:
        return "applicability_analysis"
    return "approach_identification"


__all__ = [
    "GroundedFollowUpOutput",
    "PydanticAIApp",
    "create_default_pydantic_ai_app",
    "infer_answer_prompt_kind",
    "resolve_pydantic_ai_runtime",
]
