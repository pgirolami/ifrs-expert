"""Run stability scoring on experiment outputs."""

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

from experiments.analysis.stability_scorer import compute_stability_score


@dataclass
class QuestionScore:
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
    # Additional fields for comparison
    top_chunk_score: float = 0.0
    low_chunk_score: float = 0.0
    retrieval_sections: dict = None  # type: ignore[assignment]
    expansion_sections: dict = None  # type: ignore[assignment]


def load_b_response(run_dir: Path) -> dict | None:
    """Load B-response.md file, parsing JSON from markdown."""
    b_response_path = run_dir / "B-response.md"
    if not b_response_path.exists():
        return None

    content = b_response_path.read_text()
    content = content.strip()
    content = content.removeprefix("```json")
    content = content.removeprefix("```")
    content = content.removesuffix("```")
    content = content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None


def extract_chunks(prompt_file: Path) -> list[tuple[str, str, str]]:
    """Extract chunks with doc_uid, section_path and score from A-prompt.txt."""
    content = prompt_file.read_text()
    pattern = r'<chunk id="([^"]+)" doc_uid="([^"]+)" section_path="([^"]+)" score="([^"]+)">'
    matches = re.findall(pattern, content)
    return [(doc_uid, section_path, score) for chunk_id, doc_uid, section_path, score in matches]


def analyze_retrieval(run_dir: Path) -> dict:
    """Extract retrieval metrics from a run directory."""
    prompt_file = run_dir / "A-prompt.txt"
    if not prompt_file.exists():
        return {"top_score": 0.0, "low_score": 0.0, "retrieval_sections": {}, "expansion_sections": {}}

    chunks = extract_chunks(prompt_file)
    retrieval = [(d, s, float(sc)) for d, s, sc in chunks if float(sc) > 0]
    expansion = [(d, s) for d, s, sc in chunks if float(sc) == 0]

    # Group by doc
    retrieval_by_doc = defaultdict(list)
    for doc, sec, sc in retrieval:
        retrieval_by_doc[doc].append((sec, sc))

    all_scores = [sc for d, sec, sc in retrieval]
    top_score = max(all_scores) if all_scores else 0
    sorted_scores = sorted(all_scores, reverse=True)
    low_score = sorted_scores[-1] if sorted_scores else 0

    # Get sections with scores
    retrieval_sections = {doc: sorted(sections, key=lambda x: x[0]) for doc, sections in retrieval_by_doc.items()}

    expansion_by_doc = defaultdict(set)
    for doc, sec in expansion:
        expansion_by_doc[doc].add(sec)
    expansion_sections = {doc: sorted(sections) for doc, sections in expansion_by_doc.items()}

    return {
        "top_score": top_score,
        "low_score": low_score,
        "retrieval_sections": retrieval_sections,
        "expansion_sections": expansion_sections,
    }


