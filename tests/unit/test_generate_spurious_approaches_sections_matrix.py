"""Unit tests for the spurious approaches vs sections HTML matrix generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


def _repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return the analysis script path."""
    return _repo_root() / "experiments" / "analysis" / "generate_spurious_approaches_sections_matrix.py"


def _load_module() -> ModuleType:
    """Load the analysis script as a module for unit tests."""
    spec = importlib.util.spec_from_file_location(
        "tests_generate_spurious_approaches_sections_matrix_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        error_message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(error_message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_generate_spurious_approaches_sections_matrix_module"
    sys.modules["tests_generate_spurious_approaches_sections_matrix_module"] = module
    spec.loader.exec_module(module)
    return module


def test_parse_prompt_chunks_supports_section_path_and_chunk_number() -> None:
    """Prompt chunk parsing should support both historical and current attribute names."""
    module = _load_module()
    parser = module.PromptChunkParser()
    content = """
    <chunk id="10" doc_uid="ifrs-9" section_path="6.3.5" score="0.6123">A</chunk>
    <chunk id="11" doc_uid="ias-21" chunk_number="15" score="0.4876">B</chunk>
    """

    chunks = parser.parse(content)

    expected_chunk_count = 2
    if len(chunks) != expected_chunk_count:
        error_message = f"Expected {expected_chunk_count} chunks, got {len(chunks)}"
        raise AssertionError(error_message)

    first_chunk = chunks[0]
    second_chunk = chunks[1]

    if first_chunk != module.PromptChunkReference(
        chunk_db_id=10,
        doc_uid="ifrs-9",
        chunk_number="6.3.5",
        score=0.6123,
    ):
        error_message = f"Unexpected first parsed chunk: {first_chunk!r}"
        raise AssertionError(error_message)

    if second_chunk != module.PromptChunkReference(
        chunk_db_id=11,
        doc_uid="ias-21",
        chunk_number="15",
        score=0.4876,
    ):
        error_message = f"Unexpected second parsed chunk: {second_chunk!r}"
        raise AssertionError(error_message)


def test_matrix_builder_uses_only_observed_retrieved_sections() -> None:
    """Matrix columns should include only sections with at least one retrieved chunk."""
    module = _load_module()
    builder = module.MatrixBuilder()

    runs = [
        module.RunRecord(
            question_id="Q1.0",
            run_id="base",
            recommendation="oui",
            labels=("cash_flow_hedge", "foreign_currency_accounting"),
            prompt_chunks=(
                module.PromptChunkReference(
                    chunk_db_id=10,
                    doc_uid="ifrs-9",
                    chunk_number="6.3.5",
                    score=0.61,
                ),
                module.PromptChunkReference(
                    chunk_db_id=11,
                    doc_uid="ifrs-9",
                    chunk_number="6.3.6",
                    score=0.58,
                ),
                module.PromptChunkReference(
                    chunk_db_id=12,
                    doc_uid="ias-21",
                    chunk_number="15",
                    score=0.49,
                ),
                module.PromptChunkReference(
                    chunk_db_id=13,
                    doc_uid="ifric-16",
                    chunk_number="13",
                    score=0.0,
                ),
            ),
        ),
    ]

    chunk_lookup = {
        10: module.ChunkLookupRecord(
            chunk_db_id=10,
            doc_uid="ifrs-9",
            chunk_number="6.3.5",
            containing_section_id="std_ifrs9-sec-63",
        ),
        11: module.ChunkLookupRecord(
            chunk_db_id=11,
            doc_uid="ifrs-9",
            chunk_number="6.3.6",
            containing_section_id="std_ifrs9-sec-63",
        ),
        12: module.ChunkLookupRecord(
            chunk_db_id=12,
            doc_uid="ias-21",
            chunk_number="15",
            containing_section_id="std_ias21-sec-15",
        ),
        13: module.ChunkLookupRecord(
            chunk_db_id=13,
            doc_uid="ifric-16",
            chunk_number="13",
            containing_section_id="std_ifric16-sec-13",
        ),
    }

    section_lookup = {
        "std_ifrs9-sec-63": module.SectionDisplayRecord(
            doc_uid="ifrs-9",
            section_id="std_ifrs9-sec-63",
            title="Hedged items",
            section_lineage=("Hedge accounting", "Hedged items"),
            position=10,
        ),
        "std_ias21-sec-15": module.SectionDisplayRecord(
            doc_uid="ias-21",
            section_id="std_ias21-sec-15",
            title="Net investment",
            section_lineage=("Foreign operation", "Net investment"),
            position=20,
        ),
        "std_ifric16-sec-13": module.SectionDisplayRecord(
            doc_uid="ifric-16",
            section_id="std_ifric16-sec-13",
            title="Conclusions",
            section_lineage=("Application", "Conclusions"),
            position=30,
        ),
    }

    matrix = builder.build(
        runs=runs,
        chunk_lookup=chunk_lookup,
        section_lookup=section_lookup,
    )

    observed_section_keys = tuple(column.column_key for column in matrix.section_columns)
    expected_section_keys = (
        "ifrs9::std_ifrs9-sec-63",
        "ias21::std_ias21-sec-15",
        "ifric16::std_ifric16-sec-13",
    )
    if observed_section_keys != expected_section_keys:
        error_message = f"Unexpected observed section columns: {observed_section_keys!r}"
        raise AssertionError(error_message)

    row = matrix.rows[0]
    if row.spurious_labels != ("foreign_currency_accounting",):
        error_message = f"Unexpected spurious labels: {row.spurious_labels!r}"
        raise AssertionError(error_message)

    if row.section_cells["ifrs9::std_ifrs9-sec-63"].retrieved_display_text != "0.58-0.61":
        error_message = f"Expected IFRS 9 section score range 0.58-0.61, got {row.section_cells['ifrs9::std_ifrs9-sec-63'].retrieved_display_text!r}"
        raise AssertionError(error_message)

    if row.section_cells["ias21::std_ias21-sec-15"].retrieved_display_text != "0.49":
        error_message = f"Expected IAS 21 section score display 0.49, got {row.section_cells['ias21::std_ias21-sec-15'].retrieved_display_text!r}"
        raise AssertionError(error_message)

    if row.section_cells["ifric16::std_ifric16-sec-13"].visible_display_text != "0.00":
        error_message = f"Expected IFRIC 16 visible-context score display 0.00, got {row.section_cells['ifric16::std_ifric16-sec-13'].visible_display_text!r}"
        raise AssertionError(error_message)

    if row.section_cells["ifric16::std_ifric16-sec-13"].retrieved_display_text != "":
        error_message = f"Expected IFRIC 16 retrieved-only display to be blank, got {row.section_cells['ifric16::std_ifric16-sec-13'].retrieved_display_text!r}"
        raise AssertionError(error_message)


def test_html_renderer_includes_group_headers_and_tooltips() -> None:
    """Rendered HTML should expose grouped headers and detailed tooltips."""
    module = _load_module()
    renderer = module.HtmlMatrixRenderer()

    matrix = module.MatrixModel(
        experiment_name="exp-23",
        provider_name="provider-x",
        generated_at="2026-04-09T12:00:00",
        label_columns=(
            module.LabelColumn(label="cash_flow_hedge", is_core=True),
            module.LabelColumn(label="foreign_currency_accounting", is_core=False),
        ),
        section_columns=(
            module.SectionColumn(
                column_key="ifrs9::std_ifrs9-sec-63",
                canonical_doc_key="ifrs9",
                doc_display_name="IFRS 9",
                section_id="std_ifrs9-sec-63",
                title="Hedged items",
                section_lineage=("Hedge accounting", "Hedged items"),
                position=10,
            ),
        ),
        rows=(
            module.MatrixRow(
                question_id="Q1.0",
                run_id="base",
                recommendation="oui_sous_conditions",
                labels=("cash_flow_hedge", "foreign_currency_accounting"),
                spurious_labels=("foreign_currency_accounting",),
                label_presence={
                    "cash_flow_hedge": True,
                    "foreign_currency_accounting": True,
                },
                section_cells={
                    "ifrs9::std_ifrs9-sec-63": module.SectionCell(
                        retrieved_scores=(0.58, 0.61),
                        retrieved_display_text="0.58-0.61",
                        retrieved_max_score=0.61,
                        retrieved_chunk_numbers=("6.3.5", "6.3.6"),
                        visible_scores=(0.58, 0.61),
                        visible_display_text="0.58-0.61",
                        visible_max_score=0.61,
                        visible_chunk_numbers=("6.3.5", "6.3.6"),
                    )
                },
            ),
        ),
        doc_section_counts={"ifrs9": 1, "ias21": 0, "ifric16": 0},
    )

    html = renderer.render(matrix)

    expected_fragments = (
        "Spurious approaches vs retrieved sections matrix",
        "IFRS 9",
        "foreign_currency_accounting",
        "0.58-0.61",
        "ifrs9-sec-63",
        "Hedge accounting &gt; Hedged items",
        "6.3.5 (0.58)",
        "6.3.6 (0.61)",
        "oui_sc",
        "Q",
        "rec",
        "spur",
        "show-visible-context",
        "retrieved display: 0.58-0.61",
        "visible display: 0.58-0.61",
    )
    for fragment in expected_fragments:
        if fragment not in html:
            error_message = f"Expected HTML fragment not found: {fragment}"
            raise AssertionError(error_message)
