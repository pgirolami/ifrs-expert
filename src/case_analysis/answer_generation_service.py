"""Answer generation service wrapping the case-analysis engine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from src.case_analysis.engine import AnswerEngine, AnswerEngineConfigProtocol, AnswerEngineHooks

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult
    from src.policy import RetrievalPolicy


class AnswerEngineFactory(Protocol):
    """Factory for building an answer engine instance."""

    def __call__(
        self,
        query: str,
        policy: RetrievalPolicy,
        config: AnswerEngineConfigProtocol,
        hooks: AnswerEngineHooks | None = None,
    ) -> AnswerEngine:
        """Build an answer engine for one query."""
        ...


@dataclass(frozen=True)
class AnswerGenerationService:
    """Thin service boundary for answer generation orchestration."""

    query: str
    policy: RetrievalPolicy
    config: AnswerEngineConfigProtocol
    hooks: AnswerEngineHooks | None = None
    engine_factory: AnswerEngineFactory = AnswerEngine

    def run(self) -> AnswerCommandResult:
        """Build the answer engine and run the workflow."""
        engine = self.engine_factory(self.query, self.policy, self.config, self.hooks)
        return engine.run()


__all__ = ["AnswerEngineFactory", "AnswerGenerationService"]
