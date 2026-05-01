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
    assert (output_dir / module.DEFAULT_RUN_HTML_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_MD_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RUN_JSON_FILENAME).exists()
    assert (output_dir / module.DEFAULT_RAW_DIRNAME / "Q1.0.chunks.json").exists()
    assert (experiment_dir / module.DEFAULT_DIAGNOSTICS_DIRNAME / module.DEFAULT_INDEX_JSON_FILENAME).exists()

    html = (output_dir / module.DEFAULT_RUN_HTML_FILENAME).read_text(encoding="utf-8")
    assert '<table id="matrix-table">' in html
    assert "question:" in html
    assert "embedded question:" in html
    assert "🎯" in html
    assert 'data-is-target="1"' in html
    assert "header.dataset.isTarget === '1' ||" in html
    assert "IAS 21" in html

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


def test_target_chunk_html_treats_section_expanded_targets_as_retrieved() -> None:
    """Section-expanded target chunks should not be rendered as dropped."""
    assert module._chunk_number_in_range("B4.1.9A", "B4.1.7", "B4.1.26")
    chunks = (
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.7A",
            chunk_id="IFRS09_B4.1.7A",
            score=0.61,
            rank=0,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_gB4.1.7-B4.1.26",
            text_sha256=None,
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.9A",
            chunk_id="IFRS09_B4.1.9A",
            score=0.0,
            rank=1,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_gB4.1.9A-B4.1.9E",
            text_sha256=None,
        ),
    )

    row = module.QuestionDiagnostics(
        question_id="Q3.0",
        run_id="run",
        question_path=Path("Q3.0.txt"),
        question_text="question",
        embedded_question_text="question",
        question_text_sha256="sha",
        chunks=chunks,
        target_documents=("ifrs9",),
        expected_ranges=(
            module.RangeCoverage(
                key="ifrs9:B4.1.7-B4.1.26",
                document="ifrs9",
                start="B4.1.7",
                end="B4.1.26",
                display_label="IFRS 9 B4.1.7-B4.1.26",
                present=True,
                chunk_count=1,
                best_rank=0,
                best_score=0.0,
                chunk_numbers=("B4.1.9A",),
            ),
        ),
    )
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    section_cells = generator._section_cells(row)
    parent_key = module._section_column_key("ifrs9", "ifrs9_B4.1.7-B4.1.26")
    child_key = module._section_column_key("ifrs9", "IFRS09_gB4.1.9A-B4.1.9E")

    assert parent_key in section_cells
    assert child_key not in section_cells
    assert section_cells[parent_key].retrieved_chunk_numbers == ("B4.1.7A", "B4.1.9A")
    assert section_cells[parent_key].retrieved_display_text == "0.61"

    cell = module._build_section_cell(
        [
            chunks[1],
        ],
        row=row,
    )

    assert cell.retrieved_chunk_numbers == ("B4.1.9A",)
    assert cell.retrieved_chunks[0].authority_category == "authoritative"
    assert not cell.dropped_chunks


