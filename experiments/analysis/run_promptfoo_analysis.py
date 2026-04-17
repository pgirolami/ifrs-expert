#!/usr/bin/env python3
"""Run stability analysis on promptfoo experiment outputs.

Usage:
    python run_promptfoo_analysis.py openai
    python run_promptfoo_analysis.py anthropic --experiment 15_promptfoo_baseline_Q1
"""

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


# =============================================================================
# Configuration
# =============================================================================

# Resolve relative to this script's location
SCRIPT_DIR = Path(__file__).parent
EXPERIMENTS_DIR = SCRIPT_DIR.parent
DEFAULT_EXPERIMENT = "15_promptfoo_baseline_Q1"


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class StabilityDiagnostics:
    """Diagnostics data for stability analysis."""
    run_count: int
    average_approach_count: float
    average_pairwise_jaccard: float
    average_pairwise_jaccard_canonical: float
    average_pairwise_applicability_consistency: float
    average_pairwise_applicability_consistency_loose: float
    average_pairwise_recommendation_consistency: float
    average_pairwise_recommendation_consistency_loose: float
    structural_validity_flag: bool
    weird_alternatives_count: int
    duplicate_alternatives_count: int
    missing_expected_alternatives_count: int
    recommendation_distribution: dict[str, int]
    applicability_distribution_by_label: dict[str, dict[str, int]]


@dataclass
class StabilityResult:
    """Result of stability scoring analysis."""
    stability_score: float
    stability_score_loose: float
    approach_set_stability: float
    approach_set_stability_canonical: float
    applicability_stability: float
    applicability_stability_loose: float
    recommendation_stability: float
    recommendation_stability_loose: float
    structural_validity_stability: float
    diagnostics: StabilityDiagnostics


@dataclass
class QuestionScore:
    """Score and diagnostics for a single question."""
    question_id: str
    runs: int
    stability_score: float
    stability_score_loose: float
    approach_stability: float
    approach_stability_canonical: float
    applicability_stability: float
    applicability_stability_loose: float
    recommendation_stability: float
    recommendation_stability_loose: float
    structural_valid: bool
    rec_dist: dict
    label_counts: dict[str, int]  # normalized_label -> count
    citation_counts: dict[str, int]  # citation_key (doc+section) -> count across all runs
    retrieval_context: dict[str, list[tuple[str, float]]]  # doc_uid -> [(section_path, score), ...]


@dataclass
class Chunk:
    """Represents a single chunk from the retrieval context."""
    chunk_id: str
    doc_uid: str
    section_path: str
    score: float


# =============================================================================
# Canonical Label Mapping
# =============================================================================

VALID_RECOMMENDATION_ANSWERS = frozenset({"oui", "non", "oui_sous_conditions"})
VALID_APPLICABILITY_VALUES = frozenset({"oui", "non", "oui_sous_conditions"})

# Canonical mapping: maps variant normalized_labels to their canonical form
CANONICAL_LABEL_MAPPING: dict[str, str] = {
    # Fair value hedge - keep as-is
    "fair_value_hedge": "fair_value_hedge",
    # Cash flow hedge - keep as-is
    "cash_flow_hedge": "cash_flow_hedge",
    # Net investment hedge - keep as-is
    "net_investment_hedge": "net_investment_hedge",
    # All foreign currency/monetary item hedges map to cash flow hedge
    "foreign_currency_hedge": "cash_flow_hedge",
    "foreign_currency_component_hedge": "cash_flow_hedge",
    "intragroup_monetary_hedge": "cash_flow_hedge",
    "monetary_item_hedge": "cash_flow_hedge",
    # Analysis-only approaches
    "cartographie_des_entites_et_devises_fonctionnelles": "analysis_only",
    "choix_entre_creance_de_dividende_et_couverture_d_investissement_net": "analysis_only",
    "qualification_du_solde_comme_reglement_proche_ou_investissement_net": "analysis_only",
    # Measurement basis approaches (not hedge accounting routes)
    "amortised_cost": "measurement_basis",
    "fair_value_oci": "measurement_basis",
    "fair_value_pl": "measurement_basis",
}


# =============================================================================
# Label Normalization and Extraction Functions
# =============================================================================

def normalize_label(label: str) -> str:
    """Normalize a normalized_label by stripping whitespace and lowercasing."""
    return label.strip().lower()


def canonicalize_label(label: str) -> str:
    """Convert a normalized label to its canonical form."""
    normalized = normalize_label(label)
    return CANONICAL_LABEL_MAPPING.get(normalized, normalized)


def extract_approaches(run: dict) -> list[dict]:
    """Extract approaches from a run, returning empty list if missing."""
    approaches = run.get("approaches")
    if not isinstance(approaches, list):
        return []
    return approaches


def extract_normalized_labels(run: dict) -> set[str]:
    """Extract normalized labels from a run's approaches."""
    approaches = extract_approaches(run)
    labels: set[str] = set()
    for approach in approaches:
        label = approach.get("normalized_label")
        if isinstance(label, str) and label.strip():
            labels.add(normalize_label(label))
    return labels


def extract_canonical_labels(run: dict) -> set[str]:
    """Extract canonical labels from a run's approaches."""
    approaches = extract_approaches(run)
    labels: set[str] = set()
    for approach in approaches:
        label = approach.get("normalized_label")
        if isinstance(label, str) and label.strip():
            labels.add(canonicalize_label(label))
    return labels


def extract_applicability_map(run: dict) -> dict[str, str]:
    """Extract applicability values keyed by normalized label."""
    approaches = extract_approaches(run)
    result: dict[str, str] = {}
    for approach in approaches:
        label = approach.get("normalized_label")
        applicability = approach.get("applicability")
        if isinstance(label, str) and label.strip() and isinstance(applicability, str):
            result[normalize_label(label)] = applicability.strip()
    return result


