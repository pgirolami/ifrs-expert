"""Tests for the Q1 variant similarity table analysis script."""

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
    return _repo_root() / "experiments" / "analysis" / "run_q1_variant_similarity_table.py"


def _load_module() -> ModuleType:
    """Load the analysis script as a module."""
    spec = importlib.util.spec_from_file_location(
        "tests_run_q1_variant_similarity_table_module",
        _script_path(),
    )
    if spec is None or spec.loader is None:
        message = f"Could not load module spec for {_script_path()}"
        raise AssertionError(message)

    module = importlib.util.module_from_spec(spec)
    module.__name__ = "tests_run_q1_variant_similarity_table_module"
    sys.modules["tests_run_q1_variant_similarity_table_module"] = module
    spec.loader.exec_module(module)
    return module


def test_score_direction_arrow_reflects_change_direction() -> None:
    """The formatter should use arrows to show enrichment direction."""
    module = _load_module()

    if module.score_direction_arrow(0.5, 0.6) != "↗":
        message = "Expected higher right score to use the upward arrow"
        raise AssertionError(message)
    if module.score_direction_arrow(0.6, 0.5) != "↘":
        message = "Expected lower right score to use the downward arrow"
        raise AssertionError(message)
    if module.score_direction_arrow(0.5, 0.5) != "→":
        message = "Expected equal scores to use the neutral arrow"
        raise AssertionError(message)


def test_format_delta_change_uses_two_decimal_delta_and_integer_percentage() -> None:
    """Delta formatting should use two decimals and integer percent change."""
    module = _load_module()

    if module.format_delta_change(0.4799, 0.6173) != "(+0.14 = +28%)":
        message = "Unexpected positive delta format"
        raise AssertionError(message)
    if module.format_delta_change(0.63, 0.58) != "(-0.05 = -7%)":
        message = "Unexpected negative delta format"
        raise AssertionError(message)


def test_format_ranked_standards_stack_shows_raw_above_enriched_lists() -> None:
    """Ranked summaries should stack raw above enriched rankings."""
    module = _load_module()

    ranked_scores = (
        module.RankedStandardScore(standard_doc_uid="ifric16", raw_score=0.60, enriched_score=0.55),
        module.RankedStandardScore(standard_doc_uid="ias39", raw_score=0.50, enriched_score=0.70),
        module.RankedStandardScore(standard_doc_uid="ifrs19", raw_score=0.45, enriched_score=0.45),
    )

    stacked = module._format_ranked_standards_stack(ranked_scores)

    expected = "ifric16 (0.6000), ias39 (0.5000), ifrs19 (0.4500)<br>ias39 (0.7000), ifric16 (0.5500), ifrs19 (0.4500)"
    if stacked != expected:
        message = f"Unexpected stacked ranking format: {stacked}"
        raise AssertionError(message)


def test_format_doc_uid_cell_adds_wrapped_italicized_title_for_standard_rows() -> None:
    """Standard rows should show their title on wrapped italicized lines."""
    module = _load_module()

    standard_row = module.VariantRow(
        doc_uid="ifric16",
        document_type="IFRIC",
        preferred_representation="scope",
        scores_by_representation={"scope": module.RepresentationScores(raw=0.54, enriched=0.61)},
    )
    variant_row = module.VariantRow(
        doc_uid="ifric16-bc",
        document_type="IFRIC-BC",
        preferred_representation="scope",
        scores_by_representation={"scope": module.RepresentationScores(raw=0.50, enriched=0.45)},
    )
    titles_by_doc_uid = {
        "ifric16": "IFRS - IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
        "ifric16-bc": "IFRS - IFRIC 16 Hedges of a Net Investment in a Foreign Operation - Basis for Conclusions",
    }

    expected_standard_cell = "ifric16<br><em>IFRIC 16 Hedges of a Net<br>Investment in a Foreign<br>Operation</em>"
    if module.format_doc_uid_cell(standard_row, titles_by_doc_uid) != expected_standard_cell:
        message = "Unexpected standard doc_uid cell format"
        raise AssertionError(message)
    if module.format_doc_uid_cell(variant_row, titles_by_doc_uid) != "ifric16-bc":
        message = "Unexpected variant doc_uid cell format"
        raise AssertionError(message)