def test_target_chunk_headers_show_exact_targets_and_provenance(tmp_path: Path) -> None:
    """Headers should keep the exact target ranges visible and expose provenance markers."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    chunks = (
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.10",
            chunk_id="fake-1",
            score=0.91,
            rank=0,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.10-B4.1.19",
            text_sha256=None,
            provenance="seed-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.19",
            chunk_id="fake-2",
            score=0.0,
            rank=1,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.10-B4.1.19",
            text_sha256=None,
            provenance="section-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.7",
            chunk_id="fake-3",
            score=0.0,
            rank=2,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.7-B4.1.26",
            text_sha256=None,
            provenance="section-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.26",
            chunk_id="fake-4",
            score=0.0,
            rank=3,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.7-B4.1.26",
            text_sha256=None,
            provenance="section-source",
        ),
    )
    row = module.QuestionDiagnostics(
        question_id="Q2.0",
        run_id="run",
        question_path=Path("Q2.0.txt"),
        question_text="question",
        embedded_question_text="question",
        question_text_sha256="sha",
        chunks=chunks,
        target_documents=("ifrs9",),
        expected_ranges=(
            module.RangeCoverage(
                key="ifrs9:B4.1.7-B4.1.9",
                document="ifrs9",
                start="B4.1.7",
                end="B4.1.9",
                display_label="IFRS 9 B4.1.7-B4.1.9",
                present=True,
                chunk_count=1,
                best_rank=0,
                best_score=0.91,
                chunk_numbers=("99.7",),
            ),
            module.RangeCoverage(
                key="ifrs9:B4.1.10-B4.1.19",
                document="ifrs9",
                start="B4.1.10",
                end="B4.1.19",
                display_label="IFRS 9 B4.1.10-B4.1.19",
                present=True,
                chunk_count=2,
                best_rank=0,
                best_score=0.91,
                chunk_numbers=("99.10", "99.11"),
            ),
        ),
    )
    section_columns = (
        module.SectionColumn(
            column_key=module._section_column_key("ifrs9", "ifrs9_B4.1.10-B4.1.19"),
            canonical_doc_key="ifrs9",
            doc_display_name="IFRS 9",
            section_id="ifrs9_B4.1.10-B4.1.19",
            title="target",
            section_lineage=("ifrs9_B4.1.10-B4.1.19",),
            position=1,
            is_target=True,
        ),
        module.SectionColumn(
            column_key=module._section_column_key("ifrs9", "IFRS09_B4.1.7-B4.1.26"),
            canonical_doc_key="ifrs9",
            doc_display_name="IFRS 9",
            section_id="IFRS09_B4.1.7-B4.1.26",
            title="expanded",
            section_lineage=("IFRS09_B4.1.7-B4.1.26",),
            position=2,
            is_target=False,
        ),
    )
    metadata_by_column = generator._section_header_metadata_by_column(
        rows=(row,),
        section_columns=section_columns,
        expected_section_ranges=(
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.7", end="B4.1.9"),
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.10", end="B4.1.19"),
        ),
    )

    assert metadata_by_column[section_columns[0].column_key].display_label == "B4.1.10-B4.1.19"
    assert metadata_by_column[section_columns[0].column_key].provenance_marker == "🎯 "
    assert metadata_by_column[section_columns[1].column_key].display_label == "B4.1.7-B4.1.26"
    assert metadata_by_column[section_columns[1].column_key].provenance_marker == ""

    diagnostics = module.RunDiagnostics(
        experiment_name="experiment",
        provider_name="provider",
        run_id="run",
        generated_at="2026-05-01T00:00:00+00:00",
        promptfoo_db_path="db",
        eval_id="eval",
        question_families=("Q2",),
        question_sources=(module.PromptfooTestCase(family_id="Q2", question_path=Path("Q2.0.txt"), description="desc"),),
        question_ids=("Q2.0",),
        policy_name="policy",
        target_documents=("ifrs9",),
        expected_section_ranges=(
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.7", end="B4.1.9"),
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.10", end="B4.1.19"),
        ),
        rows=(row,),
        range_summaries=(
            module.RangeSummary(
                key="ifrs9:B4.1.7-B4.1.9",
                document="ifrs9",
                start="B4.1.7",
                end="B4.1.9",
                display_label="IFRS 9 B4.1.7-B4.1.9",
                question_count=1,
                present_count=1,
                mean_best_rank=0.0,
                score_min=0.91,
                score_max=0.91,
            ),
            module.RangeSummary(
                key="ifrs9:B4.1.10-B4.1.19",
                document="ifrs9",
                start="B4.1.10",
                end="B4.1.19",
                display_label="IFRS 9 B4.1.10-B4.1.19",
                question_count=1,
                present_count=1,
                mean_best_rank=0.0,
                score_min=0.91,
                score_max=0.91,
            ),
        ),
    )
    html = generator.render_html(diagnostics)
    markdown = generator.render_run_markdown(diagnostics)

    assert "Legend:" in html
    assert "🎯 exact target range" in html
    assert "↳ nested subrange of the previous discovered range" in html
    assert "B4.1.10-B4.1.19" in html
    assert "🎯 " in html
    assert "B4.1.7-B4.1.26" in html
    assert "Headers use 🎯 for exact target ranges" in markdown
    assert "nested subranges of the previous discovered range" in markdown


def test_target_chunk_headers_keep_exact_target_and_broader_overlap_separate() -> None:
    """Exact target headers should not be duplicated or downgraded by a broader overlap."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    chunks = (
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.10",
            chunk_id="fake-1",
            score=0.91,
            rank=0,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.10-B4.1.19",
            text_sha256=None,
            provenance="seed-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.19",
            chunk_id="fake-2",
            score=0.0,
            rank=1,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.10-B4.1.19",
            text_sha256=None,
            provenance="section-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.7",
            chunk_id="fake-3",
            score=0.0,
            rank=2,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.7-B4.1.26",
            text_sha256=None,
            provenance="section-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.26",
            chunk_id="fake-4",
            score=0.0,
            rank=3,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.7-B4.1.26",
            text_sha256=None,
            provenance="section-source",
        ),
    )
    row = module.QuestionDiagnostics(
        question_id="Q2.1",
        run_id="run",
        question_path=Path("Q2.1.txt"),
        question_text="question",
        embedded_question_text="question",
        question_text_sha256="sha",
        chunks=chunks,
        target_documents=("ifrs9",),
        expected_ranges=(
            module.RangeCoverage(
                key="ifrs9:B4.1.7-B4.1.9",
                document="ifrs9",
                start="B4.1.7",
                end="B4.1.9",
                display_label="IFRS 9 B4.1.7-B4.1.9",
                present=True,
                chunk_count=1,
                best_rank=0,
                best_score=0.91,
                chunk_numbers=("B4.1.7",),
            ),
            module.RangeCoverage(
                key="ifrs9:B4.1.10-B4.1.19",
                document="ifrs9",
                start="B4.1.10",
                end="B4.1.19",
                display_label="IFRS 9 B4.1.10-B4.1.19",
                present=True,
                chunk_count=2,
                best_rank=0,
                best_score=0.91,
                chunk_numbers=("B4.1.10", "B4.1.19"),
            ),
        ),
    )
    diagnostics = module.RunDiagnostics(
        experiment_name="experiment",
        provider_name="provider",
        run_id="run",
        generated_at="2026-05-01T00:00:00+00:00",
        promptfoo_db_path="db",
        eval_id="eval",
        question_families=("Q2",),
        question_sources=(module.PromptfooTestCase(family_id="Q2", question_path=Path("Q2.1.txt"), description="desc"),),
        question_ids=("Q2.1",),
        policy_name="policy",
        target_documents=("ifrs9",),
        expected_section_ranges=(
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.7", end="B4.1.9"),
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.10", end="B4.1.19"),
        ),
        rows=(row,),
        range_summaries=(),
    )
    html = generator.render_html(diagnostics)

    assert html.count("🎯 B4.1.10-B4.1.19") == 1
    assert "ifrs9::IFRS09_gB4.1.10-B4.1.19" not in html
    assert "🎯 B4.1.7-B4.1.26" not in html
    assert "B4.1.7-B4.1.26" in html