def extract_recommendation_answer(run: dict) -> str | None:
    """Extract recommendation answer from a run, or None if missing/invalid."""
    recommendation = run.get("recommendation")
    if not isinstance(recommendation, dict):
        return None
    answer = recommendation.get("answer")
    if isinstance(answer, str) and answer.strip():
        return answer.strip()
    return None


def is_structurally_valid(run: dict) -> bool:
    """Check if a run is valid and parseable with a recommendation in expected enum."""
    if not isinstance(run, dict):
        return False
    answer = extract_recommendation_answer(run)
    return answer in VALID_RECOMMENDATION_ANSWERS


def extract_citations_from_run(run: dict) -> set[str]:
    """Extract citation keys from a run's approaches.
    
    Returns a set of citation keys in format 'doc_uid:section'.
    """
    approaches = extract_approaches(run)
    citations: set[str] = set()
    
    for approach in approaches:
        references = approach.get("references")
        if not isinstance(references, list):
            continue
        
        for ref in references:
            document = ref.get("document")
            section = ref.get("section")
            if isinstance(document, str) and isinstance(section, str):
                citation_key = f"{document}:{section}"
                citations.add(citation_key)
    
    return citations


# =============================================================================
# Similarity Functions
# =============================================================================

def jaccard_similarity(set_a: set[str], set_b: set[str]) -> float:
    """Compute Jaccard similarity between two sets."""
    if not set_a and not set_b:
        return 1.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def applicability_consistency(run_a: dict, run_b: dict) -> float:
    """Compute pairwise applicability consistency between two runs."""
    map_a = extract_applicability_map(run_a)
    map_b = extract_applicability_map(run_b)

    shared_labels = set(map_a.keys()) & set(map_b.keys())

    if not shared_labels:
        empty_a = not map_a
        empty_b = not map_b
        return 1.0 if (empty_a and empty_b) else 0.0

    matches = sum(1 for label in shared_labels if map_a[label] == map_b[label])
    return matches / len(shared_labels)


def _normalize_applicability_loose(value: str) -> str:
    """Normalize applicability for loose comparison."""
    normalized = value.strip().lower()
    if normalized in ("oui", "oui_sous_conditions"):
        return "oui_or_oui_sous_conditions"
    return normalized


def applicability_consistency_loose(run_a: dict, run_b: dict) -> float:
    """Compute pairwise applicability consistency with loose normalization."""
    map_a = extract_applicability_map(run_a)
    map_b = extract_applicability_map(run_b)

    shared_labels = set(map_a.keys()) & set(map_b.keys())

    if not shared_labels:
        empty_a = not map_a
        empty_b = not map_b
        return 1.0 if (empty_a and empty_b) else 0.0

    matches = sum(1 for label in shared_labels if _normalize_applicability_loose(map_a[label]) == _normalize_applicability_loose(map_b[label]))
    return matches / len(shared_labels)


def recommendation_consistency(run_a: dict, run_b: dict) -> float:
    """Compute pairwise recommendation consistency between two runs."""
    answer_a = extract_recommendation_answer(run_a)
    answer_b = extract_recommendation_answer(run_b)

    if answer_a is None or answer_b is None:
        return 0.0

    return 1.0 if answer_a == answer_b else 0.0


def recommendation_consistency_loose(run_a: dict, run_b: dict) -> float:
    """Compute pairwise recommendation consistency with loose normalization."""
    answer_a = extract_recommendation_answer(run_a)
    answer_b = extract_recommendation_answer(run_b)

    if answer_a is None or answer_b is None:
        return 0.0

    normalized_a = _normalize_applicability_loose(answer_a)
    normalized_b = _normalize_applicability_loose(answer_b)

    return 1.0 if normalized_a == normalized_b else 0.0


def count_duplicates(run: dict) -> int:
    """Count approaches with duplicate normalized_label in a single run."""
    approaches = extract_approaches(run)
    labels: list[str] = []
    for approach in approaches:
        label = approach.get("normalized_label")
        if isinstance(label, str) and label.strip():
            labels.append(normalize_label(label))

    seen: set[str] = set()
    duplicates = 0
    for label in labels:
        if label in seen:
            duplicates += 1
        else:
            seen.add(label)
    return duplicates


def count_weird_alternatives(run: dict, expected_labels: set[str] | None) -> int:
    """Count approaches whose normalized_label is not in expected set."""
    if expected_labels is None:
        return 0

    approaches = extract_approaches(run)
    weird = 0
    for approach in approaches:
        label = approach.get("normalized_label")
        if isinstance(label, str) and label.strip() and normalize_label(label) not in expected_labels:
            weird += 1
    return weird


def count_missing_expected(run: dict, expected_labels: set[str]) -> int:
    """Count how many expected normalized_labels are missing from this run."""
    run_labels = extract_normalized_labels(run)
    missing = 0
    for expected in expected_labels:
        if expected not in run_labels:
            missing += 1
    return missing


# =============================================================================
# Core Stability Computation
# =============================================================================

