"""Pydantic AI model resolution and generation adapters."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TypeVar

from pydantic import BaseModel
from pydantic_ai import Agent

from src.ai.runtime import resolve_pydantic_ai_runtime
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput

logger = logging.getLogger(__name__)
TOutput = TypeVar("TOutput", bound=BaseModel)


@dataclass(frozen=True)
class PydanticAITextGenerator:
    """Thin Pydantic AI text-generation adapter for free-form completions."""

    model: str

    def generate_text(self, prompt: str) -> str:
        """Generate text through Pydantic AI and return the final output."""
        agent: Agent[None, str] = Agent(self.model, output_type=str)
        result = agent.run_sync(prompt)
        output = result.output
        logger.info(f"Pydantic AI completion received model={self.model} output_chars={len(output)}")
        return output


@dataclass(frozen=True)
class PydanticAIAnswerGenerator:
    """Structured Pydantic AI generator for approach identification and applicability analysis outputs."""

    model: str
    output_retries: int = 2

    def generate_approach_identification(self, prompt: str) -> ApproachIdentificationOutput:
        """Generate approach identification through a typed Pydantic AI contract."""
        return self._run_structured_agent(prompt=prompt, output_type=ApproachIdentificationOutput, prompt_kind="approach_identification")  # ty: ignore[invalid-argument-type]

    def generate_applicability_analysis(self, prompt: str) -> ApplicabilityAnalysisOutput:
        """Generate applicability analysis through a typed Pydantic AI contract."""
        return self._run_structured_agent(prompt=prompt, output_type=ApplicabilityAnalysisOutput, prompt_kind="applicability_analysis")  # ty: ignore[invalid-argument-type]

    def _run_structured_agent(
        self,
        *,
        prompt: str,
        output_type: type[TOutput],
        prompt_kind: str,
    ) -> TOutput:
        """Run one typed Pydantic AI agent and return its model output."""
        agent = Agent(self.model, output_type=output_type, output_retries=self.output_retries)
        result = agent.run_sync(prompt)
        output: TOutput = result.output  # ty: ignore[invalid-assignment]
        logger.info(f"Pydantic AI structured completion received model={self.model} prompt_kind={prompt_kind}")
        return output


def create_default_text_generator() -> PydanticAITextGenerator:
    """Create a Pydantic AI text generator from the app runtime configuration."""
    runtime = resolve_pydantic_ai_runtime()
    logger.info(f"Using Pydantic AI model: {runtime.model_name}")
    return PydanticAITextGenerator(model=runtime.model_name)


def create_default_answer_generator() -> PydanticAIAnswerGenerator:
    """Create a structured Pydantic AI answer generator from the app runtime configuration."""
    runtime = resolve_pydantic_ai_runtime()
    logger.info(f"Using Pydantic AI structured answer model: {runtime.model_name}")
    return PydanticAIAnswerGenerator(model=runtime.model_name)


def resolve_pydantic_ai_model_name() -> str:
    """Resolve the configured provider/model into a Pydantic AI model name."""
    return resolve_pydantic_ai_runtime().model_name


def infer_answer_prompt_kind(prompt: str) -> str:
    """Infer whether a prompt is approach identification or applicability analysis from stable markers."""
    if "<identified_approaches>" in prompt:
        return "applicability_analysis"
    return "approach_identification"


__all__ = [
    "PydanticAIAnswerGenerator",
    "PydanticAITextGenerator",
    "create_default_answer_generator",
    "create_default_text_generator",
    "infer_answer_prompt_kind",
    "resolve_pydantic_ai_model_name",
    "resolve_pydantic_ai_runtime",
]
