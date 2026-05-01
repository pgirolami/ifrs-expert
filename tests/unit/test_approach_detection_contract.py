"""Tests for canonical approach detection diagnostics."""

from __future__ import annotations

import json
from pathlib import Path

import yaml
import pytest

from experiments.analysis.approach_detection import approach_detection_contract as module


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _build_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo_root = tmp_path
    question_dir = repo_root / "experiments" / "00_QUESTIONS" / "QX"
    question_dir.mkdir(parents=True)
    (question_dir / "QX.0.txt").write_text("Can we apply hedge accounting?", encoding="utf-8")
    (question_dir / "family.yaml").write_text(
        yaml.safe_dump(
            {
                "family_id": "QX",
                "assert": [
                    {
                        "type": "javascript",
                        "value": "const labels = data.approaches.map(a => a.normalized_label); return labels.includes('expected_approach');",
                    }
                ],
                "assert_retrieve": {
                    "required_section_ranges": [
                        {"document": "ifrs9", "start": "6.3.1", "end": "6.3.6"},
                    ]
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    experiment_dir = repo_root / "experiments" / "99_approach_fixture"
    run_dir = experiment_dir / "runs" / "2026-04-26_approach"
    run_dir.mkdir(parents=True)
    _write_json(
        run_dir / "run.json",
        {
            "description": "promptfoo eval family=QX",
            "artifacts_path": str(run_dir / "artifacts"),
            "promptfoo_args": ["--filter-metadata", "family=QX¤"],
            "created_at_utc": "2026-04-26T00:00:00+00:00",
        },
    )
    (run_dir / "promptfooconfig.yaml").write_text(
        yaml.safe_dump(
            {
                "providers": [{"label": "Fake provider", "config": {}}],
                "tests": [
                    {
                        "vars": {"question": "file://../../../00_QUESTIONS/QX/QX.0.txt"},
                        "metadata": {
                            "family": "QX¤",
                            "variant": "QX.0¤",
                            "question_path": "experiments/00_QUESTIONS/QX/QX.0.txt",
                        },
                        "description": "QX.0 fake question",
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    artifact_dir = run_dir / "artifacts" / "QX" / "QX.0" / "llm_provider=fake__policy-config=." / "effective" / "policy.default.yaml"
    repeat_dir = artifact_dir / "repeat-1"
    for output_dir, extra_label in ((artifact_dir, "spurious_approach"), (repeat_dir, "")):
        output_dir.mkdir(parents=True)
        (output_dir / "A-prompt.txt").write_text(
            '<chunk id="1" doc_uid="ifrs9" chunk_number="6.3.2" score="0.88">text</chunk>',
            encoding="utf-8",
        )
        approaches = [
            {"normalized_label": "expected_approach", "label_fr": "Expected", "applicability": "oui", "references": [{"document": "ifrs9"}]},
        ]
        if extra_label:
            approaches.append({"normalized_label": extra_label, "label_fr": "Spurious", "applicability": "non", "references": []})
        _write_json(output_dir / "B-response.json", {"recommendation": {"answer": "oui"}, "approaches": approaches})
    (experiment_dir / "EXPERIMENTS.md").write_text("# Notes\n", encoding="utf-8")
    return repo_root, experiment_dir


def test_generate_approach_detection_diagnostics_writes_html_markdown_json(tmp_path: Path) -> None:
    repo_root, experiment_dir = _build_fixture(tmp_path)
    generator = module.ApproachDetectionDiagnosticsGenerator(repo_root)

    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=None)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    generator.refresh_experiment_index(experiment_dir)

    assert diagnostics.expected_labels == ("expected_approach",)
    assert len(diagnostics.rows) == 2
    assert diagnostics.rows[0].prompt_chunks[0].expected
    assert (output_dir / module.DEFAULT_RUN_HTML_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_MD_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_JSON_FILENAME).exists()
    assert (experiment_dir / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_INDEX_JSON_FILENAME).exists()
    html = (output_dir / module.DEFAULT_RUN_HTML_FILENAME).read_text(encoding="utf-8")
    assert "Spurious" in html or "spurious_approach" in html
    assert '<th class="sticky-1 metadata-col">Q</th>' in html
    assert '<th class="sticky-3 metadata-col">rec</th>' in html
    assert '<th class="sticky-4 metadata-col">spur</th>' not in html
    assert "Show only runs with spurious labels" in html
    assert ">✅</td>" in html


def test_compare_and_analyze_approach_detection_diagnostics(tmp_path: Path) -> None:
    repo_root, experiment_dir = _build_fixture(tmp_path)
    generator = module.ApproachDetectionDiagnosticsGenerator(repo_root)
    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=None)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    generator.refresh_experiment_index(experiment_dir)
    run_json = output_dir / module.DEFAULT_RUN_JSON_FILENAME

    comparer = module.ApproachDetectionDiagnosticsComparer(repo_root)
    comparison_dir = tmp_path / "comparison"
    comparer.compare(inputs=[("left", run_json), ("right", run_json)], output_dir=comparison_dir)
    comparison_markdown = (comparison_dir / module.DEFAULT_COMPARE_MD_FILENAME).read_text(encoding="utf-8")
    assert "# approach_detection_diagnostics__comparison" in comparison_markdown
    assert "expected_approach" in comparison_markdown

    analyzer = module.ApproachDetectionDiagnosticsAnalyzer(repo_root)
    rendered = analyzer.analyze(experiment_dir=experiment_dir, input_path=None, section_title="Approach Review")
    assert "## Approach Review" in rendered
    assert "Missing expected approach rows" in rendered
    assert "[diagnostics markdown](runs/2026-04-26_approach/diagnostics/approach_detection/approach_detection_diagnostics.md)" in rendered


def test_approach_detection_headers_use_exact_expected_range_label_for_targets(monkeypatch: pytest.MonkeyPatch) -> None:
    """Target sections should display the exact expected paragraph range when one is available."""
    generator = module.ApproachDetectionDiagnosticsGenerator(Path("."))
    row = module.QuestionRunDiagnostics(
        question_id="Q5.0",
        question_text="question",
        embedded_question_text="question",
        family_id="Q5",
        run_label="base",
        artifact_dir=Path("/tmp/artifacts"),
        recommendation="oui",
        approaches=(),
        labels=(),
        missing_expected_labels=(),
        spurious_labels=(),
        prompt_chunks=(
            module.PromptChunk(doc_uid="ifrs13", chunk_number="42", score=0.0, chunk_id="1", expected=True),
            module.PromptChunk(doc_uid="ifrs13", chunk_number="43", score=0.68, chunk_id="2", expected=False),
        ),
        authoritative_references=(("ifrs13", "42"),),
        secondary_references=(),
        peripheral_references=(),
        dropped_documents=(),
    )
    expected_ranges = (module.ExpectedSectionRange(document="ifrs13", start="42", end="42"),)
    section_record = module.SectionDisplayRecord(
        doc_uid="ifrs13",
        section_id="IFRS13_g42-44",
        title="Non-performance risk",
        section_lineage=("International Financial Reporting Standard 13 Fair Value Measurement",),
        position=16,
    )
    chunk_lookup = {
        1: module.ChunkLookupRecord(chunk_db_id=1, doc_uid="ifrs13", chunk_number="42", containing_section_id="IFRS13_g42-44"),
        2: module.ChunkLookupRecord(chunk_db_id=2, doc_uid="ifrs13", chunk_number="43", containing_section_id="IFRS13_g42-44"),
    }

    monkeypatch.setattr(module, "_load_chunk_lookup", lambda _ids: chunk_lookup)
    monkeypatch.setattr(module, "_load_chunk_lookup_by_reference", lambda _references: {})
    monkeypatch.setattr(module, "_load_expected_section_display_records", lambda _ranges: {"ifrs13": (section_record,)})
    monkeypatch.setattr(module, "_load_section_lookup", lambda _section_ids: {"IFRS13_g42-44": section_record})

    section_columns = generator._section_columns((row,), expected_ranges)

    assert len(section_columns) == 1
    assert section_columns[0].is_target
    assert section_columns[0].display_label == "42-42"
    html = generator._render_section_header(section_columns[0], expected_ranges)
    assert "🎯 42-42" in html
