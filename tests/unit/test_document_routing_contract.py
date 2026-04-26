"""Tests for canonical document routing diagnostics."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from experiments.analysis.document_routing import document_routing_contract as module


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _source_experiment_dir() -> Path:
    return _repo_root() / "experiments" / "44_retrieval_non_regression_test"


def _copy_experiment_fixture(tmp_path: Path) -> Path:
    source = _source_experiment_dir()
    destination = tmp_path / source.name
    shutil.copytree(source / "runs", destination / "runs")
    shutil.copytree(
        source / ".promptfoo",
        destination / ".promptfoo",
        ignore=shutil.ignore_patterns("promptfoo.db-wal", "promptfoo.db-shm"),
    )
    (destination / "EXPERIMENTS.md").write_text("# Experiment notes\n", encoding="utf-8")
    return destination


def _generate_fixture_run(tmp_path: Path) -> tuple[Path, module.RunDiagnostics, Path]:
    experiment_dir = _copy_experiment_fixture(tmp_path)
    generator = module.DocumentRoutingDiagnosticsGenerator(_repo_root())
    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=None)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    generator.refresh_experiment_index(experiment_dir)
    return experiment_dir, diagnostics, output_dir


def test_generate_document_routing_diagnostics_uses_promptfoo_artifacts(tmp_path: Path) -> None:
    """The generator should read the saved Promptfoo run instead of rerunning retrieval."""
    experiment_dir, diagnostics, output_dir = _generate_fixture_run(tmp_path)

    assert diagnostics.run_id == "2026-04-23_22-19-14_promptfoo-eval-family-q1"
    assert diagnostics.question_families == ("Q1¤",)
    assert diagnostics.question_ids[0] == "Q1.0"
    assert diagnostics.target_documents[:3] == ("ifrs9", "ias39", "ifric16")
    assert diagnostics.rows[0].question_text_sha256
    assert (output_dir / module.DEFAULT_RUN_MD_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_JSON_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RAW_DIRNAME / "Q1.0.retrieve.json").exists()
    assert (experiment_dir / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_INDEX_JSON_FILENAME).exists()
    index_markdown = (experiment_dir / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_INDEX_MD_FILENAME).read_text(encoding="utf-8")
    assert "../runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/diagnostics/document_routing/document_routing_diagnostics.md" in index_markdown

    markdown = (output_dir / module.DEFAULT_RUN_MD_FILENAME).read_text(encoding="utf-8")
    assert markdown.startswith("This table shows every document retrieved for each question.")
    assert "| Question | Total | IFRS 9 | IAS 39 | IFRIC 16 | IAS 21 | IFRS 10 | IFRS 7 | IAS 32 | IFRS 1 | IFRS 18 | IFRIC 2 | IFRS 17 | IFRS 19 |" in markdown
    assert "|  | Total | 23 (0.68-0.80) |" in markdown


def test_compare_document_routing_diagnostics_renders_target_tables(tmp_path: Path) -> None:
    """The comparison script should consume saved run JSON and render cross-run tables."""
    _, diagnostics, output_dir = _generate_fixture_run(tmp_path)
    baseline_json = output_dir / module.DEFAULT_RUN_JSON_FILENAME
    candidate_json = tmp_path / "candidate.json"
    payload = json.loads(baseline_json.read_text(encoding="utf-8"))
    payload["run_id"] = "candidate-run"
    payload["rows"][0]["target_document_scores"]["ifrs9"] = 0.99
    payload["rows"][0]["target_document_ranks"]["ifrs9"] = 1
    candidate_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    comparer = module.DocumentRoutingDiagnosticsComparer(_repo_root())
    comparison_dir = tmp_path / "comparison"
    diagnostics = comparer.compare(
        inputs=[
            ("baseline", baseline_json),
            ("candidate", candidate_json),
        ],
        output_dir=comparison_dir,
        target_documents=["ifrs9", "ias39", "ifric16"],
    )

    assert diagnostics.input_labels == ("baseline", "candidate")
    markdown = (comparison_dir / module.DEFAULT_COMPARE_MD_FILENAME).read_text(encoding="utf-8")
    assert "# document_routing_diagnostics__comparison" in markdown
    assert "## IFRS 9" in markdown
    assert "<span style=\"display:block; background-color:" in markdown
    assert "2 (+0)" in markdown
    assert "1 (+1)" in markdown
    assert "<br>0.99" in markdown


def test_analyze_document_routing_diagnostics_appends_section(tmp_path: Path) -> None:
    """The analyzer should append a reproducible section to EXPERIMENTS.md."""
    experiment_dir, diagnostics, output_dir = _generate_fixture_run(tmp_path)
    analyzer = module.DocumentRoutingDiagnosticsAnalyzer(_repo_root())

    rendered = analyzer.analyze(
        experiment_dir=experiment_dir,
        input_path=output_dir / module.DEFAULT_RUN_JSON_FILENAME,
        section_title="Routing Review",
    )

    experiments_md = (experiment_dir / "EXPERIMENTS.md").read_text(encoding="utf-8")
    assert "## Routing Review" in rendered
    assert "covered 23 question(s)" in rendered
    assert "IFRS 9:" in rendered
    assert "IAS 39:" in rendered
    assert "IFRIC 16:" in rendered
    assert "IFRS 7:" not in rendered
    assert "## Routing Review" in experiments_md
    assert diagnostics.provider_name in rendered


def test_load_document_routing_payload_falls_back_to_answer_artifact(tmp_path: Path) -> None:
    """The loader should use a saved answer routing artifact when Promptfoo output lacks document hits."""
    generator = module.DocumentRoutingDiagnosticsGenerator(_repo_root())
    artifacts_dir = tmp_path / "artifacts"
    artifact_path = artifacts_dir / "Q1" / "Q1.0" / "routing" / module.DEFAULT_DOCUMENT_ROUTING_FILENAME
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(
        json.dumps(
            {
                "document_hits": [
                    {
                        "doc_uid": "ifrs9",
                        "score": 0.91,
                        "document_type": "ifrs",
                        "document_kind": "standard",
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    payload = generator._load_document_routing_payload(
        promptfoo_response=json.dumps({"output": json.dumps({"recommendation": {"answer": "oui"}})}, ensure_ascii=False),
        run_artifacts_dir=artifacts_dir,
        question_source=module.PromptfooTestCase(
            family_id="Q1¤",
            question_path=Path("experiments/00_QUESTIONS/Q1/Q1.0.txt"),
            description="promptfoo test",
        ),
    )

    assert payload["document_hits"][0]["doc_uid"] == "ifrs9"