def compute_stability_score(
    runs: list[dict],
    expected_normalized_labels: set[str] | None = None,
) -> StabilityResult:
    """Compute stability score for a set of repeated runs."""
    run_count = len(runs)

    # Single run edge case
    if run_count == 1:
        run = runs[0]
        approaches = extract_approaches(run)
        answer = extract_recommendation_answer(run)

        recommendation_dist: dict[str, int] = {}
        if answer in VALID_RECOMMENDATION_ANSWERS:
            recommendation_dist[answer] = 1

        applicability_dist: dict[str, dict[str, int]] = {}
        for approach in approaches:
            label = approach.get("normalized_label")
            applicability = approach.get("applicability")
            if isinstance(label, str) and isinstance(applicability, str):
                norm_label = normalize_label(label)
                if norm_label not in applicability_dist:
                    applicability_dist[norm_label] = {}
                applicability_dist[norm_label][applicability] = applicability_dist[norm_label].get(applicability, 0) + 1

        diagnostics = StabilityDiagnostics(
            run_count=1,
            average_approach_count=float(len(approaches)),
            average_pairwise_jaccard=1.0,
            average_pairwise_jaccard_canonical=1.0,
            average_pairwise_applicability_consistency=1.0,
            average_pairwise_applicability_consistency_loose=1.0,
            average_pairwise_recommendation_consistency=1.0,
            average_pairwise_recommendation_consistency_loose=1.0,
            structural_validity_flag=is_structurally_valid(run),
            weird_alternatives_count=count_weird_alternatives(run, expected_normalized_labels),
            duplicate_alternatives_count=count_duplicates(run),
            missing_expected_alternatives_count=count_missing_expected(run, expected_normalized_labels) if expected_normalized_labels else 0,
            recommendation_distribution=recommendation_dist,
            applicability_distribution_by_label=applicability_dist,
        )

        return StabilityResult(
            stability_score=100.0,
            stability_score_loose=100.0,
            approach_set_stability=1.0,
            approach_set_stability_canonical=1.0,
            applicability_stability=1.0,
            applicability_stability_loose=1.0,
            recommendation_stability=1.0,
            recommendation_stability_loose=1.0,
            structural_validity_stability=1.0 if diagnostics.structural_validity_flag else 0.0,
            diagnostics=diagnostics,
        )

    # Multiple runs: compute all pairwise metrics
    pairwise_jaccards: list[float] = []
    pairwise_jaccards_canonical: list[float] = []
    pairwise_applicability: list[float] = []
    pairwise_applicability_loose: list[float] = []
    pairwise_recommendation: list[float] = []
    pairwise_recommendation_loose: list[float] = []

    for run_a, run_b in combinations(runs, 2):
        pairwise_jaccards.append(
            jaccard_similarity(
                extract_normalized_labels(run_a),
                extract_normalized_labels(run_b),
            ),
        )
        pairwise_jaccards_canonical.append(
            jaccard_similarity(
                extract_canonical_labels(run_a),
                extract_canonical_labels(run_b),
            ),
        )
        pairwise_applicability.append(applicability_consistency(run_a, run_b))
        pairwise_applicability_loose.append(applicability_consistency_loose(run_a, run_b))
        pairwise_recommendation.append(recommendation_consistency(run_a, run_b))
        pairwise_recommendation_loose.append(recommendation_consistency_loose(run_a, run_b))

    avg_jaccard = sum(pairwise_jaccards) / len(pairwise_jaccards)
    avg_jaccard_canonical = sum(pairwise_jaccards_canonical) / len(pairwise_jaccards_canonical) if pairwise_jaccards_canonical else 1.0
    avg_applicability = sum(pairwise_applicability) / len(pairwise_applicability)
    avg_applicability_loose = sum(pairwise_applicability_loose) / len(pairwise_applicability_loose)
    avg_recommendation = sum(pairwise_recommendation) / len(pairwise_recommendation)
    avg_recommendation_loose = sum(pairwise_recommendation_loose) / len(pairwise_recommendation_loose)

    approach_set_stability = avg_jaccard
    approach_set_stability_canonical = avg_jaccard_canonical
    applicability_stability = avg_applicability
    recommendation_stability = avg_recommendation
    applicability_stability_loose = avg_applicability_loose
    recommendation_stability_loose = avg_recommendation_loose
    structural_validity_stability = 1.0 if all(is_structurally_valid(r) for r in runs) else 0.0

    # Final scores
    stability_score = 35.0 * approach_set_stability + 30.0 * applicability_stability + 20.0 * recommendation_stability + 15.0 * structural_validity_stability
    stability_score = max(0.0, min(100.0, stability_score))

    stability_score_loose = 35.0 * approach_set_stability_canonical + 30.0 * applicability_stability_loose + 20.0 * recommendation_stability_loose + 15.0 * structural_validity_stability
    stability_score_loose = max(0.0, min(100.0, stability_score_loose))

    # Diagnostics
    total_approaches = sum(len(extract_approaches(r)) for r in runs)
    avg_approach_count = total_approaches / run_count

    structural_validity_flag = all(is_structurally_valid(r) for r in runs)
    weird_count = sum(count_weird_alternatives(r, expected_normalized_labels) for r in runs)
    duplicate_count = sum(count_duplicates(r) for r in runs)

    missing_count = 0
    if expected_normalized_labels:
        for run in runs:
            missing_count += count_missing_expected(run, expected_normalized_labels)

    recommendation_dist: dict[str, int] = {}
    for run in runs:
        answer = extract_recommendation_answer(run)
        if answer in VALID_RECOMMENDATION_ANSWERS:
            recommendation_dist[answer] = recommendation_dist.get(answer, 0) + 1

    applicability_dist: dict[str, dict[str, int]] = {}
    for run in runs:
        for approach in extract_approaches(run):
            label = approach.get("normalized_label")
            applicability = approach.get("applicability")
            if isinstance(label, str) and isinstance(applicability, str):
                norm_label = normalize_label(label)
                if norm_label not in applicability_dist:
                    applicability_dist[norm_label] = {}
                applicability_dist[norm_label][applicability] = applicability_dist[norm_label].get(applicability, 0) + 1

    diagnostics = StabilityDiagnostics(
        run_count=run_count,
        average_approach_count=avg_approach_count,
        average_pairwise_jaccard=avg_jaccard,
        average_pairwise_jaccard_canonical=avg_jaccard_canonical,
        average_pairwise_applicability_consistency=avg_applicability,
        average_pairwise_applicability_consistency_loose=avg_applicability_loose,
        average_pairwise_recommendation_consistency=avg_recommendation,
        average_pairwise_recommendation_consistency_loose=avg_recommendation_loose,
        structural_validity_flag=structural_validity_flag,
        weird_alternatives_count=weird_count,
        duplicate_alternatives_count=duplicate_count,
        missing_expected_alternatives_count=missing_count,
        recommendation_distribution=recommendation_dist,
        applicability_distribution_by_label=applicability_dist,
    )

    return StabilityResult(
        stability_score=stability_score,
        stability_score_loose=stability_score_loose,
        approach_set_stability=approach_set_stability,
        approach_set_stability_canonical=approach_set_stability_canonical,
        applicability_stability=applicability_stability,
        applicability_stability_loose=applicability_stability_loose,
        recommendation_stability=recommendation_stability,
        recommendation_stability_loose=recommendation_stability_loose,
        structural_validity_stability=structural_validity_stability,
        diagnostics=diagnostics,
    )


