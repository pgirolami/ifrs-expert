"""Pydantic AI integration for IFRS Expert."""

from src.ai.agent_factory import GenerationDeps, GenerationRunControls, build_generation_instruction, build_generation_run_controls, build_structured_agent, build_text_agent
from src.ai.agent_specs import GENERATION_AGENT_SPEC_PATH, load_generation_agent_spec
from src.ai.pydantic_client import GroundedFollowUpOutput, PydanticAIApp, create_default_pydantic_ai_app, infer_answer_prompt_kind
from src.ai.runtime import PydanticAIRuntime, resolve_pydantic_ai_runtime

__all__ = [
    "GENERATION_AGENT_SPEC_PATH",
    "GenerationDeps",
    "GenerationRunControls",
    "GroundedFollowUpOutput",
    "PydanticAIApp",
    "PydanticAIRuntime",
    "build_generation_instruction",
    "build_generation_run_controls",
    "build_structured_agent",
    "build_text_agent",
    "create_default_pydantic_ai_app",
    "infer_answer_prompt_kind",
    "load_generation_agent_spec",
    "resolve_pydantic_ai_runtime",
]
