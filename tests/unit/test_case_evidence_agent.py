"""Tests for bounded case-evidence gathering agent node."""

from __future__ import annotations

from src.case_analysis.agent_tools import CaseEvidenceGatheringAgentNode, ToolRequest
from src.case_analysis.models import CaseEvidenceAgentInput, CaseEvidenceAgentResult, ToolCallRecord, ValidationFailure


def test_case_evidence_agent_returns_disabled_result_when_flag_off() -> None:
    """Disabled agent node should not call planner or tools."""
    planner_calls = 0

    def planner(agent_input: CaseEvidenceAgentInput) -> list[ToolRequest]:
        nonlocal planner_calls
        del agent_input
        planner_calls += 1
        return [ToolRequest(name="retrieve_case_evidence", arguments={"query": "leases"})]

    node = CaseEvidenceGatheringAgentNode(enabled=False, planner_fn=planner, tools={})

    result = node.execute(CaseEvidenceAgentInput(case_id="case-1", issue_type="IFRS16", known_facts=[], required_criteria=[]))

    assert isinstance(result, CaseEvidenceAgentResult)
    assert result.status == "disabled"
    assert result.tool_calls == []
    assert planner_calls == 0


def test_case_evidence_agent_executes_allowed_tool_call() -> None:
    """Enabled agent node should execute planned allowed tools and record outputs."""

    def planner(agent_input: CaseEvidenceAgentInput) -> list[ToolRequest]:
        assert agent_input.case_id == "case-1"
        return [ToolRequest(name="retrieve_case_evidence", arguments={"query": "lease term"})]

    def retrieve_case_evidence(arguments: dict[str, object]) -> dict[str, object]:
        return {"query": arguments["query"], "snippets": ["12-month lease"]}

    node = CaseEvidenceGatheringAgentNode(
        enabled=True,
        planner_fn=planner,
        tools={"retrieve_case_evidence": retrieve_case_evidence},
        max_tool_calls=3,
    )

    result = node.execute(CaseEvidenceAgentInput(case_id="case-1", issue_type="IFRS16", known_facts=[], required_criteria=[]))

    assert isinstance(result, CaseEvidenceAgentResult)
    assert result.status == "complete"
    assert result.tool_calls == [
        ToolCallRecord(
            tool_name="retrieve_case_evidence",
            arguments={"query": "lease term"},
            output={"query": "lease term", "snippets": ["12-month lease"]},
            error=None,
        )
    ]


def test_case_evidence_agent_rejects_unallowed_tool() -> None:
    """Agent node should fail closed when the planner asks for an unknown tool."""

    def planner(agent_input: CaseEvidenceAgentInput) -> list[ToolRequest]:
        del agent_input
        return [ToolRequest(name="delete_case", arguments={})]

    node = CaseEvidenceGatheringAgentNode(enabled=True, planner_fn=planner, tools={"retrieve_case_evidence": lambda arguments: {}})

    result = node.execute(CaseEvidenceAgentInput(case_id="case-1", issue_type="IFRS16", known_facts=[], required_criteria=[]))

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "case_evidence_agent"
    assert result.reason == "tool_not_allowed"


def test_case_evidence_agent_enforces_tool_budget() -> None:
    """Agent node should enforce max tool-call budget before executing tools."""

    def planner(agent_input: CaseEvidenceAgentInput) -> list[ToolRequest]:
        del agent_input
        return [
            ToolRequest(name="retrieve_case_evidence", arguments={"query": "one"}),
            ToolRequest(name="retrieve_case_evidence", arguments={"query": "two"}),
        ]

    node = CaseEvidenceGatheringAgentNode(enabled=True, planner_fn=planner, tools={"retrieve_case_evidence": lambda arguments: {}}, max_tool_calls=1)

    result = node.execute(CaseEvidenceAgentInput(case_id="case-1", issue_type="IFRS16", known_facts=[], required_criteria=[]))

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "case_evidence_agent"
    assert result.reason == "tool_budget_exceeded"