# =============================================================================
# Directory Navigation and Loading
# =============================================================================

def find_latest_run_dir(experiment_dir: Path) -> Path | None:
    """Find the most recent run directory in an experiment."""
    runs_dir = experiment_dir / "runs"
    if not runs_dir.exists():
        return None
    
    run_dirs = [d for d in runs_dir.iterdir() if d.is_dir()]
    if not run_dirs:
        return None
    
    # Sort by name (which includes timestamp) and return the latest
    return sorted(run_dirs, key=lambda x: x.name, reverse=True)[0]


def get_provider_dirs(run_dir: Path, provider: str) -> list[tuple[Path, str]]:
    """Get all (provider_dir, question_id) pairs matching the given provider name.
    
    Returns list of tuples with (provider_directory, question_id).
    Handles nested structure: artifacts/<group>/<question>/<provider>/
    """
    artifacts_dir = run_dir / "artifacts"
    if not artifacts_dir.exists():
        return []
    
    provider_dirs: list[tuple[Path, str]] = []
    
    # First level: group directories (e.g., Q1, Q2, etc.)
    for group_dir in artifacts_dir.iterdir():
        if not group_dir.is_dir():
            continue
        
        # Second level: question directories (e.g., Q1.0, Q1.1, etc.)
        for question_dir in group_dir.iterdir():
            if not question_dir.is_dir():
                continue
            
            provider_path = question_dir / provider
            if provider_path.exists() and provider_path.is_dir():
                provider_dirs.append((provider_path, question_dir.name))
    
    return provider_dirs


def load_b_response(provider_dir: Path, repetition: str | None = None) -> dict | None:
    """Load B-response.json file from a provider directory or repetition subdirectory."""
    if repetition:
        dir_path = provider_dir / repetition
    else:
        dir_path = provider_dir
    
    json_path = dir_path / "B-response.json"
    if not json_path.exists():
        return None
    
    try:
        return json.loads(json_path.read_text())
    except json.JSONDecodeError:
        return None


def get_repetitions(provider_dir: Path) -> list[str]:
    """Get list of repetitions for a provider directory.
    
    Returns ['repeat-1', 'repeat-2', ...] for directories with repetitions.
    Also includes None for the base run if it has a B-response.json.
    """
    repetitions: list[str] = []
    
    # Check base directory
    if (provider_dir / "B-response.json").exists():
        repetitions.append(None)  # None represents the base run
    
    # Check for repeat-N subdirectories
    for item in provider_dir.iterdir():
        if item.is_dir() and item.name.startswith("repeat-"):
            if (item / "B-response.json").exists():
                repetitions.append(item.name)
    
    return repetitions


def load_a_prompt(provider_dir: Path, repetition: str | None = None) -> str | None:
    """Load A-prompt.txt file content from a provider directory or repetition subdirectory."""
    if repetition:
        dir_path = provider_dir / repetition
    else:
        dir_path = provider_dir
    
    prompt_path = dir_path / "A-prompt.txt"
    if not prompt_path.exists():
        return None
    
    try:
        return prompt_path.read_text()
    except Exception:
        return None


def parse_chunks_from_a_prompt(content: str) -> list[Chunk]:
    """Parse chunks from A-prompt.txt content.
    
    Extracts all <chunk> tags with their attributes: id, doc_uid, section_path, score.
    Chunks are returned in the order they appear in the document.
    """
    chunks: list[Chunk] = []
    
    # Pattern to match <chunk id="..." doc_uid="..." section_path="..." score="...">
    pattern = r'<chunk id="([^"]+)" doc_uid="([^"]+)" section_path="([^"]+)" score="([^"]+)">'
    
    for match in re.finditer(pattern, content):
        chunk_id = match.group(1)
        doc_uid = match.group(2)
        section_path = match.group(3)
        score = float(match.group(4))
        
        chunks.append(Chunk(
            chunk_id=chunk_id,
            doc_uid=doc_uid,
            section_path=section_path,
            score=score,
        ))
    
    return chunks


def get_retrieval_context(provider_dir: Path, repetition: str | None = None) -> dict[str, list[tuple[str, float]]]:
    """Get retrieval context for a single run.
    
    Returns a dict mapping doc_uid to list of (section_path, score) tuples.
    Chunks are ordered as they appear in the document.
    """
    content = load_a_prompt(provider_dir, repetition)
    if not content:
        return {}
    
    chunks = parse_chunks_from_a_prompt(content)
    
    # Group by doc_uid, preserving order
    context: dict[str, list[tuple[str, float]]] = {}
    for chunk in chunks:
        if chunk.doc_uid not in context:
            context[chunk.doc_uid] = []
        context[chunk.doc_uid].append((chunk.section_path, chunk.score))
    
    return context


