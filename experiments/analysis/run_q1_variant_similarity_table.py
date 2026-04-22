"""Build a variant-level document similarity table for selected Q1 variants.

For each requested question variant, this script:
- loads the French question text
- builds both raw and enriched query texts
- queries each document-level representation index (`full`, `background_and_issue`, `scope`, `toc`)
- consolidates top hits to standard doc_uids to identify candidate standards
- expands those standards back to their available support-material variants
- writes a markdown artifact with one table per question

Usage:
    uv run python experiments/analysis/run_q1_variant_similarity_table.py
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
import math
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import yaml

from src.db.documents import DocumentStore
from src.models.document import infer_exact_document_type, resolve_standard_doc_uid
from src.policy import (
    SIMILARITY_REPRESENTATIONS,
    DocumentSimilarityRepresentation,
    load_policy_config,
)
from src.retrieval.query_embedding import GlossaryEntry, GlossarySourceProtocol, build_query_embedding_text
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path

logger = logging.getLogger(__name__)

DEFAULT_OUTPUT_FILENAME = "variant_similarity_table.md"
DEFAULT_QUESTION_DIR = "experiments/00_QUESTIONS/Q1"
DEFAULT_GLOSSARY_PATH = "config/en-fr-glossary_all.yaml"
DEFAULT_POLICY_PATH = "config/policy.default.yaml"
DEFAULT_TOP_PER_REPRESENTATION = 12
DEFAULT_QUESTION_IDS: tuple[str, ...] = ("Q1.1", "Q1.6", "Q1.9", "Q1.11", "Q1.14", "Q1.18")
VARIANT_TYPE_ORDER: tuple[str, ...] = (
    "IFRS-S",
    "IAS-S",
    "IFRIC",
    "SIC",
    "PS",
    "IFRS-BC",
    "IAS-BC",
    "IAS-BCIASC",
    "IFRIC-BC",
    "SIC-BC",
    "PS-BC",
    "IFRS-IE",
    "IAS-IE",
    "IFRIC-IE",
    "SIC-IE",
    "IFRS-IG",
    "IAS-IG",
    "IFRIC-IG",
    "IAS-SM",
)
ScoreSide = Literal["raw", "enriched"]
STANDARD_ROW_DOCUMENT_TYPES: tuple[str, ...] = ("IFRS-S", "IAS-S", "IFRIC", "SIC", "PS")


@dataclass(frozen=True)
class ExperimentConfig:
    """Configuration for one similarity-table run."""

    repo_root: Path
    question_dir: Path
    question_ids: tuple[str, ...]
    glossary_path: Path
    policy_path: Path
    output_path: Path
    top_per_representation: int


@dataclass(frozen=True)
class QuestionCase:
    """One selected Q1 question variant."""

    question_id: str
    question_text: str
    source_path: Path


@dataclass(frozen=True)
class RepresentationScores:
    """Scores for one document across raw and enriched queries."""

    raw: float
    enriched: float


@dataclass(frozen=True)
class VariantRow:
    """One row in the variant similarity table."""

    doc_uid: str
    document_type: str
    preferred_representation: DocumentSimilarityRepresentation
    scores_by_representation: dict[DocumentSimilarityRepresentation, RepresentationScores]


@dataclass(frozen=True)
class ScoreLocation:
    """A single score location within the table."""

    row_index: int
    doc_uid: str
    representation: DocumentSimilarityRepresentation
    side: ScoreSide
    score: float


@dataclass(frozen=True)
class FamilyWinners:
    """The raw and enriched winners for one standards family."""

    raw: ScoreLocation | None
    enriched: ScoreLocation | None


@dataclass(frozen=True)
class RankedStandardScore:
    """One ranked standard score for the section summary bullets."""

    standard_doc_uid: str
    raw_score: float
    enriched_score: float


@dataclass(frozen=True)
class QuestionSection:
    """All data needed to render one question section."""

    question: QuestionCase
    raw_query_text: str
    enriched_query_text: str
    standard_doc_uids: tuple[str, ...]
    rows: tuple[VariantRow, ...]
    winners_by_standard_doc_uid: dict[str, FamilyWinners]
    document_titles_by_doc_uid: dict[str, str]
    documents2_top_standards: tuple[RankedStandardScore, ...]
    std_only_top_standards: tuple[RankedStandardScore, ...]
    toc_documents2_top_standards: tuple[RankedStandardScore, ...]
    toc_std_only_top_standards: tuple[RankedStandardScore, ...]


class YamlGlossarySource(GlossarySourceProtocol):
    """Load glossary entries from a specific YAML path."""

    def __init__(self, glossary_path: Path) -> None:
        """Initialize the glossary source."""
        self._glossary_path = glossary_path

    def load_entries(self) -> tuple[GlossaryEntry, ...]:
        """Load glossary entries from the configured YAML file."""
        if not self._glossary_path.exists():
            message = f"Glossary file not found: {self._glossary_path}"
            raise FileNotFoundError(message)

        raw_data = yaml.safe_load(self._glossary_path.read_text(encoding="utf-8"))
        if not isinstance(raw_data, dict):
            message = f"Glossary file must contain a mapping: {self._glossary_path}"
            raise TypeError(message)

        raw_entries = raw_data.get("question_glossary")
        if not isinstance(raw_entries, list):
            message = f"Glossary file must contain a question_glossary list: {self._glossary_path}"
            raise TypeError(message)

        entries: list[GlossaryEntry] = []
        for raw_entry in raw_entries:
            if not isinstance(raw_entry, dict):
                continue
            fr_value = raw_entry.get("fr")
            en_values = raw_entry.get("en")
            if not isinstance(fr_value, str) or not isinstance(en_values, list):
                continue
            english_terms = tuple(term.strip() for term in en_values if isinstance(term, str) and term.strip())
            french_term = fr_value.strip()
            if not french_term or not english_terms:
                continue
            entries.append(GlossaryEntry(fr=french_term, en=english_terms))
        return tuple(entries)


class Q1VariantSimilarityTableExperiment:
    """Build a variant-level similarity table for selected Q1 questions."""

    def __init__(self, config: ExperimentConfig) -> None:
        """Initialize the experiment from a single configuration object."""
        self._repo_root = config.repo_root
        self._question_dir = config.question_dir
        self._question_ids = config.question_ids
        self._glossary_path = config.glossary_path
        self._policy_path = config.policy_path
        self._output_path = config.output_path
        self._top_per_representation = config.top_per_representation
        self._glossary_source = YamlGlossarySource(config.glossary_path)
        self._available_doc_uids = self._load_available_doc_uids()
        self._document_titles_by_doc_uid = self._load_document_titles()
        self._policy_similarity_representation_by_document_type = self._load_policy_similarity_representations()

    def run(self) -> str:
        """Run the analysis and write the markdown artifact."""
        sections = [self._build_question_section(question_id) for question_id in self._question_ids]
        markdown = self._build_markdown(sections)
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        self._output_path.write_text(markdown, encoding="utf-8")
        logger.info(f"Wrote variant similarity table to {self._output_path}")
        return markdown

    def _load_policy_similarity_representations(self) -> dict[str, DocumentSimilarityRepresentation]:
        """Load the document-type to similarity-representation mapping from policy YAML."""
        policy_config = load_policy_config(self._policy_path)
        return {
            document_type: policy.similarity_representation
            for document_type, policy in policy_config.retrieval.documents.by_document_type.items()
        }

    def _build_question_section(self, question_id: str) -> QuestionSection:
        question = self._load_question(question_id)
        raw_query_text = question.question_text
        enriched_query_text = build_query_embedding_text(
            question.question_text,
            glossary_source=self._glossary_source,
        ).embedding_text
        raw_scores_by_representation = self._search_all_representations(raw_query_text)
        enriched_scores_by_representation = self._search_all_representations(enriched_query_text)
        candidate_standard_doc_uids = self._select_candidate_standard_doc_uids(enriched_scores_by_representation)
        rows = self._build_rows(candidate_standard_doc_uids, raw_scores_by_representation, enriched_scores_by_representation)
        winners_by_standard_doc_uid = self._select_family_winners(rows, candidate_standard_doc_uids)
        documents2_top_standards = self._build_documents2_top_standards(rows)
        std_only_top_standards = self._build_std_only_top_standards(rows)
        toc_documents2_top_standards = self._build_toc_documents2_top_standards(rows)
        toc_std_only_top_standards = self._build_toc_std_only_top_standards(rows)
        return QuestionSection(
            question=question,
            raw_query_text=raw_query_text,
            enriched_query_text=enriched_query_text,
            standard_doc_uids=candidate_standard_doc_uids,
            rows=rows,
            winners_by_standard_doc_uid=winners_by_standard_doc_uid,
            document_titles_by_doc_uid=self._document_titles_by_doc_uid,
            documents2_top_standards=documents2_top_standards,
            std_only_top_standards=std_only_top_standards,
            toc_documents2_top_standards=toc_documents2_top_standards,
            toc_std_only_top_standards=toc_std_only_top_standards,
        )

    def _load_question(self, question_id: str) -> QuestionCase:
        question_path = self._question_dir / f"{question_id}.txt"
        if not question_path.exists():
            message = f"Question file not found: {question_path}"
            raise FileNotFoundError(message)
        question_text = question_path.read_text(encoding="utf-8").strip()
        if not question_text:
            message = f"Question file is empty: {question_path}"
            raise ValueError(message)
        return QuestionCase(question_id=question_id, question_text=question_text, source_path=question_path)

    def _search_all_representations(
        self,
        query_text: str,
    ) -> dict[DocumentSimilarityRepresentation, dict[str, float]]:
        scores_by_representation: dict[DocumentSimilarityRepresentation, dict[str, float]] = {}
        for representation in SIMILARITY_REPRESENTATIONS:
            vector_store = DocumentVectorStore(
                index_path=get_document_index_path(representation),
                id_map_path=get_document_id_map_path(representation),
            )
            with vector_store as active_vector_store:
                ranked_results = active_vector_store.search_all(query_text)
            scores_by_representation[representation] = {
                str(result["doc_uid"]): float(result["score"])
                for result in ranked_results
                if isinstance(result.get("doc_uid"), str)
            }
        return scores_by_representation

    def _select_candidate_standard_doc_uids(
        self,
        scores_by_representation: dict[DocumentSimilarityRepresentation, dict[str, float]],
    ) -> tuple[str, ...]:
        best_score_by_standard_doc_uid: dict[str, float] = {}
        for representation in SIMILARITY_REPRESENTATIONS:
            representation_scores = scores_by_representation[representation]
            ranked_doc_uids = sorted(
                representation_scores,
                key=lambda doc_uid: representation_scores[doc_uid],
                reverse=True,
            )
            selected_doc_uids = ranked_doc_uids[: self._top_per_representation]
            for doc_uid in selected_doc_uids:
                document_type = infer_exact_document_type(doc_uid)
                if document_type is None or document_type == "NAVIS":
                    continue
                standard_doc_uid = resolve_standard_doc_uid(doc_uid)
                if standard_doc_uid is None:
                    continue
                score = representation_scores[doc_uid]
                existing_score = best_score_by_standard_doc_uid.get(standard_doc_uid)
                if existing_score is None or score > existing_score:
                    best_score_by_standard_doc_uid[standard_doc_uid] = score

        ordered_standard_doc_uids = sorted(
            best_score_by_standard_doc_uid,
            key=lambda doc_uid: (-best_score_by_standard_doc_uid[doc_uid], doc_uid),
        )
        return tuple(ordered_standard_doc_uids)

    def _build_rows(
        self,
        standard_doc_uids: tuple[str, ...],
        raw_scores_by_representation: dict[DocumentSimilarityRepresentation, dict[str, float]],
        enriched_scores_by_representation: dict[DocumentSimilarityRepresentation, dict[str, float]],
    ) -> tuple[VariantRow, ...]:
        rows: list[VariantRow] = []
        for standard_doc_uid in standard_doc_uids:
            variant_doc_uids = [
                doc_uid
                for doc_uid in self._available_doc_uids
                if resolve_standard_doc_uid(doc_uid) == standard_doc_uid
            ]
            variant_doc_uids.sort(key=self._variant_sort_key)
            for doc_uid in variant_doc_uids:
                document_type = infer_exact_document_type(doc_uid)
                if document_type is None:
                    continue
                row_scores_by_representation: dict[DocumentSimilarityRepresentation, RepresentationScores] = {}
                for representation in SIMILARITY_REPRESENTATIONS:
                    raw_score = raw_scores_by_representation[representation].get(doc_uid)
                    enriched_score = enriched_scores_by_representation[representation].get(doc_uid)
                    if raw_score is None or enriched_score is None:
                        continue
                    row_scores_by_representation[representation] = RepresentationScores(raw=raw_score, enriched=enriched_score)
                if not row_scores_by_representation:
                    continue
                preferred_representation = self._policy_similarity_representation_by_document_type[document_type]
                rows.append(
                    VariantRow(
                        doc_uid=doc_uid,
                        document_type=document_type,
                        preferred_representation=preferred_representation,
                        scores_by_representation=row_scores_by_representation,
                    )
                )
        return tuple(rows)

    def _select_family_winners(
        self,
        rows: tuple[VariantRow, ...],
        standard_doc_uids: tuple[str, ...],
    ) -> dict[str, FamilyWinners]:
        winners: dict[str, FamilyWinners] = {}
        rows_by_standard_doc_uid = self._group_rows_by_standard_doc_uid(rows)
        for standard_doc_uid in standard_doc_uids:
            family_rows = rows_by_standard_doc_uid.get(standard_doc_uid, ())
            winners[standard_doc_uid] = FamilyWinners(
                raw=self._select_family_winner_for_rows(family_rows, side="raw"),
                enriched=self._select_family_winner_for_rows(family_rows, side="enriched"),
            )
        return winners

    def _group_rows_by_standard_doc_uid(self, rows: tuple[VariantRow, ...]) -> dict[str, tuple[VariantRow, ...]]:
        grouped_rows: dict[str, list[VariantRow]] = {}
        for row in rows:
            standard_doc_uid = resolve_standard_doc_uid(row.doc_uid)
            if standard_doc_uid is None:
                continue
            grouped_rows.setdefault(standard_doc_uid, []).append(row)
        return {standard_doc_uid: tuple(group_rows) for standard_doc_uid, group_rows in grouped_rows.items()}

    def _select_family_winner_for_rows(
        self,
        rows: tuple[VariantRow, ...],
        side: ScoreSide,
    ) -> ScoreLocation | None:
        winner: ScoreLocation | None = None
        for row_index, row in enumerate(rows):
            scores = row.scores_by_representation.get(row.preferred_representation)
            if scores is None:
                continue
            score = scores.raw if side == "raw" else scores.enriched
            candidate = ScoreLocation(
                row_index=row_index,
                doc_uid=row.doc_uid,
                representation=row.preferred_representation,
                side=side,
                score=score,
            )
            if winner is None or is_better_score_location(candidate, winner):
                winner = candidate
        return winner

    def _build_documents2_top_standards(self, rows: tuple[VariantRow, ...]) -> tuple[RankedStandardScore, ...]:
        """Rank standards using all rows, like documents2 consolidation."""
        return self._build_top_standard_scores(rows)

    def _build_std_only_top_standards(self, rows: tuple[VariantRow, ...]) -> tuple[RankedStandardScore, ...]:
        """Rank standards using only standard rows."""
        standard_rows = tuple(row for row in rows if row.document_type in STANDARD_ROW_DOCUMENT_TYPES)
        return self._build_top_standard_scores(standard_rows)

    def _build_toc_documents2_top_standards(self, rows: tuple[VariantRow, ...]) -> tuple[RankedStandardScore, ...]:
        """Rank standards using TOC scores across all rows."""
        return build_top_standard_scores_for_representation(rows, representation="toc", standard_only=False)

    def _build_toc_std_only_top_standards(self, rows: tuple[VariantRow, ...]) -> tuple[RankedStandardScore, ...]:
        """Rank standards using TOC scores from standard rows only."""
        return build_top_standard_scores_for_representation(rows, representation="toc", standard_only=True)

    def _build_top_standard_scores(self, rows: tuple[VariantRow, ...]) -> tuple[RankedStandardScore, ...]:
        best_by_standard_doc_uid: dict[str, RankedStandardScore] = {}
        for row in rows:
            standard_doc_uid = resolve_standard_doc_uid(row.doc_uid)
            if standard_doc_uid is None:
                continue
            scores = row.scores_by_representation.get(row.preferred_representation)
            if scores is None:
                continue
            candidate = RankedStandardScore(
                standard_doc_uid=standard_doc_uid,
                raw_score=scores.raw,
                enriched_score=scores.enriched,
            )
            existing_score = best_by_standard_doc_uid.get(standard_doc_uid)
            if existing_score is None or self._is_better_ranked_standard_score(candidate, existing_score):
                best_by_standard_doc_uid[standard_doc_uid] = candidate
        ranked_scores = sorted(
            best_by_standard_doc_uid.values(),
            key=lambda ranked_score: (-ranked_score.enriched_score, -ranked_score.raw_score, ranked_score.standard_doc_uid),
        )
        return tuple(ranked_scores[:5])

    def _is_better_ranked_standard_score(self, candidate: RankedStandardScore, current: RankedStandardScore) -> bool:
        """Return whether a ranked standard score should replace the current best."""
        if candidate.enriched_score != current.enriched_score:
            return candidate.enriched_score > current.enriched_score
        if candidate.raw_score != current.raw_score:
            return candidate.raw_score > current.raw_score
        return candidate.standard_doc_uid < current.standard_doc_uid

    def _variant_sort_key(self, doc_uid: str) -> tuple[int, str]:
        document_type = infer_exact_document_type(doc_uid)
        if document_type is None:
            return (len(VARIANT_TYPE_ORDER), doc_uid)
        try:
            type_rank = VARIANT_TYPE_ORDER.index(document_type)
        except ValueError:
            type_rank = len(VARIANT_TYPE_ORDER)
        return (type_rank, doc_uid)

    def _load_available_doc_uids(self) -> tuple[str, ...]:
        available_doc_uids: set[str] = set()
        for representation in SIMILARITY_REPRESENTATIONS:
            id_map_path = get_document_id_map_path(representation)
            raw_id_map = json.loads(id_map_path.read_text(encoding="utf-8"))
            if not isinstance(raw_id_map, dict):
                message = f"Document id-map must contain a mapping: {id_map_path}"
                raise TypeError(message)
            for raw_doc_uid in raw_id_map.values():
                if isinstance(raw_doc_uid, str):
                    available_doc_uids.add(raw_doc_uid)
        return tuple(sorted(available_doc_uids))

    def _load_document_titles(self) -> dict[str, str]:
        document_titles_by_doc_uid: dict[str, str] = {}
        with DocumentStore() as document_store:
            for doc_uid in self._available_doc_uids:
                document = document_store.get_document(doc_uid)
                if document is None:
                    continue
                title = document.source_title.strip()
                if title:
                    document_titles_by_doc_uid[doc_uid] = title
        return document_titles_by_doc_uid

    def _build_markdown(self, sections: list[QuestionSection]) -> str:
        lines = [
            "<!-- Generated by experiments/analysis/run_q1_variant_similarity_table.py -->",
            "# Similarity scores for IFRIC / IFRS / IAS variants",
            "",
            "Computed from the FAISS document indices using the configured `BAAI/bge-m3` embedding model.",
            "Each cell shows `raw ↗ enriched`, or `raw ↘ enriched` when the enriched score is lower.",
            "The preferred representation cell is bold when it matches the configured `similarity_representation` for the document type.",
            "The preferred representation cell shows `❌` when that score is missing for the row.",
            "The `✅` marks the top score for that standard family among the bold cells shown for its variants.",
            "",
        ]
        for section in sections:
            lines.extend(self._build_question_section_lines(section))
        return "\n".join(lines) + "\n"

    def _build_ranking_comparison_rows(
        self,
        section: QuestionSection,
    ) -> tuple[tuple[str, tuple[RankedStandardScore, ...], tuple[RankedStandardScore, ...]], ...]:
        """Build the ranking-comparison rows for the stacked summary table."""
        return (
            (
                "policy in policy file",
                section.documents2_top_standards,
                section.std_only_top_standards,
            ),
            (
                "TOC only",
                section.toc_documents2_top_standards,
                section.toc_std_only_top_standards,
            ),
            (
                "scope only",
                build_top_standard_scores_for_representation(section.rows, representation="scope", standard_only=False),
                build_top_standard_scores_for_representation(section.rows, representation="scope", standard_only=True),
            ),
            (
                "background_and_issue only",
                build_top_standard_scores_for_representation(
                    section.rows,
                    representation="background_and_issue",
                    standard_only=False,
                ),
                build_top_standard_scores_for_representation(
                    section.rows,
                    representation="background_and_issue",
                    standard_only=True,
                ),
            ),
            (
                "full only",
                build_top_standard_scores_for_representation(section.rows, representation="full", standard_only=False),
                build_top_standard_scores_for_representation(section.rows, representation="full", standard_only=True),
            ),
        )

    def _build_ranking_change_summary(self, section: QuestionSection) -> list[str]:
        """Build the top increase/decrease summaries from the detailed table rows."""
        increase_changes, decrease_changes = self._collect_table_change_groups(section.rows)
        if not increase_changes and not decrease_changes:
            return ["- **Top 5 increases:** (none)", "- **Top 5 decreases:** (none)"]

        return [
            f"- **Top 5 increases:** {self._format_ranking_change_list(self._top_ranking_changes(increase_changes, descending=True))}",
            f"- **Top 5 decreases:** {self._format_ranking_change_list(self._top_ranking_changes(decrease_changes, descending=False))}",
        ]

    def _collect_table_change_groups(
        self,
        rows: tuple[VariantRow, ...],
    ) -> tuple[list[tuple[str, float, float]], list[tuple[str, float, float]]]:
        """Collect family-level best raw/enriched changes from the main table rows."""
        best_scores_by_family: dict[str, tuple[float, float]] = {}
        for row in rows:
            scores = row.scores_by_representation.get(row.preferred_representation)
            if scores is None:
                continue
            family_doc_uid = resolve_standard_doc_uid(row.doc_uid) or row.doc_uid
            current_best_raw, current_best_enriched = best_scores_by_family.get(family_doc_uid, (float("-inf"), float("-inf")))
            if scores.raw > current_best_raw:
                current_best_raw = scores.raw
            if scores.enriched > current_best_enriched:
                current_best_enriched = scores.enriched
            best_scores_by_family[family_doc_uid] = (current_best_raw, current_best_enriched)

        positive_changes: list[tuple[str, float, float]] = []
        negative_changes: list[tuple[str, float, float]] = []
        for family_doc_uid, (best_raw, best_enriched) in best_scores_by_family.items():
            display_percentage_change = _display_percentage_change(best_raw, best_enriched)
            if display_percentage_change > 0:
                positive_changes.append((family_doc_uid, best_raw, best_enriched))
            elif display_percentage_change < 0:
                negative_changes.append((family_doc_uid, best_raw, best_enriched))
        return positive_changes, negative_changes

    def _top_ranking_changes(
        self,
        changes: list[tuple[str, float, float]],
        *,
        descending: bool,
    ) -> list[tuple[str, float, float]]:
        """Return the strongest ranking changes for one representation."""
        if descending:
            sorted_changes = sorted(
                changes,
                key=lambda item: (-calculate_percentage_change(item[1], item[2]), -item[2], item[0]),
            )
        else:
            sorted_changes = sorted(
                changes,
                key=lambda item: (calculate_percentage_change(item[1], item[2]), item[1], item[0]),
            )
        return sorted_changes[:5]

    def _format_ranking_change_list(self, changes: list[tuple[str, float, float]]) -> str:
        """Format a compact comma-separated list of ranking changes."""
        if not changes:
            return "(none)"
        formatted_changes = []
        for doc_uid, raw_score, enriched_score in changes:
            delta_text = format_delta_change(raw_score, enriched_score)
            formatted_changes.append(f"{doc_uid} {delta_text}")
        return ", ".join(formatted_changes)

    def _build_question_section_lines(self, section: QuestionSection) -> list[str]:
        ranking_comparison_rows = self._build_ranking_comparison_rows(section)
        ranking_change_summary = self._build_ranking_change_summary(section)
        lines = [
            f"## {section.question.question_id}",
            "",
            "Question:",
            "",
            f"> {section.question.question_text}",
            "",
            "Raw query text:",
            "",
            "```text",
            section.raw_query_text,
            "```",
            "",
            "Enriched query text:",
            "",
            "```text",
            section.enriched_query_text,
            "```",
            "",
            "Variant table change summary",
            "",
        ]
        lines.extend(ranking_change_summary)
        lines.extend([
            "",
            "Ranked documents by ranking basis",
            "",
            "| ranking basis | documents2 (raw / enriched) | std only (raw / enriched) |",
            "| --- | --- | --- |",
        ])
        for row_label, documents2_scores, std_only_scores in ranking_comparison_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        row_label,
                        _format_ranked_standards_stack(documents2_scores),
                        _format_ranked_standards_stack(std_only_scores),
                    ]
                )
                + " |"
            )
        lines.extend([
            "",
            "| doc_uid | document_type | full | background_and_issue | scope | toc |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ])
        for row in section.rows:
            standard_doc_uid = resolve_standard_doc_uid(row.doc_uid)
            family_winners = section.winners_by_standard_doc_uid.get(standard_doc_uid or "")
            lines.append(
                "| "
                + " | ".join(
                    [
                        format_doc_uid_cell(row=row, document_titles_by_doc_uid=section.document_titles_by_doc_uid),
                        row.document_type,
                        format_representation_cell(
                            row=row,
                            representation="full",
                            family_winners=family_winners,
                        ),
                        format_representation_cell(
                            row=row,
                            representation="background_and_issue",
                            family_winners=family_winners,
                        ),
                        format_representation_cell(
                            row=row,
                            representation="scope",
                            family_winners=family_winners,
                        ),
                        format_representation_cell(
                            row=row,
                            representation="toc",
                            family_winners=family_winners,
                        ),
                    ]
                )
                + " |"
            )
        lines.append("")
        return lines


def _format_ranked_standards_bullet(
    label: str,
    ranked_scores: tuple[RankedStandardScore, ...],
) -> str:
    """Format one ranked-standard bullet line for a question section."""
    if not ranked_scores:
        return f"- **{label}:** (none)"
    raw_ranked_scores = sorted(
        ranked_scores,
        key=lambda ranked_score: (-ranked_score.raw_score, -ranked_score.enriched_score, ranked_score.standard_doc_uid),
    )[:5]
    enriched_ranked_scores = sorted(
        ranked_scores,
        key=lambda ranked_score: (-ranked_score.enriched_score, -ranked_score.raw_score, ranked_score.standard_doc_uid),
    )[:5]
    raw_text = ", ".join(f"{ranked_score.standard_doc_uid} ({ranked_score.raw_score:.4f})" for ranked_score in raw_ranked_scores)
    enriched_text = ", ".join(
        f"{ranked_score.standard_doc_uid} ({ranked_score.enriched_score:.4f})" for ranked_score in enriched_ranked_scores
    )
    return f"- **{label}:** {raw_text} -> {enriched_text}"


def _format_ranked_standards_stack(ranked_scores: tuple[RankedStandardScore, ...]) -> str:
    """Format a compact stacked raw/enriched ranking cell."""
    if not ranked_scores:
        return "(none)"
    raw_ranked_scores = sorted(
        ranked_scores,
        key=lambda ranked_score: (-ranked_score.raw_score, -ranked_score.enriched_score, ranked_score.standard_doc_uid),
    )[:5]
    enriched_ranked_scores = sorted(
        ranked_scores,
        key=lambda ranked_score: (-ranked_score.enriched_score, -ranked_score.raw_score, ranked_score.standard_doc_uid),
    )[:5]
    raw_text = ", ".join(f"{ranked_score.standard_doc_uid} ({ranked_score.raw_score:.4f})" for ranked_score in raw_ranked_scores)
    enriched_text = ", ".join(
        f"{ranked_score.standard_doc_uid} ({ranked_score.enriched_score:.4f})" for ranked_score in enriched_ranked_scores
    )
    return f"{raw_text}<br>{enriched_text}"


def build_top_standard_scores_for_representation(
    rows: tuple[VariantRow, ...],
    *,
    representation: DocumentSimilarityRepresentation,
    standard_only: bool,
) -> tuple[RankedStandardScore, ...]:
    """Rank standards by one representation, optionally using standard rows only."""
    relevant_rows = tuple(row for row in rows if row.document_type in STANDARD_ROW_DOCUMENT_TYPES) if standard_only else rows
    best_by_standard_doc_uid: dict[str, RankedStandardScore] = {}
    for row in relevant_rows:
        standard_doc_uid = resolve_standard_doc_uid(row.doc_uid)
        if standard_doc_uid is None:
            continue
        scores = row.scores_by_representation.get(representation)
        if scores is None:
            continue
        candidate = RankedStandardScore(
            standard_doc_uid=standard_doc_uid,
            raw_score=scores.raw,
            enriched_score=scores.enriched,
        )
        existing_score = best_by_standard_doc_uid.get(standard_doc_uid)
        if existing_score is None or is_better_ranked_standard_score(candidate, existing_score):
            best_by_standard_doc_uid[standard_doc_uid] = candidate
    ranked_scores = sorted(
        best_by_standard_doc_uid.values(),
        key=lambda ranked_score: (-ranked_score.enriched_score, -ranked_score.raw_score, ranked_score.standard_doc_uid),
    )
    return tuple(ranked_scores[:5])


def is_better_ranked_standard_score(candidate: RankedStandardScore, current: RankedStandardScore) -> bool:
    """Return whether a ranked standard score should replace the current best."""
    if candidate.enriched_score != current.enriched_score:
        return candidate.enriched_score > current.enriched_score
    if candidate.raw_score != current.raw_score:
        return candidate.raw_score > current.raw_score
    return candidate.standard_doc_uid < current.standard_doc_uid


def format_doc_uid_cell(row: VariantRow, document_titles_by_doc_uid: dict[str, str]) -> str:
    """Format the doc_uid cell, adding an italicized title for standard rows."""
    title = document_titles_by_doc_uid.get(row.doc_uid)
    if row.document_type in STANDARD_ROW_DOCUMENT_TYPES and title is not None:
        display_title = remove_ifrs_prefix(title)
        wrapped_title = wrap_title(display_title, width=30)
        return f"{row.doc_uid}<br><em>{wrapped_title}</em>"
    return row.doc_uid



def remove_ifrs_prefix(title: str) -> str:
    """Remove the leading IFRS prefix from a document title when present."""
    prefix = "IFRS - "
    if title.startswith(prefix):
        return title[len(prefix) :]
    return title



def wrap_title(title: str, *, width: int = 30) -> str:
    """Wrap a title into fixed-width lines separated by HTML breaks."""
    wrapped_lines = textwrap.wrap(title, width=width, break_long_words=False, break_on_hyphens=False)
    return "<br>".join(wrapped_lines)


def format_score_value(score: float, *, highlighted: bool) -> str:
    """Format one score with an optional family-best marker."""
    score_text = f"{score:.4f}"
    if highlighted:
        return f"{score_text}✅"
    return score_text


def score_direction_arrow(left_score: float, right_score: float) -> str:
    """Return an arrow showing whether the right score is higher or lower than the left score."""
    if right_score > left_score:
        return "↗"
    if right_score < left_score:
        return "↘"
    return "→"


def _display_percentage_change(raw_score: float, enriched_score: float) -> int:
    """Calculate the displayed integer percentage change for a score pair."""
    percentage_change = calculate_percentage_change(raw_score=raw_score, enriched_score=enriched_score)
    return math.trunc(percentage_change + 1e-9 if percentage_change >= 0.0 else percentage_change - 1e-9)


def format_delta_change(raw_score: float, enriched_score: float) -> str:
    """Format the raw-to-enriched delta and percent change for a cell."""
    delta = enriched_score - raw_score
    delta_text = f"{delta:+.2f}"
    percentage_delta = _display_percentage_change(raw_score, enriched_score)
    percentage_text = f"{percentage_delta:+d}%"
    return f"({delta_text} = {percentage_text})"



def calculate_percentage_change(raw_score: float, enriched_score: float) -> float:
    """Calculate the percentage change from raw to enriched scores."""
    delta = enriched_score - raw_score
    if raw_score == 0.0:
        if delta == 0.0:
            return 0.0
        return 100.0 if delta > 0.0 else -100.0
    return (delta / raw_score) * 100.0



HEATMAP_COLOR_SCALE_PERCENT = 20.0


def format_heatmap_style(raw_score: float, enriched_score: float) -> str:
    """Format an inline heatmap background color for a score cell."""
    percentage_change = calculate_percentage_change(raw_score=raw_score, enriched_score=enriched_score)
    clamped_percentage = max(-100.0, min(100.0, percentage_change))
    neutral_rgb = (245, 245, 245)
    positive_rgb = (143, 238, 143)
    negative_rgb = (238, 143, 143)
    intensity = min(abs(clamped_percentage) / HEATMAP_COLOR_SCALE_PERCENT, 1.0)
    if clamped_percentage >= 0.0:
        color_rgb = _interpolate_rgb(neutral_rgb, positive_rgb, intensity)
    else:
        color_rgb = _interpolate_rgb(neutral_rgb, negative_rgb, intensity)
    return f"background-color: rgb({color_rgb[0]}, {color_rgb[1]}, {color_rgb[2]}); padding: 0.15rem 0.25rem; display: block;"



def _interpolate_rgb(start_rgb: tuple[int, int, int], end_rgb: tuple[int, int, int], factor: float) -> tuple[int, int, int]:
    """Linearly interpolate between two RGB colors."""
    clamped_factor = max(0.0, min(1.0, factor))
    red = round(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * clamped_factor)
    green = round(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * clamped_factor)
    blue = round(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * clamped_factor)
    return (red, green, blue)


def score_location_sort_key(location: ScoreLocation) -> tuple[float, int, int, int]:
    """Build a sort key where larger values are better."""
    representation_index = SIMILARITY_REPRESENTATIONS.index(location.representation)
    side_rank = 1 if location.side == "raw" else 0
    return (
        location.score,
        -location.row_index,
        -representation_index,
        side_rank,
    )


def is_better_score_location(candidate: ScoreLocation, current: ScoreLocation) -> bool:
    """Return whether a candidate score should replace the current winner."""
    return score_location_sort_key(candidate) > score_location_sort_key(current)


def _is_family_winner(
    family_winners: FamilyWinners | None,
    row: VariantRow,
    representation: DocumentSimilarityRepresentation,
    side: ScoreSide,
) -> bool:
    """Return whether this side is the family winner for the row."""
    if family_winners is None:
        return False
    winner = family_winners.raw if side == "raw" else family_winners.enriched
    if winner is None:
        return False
    return winner.doc_uid == row.doc_uid and winner.representation == representation and winner.side == side


def format_representation_cell(
    row: VariantRow,
    representation: DocumentSimilarityRepresentation,
    family_winners: FamilyWinners | None,
) -> str:
    """Format one table cell for a representation."""
    scores = row.scores_by_representation.get(representation)
    is_preferred_representation = representation == row.preferred_representation
    if scores is None:
        return "**❌**" if is_preferred_representation else "—"

    enriched_highlighted = _is_family_winner(
        family_winners=family_winners,
        row=row,
        representation=representation,
        side="enriched",
    )
    raw_highlighted = _is_family_winner(
        family_winners=family_winners,
        row=row,
        representation=representation,
        side="raw",
    )
    raw_text = format_score_value(scores.raw, highlighted=raw_highlighted)
    enriched_text = format_score_value(scores.enriched, highlighted=enriched_highlighted)
    arrow = score_direction_arrow(scores.raw, scores.enriched)
    cell_text = f"{raw_text} {arrow} {enriched_text}"
    if is_preferred_representation:
        cell_text = f"<strong>{cell_text}</strong>"
    heatmap_style = format_heatmap_style(scores.raw, scores.enriched)
    return f'<span style="{heatmap_style}">{cell_text}<br>{format_delta_change(scores.raw, scores.enriched)}</span>'


def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(description="Build a variant-level similarity table for selected Q1 variants")
    parser.add_argument(
        "--question-dir",
        type=Path,
        default=None,
        help=f"Question directory (default: {DEFAULT_QUESTION_DIR})",
    )
    parser.add_argument(
        "--question-ids",
        nargs="+",
        default=list(DEFAULT_QUESTION_IDS),
        help="Question ids to analyze, for example: Q1.1 Q1.6 Q1.9",
    )
    parser.add_argument(
        "--glossary-path",
        type=Path,
        default=None,
        help=f"Glossary path used for enriched query text (default: {DEFAULT_GLOSSARY_PATH})",
    )
    parser.add_argument(
        "--policy-path",
        type=Path,
        default=None,
        help=f"Policy path used to determine the active similarity representation (default: {DEFAULT_POLICY_PATH})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=f"Markdown output path (default: {DEFAULT_OUTPUT_FILENAME} next to this script)",
    )
    parser.add_argument(
        "--top-per-representation",
        type=int,
        default=DEFAULT_TOP_PER_REPRESENTATION,
        help="How many top hits per representation to use when selecting candidate standards",
    )
    return parser


def main() -> None:
    """Run the experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    question_dir = args.question_dir or (repo_root / DEFAULT_QUESTION_DIR)
    glossary_path = args.glossary_path or (repo_root / DEFAULT_GLOSSARY_PATH)
    policy_path = args.policy_path or (repo_root / DEFAULT_POLICY_PATH)
    output_path = args.output or (script_dir / DEFAULT_OUTPUT_FILENAME)

    experiment = Q1VariantSimilarityTableExperiment(
        ExperimentConfig(
            repo_root=repo_root,
            question_dir=question_dir,
            question_ids=tuple(args.question_ids),
            glossary_path=glossary_path,
            policy_path=policy_path,
            output_path=output_path,
            top_per_representation=args.top_per_representation,
        )
    )
    markdown = experiment.run()
    sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
