"""Case-file workflow persistence and artifact helpers."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Literal, Protocol

if TYPE_CHECKING:
    from pathlib import Path

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class EvidenceFileRecord(BaseModel):
    """One evidence file attached to a case."""

    file_id: str
    filename: str
    text: str


class CaseWorkflowState(BaseModel):
    """Persisted workflow state for one case-file analysis."""

    case_id: str
    question: str
    status: Literal["created", "awaiting_clarification", "ready_for_analysis"] = "created"
    evidence_files: list[EvidenceFileRecord] = []
    clarification_questions: list[str] = []
    clarification_answers: dict[str, str] = {}


class CaseStateStore(Protocol):
    """Persistence contract for case workflow state."""

    def save_case(self, state: CaseWorkflowState) -> None:
        """Persist a case workflow state."""

    def load_case(self, case_id: str) -> CaseWorkflowState | None:
        """Load a case workflow state by ID."""


class JsonCaseStateStore:
    """Simple JSON-file case state store for local case workflow experiments."""

    def __init__(self, root_dir: Path) -> None:
        """Initialize the store and create its root directory."""
        self._root_dir = root_dir
        self._root_dir.mkdir(parents=True, exist_ok=True)

    def save_case(self, state: CaseWorkflowState) -> None:
        """Persist a case workflow state as JSON."""
        path = self._case_path(state.case_id)
        path.write_text(state.model_dump_json(indent=2), encoding="utf-8")
        logger.info(f"Saved case workflow state case_id={state.case_id} path={path}")

    def load_case(self, case_id: str) -> CaseWorkflowState | None:
        """Load a case workflow state from JSON."""
        path = self._case_path(case_id)
        if not path.exists():
            return None
        return CaseWorkflowState.model_validate_json(path.read_text(encoding="utf-8"))

    def _case_path(self, case_id: str) -> Path:
        """Return the JSON file path for a case ID."""
        safe_case_id = case_id.replace("/", "_")
        return self._root_dir / f"{safe_case_id}.json"


class CaseFileWorkflow:
    """Application service for case-file state, clarification, and workpaper export."""

    def __init__(self, store: CaseStateStore) -> None:
        """Initialize the workflow with a case-state store."""
        self._store = store

    def create_case(self, case_id: str, question: str) -> CaseWorkflowState:
        """Create and persist a new case workflow state."""
        state = CaseWorkflowState(case_id=case_id, question=question.strip())
        self._store.save_case(state)
        return state

    def add_evidence_file(self, case_id: str, file_id: str, filename: str, text: str) -> CaseWorkflowState:
        """Attach an evidence file to a persisted case."""
        state = self._require_case(case_id)
        state.evidence_files.append(EvidenceFileRecord(file_id=file_id, filename=filename, text=text))
        self._store.save_case(state)
        logger.info(f"Added evidence file to case_id={case_id} file_id={file_id} filename={filename}")
        return state

    def request_clarification(self, case_id: str, questions: list[str]) -> CaseWorkflowState:
        """Pause a case while waiting for clarification answers."""
        state = self._require_case(case_id)
        state.status = "awaiting_clarification"
        state.clarification_questions = questions
        self._store.save_case(state)
        logger.info(f"Case awaiting clarification case_id={case_id} question_count={len(questions)}")
        return state

    def answer_clarification(self, case_id: str, answers: dict[str, str]) -> CaseWorkflowState:
        """Save clarification answers and mark the case ready for analysis."""
        state = self._require_case(case_id)
        state.clarification_answers.update(answers)
        state.status = "ready_for_analysis"
        self._store.save_case(state)
        logger.info(f"Case clarification answered case_id={case_id} answer_count={len(answers)}")
        return state

    def export_workpaper(self, case_id: str, output_dir: Path) -> Path:
        """Export a markdown workpaper from persisted case state."""
        state = self._require_case(case_id)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{case_id}.md"
        output_path.write_text(self._render_workpaper(state), encoding="utf-8")
        logger.info(f"Exported case workpaper case_id={case_id} path={output_path}")
        return output_path

    def _require_case(self, case_id: str) -> CaseWorkflowState:
        """Load a case or raise a clear error when missing."""
        state = self._store.load_case(case_id)
        if state is None:
            message = f"Case not found: {case_id}"
            raise ValueError(message)
        return state

    def _render_workpaper(self, state: CaseWorkflowState) -> str:
        """Render a simple markdown workpaper for a case."""
        lines = [
            f"# Case workpaper: {state.case_id}",
            "",
            f"Status: {state.status}",
            "",
            "## Question",
            "",
            state.question,
            "",
            "## Evidence files",
            "",
        ]
        if not state.evidence_files:
            lines.append("- none")
        lines.extend(f"- `{evidence_file.file_id}` — {evidence_file.filename}" for evidence_file in state.evidence_files)
        if state.clarification_questions:
            lines.extend(["", "## Clarifications", ""])
            for question in state.clarification_questions:
                answer = state.clarification_answers.get(question, "(unanswered)")
                lines.append(f"- {question}: {answer}")
        return "\n".join(lines) + "\n"