def aggregate_retrieval_context(
    provider_dir: Path,
    repetitions: list[str],
) -> dict[str, list[tuple[str, float]]]:
    """Aggregate retrieval context across multiple runs for a question.
    
    For chunks with score > 0 (retrieval), takes the mode across runs.
    For chunks with score = 0 (expansion), includes all unique chunks.
    
    Returns a dict mapping doc_uid to list of (section_path, score) tuples,
    ordered by first appearance in the document.
    """
    if not repetitions:
        return {}
    
    # Collect all chunks from all runs
    all_contexts: list[dict[str, list[tuple[str, float]]]] = []
    for rep in repetitions:
        ctx = get_retrieval_context(provider_dir, rep)
        if ctx:
            all_contexts.append(ctx)
    
    if not all_contexts:
        return {}
    
    # Get all unique docs
    all_docs: set[str] = set()
    for ctx in all_contexts:
        all_docs.update(ctx.keys())
    
    result: dict[str, list[tuple[str, float]]] = {}
    
    for doc in sorted(all_docs):
        # Get all chunks for this doc across all runs
        doc_chunks: list[tuple[str, float, int]] = []  # (section_path, score, run_idx)
        
        for run_idx, ctx in enumerate(all_contexts):
            if doc in ctx:
                for section_path, score in ctx[doc]:
                    doc_chunks.append((section_path, score, run_idx))
        
        # Separate retrieval (score > 0) and expansion (score = 0)
        retrieval_chunks = [(s, sc) for s, sc, _ in doc_chunks if sc > 0]
        expansion_chunks = [(s, sc) for s, sc, _ in doc_chunks if sc == 0]
        
        # For retrieval chunks: deduplicate by section_path, use average score across runs
        seen_retrieval: dict[str, list[float]] = {}
        for section_path, score in retrieval_chunks:
            if section_path not in seen_retrieval:
                seen_retrieval[section_path] = []
            seen_retrieval[section_path].append(score)
        
        retrieval_result = [(s, sum(scores) / len(scores)) for s, scores in seen_retrieval.items()]
        retrieval_result.sort(key=lambda x: x[0])  # Sort by section path
        
        # For expansion chunks: deduplicate by section_path
        seen_expansion: set[str] = set()
        expansion_result: list[tuple[str, float]] = []
        for section_path, score in expansion_chunks:
            if section_path not in seen_expansion:
                seen_expansion.add(section_path)
                expansion_result.append((section_path, 0.0))  # Expansion score is always 0
        
        # Combine: retrieval first, then expansion
        result[doc] = retrieval_result + expansion_result
    
    return result


def question_sort_key(q: str) -> tuple[int, int]:
    """Sort key for question IDs like Q1, Q1.1, Q1.10."""
    # Extract numeric parts: Q1.1 -> (1, 1), Q1.10 -> (1, 10)
    import re
    match = re.match(r"Q(\d+)\.(\d+)", q)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    match = re.match(r"Q(\d+)$", q)
    if match:
        return (int(match.group(1)), 0)
    return (999, 999)  # Unknown questions go last


# =============================================================================
# Main Analysis Functions
# =============================================================================

def analyze_question_for_provider(
    provider_dir: Path,
    question_id: str,
) -> QuestionScore | None:
    """Analyze stability for a single question across all repetitions."""
    repetitions = get_repetitions(provider_dir)
    
    if len(repetitions) < 2:
        return None  # Need at least 2 runs for stability analysis
    
    # Load all runs
    runs = []
    for rep in repetitions:
        run = load_b_response(provider_dir, rep)
        if run:
            runs.append(run)
    
    if len(runs) < 2:
        return None
    
    result = compute_stability_score(runs)
    
    # Compute label counts across all runs
    label_counts: dict[str, int] = defaultdict(int)
    for run in runs:
        for label in extract_normalized_labels(run):
            label_counts[label] += 1
    
    # Compute retrieval context across all runs
    retrieval_context = aggregate_retrieval_context(provider_dir, repetitions)
    
    # Compute citation counts across all runs
    citation_counts: dict[str, int] = defaultdict(int)
    for run in runs:
        for citation in extract_citations_from_run(run):
            citation_counts[citation] += 1
    
    return QuestionScore(
        question_id=question_id,
        runs=len(runs),
        stability_score=result.stability_score,
        stability_score_loose=result.stability_score_loose,
        approach_stability=result.approach_set_stability,
        approach_stability_canonical=result.approach_set_stability_canonical,
        applicability_stability=result.applicability_stability,
        applicability_stability_loose=result.applicability_stability_loose,
        recommendation_stability=result.recommendation_stability,
        recommendation_stability_loose=result.recommendation_stability_loose,
        structural_valid=result.diagnostics.structural_validity_flag,
        rec_dist=result.diagnostics.recommendation_distribution,
        label_counts=dict(label_counts),
        citation_counts=dict(citation_counts),
        retrieval_context=retrieval_context,
    )