def test_format_representation_cell_highlights_left_winner_in_bold_cell() -> None:
    """The left score should be marked when enriched wins and the active representation is bold."""
    module = _load_module()

    row = module.VariantRow(
        doc_uid="ifric16",
        document_type="IFRIC",
        preferred_representation="scope",
        scores_by_representation={
            "scope": module.RepresentationScores(raw=0.54, enriched=0.61),
            "full": module.RepresentationScores(raw=0.50, enriched=0.45),
        },
    )
    family_winners = module.FamilyWinners(
        raw=None,
        enriched=module.ScoreLocation(
            row_index=0,
            doc_uid="ifric16",
            representation="scope",
            side="enriched",
            score=0.61,
        ),
    )

    active_cell = module.format_representation_cell(
        row=row,
        representation="scope",
        family_winners=family_winners,
    )
    inactive_cell = module.format_representation_cell(
        row=row,
        representation="full",
        family_winners=family_winners,
    )

    if "<span style=\"background-color:" not in active_cell:
        message = f"Expected heatmap styling in active cell: {active_cell}"
        raise AssertionError(message)
    if "<strong>0.5400 ↗ 0.6100✅</strong><br>(+0.07 = +12%)" not in active_cell:
        message = f"Unexpected active cell format: {active_cell}"
        raise AssertionError(message)
    if "0.5000 ↘ 0.4500" not in inactive_cell or "<br>(-0.05 = -10%)" not in inactive_cell:
        message = f"Unexpected inactive cell format: {inactive_cell}"
        raise AssertionError(message)


def test_format_representation_cell_highlights_right_winner_in_bold_cell() -> None:
    """The right score should be marked when raw wins and the active representation is bold."""
    module = _load_module()

    row = module.VariantRow(
        doc_uid="ias39",
        document_type="IAS-S",
        preferred_representation="toc",
        scores_by_representation={
            "toc": module.RepresentationScores(raw=0.63, enriched=0.58),
        },
    )
    family_winners = module.FamilyWinners(
        raw=module.ScoreLocation(
            row_index=0,
            doc_uid="ias39",
            representation="toc",
            side="raw",
            score=0.63,
        ),
        enriched=None,
    )

    cell = module.format_representation_cell(
        row=row,
        representation="toc",
        family_winners=family_winners,
    )

    if "<span style=\"background-color:" not in cell:
        message = f"Expected heatmap styling in winner cell: {cell}"
        raise AssertionError(message)
    if "<strong>0.6300✅ ↘ 0.5800</strong><br>(-0.05 = -7%)" not in cell:
        message = f"Unexpected winner cell format: {cell}"
        raise AssertionError(message)


def test_format_representation_cell_marks_missing_preferred_representation() -> None:
    """Rows that fall back from the preferred representation should be easy to spot."""
    module = _load_module()

    row = module.VariantRow(
        doc_uid="ifric7",
        document_type="IFRIC",
        preferred_representation="scope",
        scores_by_representation={
            "full": module.RepresentationScores(raw=0.50, enriched=0.45),
        },
    )

    preferred_cell = module.format_representation_cell(
        row=row,
        representation="scope",
        family_winners=None,
    )
    fallback_cell = module.format_representation_cell(
        row=row,
        representation="full",
        family_winners=None,
    )

    if preferred_cell != "**❌**":
        message = f"Unexpected missing preferred cell format: {preferred_cell}"
        raise AssertionError(message)
    if "<span style=\"background-color:" not in fallback_cell:
        message = f"Expected heatmap styling in non-preferred cell: {fallback_cell}"
        raise AssertionError(message)
    if "0.5000 ↘ 0.4500" not in fallback_cell or "<br>(-0.05 = -10%)" not in fallback_cell:
        message = f"Unexpected non-preferred cell format: {fallback_cell}"
        raise AssertionError(message)


def test_format_heatmap_style_uses_distinct_green_and_red_tints() -> None:
    """Heatmap colors should clearly distinguish positive and negative changes."""
    module = _load_module()

    positive_style = module.format_heatmap_style(0.50, 0.55)
    negative_style = module.format_heatmap_style(0.55, 0.50)

    if "rgb(194, 242, 194)" not in positive_style:
        message = f"Unexpected positive heatmap color: {positive_style}"
        raise AssertionError(message)
    if "rgb(242, 199, 199)" not in negative_style:
        message = f"Unexpected negative heatmap color: {negative_style}"
        raise AssertionError(message)


