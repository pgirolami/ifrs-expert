"""Tests for case-file workflow persistence and handoff artifacts."""

from __future__ import annotations

from pathlib import Path

from src.case_analysis.case_file import CaseFileWorkflow, JsonCaseStateStore


def test_case_file_workflow_persists_uploaded_evidence(tmp_path: Path) -> None:
    """Case workflow should persist case state and uploaded evidence metadata."""
    store = JsonCaseStateStore(root_dir=tmp_path)
    workflow = CaseFileWorkflow(store=store)

    created = workflow.create_case(case_id="case-1", question="Can we use the exemption?")
    updated = workflow.add_evidence_file(case_id=created.case_id, file_id="file-1", filename="lease.pdf", text="Lease term is 12 months.")
    reloaded = store.load_case("case-1")

    assert updated.case_id == "case-1"
    assert reloaded is not None
    assert reloaded.evidence_files[0].filename == "lease.pdf"
    assert reloaded.evidence_files[0].text == "Lease term is 12 months."


def test_case_file_workflow_interrupts_and_resumes_clarification(tmp_path: Path) -> None:
    """Clarification questions should pause and resume the case workflow."""
    workflow = CaseFileWorkflow(store=JsonCaseStateStore(root_dir=tmp_path))
    workflow.create_case(case_id="case-1", question="Can we recognize revenue?")

    paused = workflow.request_clarification(case_id="case-1", questions=["Is control transferred?"])
    resumed = workflow.answer_clarification(case_id="case-1", answers={"Is control transferred?": "Yes"})

    assert paused.status == "awaiting_clarification"
    assert resumed.status == "ready_for_analysis"
    assert resumed.clarification_answers == {"Is control transferred?": "Yes"}


def test_case_file_workflow_exports_workpaper(tmp_path: Path) -> None:
    """Case workflow should export a workpaper artifact from persisted state."""
    workflow = CaseFileWorkflow(store=JsonCaseStateStore(root_dir=tmp_path))
    workflow.create_case(case_id="case-1", question="Can we apply IFRS 16 short-term lease exemption?")
    workflow.add_evidence_file(case_id="case-1", file_id="file-1", filename="lease.txt", text="Lease term is 12 months.")

    export_path = workflow.export_workpaper(case_id="case-1", output_dir=tmp_path / "exports")

    exported = export_path.read_text(encoding="utf-8")
    assert "# Case workpaper: case-1" in exported
    assert "Can we apply IFRS 16" in exported
    assert "lease.txt" in exported