def print_label_frequency_table(results: list[QuestionScore]) -> None:
    """Print label frequency by question table in markdown format."""
    print("\n## Label Frequency by Question\n")
    
    if not results:
        print("No data available.\n")
        return
    
    sorted_results = sorted(results, key=lambda x: question_sort_key(x.question_id))
    total_runs = sum(r.runs for r in sorted_results)
    
    # Collect all unique labels
    all_labels: set[str] = set()
    for r in results:
        all_labels.update(r.label_counts.keys())
    
    if not all_labels:
        print("No labels found.\n")
        return
    
    # Separate core labels (>= 10% of runs) from spurious (< 10%)
    core_labels: list[tuple[str, int]] = []
    spurious_labels_list: list[tuple[str, int]] = []
    
    for label in sorted(all_labels):
        total_count = sum(r.label_counts.get(label, 0) for r in sorted_results)
        if total_count >= total_runs * 0.1:  # >= 10% threshold
            core_labels.append((label, total_count))
        elif total_count > 0:
            spurious_labels_list.append((label, total_count))
    
    # Sort by total count descending within each group
    core_labels.sort(key=lambda x: x[1], reverse=True)
    spurious_labels_list.sort(key=lambda x: x[1], reverse=True)
    
    # Sort labels alphabetically
    core_labels.sort(key=lambda x: x[0])
    spurious_labels_list.sort(key=lambda x: x[0])
    
    question_ids = sorted([r.question_id for r in sorted_results])
    
    # Core labels table
    print("### Core Labels (>= 10% of runs)\n")
    
    # Build header cells
    header_cells = ["Label", "Relevant", "Total"] + list(question_ids)
    
    # Simple markdown table without space padding
    print("| " + " | ".join(header_cells) + " |")
    print("|" + "|".join("---" for _ in header_cells) + "|")
    
    # Data rows for core labels
    for label, _ in core_labels:
        row = [label, "", ""]
        total = 0
        for r in sorted_results:
            count = r.label_counts.get(label, 0)
            total += count
        row[2] = str(total)
        for r in sorted_results:
            count = r.label_counts.get(label, 0)
            row.append(str(count))
        print("| " + " | ".join(row) + " |")
    
    # Spurious labels table
    if spurious_labels_list:
        print(f"\n### Spurious Labels (< 10% of runs)\n")
        
        spurious_header = ["Label", "Correct", "Total"] + list(question_ids)
        print("| " + " | ".join(spurious_header) + " |")
        print("|" + "|".join("---" for _ in spurious_header) + "|")
        
        for label, _ in spurious_labels_list:
            total = sum(r.label_counts.get(label, 0) for r in sorted_results)
            row = [label, "", str(total)]
            for r in sorted_results:
                count = r.label_counts.get(label, 0)
                row.append(str(count))
            print("| " + " | ".join(row) + " |")


def print_citation_frequency_table(results: list[QuestionScore]) -> None:
    """Print citation frequency by question table in markdown format.
    
    1 row per citation (document + section), 1 column per question,
    each cell contains the number of times the citation was used.
    """
    print("\n## Citation Frequency by Question\n")
    
    if not results:
        print("No data available.\n")
        return
    
    sorted_results = sorted(results, key=lambda x: question_sort_key(x.question_id))
    total_runs = sum(r.runs for r in sorted_results)
    
    # Collect all unique citations
    all_citations: set[str] = set()
    for r in results:
        all_citations.update(r.citation_counts.keys())
    
    if not all_citations:
        print("No citations found.\n")
        return
    
    # Separate core citations (>= 10% of runs) from spurious (< 10%)
    core_citations: list[tuple[str, int]] = []
    spurious_citations: list[tuple[str, int]] = []
    
    for citation in sorted(all_citations):
        total_count = sum(r.citation_counts.get(citation, 0) for r in sorted_results)
        if total_count >= total_runs * 0.1:  # >= 10% threshold
            core_citations.append((citation, total_count))
        elif total_count > 0:
            spurious_citations.append((citation, total_count))
    
    # Sort by total count descending within each group
    core_citations.sort(key=lambda x: x[1], reverse=True)
    spurious_citations.sort(key=lambda x: x[1], reverse=True)
    
    # Sort citations alphabetically
    core_citations.sort(key=lambda x: x[0])
    spurious_citations.sort(key=lambda x: x[0])
    
    question_ids = sorted([r.question_id for r in sorted_results])
    
    # Core citations table
    print("### Core Citations (>= 10% of runs)\n")
    
    header_cells = ["Citation", "Correct", "Total"] + list(question_ids)
    print("| " + " | ".join(header_cells) + " |")
    print("|" + "|".join("---" for _ in header_cells) + "|")
    
    for citation, _ in core_citations:
        row = [citation, "", ""]
        total = 0
        for r in sorted_results:
            count = r.citation_counts.get(citation, 0)
            total += count
        row[2] = str(total)
        for r in sorted_results:
            count = r.citation_counts.get(citation, 0)
            row.append(str(count))
        print("| " + " | ".join(row) + " |")
    
    # Spurious citations table
    if spurious_citations:
        print(f"\n### Spurious Citations (< 10% of runs)\n")
        
        spurious_header = ["Citation", "Correct", "Total"] + list(question_ids)
        print("| " + " | ".join(spurious_header) + " |")
        print("|" + "|".join("---" for _ in spurious_header) + "|")
        
        for citation, _ in spurious_citations:
            total = sum(r.citation_counts.get(citation, 0) for r in sorted_results)
            row = [citation, "", str(total)]
            for r in sorted_results:
                count = r.citation_counts.get(citation, 0)
                row.append(str(count))
            print("| " + " | ".join(row) + " |")