def test_target_chunk_headers_render_arrow_marker_on_new_line() -> None:
    """The arrow marker should be rendered on its own line when present."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    section_column = module.SectionColumn(
        column_key=module._section_column_key("ifrs9", "IFRS09_gB4.1.7-B4.1.26"),
        canonical_doc_key="ifrs9",
        doc_display_name="IFRS 9",
        section_id="IFRS09_gB4.1.7-B4.1.26",
        title="expanded",
        section_lineage=("IFRS09_gB4.1.7-B4.1.26",),
        position=2,
        is_target=False,
    )
    html = generator._render_section_header(
        section_column,
        {
            section_column.column_key: module.SectionHeaderMetadata(
                display_label="B4.1.7-B4.1.26",
                observed_range="B4.1.7-B4.1.26",
                provenance_marker="↳ ",
                provenance_summary="expanded-source",
                marker_leading_break=True,
            )
        },
    )

    assert "<br>↳ B4.1.7-B4.1.26" in html


def test_display_observed_chunk_range_strips_corpus_prefix() -> None:
    """Observed ranges should not surface the synthetic corpus g prefix."""
    assert module._display_observed_chunk_range("IAS32_g17-20", ["17", "20"]) == "17-20"
    assert module._display_observed_chunk_range("IAS32_sgAG94-AG97", ["AG94", "AG97"]) == "AG94-AG97"


def test_section_header_sort_key_orders_ranges_naturally() -> None:
    """Section headers should use natural section ordering, not lexicographic ordering."""
    section_ids = [
        "IFRS09_B4.1.20-B4.1.26",
        "IFRS09_gB4.1.9A-B4.1.9E",
        "IFRS09_B4.1.7-B4.1.9",
    ]

    assert sorted(section_ids, key=module._section_header_sort_key) == [
        "IFRS09_B4.1.7-B4.1.9",
        "IFRS09_gB4.1.9A-B4.1.9E",
        "IFRS09_B4.1.20-B4.1.26",
    ]


def test_target_chunk_headers_choose_one_exact_target_column_per_range() -> None:
    """Only one column should claim the exact target marker for a single expected range."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    chunks = (
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.7",
            chunk_id="fake-1",
            score=0.82,
            rank=0,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_B4.1.7-B4.1.26",
            text_sha256=None,
            provenance="direct-source",
        ),
        module.RetrievedChunk(
            doc_uid="ifrs9",
            chunk_number="B4.1.26",
            chunk_id="fake-2",
            score=0.0,
            rank=1,
            document_type="ifrs",
            document_kind="required",
            containing_section_id="IFRS09_gB4.1.7-B4.1.26",
            text_sha256=None,
            provenance="expanded-source",
        ),
    )
    row = module.QuestionDiagnostics(
        question_id="Q3.0",
        run_id="run",
        question_path=Path("Q3.0.txt"),
        question_text="question",
        embedded_question_text="question",
        question_text_sha256="sha",
        chunks=chunks,
        target_documents=("ifrs9",),
        expected_ranges=(
            module.RangeCoverage(
                key="ifrs9:B4.1.7-B4.1.26",
                document="ifrs9",
                start="B4.1.7",
                end="B4.1.26",
                display_label="IFRS 9 B4.1.7-B4.1.26",
                present=True,
                chunk_count=2,
                best_rank=0,
                best_score=0.82,
                chunk_numbers=("99.7", "99.26"),
            ),
        ),
    )
    section_columns = (
        module.SectionColumn(
            column_key=module._section_column_key("ifrs9", "ifrs9_B4.1.7-B4.1.26"),
            canonical_doc_key="ifrs9",
            doc_display_name="IFRS 9",
            section_id="ifrs9_B4.1.7-B4.1.26",
            title="target",
            section_lineage=("ifrs9_B4.1.7-B4.1.26",),
            position=1,
            is_target=True,
        ),
        module.SectionColumn(
            column_key=module._section_column_key("ifrs9", "IFRS09_gB4.1.7-B4.1.26"),
            canonical_doc_key="ifrs9",
            doc_display_name="IFRS 9",
            section_id="IFRS09_gB4.1.7-B4.1.26",
            title="expanded",
            section_lineage=("IFRS09_gB4.1.7-B4.1.26",),
            position=2,
            is_target=True,
        ),
    )
    metadata_by_column = generator._section_header_metadata_by_column(
        rows=(row,),
        section_columns=section_columns,
        expected_section_ranges=(
            module.ExpectedSectionRange(document="ifrs9", start="B4.1.7", end="B4.1.26"),
        ),
    )

    target_labels = [metadata.provenance_marker + metadata.display_label for metadata in metadata_by_column.values() if metadata.provenance_marker == "🎯 "]
    assert target_labels == ["🎯 B4.1.7-B4.1.26"]
    assert metadata_by_column[section_columns[1].column_key].provenance_marker != "🎯 "

    html = generator.render_html(
        module.RunDiagnostics(
            experiment_name="experiment",
            provider_name="provider",
            run_id="run",
            generated_at="2026-05-01T00:00:00+00:00",
            promptfoo_db_path="db",
            eval_id="eval",
            question_families=("Q3",),
            question_sources=(module.PromptfooTestCase(family_id="Q3", question_path=Path("Q3.0.txt"), description="desc"),),
            question_ids=("Q3.0",),
            policy_name="policy",
            target_documents=("ifrs9",),
            expected_section_ranges=(
                module.ExpectedSectionRange(document="ifrs9", start="B4.1.7", end="B4.1.26"),
            ),
            rows=(row,),
            range_summaries=(
                module.RangeSummary(
                    key="ifrs9:B4.1.7-B4.1.26",
                    document="ifrs9",
                    start="B4.1.7",
                    end="B4.1.26",
                    display_label="IFRS 9 B4.1.7-B4.1.26",
                    question_count=1,
                    present_count=1,
                    mean_best_rank=0.0,
                    score_min=0.82,
                    score_max=0.82,
                ),
            ),
        )
    )
    assert "Legend:" in html
    assert "🎯 exact target range" in html
    assert "↳ nested subrange of the previous discovered range" in html


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


def test_load_chunk_payload_falls_back_to_document_routing_raw_for_provenance(tmp_path: Path) -> None:
    """The loader should recover provenance from the raw document-routing artifact when needed."""
    generator = module.TargetChunkRetrievalDiagnosticsGenerator(_repo_root())
    run_dir = tmp_path / "runs" / "run-1"
    artifacts_dir = run_dir / "artifacts"
    document_routing_raw = run_dir / "diagnostics" / "document_routing" / "raw"
    document_routing_raw.mkdir(parents=True, exist_ok=True)
    (document_routing_raw / "Q1.0.retrieve.json").write_text(
        json.dumps(
            {
                "chunks": [
                    {
                        "doc_uid": "ifrs9",
                        "chunk_number": "6.3.1",
                        "chunk_id": "IFRS9_6.3.1",
                        "score": 0.91,
                        "provenance": "top_similarity",
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
            family_id="Q1",
            question_path=Path("experiments/00_QUESTIONS/Q1/Q1.0.txt"),
            description="promptfoo test",
        ),
    )

    assert payload["chunks"][0]["provenance"] == "top_similarity"
    parsed_chunks = module._parse_chunks(payload)
    assert parsed_chunks[0].provenance == "top_similarity"
