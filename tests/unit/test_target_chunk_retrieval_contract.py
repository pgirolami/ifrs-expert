"""Tests for canonical target chunk retrieval diagnostics."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from experiments.analysis.target_chunk_retrieval import target_chunk_retrieval_contract as module


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
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=None)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    generator.refresh_experiment_index(experiment_dir)
    return experiment_dir, diagnostics, output_dir


def test_generate_target_chunk_retrieval_diagnostics_uses_promptfoo_artifacts(tmp_path: Path) -> None:
    """The generator should read saved retrieve outputs and render expected range coverage."""
    experiment_dir, diagnostics, output_dir = _generate_fixture_run(tmp_path)

    assert diagnostics.run_id == "2026-04-23_22-19-14_promptfoo-eval-family-q1"
    assert diagnostics.question_ids[0] == "Q1.0"
    assert diagnostics.target_documents[:3] == ("ifrs9", "ias39", "ifric16")
    assert diagnostics.expected_section_ranges[0].key == "ifrs9:6.3.1-6.3.6"
    assert diagnostics.rows[0].expected_ranges[0].present
    assert (output_dir / module.DEFAULT_RUN_MD_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_JSON_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RAW_DIRNAME / "Q1.0.chunks.json").exists()
    assert (experiment_dir / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_INDEX_JSON_FILENAME).exists()

    markdown = (output_dir / module.DEFAULT_RUN_MD_FILENAME).read_text(encoding="utf-8")
    assert markdown.startswith("This table checks whether the expected target paragraph ranges")
    assert "| Question | Target chunks | Expected ranges present | IFRS 9 6.3.1-6.3.6 |" in markdown
    assert "chunk(s)<br>rank" in markdown


def test_compare_target_chunk_retrieval_diagnostics_renders_count_deltas(tmp_path: Path) -> None:
    """The comparison script should consume saved run JSON and render cross-run range tables."""
    _, _, output_dir = _generate_fixture_run(tmp_path)
    baseline_json = output_dir / module.DEFAULT_RUN_JSON_FILENAME
    candidate_json = tmp_path / "candidate.json"
    payload = json.loads(baseline_json.read_text(encoding="utf-8"))
    payload["run_id"] = "candidate-run"
    payload["rows"][0]["expected_ranges"][0]["chunk_count"] += 1
    candidate_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    comparer = module.TargetChunkRetrievalDiagnosticsComparer(_repo_root())
    comparison_dir = tmp_path / "comparison"
    diagnostics = comparer.compare(
        inputs=[
            ("baseline", baseline_json),
            ("candidate", candidate_json),
        ],
        output_dir=comparison_dir,
    )

    assert diagnostics.input_labels == ("baseline", "candidate")
    markdown = (comparison_dir / module.DEFAULT_COMPARE_MD_FILENAME).read_text(encoding="utf-8")
    assert "# target_chunk_retrieval_diagnostics__comparison" in markdown
    assert "IFRS 9 6.3.1-6.3.6" in markdown
    assert "(+1)<br>rank" in markdown


def test_analyze_target_chunk_retrieval_diagnostics_appends_section(tmp_path: Path) -> None:
    """The analyzer should append a reproducible section to EXPERIMENTS.md."""
    experiment_dir, diagnostics, output_dir = _generate_fixture_run(tmp_path)
    analyzer = module.TargetChunkRetrievalDiagnosticsAnalyzer(_repo_root())

    rendered = analyzer.analyze(
        experiment_dir=experiment_dir,
        input_path=output_dir / module.DEFAULT_RUN_JSON_FILENAME,
        section_title="Chunk Review",
    )

    experiments_md = (experiment_dir / "EXPERIMENTS.md").read_text(encoding="utf-8")
    assert "## Chunk Review" in rendered
    assert "covered 23 question(s)" in rendered
    assert "IFRS 9 6.3.1-6.3.6:" in rendered
    assert (
        "[diagnostics markdown](runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.md)"
        in rendered
    )
    assert "## Chunk Review" in experiments_md
    assert diagnostics.provider_name in rendered


def test_load_chunk_payload_falls_back_to_answer_artifact(tmp_path: Path) -> None:
    """The loader should use a saved answer chunk artifact when Promptfoo output lacks chunks."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    artifacts_dir = tmp_path / "artifacts"
    artifact_path = artifacts_dir / "Q1" / "Q1.0" / "routing" / module.DEFAULT_ANSWER_SOURCE_FILENAME
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(
        json.dumps(
            {
                "chunks": [
                    {
                        "doc_uid": "ifrs9",
                        "chunk_number": "6.3.1",
                        "chunk_id": "IFRS9_6.3.1",
                        "score": 0.91,
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    payload = generator._load_chunk_payload(
        promptfoo_response=json.dumps({"output": json.dumps({"recommendation": {"answer": "oui"}})}, ensure_ascii=False),
        run_artifacts_dir=artifacts_dir,
        question_source=module.PromptfooTestCase(
            family_id="Q1¤",
            question_path=Path("experiments/00_QUESTIONS/Q1/Q1.0.txt"),
            description="promptfoo test",
        ),
    )

    assert payload["chunks"][0]["chunk_number"] == "6.3.1"