def print_top_vs_low_performers(results: list[QuestionScore]) -> None:
    """Print comparison of top vs low performers in markdown format."""
    print("\n## Comparison: Top vs Low Performers\n")
    
    if not results:
        print("No data available.\n")
        return
    
    sorted_results = sorted(results, key=lambda x: question_sort_key(x.question_id))
    
    # Sort by loose score for comparison
    by_loose_score = sorted(results, key=lambda x: x.stability_score_loose, reverse=True)
    
    # Define thresholds
    top_threshold = 95.0  # Top performers: score >= 95
    low_threshold = 80.0  # Low performers: score < 80
    
    top_performers = [r for r in by_loose_score if r.stability_score_loose >= top_threshold]
    low_performers = [r for r in by_loose_score if r.stability_score_loose < low_threshold]
    
    # Top performers table
    print(f"### Top Performers (loose score >= {top_threshold})\n")
    print("| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |")
    print("|----------|------|-------|---------------|----------|--------|-----|")
    
    # Sort by score descending
    for r in sorted(top_performers, key=lambda x: x.stability_score_loose, reverse=True):
        print(f"| {r.question_id} | {r.runs} | {r.stability_score:.1f} | {r.stability_score_loose:.1f} | {r.approach_stability:.2f} | {r.applicability_stability_loose:.2f} | {r.recommendation_stability_loose:.2f} |")
    
    pct_top = 100 * len(top_performers) / len(results)
    print(f"\n**{len(top_performers)}/{len(results)} questions ({pct_top:.0f}%) are top performers**\n")
    
    # Low performers table
    print(f"### Low Performers (loose score < {low_threshold})\n")
    print("| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |")
    print("|----------|------|-------|---------------|----------|--------|-----|")
    
    # Sort by score ascending
    for r in sorted(low_performers, key=lambda x: x.stability_score_loose):
        print(f"| {r.question_id} | {r.runs} | {r.stability_score:.1f} | {r.stability_score_loose:.1f} | {r.approach_stability:.2f} | {r.applicability_stability_loose:.2f} | {r.recommendation_stability_loose:.2f} |")
    
    pct_low = 100 * len(low_performers) / len(results)
    print(f"\n**{len(low_performers)}/{len(results)} questions ({pct_low:.0f}%) are low performers**\n")
    
    # Key observations
    if top_performers and low_performers:
        print("### Key Observations\n")
        
        # Compute averages for comparison
        avg_approach_top = sum(r.approach_stability for r in top_performers) / len(top_performers) if top_performers else 0
        avg_approach_low = sum(r.approach_stability for r in low_performers) / len(low_performers) if low_performers else 0
        
        avg_approach_canonical_top = sum(r.approach_stability_canonical for r in top_performers) / len(top_performers) if top_performers else 0
        avg_approach_canonical_low = sum(r.approach_stability_canonical for r in low_performers) / len(low_performers) if low_performers else 0
        
        avg_applic_top = sum(r.applicability_stability_loose for r in top_performers) / len(top_performers) if top_performers else 0
        avg_applic_low = sum(r.applicability_stability_loose for r in low_performers) / len(low_performers) if low_performers else 0
        
        avg_rec_top = sum(r.recommendation_stability_loose for r in top_performers) / len(top_performers) if top_performers else 0
        avg_rec_low = sum(r.recommendation_stability_loose for r in low_performers) / len(low_performers) if low_performers else 0
        
        print(f"- **Approach stability (strict)**: Top={avg_approach_top:.3f}, Low={avg_approach_low:.3f}, Delta={avg_approach_top - avg_approach_low:+.3f}")
        print(f"- **Approach stability (canonical)**: Top={avg_approach_canonical_top:.3f}, Low={avg_approach_canonical_low:.3f}, Delta={avg_approach_canonical_top - avg_approach_canonical_low:+.3f}")
        print(f"- **Applicability consistency (loose)**: Top={avg_applic_top:.3f}, Low={avg_applic_low:.3f}, Delta={avg_applic_top - avg_applic_low:+.3f}")
        print(f"- **Recommendation consistency (loose)**: Top={avg_rec_top:.3f}, Low={avg_rec_low:.3f}, Delta={avg_rec_top - avg_rec_low:+.3f}")
        
        # Label diversity comparison
        avg_labels_top = sum(len(r.label_counts) for r in top_performers) / len(top_performers) if top_performers else 0
        avg_labels_low = sum(len(r.label_counts) for r in low_performers) / len(low_performers) if low_performers else 0
        print(f"- **Avg unique labels per run**: Top={avg_labels_top:.1f}, Low={avg_labels_low:.1f}\n")


def print_retrieval_context_table(results: list[QuestionScore]) -> None:
    """Print retrieval context table showing chunks per question per document.
    
    NOTE: This function is deprecated. Retrieval context is now merged into
    the per-question scores table in print_results().
    """
    print("\n## Retrieval Context by Question (Deprecated)\n")
    print("*Chunks with score > 0 are retrieval; score = 0 are expansion*\n")
    
    if not results:
        print("No data available.\n")
        return
    
    sorted_results = sorted(results, key=lambda x: question_sort_key(x.question_id))
    
    # Get all unique docs across all questions
    all_docs: set[str] = set()
    for r in results:
        all_docs.update(r.retrieval_context.keys())
    
    if not all_docs:
        print("No retrieval context found.\n")
        return
    
    # Sort docs for consistent ordering
    sorted_docs = sorted(all_docs)
    
    # Build table rows
    # Columns: Question | runs | [Doc1] | [Doc2] | ...
    
    # Header
    header_parts = ["Question", "Runs"] + sorted_docs
    print("| " + " | ".join(header_parts) + " |")
    print("|" + "|".join("---" for _ in header_parts) + "|")
    
    # Data rows
    for r in sorted_results:
        row = [r.question_id, str(r.runs)]
        
        for doc in sorted_docs:
            chunks = r.retrieval_context.get(doc, [])
            
            if not chunks:
                row.append("")
                continue
            
            # Format chunks: section_path (score)
            chunk_lines: list[str] = []
            for section_path, score in chunks:
                if score > 0:
                    chunk_lines.append(f"{section_path} ({score:.4f})")
            
            if chunk_lines:
                # Join with <br> for markdown
                row.append("<br>".join(chunk_lines))
            else:
                row.append("")
        
        print("| " + " | ".join(row) + " |")


def _format_doc_chunks(
    retrieval_context: dict[str, list[tuple[str, float]]],
    doc: str,
) -> str:
    """Format all non-zero retrieval chunks for a single document."""
    chunks = retrieval_context.get(doc, [])
    if not chunks:
        return ""
    
    retrieval_chunks = [(section_path, score) for section_path, score in chunks if score > 0]
    retrieval_chunks.sort(key=lambda item: item[1], reverse=True)
    
    if not retrieval_chunks:
        return ""
    
    return ", ".join(f"{section_path} ({score:.2f})" for section_path, score in retrieval_chunks)