def main():
    exp_dir = Path("experiments")
    exp_08_dirs = sorted([d for d in exp_dir.iterdir() if d.is_dir() and d.name.startswith("08")])

    all_results: list[QuestionScore] = []
    all_runs_data: list[tuple[str, dict]] = []  # For aggregate metrics

    for exp_dir_item in exp_08_dirs:
        print(f"\n{'=' * 80}")
        print(f"EXPERIMENT: {exp_dir_item.name}")
        print(f"{'=' * 80}\n")

        run_dirs = sorted([d for d in exp_dir_item.iterdir() if d.is_dir() and "__run" in d.name])

        runs_by_question: dict[str, list[Path]] = {}
        for run_dir in run_dirs:
            parts = run_dir.name.split("__run")
            if len(parts) >= 2:
                question_id = parts[0]
                if question_id not in runs_by_question:
                    runs_by_question[question_id] = []
                runs_by_question[question_id].append(run_dir)

        for question_id, run_paths in sorted(runs_by_question.items()):
            runs = []
            retrieval_data = None
            for run_path in sorted(run_paths):
                b_response = load_b_response(run_path)
                if b_response:
                    runs.append(b_response)
                    all_runs_data.append((question_id, b_response))
                # Get retrieval data from first run
                if retrieval_data is None:
                    retrieval_data = analyze_retrieval(run_path)

            if len(runs) < 2:
                print(f"  [SKIP] {question_id}: only {len(runs)} run(s)")
                continue

            result = compute_stability_score(runs)

            all_results.append(
                QuestionScore(
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
                    top_chunk_score=retrieval_data["top_score"] if retrieval_data else 0.0,
                    low_chunk_score=retrieval_data["low_score"] if retrieval_data else 0.0,
                    retrieval_sections=retrieval_data["retrieval_sections"] if retrieval_data else {},
                    expansion_sections=retrieval_data["expansion_sections"] if retrieval_data else {},
                )
            )

            print(f"  {question_id}: Score={result.stability_score:.1f}, Score(loose)={result.stability_score_loose:.1f}  (runs={len(runs)}, valid={result.diagnostics.structural_validity_flag})")
            print(f"    Approach={result.approach_set_stability:.2f} (mapped={result.approach_set_stability_canonical:.2f}), Applicability={result.applicability_stability:.2f}, Rec={result.recommendation_stability:.2f}")

    # Summary table
    print(f"\n{'=' * 80}")
    print("SUMMARY TABLE")
    print(f"{'=' * 80}")
    print(f"{'Question':<35} {'Runs':>5} {'Score':>7} {'Score(loose)':>12} {'Valid':>5}")
    print(f"{'-' * 35} {'-' * 5} {'-' * 7} {'-' * 12} {'-' * 5}")

    total_score = 0
    total_score_loose = 0
    count = 0
    for r in sorted(all_results, key=lambda x: x.stability_score, reverse=True):
        print(f"{r.question_id:<35} {r.runs:>5} {r.stability_score:>7.1f} {r.stability_score_loose:>12.1f} {r.structural_valid!s:>5}")
        total_score += r.stability_score
        total_score_loose += r.stability_score_loose
        count += 1

    if count > 0:
        print(f"{'-' * 35} {'-' * 5} {'-' * 7} {'-' * 12} {'-' * 5}")
        print(f"{'AVERAGE':<35} {'':>5} {total_score / count:>7.1f} {total_score_loose / count:>12.1f} {'':>5}")

    # Aggregate metrics (treating each run equally)
    print(f"\n{'=' * 80}")
    print("AGGREGATE METRICS (across all runs, treating each run equally)")
    print(f"{'=' * 80}")
    
    if len(all_runs_data) >= 2:
        aggregate = compute_aggregate_metrics(all_runs_data, all_results)
        print(f"\n| Component | Strict | Loose |")
        print(f"|-----------|--------|-------|")
        print(f"| **Score** | **{aggregate['score_strict']:.1f}** | **{aggregate['score_loose']:.1f}** |")
        print(f"| Approach (Jaccard) | {aggregate['approach_original']:.4f} | {aggregate['approach_canonical']:.4f} |")
        print(f"| Applicability | {aggregate['applicability_strict']:.4f} | {aggregate['applicability_loose']:.4f} |")
        print(f"| Recommendation | {aggregate['recommendation_strict']:.4f} | {aggregate['recommendation_loose']:.4f} |")
        print(f"|")
        print(f"| Avg Top Score | {aggregate['avg_top_score']:.4f} |")
        print(f"| Avg Low Score | {aggregate['avg_low_score']:.4f} |")
        print(f"|")
        print(f"| Total Runs | {aggregate['total_runs']} |")
    else:
        print("Not enough runs for aggregate metrics")

    # Top vs Low performers comparison
    print(f"\n{'=' * 80}")
    print("COMPARISON OF TOP VS LOW PERFORMERS")
    print(f"{'=' * 80}")
    
    # Sort by loose score to get top and low performers
    sorted_results = sorted(all_results, key=lambda x: x.stability_score_loose, reverse=True)
    top_performers = [r for r in sorted_results if r.stability_score_loose >= 90.0][:4]
    low_performers = [r for r in sorted_results if r.stability_score_loose < 70.0][-4:]
    
    print(f"\n### Top Performers (loose score >= 90)")
    print(f"| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |")
    print(f"|----------|------|-------|---------------|-----------|-----------|")
    for r in top_performers:
        print(f"| {r.question_id} | {r.runs} | {r.stability_score:.1f} | {r.stability_score_loose:.1f} | {r.top_chunk_score:.4f} | {r.low_chunk_score:.4f} |")
    
    print(f"\n### Low Performers (loose score < 70)")
    print(f"| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |")
    print(f"|----------|------|-------|---------------|-----------|-----------|")
    for r in low_performers:
        print(f"| {r.question_id} | {r.runs} | {r.stability_score:.1f} | {r.stability_score_loose:.1f} | {r.top_chunk_score:.4f} | {r.low_chunk_score:.4f} |")

    # Key observations about retrieval
    if top_performers and low_performers:
        print(f"\n### Key Observations")
        print(f"- Top performers avg top chunk: {sum(r.top_chunk_score for r in top_performers)/len(top_performers):.4f}")
        print(f"- Low performers avg top chunk: {sum(r.top_chunk_score for r in low_performers)/len(low_performers):.4f}")


