"""Stability scoring module for repeated applicability analysis outputs."""

from dataclasses import dataclass, field
from itertools import combinations

VALID_RECOMMENDATION_ANSWERS = frozenset({"oui", "non", "oui_sous_conditions"})
VALID_APPLICABILITY_VALUES = frozenset({"oui", "non", "oui_sous_conditions"})

# Canonical mapping: maps variant normalized_labels to their canonical form
# This groups semantically equivalent approaches under one canonical label
CANONICAL_LABEL_MAPPING: dict[str, str] = {
    # Fair value hedge - keep as-is
    "fair_value_hedge": "fair_value_hedge",
    # Cash flow hedge - keep as-is
    "cash_flow_hedge": "cash_flow_hedge",
    # Net investment hedge - keep as-is
    "net_investment_hedge": "net_investment_hedge",
    # All foreign currency/monetary item hedges map to same canonical
    "foreign_currency_hedge": "cash_flow_hedge",
    "foreign_currency_component_hedge": "cash_flow_hedge",
    "intragroup_monetary_hedge": "cash_flow_hedge",
    "monetary_item_hedge": "cash_flow_hedge",
    # Analysis-only approaches (not hedge accounting routes)
    "cartographie_des_entites_et_devises_fonctionnelles": "analysis_only",
    "choix_entre_creance_de_dividende_et_couverture_d_investissement_net": "analysis_only",
    "qualification_du_solde_comme_reglement_proche_ou_investissement_net": "analysis_only",
}


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
    recommendation_distribution: dict[str, int] = field(default_factory=dict)
    applicability_distribution_by_label: dict[str, dict[str, int]] = field(default_factory=dict)


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


def normalize_label(label: str) -> str:
    """Normalize a normalized_label by stripping whitespace and lowercasing."""
    return label.strip().lower()


def canonicalize_label(label: str) -> str:
    """Convert a normalized label to its canonical form.

    Maps variant labels (e.g., 'monetary_item_hedge', 'foreign_currency_hedge')
    to their canonical equivalent (e.g., 'intragroup_monetary_hedge').
    """
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
    """Extract canonical labels from a run's approaches.

    Maps normalized labels to their canonical form for more meaningful comparison.
    """
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
    """Normalize applicability for loose comparison: treat 'oui' and 'oui_sous_conditions' as equivalent."""
    normalized = value.strip().lower()
    if normalized in ("oui", "oui_sous_conditions"):
        return "oui_or_oui_sous_conditions"
    return normalized


def applicability_consistency_loose(run_a: dict, run_b: dict) -> float:
    """Compute pairwise applicability consistency with loose normalization.

    Treats 'oui' and 'oui_sous_conditions' as equivalent (both map to 'oui_or_oui_sous_conditions').
    Only 'non' is considered distinct.
    """
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
    """Compute pairwise recommendation consistency with loose normalization.

    Treats 'oui' and 'oui_sous_conditions' as equivalent (both map to 'oui_or_oui_sous_conditions').
    Only 'non' is considered distinct.
    """
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


def compute_stability_score(
    runs: list[dict],
    expected_normalized_labels: set[str] | None = None,
) -> StabilityResult:
    """Compute stability score for a set of repeated applicability analysis runs."""
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
        # Original normalized label Jaccard
        pairwise_jaccards.append(
            jaccard_similarity(
                extract_normalized_labels(run_a),
                extract_normalized_labels(run_b),
            ),
        )
        # Canonical label Jaccard (maps variants to canonical forms)
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

    # Compute stability components
    approach_set_stability = avg_jaccard  # Original normalized
    approach_set_stability_canonical = avg_jaccard_canonical  # Canonical mapping
    applicability_stability = avg_applicability
    recommendation_stability = avg_recommendation
    applicability_stability_loose = avg_applicability_loose
    recommendation_stability_loose = avg_recommendation_loose
    structural_validity_stability = 1.0 if all(is_structurally_valid(r) for r in runs) else 0.0

    # Final score (strict)
    stability_score = 35.0 * approach_set_stability + 30.0 * applicability_stability + 20.0 * recommendation_stability + 15.0 * structural_validity_stability
    stability_score = max(0.0, min(100.0, stability_score))

    # Final score (loose) - treats "oui" and "oui_sous_conditions" as equivalent
    stability_score_loose = 35.0 * approach_set_stability + 30.0 * applicability_stability_loose + 20.0 * recommendation_stability_loose + 15.0 * structural_validity_stability
    stability_score_loose = max(0.0, min(100.0, stability_score_loose))

    # Canonical approach score (using canonical label mapping)
    stability_score_canonical = 35.0 * approach_set_stability_canonical + 30.0 * applicability_stability_loose + 20.0 * recommendation_stability_loose + 15.0 * structural_validity_stability
    stability_score_canonical = max(0.0, min(100.0, stability_score_canonical))

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

    # Recommendation distribution
    recommendation_dist: dict[str, int] = {}
    for run in runs:
        answer = extract_recommendation_answer(run)
        if answer in VALID_RECOMMENDATION_ANSWERS:
            recommendation_dist[answer] = recommendation_dist.get(answer, 0) + 1

    # Applicability distribution by label
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