def print_results(
    results: list[QuestionScore],
    provider: str,
    experiment: str,
    run_dir: Path,
) -> None:
    """Print analysis results in proper markdown format."""
    print("\n---\n")
    print(f"**Provider:** `{provider}`")
    print(f"**Experiment:** `{experiment}`")
    print(f"**Run:** `{run_dir.name}`\n")
    
    if not results:
        print("No questions with sufficient data for stability analysis.\n")
        return
    
    # Sort results by question ID
    sorted_results = sorted(results, key=lambda x: question_sort_key(x.question_id))
    
    # Get all unique docs for columns
    all_docs: set[str] = set()
    for r in results:
        all_docs.update(r.retrieval_context.keys())
    sorted_docs = sorted(all_docs)
    
    # Shorten doc names for headers
    doc_headers = {}
    for doc in sorted_docs:
        short = doc.split()[0].upper() if " " in doc else doc.upper()
        doc_headers[doc] = short
    
    # Per question results table
    print("## Per-Question Results\n")
    
    # Build header
    header_parts = ["Question", "Runs", "Score", "Score (loose)", "Valid"] + [doc_headers[doc] for doc in sorted_docs]
    print("| " + " | ".join(header_parts) + " |")
    print("|" + "|".join("---" for _ in header_parts) + "|")
    
    total_score = 0.0
    total_score_loose = 0.0
    count = 0
    
    for r in sorted_results:
        row_parts = [
            r.question_id,
            str(r.runs),
            f"{r.stability_score:.1f}",
            f"{r.stability_score_loose:.1f}",
            str(r.structural_valid),
        ]
        for doc in sorted_docs:
            chunks_str = _format_doc_chunks(r.retrieval_context, doc)
            row_parts.append(chunks_str if chunks_str else "")
        
        print("| " + " | ".join(row_parts) + " |")
        
        total_score += r.stability_score
        total_score_loose += r.stability_score_loose
        count += 1
    
    if count > 0:
        avg_parts = [
            "**AVERAGE**",
            "",
            f"**{total_score / count:.1f}**",
            f"**{total_score_loose / count:.1f}**",
            "",
        ]
        for _ in sorted_docs:
            avg_parts.append("")
        print("| " + " | ".join(avg_parts) + " |")
    
    # Detailed breakdown
    print("\n## Detailed Breakdown\n")
    print("| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |")
    print("|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|")
    
    for r in sorted_results:
        print(f"| {r.question_id} | {r.approach_stability:.4f} | {r.approach_stability_canonical:.4f} | {r.applicability_stability:.4f} | {r.applicability_stability_loose:.4f} | {r.recommendation_stability:.4f} | {r.recommendation_stability_loose:.4f} |")
    
    # Aggregate metrics
    print("\n## Aggregate Metrics\n")
    
    total_runs = sum(r.runs for r in results)
    avg_approach = sum(r.approach_stability for r in results) / count if count else 0
    avg_approach_canonical = sum(r.approach_stability_canonical for r in results) / count if count else 0
    avg_applicability = sum(r.applicability_stability for r in results) / count if count else 0
    avg_applicability_loose = sum(r.applicability_stability_loose for r in results) / count if count else 0
    avg_recommendation = sum(r.recommendation_stability for r in results) / count if count else 0
    avg_recommendation_loose = sum(r.recommendation_stability_loose for r in results) / count if count else 0
    
    print("| Component | Strict | Loose |")
    print("|-----------|-------:|------:|")
    print(f"| **Score** | **{total_score / count:.1f}** | **{total_score_loose / count:.1f}** |")
    print(f"| Approach (Jaccard, exact labels) | {avg_approach:.4f} | {avg_approach_canonical:.4f} |")
    print(f"| Applicability (exact values) | {avg_applicability:.4f} | {avg_applicability_loose:.4f} |")
    print(f"| Recommendation (exact values) | {avg_recommendation:.4f} | {avg_recommendation_loose:.4f} |")
    print(f"| | | |")
    print(f"| Total Questions | {count} | |")
    print(f"| Total Runs | {total_runs} | |")
    print(f"| | | |")
    print("*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`\n")
    
    # Label Frequency by Question
    print_label_frequency_table(results)
    
    # Citation Frequency by Question
    print_citation_frequency_table(results)
    
    # Top vs Low Performers
    print_top_vs_low_performers(results)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run stability analysis on promptfoo experiment outputs"
    )
    parser.add_argument(
        "provider",
        help="Provider name (e.g., openai, anthropic)"
    )
    parser.add_argument(
        "--experiment",
        default=DEFAULT_EXPERIMENT,
        help=f"Experiment directory name (default: {DEFAULT_EXPERIMENT})"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show verbose output"
    )
    
    args = parser.parse_args()
    
    # Locate experiment directory
    experiment_dir = EXPERIMENTS_DIR / args.experiment
    if not experiment_dir.exists():
        print(f"Error: Experiment directory not found: {experiment_dir}")
        return
    
    # Find latest run
    run_dir = find_latest_run_dir(experiment_dir)
    if not run_dir:
        print(f"Error: No runs found in {experiment_dir / 'runs'}")
        return
    
    if args.verbose:
        print(f"Using run directory: {run_dir}")
    
    # Verify provider exists
    provider_dirs = get_provider_dirs(run_dir, args.provider)
    if not provider_dirs:
        print(f"Error: No data found for provider '{args.provider}' in {run_dir}")
        # List available providers
        artifacts_dir = run_dir / "artifacts"
        if artifacts_dir.exists():
            for group_dir in artifacts_dir.iterdir():
                if group_dir.is_dir():
                    for q_dir in group_dir.iterdir():
                        if q_dir.is_dir():
                            providers = [d.name for d in q_dir.iterdir() if d.is_dir()]
                            if providers:
                                print(f"  Available providers in {q_dir.name}: {', '.join(providers)}")
                                break
                    break
        return
    
    if args.verbose:
        print(f"Found {len(provider_dirs)} questions for provider '{args.provider}'")
    
    # Analyze each question
    results: list[QuestionScore] = []
    
    for provider_dir, question_id in provider_dirs:
        result = analyze_question_for_provider(provider_dir, question_id)
        if result:
            results.append(result)
    
    # Print results
    print_results(results, args.provider, args.experiment, run_dir)


if __name__ == "__main__":
    main()