def normalize_label(label: str) -> str:
    return label.strip().lower()


def canonicalize_label(label: str) -> str:
    mapping = {
        "fair_value_hedge": "fair_value_hedge",
        "cash_flow_hedge": "cash_flow_hedge",
        "net_investment_hedge": "net_investment_hedge",
        "foreign_currency_hedge": "cash_flow_hedge",
        "foreign_currency_component_hedge": "cash_flow_hedge",
        "intragroup_monetary_hedge": "cash_flow_hedge",
        "monetary_item_hedge": "cash_flow_hedge",
    }
    return mapping.get(normalize_label(label), normalize_label(label))


def jaccard_similarity(set_a: set[str], set_b: set[str]) -> float:
    if not set_a and not set_b:
        return 1.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def extract_canonical_labels(run: dict) -> set[str]:
    approaches = run.get("approaches", [])
    return {canonicalize_label(a.get("normalized_label", "")) for a in approaches if a.get("normalized_label")}


def extract_original_labels(run: dict) -> set[str]:
    approaches = run.get("approaches", [])
    return {normalize_label(a.get("normalized_label", "")) for a in approaches if a.get("normalized_label")}


def extract_applicability_loose(run: dict) -> dict[str, str]:
    approaches = run.get("approaches", [])
    result = {}
    for a in approaches:
        label = normalize_label(a.get("normalized_label", ""))
        applicability = a.get("applicability", "")
        if label and applicability:
            normalized = "positive" if applicability.strip() in ("oui", "oui_sous_conditions") else applicability.strip()
            result[label] = normalized
    return result


def extract_applicability_strict(run: dict) -> dict[str, str]:
    approaches = run.get("approaches", [])
    result = {}
    for a in approaches:
        label = normalize_label(a.get("normalized_label", ""))
        applicability = a.get("applicability", "")
        if label and applicability:
            result[label] = applicability.strip()
    return result


def extract_recommendation_strict(run: dict) -> str | None:
    recommendation = run.get("recommendation", {})
    answer = recommendation.get("answer", "")
    return answer.strip() if answer else None


def extract_recommendation_loose(run: dict) -> str | None:
    recommendation = run.get("recommendation", {})
    answer = recommendation.get("answer", "")
    if answer:
        normalized = answer.strip()
        return "positive" if normalized in ("oui", "oui_sous_conditions") else normalized
    return None