if __name__ == "__main__":
    # Example with 3 fake applicability analysis runs
    fake_runs = [
        {
            "assumptions_fr": ["Assumption 1"],
            "recommendation": {"answer": "oui", "justification": "Justification for yes."},
            "approaches": [
                {
                    "id": "approach_1",
                    "normalized_label": "ifrs_15_product_revenue",
                    "label_fr": "IFRS 15 - Produits",
                    "applicability": "oui",
                    "reasoning_fr": "Applies because revenue recognition criteria met.",
                    "conditions_fr": ["Condition 1"],
                    "practical_implication_fr": "Impact: Recognize revenue now.",
                    "references": [{"section": "IFRS 15.38", "excerpt": "Revenue is recognized when..."}],
                },
                {
                    "id": "approach_2",
                    "normalized_label": "ifrs_16_lease",
                    "label_fr": "IFRS 16 - Location",
                    "applicability": "non",
                    "reasoning_fr": "Not applicable as no lease involved.",
                    "conditions_fr": [],
                    "practical_implication_fr": "No impact.",
                    "references": [],
                },
            ],
            "operational_points_fr": ["Point 1"],
        },
        {
            "assumptions_fr": ["Assumption A"],
            "recommendation": {
                "answer": "oui",
                "justification": "Justification for yes, slightly different.",
            },
            "approaches": [
                {
                    "id": "approach_1",
                    "normalized_label": "ifrs_15_product_revenue",
                    "label_fr": "IFRS 15 - Produits",
                    "applicability": "oui",
                    "reasoning_fr": "Applies because criteria are met.",
                    "conditions_fr": ["Condition 1"],
                    "practical_implication_fr": "Revenue recognition applies.",
                    "references": [{"section": "IFRS 15.38", "excerpt": "Revenue is recognized when..."}],
                },
                {
                    "id": "approach_2",
                    "normalized_label": "ifrs_16_lease",
                    "label_fr": "IFRS 16 - Location",
                    "applicability": "non",
                    "reasoning_fr": "No lease present.",
                    "conditions_fr": [],
                    "practical_implication_fr": "No impact.",
                    "references": [],
                },
            ],
            "operational_points_fr": ["Point A"],
        },
        {
            "assumptions_fr": ["Assumption B"],
            "recommendation": {
                "answer": "oui_sous_conditions",
                "justification": "Yes but with conditions.",
            },
            "approaches": [
                {
                    "id": "approach_1",
                    "normalized_label": "ifrs_15_product_revenue",
                    "label_fr": "IFRS 15 - Produits",
                    "applicability": "oui_sous_conditions",
                    "reasoning_fr": "Applies with specific conditions.",
                    "conditions_fr": ["Condition X", "Condition Y"],
                    "practical_implication_fr": "Revenue with conditions.",
                    "references": [{"section": "IFRS 15.38", "excerpt": "Revenue is recognized when..."}],
                },
                {
                    "id": "approach_3",
                    "normalized_label": "ifrs_9_financial_instruments",
                    "label_fr": "IFRS 9 - Instruments",
                    "applicability": "non",
                    "reasoning_fr": "Not relevant.",
                    "conditions_fr": [],
                    "practical_implication_fr": "No impact.",
                    "references": [],
                },
            ],
            "operational_points_fr": ["Point B"],
        },
    ]

    result = compute_stability_score(fake_runs)

    d = result.diagnostics