def test_build_top_standard_scores_for_representation_supports_toc_only_rankings() -> None:
    """TOC-only rankings should be computed separately for documents2 and standard-only rows."""
    module = _load_module()

    rows = (
        module.VariantRow(
            doc_uid="ifric16",
            document_type="IFRIC",
            preferred_representation="scope",
            scores_by_representation={"toc": module.RepresentationScores(raw=0.50, enriched=0.60)},
        ),
        module.VariantRow(
            doc_uid="ifric16-bc",
            document_type="IFRIC-BC",
            preferred_representation="scope",
            scores_by_representation={"toc": module.RepresentationScores(raw=0.70, enriched=0.75)},
        ),
        module.VariantRow(
            doc_uid="ifrs19",
            document_type="IFRS-S",
            preferred_representation="toc",
            scores_by_representation={"toc": module.RepresentationScores(raw=0.65, enriched=0.66)},
        ),
    )

    documents2_ranked = module.build_top_standard_scores_for_representation(
        rows,
        representation="toc",
        standard_only=False,
    )
    standard_only_ranked = module.build_top_standard_scores_for_representation(
        rows,
        representation="toc",
        standard_only=True,
    )

    if [score.standard_doc_uid for score in documents2_ranked] != ["ifric16", "ifrs19"]:
        message = f"Unexpected TOC documents2 ranking: {documents2_ranked}"
        raise AssertionError(message)
    if [score.standard_doc_uid for score in standard_only_ranked] != ["ifrs19", "ifric16"]:
        message = f"Unexpected TOC standard-only ranking: {standard_only_ranked}"
        raise AssertionError(message)


def test_ranking_change_summary_uses_family_best_raw_and_enriched_scores() -> None:
    """Ranking summaries should use the family best raw/enriched pair from the table rows."""
    module = _load_module()

    section = module.QuestionSection(
        question=module.QuestionCase(question_id="Q1.18", question_text="Question text", source_path=Path("Q1.18.txt")),
        raw_query_text="Question text",
        enriched_query_text="Question text",
        standard_doc_uids=(),
        rows=(
            module.VariantRow(
                doc_uid="ifrs39",
                document_type="IFRS-S",
                preferred_representation="toc",
                scores_by_representation={"toc": module.RepresentationScores(raw=0.4736, enriched=0.6004)},
            ),
            module.VariantRow(
                doc_uid="ifrs39-bc",
                document_type="IFRS-BC",
                preferred_representation="toc",
                scores_by_representation={"toc": module.RepresentationScores(raw=0.5214, enriched=0.4512)},
            ),
            module.VariantRow(
                doc_uid="ifrs17",
                document_type="IFRS-S",
                preferred_representation="full",
                scores_by_representation={"full": module.RepresentationScores(raw=0.6048, enriched=0.6018)},
            ),
            module.VariantRow(
                doc_uid="ifrs17-bc",
                document_type="IFRS-BC",
                preferred_representation="full",
                scores_by_representation={"full": module.RepresentationScores(raw=0.6121, enriched=0.5859)},
            ),
            module.VariantRow(
                doc_uid="ifric16",
                document_type="IFRIC",
                preferred_representation="full",
                scores_by_representation={"full": module.RepresentationScores(raw=0.50, enriched=0.60)},
            ),
        ),
        winners_by_standard_doc_uid={},
        document_titles_by_doc_uid={},
        documents2_top_standards=(),
        std_only_top_standards=(),
        toc_documents2_top_standards=(),
        toc_std_only_top_standards=(),
    )

    summary = module.Q1VariantSimilarityTableExperiment._build_ranking_change_summary(
        module.Q1VariantSimilarityTableExperiment.__new__(module.Q1VariantSimilarityTableExperiment),
        section,
    )

    rendered = "\n".join(summary)
    expected_snippets = (
        "ifrs39 (+0.08 = +15%)",
        "ifrs17 (-0.01 = -1%)",
    )
    for snippet in expected_snippets:
        if snippet not in rendered:
            message = f"Unexpected ranking summary: {rendered}"
            raise AssertionError(message)


def test_build_question_section_lines_includes_compact_ranking_table() -> None:
    """The rendered section should include the compact ranking-comparison table."""
    module = _load_module()

    section = module.QuestionSection(
        question=module.QuestionCase(question_id="Q1.1", question_text="Question text", source_path=Path("Q1.1.txt")),
        raw_query_text="Question text",
        enriched_query_text="Question text",
        standard_doc_uids=(),
        rows=(),
        winners_by_standard_doc_uid={},
        document_titles_by_doc_uid={},
        documents2_top_standards=(),
        std_only_top_standards=(),
        toc_documents2_top_standards=(),
        toc_std_only_top_standards=(),
    )

    lines = module.Q1VariantSimilarityTableExperiment._build_question_section_lines(
        module.Q1VariantSimilarityTableExperiment.__new__(module.Q1VariantSimilarityTableExperiment),
        section,
    )

    rendered = "\n".join(lines)
    expected_snippets = (
        "Variant table change summary",
        "Ranked documents by ranking basis",
        "| ranking basis | documents2 (raw / enriched) | std only (raw / enriched) |",
    )
    for snippet in expected_snippets:
        if snippet not in rendered:
            message = f"Missing ranking-table snippet: {snippet}"
            raise AssertionError(message)
