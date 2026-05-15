"""Pydantic AI model resolution and generation adapters."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from pydantic_ai import Agent

from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.case_analysis.stages import AnswerGeneratorProtocol

MISSING_MODEL_MESSAGE = "Model environment variable is required for this provider. Set it in your environment or .env file."

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PydanticAITextGenerator:
    """Thin Pydantic AI text-generation adapter for free-form completions."""

    model: str

    def generate_text(self, prompt: str) -> str:
        """Generate text through Pydantic AI and return the final output."""
        agent = Agent(self.model, output_type=str)
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
        output = self._run_structured_agent(
            prompt=prompt,
            output_type=ApproachIdentificationOutput,
            prompt_kind="approach_identification",
        )
        return cast("ApproachIdentificationOutput", output)

    def generate_applicability_analysis(self, prompt: str) -> ApplicabilityAnalysisOutput:
        """Generate applicability analysis through a typed Pydantic AI contract."""
        output = self._run_structured_agent(
            prompt=prompt,
            output_type=ApplicabilityAnalysisOutput,
            prompt_kind="applicability_analysis",
        )
        return cast("ApplicabilityAnalysisOutput", output)

    def generate_prompt_a(self, prompt: str) -> ApproachIdentificationOutput:
        """Backward-compatible alias for approach identification."""
        return self.generate_approach_identification(prompt)

    def generate_prompt_b(self, prompt: str) -> ApplicabilityAnalysisOutput:
        """Backward-compatible alias for applicability analysis."""
        return self.generate_applicability_analysis(prompt)

    def generate_output_json(self, prompt: str) -> str:
        """Generate a structured answer-stage output and return JSON text."""
        prompt_kind = infer_answer_prompt_kind(prompt)
        output = self.generate_approach_identification(prompt) if prompt_kind == "prompt_a" else self.generate_applicability_analysis(prompt)
        output_json = output.model_dump_json()
        logger.info(f"Serialized Pydantic AI structured completion prompt_kind={prompt_kind} output_chars={len(output_json)}")
        return output_json

    def _run_structured_agent(
        self,
        prompt: str,
        output_type: object,
        prompt_kind: str,
    ) -> BaseModel:
        """Run one typed Pydantic AI agent and return its model output."""
        agent = Agent(self.model, output_type=output_type, output_retries=self.output_retries)
        result = agent.run_sync(prompt)
        output = cast("BaseModel", result.output)
        logger.info(f"Pydantic AI structured completion received model={self.model} prompt_kind={prompt_kind}")
        return output


def create_default_text_generator() -> PydanticAITextGenerator:
    """Create a Pydantic AI text generator from the existing environment variables."""
    model = resolve_pydantic_ai_model_name()
    logger.info(f"Using Pydantic AI model: {model}")
    return PydanticAITextGenerator(model=model)


def create_default_answer_generator() -> AnswerGeneratorProtocol:
    """Create a structured Pydantic AI answer generator from environment variables."""
    model = resolve_pydantic_ai_model_name()
    logger.info(f"Using Pydantic AI structured answer model: {model}")
    return cast("AnswerGeneratorProtocol", PydanticAIAnswerGenerator(model=model))


def resolve_pydantic_ai_model_name() -> str:
    """Resolve the configured provider/model into a Pydantic AI model name."""
    provider = os.getenv("LLM_PROVIDER")
    if not provider:
        msg = "LLM_PROVIDER environment variable is required. Set it to a Pydantic AI supported provider such as openai, anthropic, mistral, or ollama"
        raise ValueError(msg)

    normalized_provider = provider.lower()
    if normalized_provider == "openai":
        return _provider_model_name(provider="openai", model_env_var="OPENAI_MODEL")
    if normalized_provider == "anthropic":
        return _provider_model_name(provider="anthropic", model_env_var="ANTHROPIC_MODEL")
    if normalized_provider == "mistral":
        return _provider_model_name(provider="mistral", model_env_var="MISTRAL_MODEL")
    if normalized_provider == "ollama":
        return _provider_model_name(provider="ollama", model_env_var="OLLAMA_MODEL")

    msg = f"Unknown Pydantic AI provider: {provider}. Supported providers: openai, anthropic, mistral, ollama"
    raise ValueError(msg)


def _provider_model_name(provider: str, model_env_var: str) -> str:
    """Build a Pydantic AI model name from one required model env var."""
    model = os.getenv(model_env_var)
    if not model:
        msg = f"{model_env_var} {MISSING_MODEL_MESSAGE}"
        raise ValueError(msg)
    return f"{provider}:{model}"


def infer_answer_prompt_kind(prompt: str) -> str:
    """Infer whether a prompt is approach identification or applicability analysis from stable markers."""
    if "<identified_approaches>" in prompt:
        return "prompt_b"
    return "prompt_a"


__all__ = [
    "PydanticAIAnswerGenerator",
    "PydanticAITextGenerator",
    "create_default_answer_generator",
    "create_default_text_generator",
    "infer_answer_prompt_kind",
    "resolve_pydantic_ai_model_name",
]