def compute_aggregate_metrics(all_runs_data: list[tuple[str, dict]], all_results: list["QuestionScore"]) -> dict:
    """Compute aggregate metrics across ALL runs (treating each run equally)."""
    if len(all_runs_data) < 2:
        return {"error": "Not enough runs"}

    all_original_labels = [extract_original_labels(br) for q, br in all_runs_data]
    all_canonical_labels = [extract_canonical_labels(br) for q, br in all_runs_data]
    all_applicability_strict = [extract_applicability_strict(br) for q, br in all_runs_data]
    all_applicability_loose = [extract_applicability_loose(br) for q, br in all_runs_data]
    all_recommendation_strict = [extract_recommendation_strict(br) for q, br in all_runs_data]
    all_recommendation_loose = [extract_recommendation_loose(br) for q, br in all_runs_data]

    # Compute all pairwise comparisons
    pairwise_approach_orig = []
    pairwise_approach_canonical = []
    pairwise_applicability_strict = []
    pairwise_applicability_loose = []
    pairwise_recommendation_strict = []
    pairwise_recommendation_loose = []

    for i in range(len(all_runs_data)):
        for j in range(i + 1, len(all_runs_data)):
            # Strict
            pairwise_approach_orig.append(jaccard_similarity(all_original_labels[i], all_original_labels[j]))
            # Loose
            pairwise_approach_canonical.append(jaccard_similarity(all_canonical_labels[i], all_canonical_labels[j]))
            # Applicability strict
            shared = set(all_applicability_strict[i].keys()) & set(all_applicability_strict[j].keys())
            if shared:
                matches = sum(1 for k in shared if all_applicability_strict[i][k] == all_applicability_strict[j][k])
                pairwise_applicability_strict.append(matches / len(shared))
            else:
                pairwise_applicability_strict.append(1.0 if (not all_applicability_strict[i] and not all_applicability_strict[j]) else 0.0)
            # Applicability loose
            shared = set(all_applicability_loose[i].keys()) & set(all_applicability_loose[j].keys())
            if shared:
                matches = sum(1 for k in shared if all_applicability_loose[i][k] == all_applicability_loose[j][k])
                pairwise_applicability_loose.append(matches / len(shared))
            else:
                pairwise_applicability_loose.append(1.0 if (not all_applicability_loose[i] and not all_applicability_loose[j]) else 0.0)
            # Recommendation strict
            if all_recommendation_strict[i] and all_recommendation_strict[j]:
                pairwise_recommendation_strict.append(1.0 if all_recommendation_strict[i] == all_recommendation_strict[j] else 0.0)
            else:
                pairwise_recommendation_strict.append(0.0)
            # Recommendation loose
            if all_recommendation_loose[i] and all_recommendation_loose[j]:
                pairwise_recommendation_loose.append(1.0 if all_recommendation_loose[i] == all_recommendation_loose[j] else 0.0)
            else:
                pairwise_recommendation_loose.append(0.0)

    avg_approach_orig = sum(pairwise_approach_orig) / len(pairwise_approach_orig) if pairwise_approach_orig else 1.0
    avg_approach_canonical = sum(pairwise_approach_canonical) / len(pairwise_approach_canonical) if pairwise_approach_canonical else 1.0
    avg_applicability_strict = sum(pairwise_applicability_strict) / len(pairwise_applicability_strict) if pairwise_applicability_strict else 1.0
    avg_applicability_loose = sum(pairwise_applicability_loose) / len(pairwise_applicability_loose) if pairwise_applicability_loose else 1.0
    avg_recommendation_strict = sum(pairwise_recommendation_strict) / len(pairwise_recommendation_strict) if pairwise_recommendation_strict else 1.0
    avg_recommendation_loose = sum(pairwise_recommendation_loose) / len(pairwise_recommendation_loose) if pairwise_recommendation_loose else 1.0

    # Compute scores
    strict_score = 35.0 * avg_approach_orig + 30.0 * avg_applicability_strict + 20.0 * avg_recommendation_strict + 15.0
    strict_score = max(0, min(100, strict_score))

    loose_score = 35.0 * avg_approach_canonical + 30.0 * avg_applicability_loose + 20.0 * avg_recommendation_loose + 15.0
    loose_score = max(0, min(100, loose_score))

    # Get all retrieval scores from results
    all_top_scores = [r.top_chunk_score for r in all_results if r.top_chunk_score > 0]
    all_low_scores = [r.low_chunk_score for r in all_results if r.low_chunk_score > 0]

    return {
        "total_runs": len(all_runs_data),
        "avg_top_score": sum(all_top_scores) / len(all_top_scores) if all_top_scores else 0,
        "avg_low_score": sum(all_low_scores) / len(all_low_scores) if all_low_scores else 0,
        "score_strict": strict_score,
        "score_loose": loose_score,
        "approach_original": avg_approach_orig,
        "approach_canonical": avg_approach_canonical,
        "applicability_strict": avg_applicability_strict,
        "applicability_loose": avg_applicability_loose,
        "recommendation_strict": avg_recommendation_strict,
        "recommendation_loose": avg_recommendation_loose,
    }


if __name__ == "__main__":
    main()
