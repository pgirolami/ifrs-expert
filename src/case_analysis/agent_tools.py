"""Bounded agent tooling primitives for case-file analysis."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass

from pydantic import BaseModel

from src.case_analysis.models import CaseEvidenceAgentInput, CaseEvidenceAgentResult, ToolCallRecord, ValidationFailure

logger = logging.getLogger(__name__)


class ToolRequest(BaseModel):
    """One bounded-agent request to call a named tool."""

    name: str
    arguments: dict[str, object]


ToolFn = Callable[[dict[str, object]], dict[str, object]]
PlannerFn = Callable[[CaseEvidenceAgentInput], list[ToolRequest]]


@dataclass(frozen=True)
class CaseEvidenceGatheringAgentNode:
    """Bounded agent node for gathering case evidence through allowed tools."""

    enabled: bool
    planner_fn: PlannerFn
    tools: dict[str, ToolFn]
    max_tool_calls: int = 5

    def execute(self, agent_input: CaseEvidenceAgentInput) -> CaseEvidenceAgentResult | ValidationFailure:
        """Run bounded case-evidence gathering with tool allow-list and budget checks."""
        if not self.enabled:
            logger.info(f"Case evidence agent disabled for case_id={agent_input.case_id}")
            return CaseEvidenceAgentResult(status="disabled", tool_calls=[])

        tool_requests = self.planner_fn(agent_input)
        if len(tool_requests) > self.max_tool_calls:
            return ValidationFailure(
                error_stage="case_evidence_agent",
                reason="tool_budget_exceeded",
                message=f"Error: case evidence agent requested {len(tool_requests)} tool calls; max is {self.max_tool_calls}",
            )

        tool_call_records: list[ToolCallRecord] = []
        for tool_request in tool_requests:
            tool = self.tools.get(tool_request.name)
            if tool is None:
                return ValidationFailure(
                    error_stage="case_evidence_agent",
                    reason="tool_not_allowed",
                    message=f"Error: tool is not allowed for case evidence agent: {tool_request.name}",
                )
            try:
                output = tool(tool_request.arguments)
            except RuntimeError as e:
                logger.exception(f"Case evidence tool failed: {tool_request.name}")
                tool_call_records.append(
                    ToolCallRecord(
                        tool_name=tool_request.name,
                        arguments=tool_request.arguments,
                        output=None,
                        error=str(e),
                    )
                )
                return ValidationFailure(
                    error_stage="case_evidence_agent",
                    reason="tool_call_failed",
                    message=f"Error: case evidence tool failed: {tool_request.name}: {e}",
                )

            tool_call_records.append(
                ToolCallRecord(
                    tool_name=tool_request.name,
                    arguments=tool_request.arguments,
                    output=output,
                    error=None,
                )
            )

        return CaseEvidenceAgentResult(status="complete", tool_calls=tool_call_records)
