"""Agent spec loading for Pydantic AI builders."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_ai.agent.spec import AgentSpec

GENERATION_AGENT_SPEC_PATH = Path(__file__).with_name("generation_agent.yaml")


@lru_cache
def load_generation_agent_spec() -> AgentSpec:
    """Load the shared generation agent spec from YAML."""
    return AgentSpec.from_file(GENERATION_AGENT_SPEC_PATH)


__all__ = ["GENERATION_AGENT_SPEC_PATH", "load_generation_agent_spec"]
