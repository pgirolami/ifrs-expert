"""Generate chunk comparison for high vs low performers and aggregated metrics."""

import json
import re
from pathlib import Path
from collections import defaultdict
from itertools import combinations


def extract_chunks(prompt_file: Path) -> list[tuple[str, str, str]]:
    """Extract chunks with doc_uid, section_path and score."""
    content = prompt_file.read_text()
    pattern = r'<chunk id="([^"]+)" doc_uid="([^"]+)" section_path="([^"]+)" score="([^"]+)">'
    matches = re.findall(pattern, content)
    return [(doc_uid, section_path, score) for chunk_id, doc_uid, section_path, score in matches]


def load_b_response(run_dir: Path) -> dict | None:
    """Load B-response.md file, parsing JSON from markdown."""
    b_response_path = run_dir / "B-response.md"
    if not b_response_path.exists():
        return None
    content = b_response_path.read_text().strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    try:
        return json.loads(content.strip())
    except json.JSONDecodeError:
        return None


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
    return {
        canonicalize_label(a.get("normalized_label", ""))
        for a in approaches
        if a.get("normalized_label")
    }


def extract_original_labels(run: dict) -> set[str]:
    """Extract original normalized labels (strict - no canonical mapping)."""
    approaches = run.get("approaches", [])
    return {
        normalize_label(a.get("normalized_label", ""))
        for a in approaches
        if a.get("normalized_label")
    }


def extract_applicability_loose(run: dict) -> dict[str, str]:
    """Extract applicability values treating oui/oui_sous_conditions as equivalent."""
    approaches = run.get("approaches", [])
    result = {}
    for a in approaches:
        label = normalize_label(a.get("normalized_label", ""))
        applicability = a.get("applicability", "")
        if label and applicability:
            # Treat oui and oui_sous_conditions as the same
            normalized = (
                "positive"
                if applicability.strip() in ("oui", "oui_sous_conditions")
                else applicability.strip()
            )
            result[label] = normalized
    return result


def extract_applicability_strict(run: dict) -> dict[str, str]:
    """Extract applicability values with strict distinction."""
    approaches = run.get("approaches", [])
    result = {}
    for a in approaches:
        label = normalize_label(a.get("normalized_label", ""))
        applicability = a.get("applicability", "")
        if label and applicability:
            result[label] = applicability.strip()
    return result


def extract_recommendation_strict(run: dict) -> str | None:
    """Extract recommendation answer strictly."""
    recommendation = run.get("recommendation", {})
    answer = recommendation.get("answer", "")
    return answer.strip() if answer else None


def extract_recommendation_loose(run: dict) -> str | None:
    """Extract recommendation answer with loose normalization."""
    recommendation = run.get("recommendation", {})
    answer = recommendation.get("answer", "")
    if answer:
        normalized = answer.strip()
        return "positive" if normalized in ("oui", "oui_sous_conditions") else normalized
    return None


def applicability_consistency_loose(run_a: dict, run_b: dict) -> float:
    map_a = extract_applicability_loose(run_a)
    map_b = extract_applicability_loose(run_b)
    shared = set(map_a.keys()) & set(map_b.keys())
    if not shared:
        return 1.0 if (not map_a and not map_b) else 0.0
    matches = sum(1 for k in shared if map_a[k] == map_b[k])
    return matches / len(shared)


def applicability_consistency_strict(run_a: dict, run_b: dict) -> float:
    map_a = extract_applicability_strict(run_a)
    map_b = extract_applicability_strict(run_b)
    shared = set(map_a.keys()) & set(map_b.keys())
    if not shared:
        return 1.0 if (not map_a and not map_b) else 0.0
    matches = sum(1 for k in shared if map_a[k] == map_b[k])
    return matches / len(shared)


def recommendation_consistency_strict(run_a: dict, run_b: dict) -> float:
    rec_a = extract_recommendation_strict(run_a)
    rec_b = extract_recommendation_strict(run_b)
    if rec_a is None or rec_b is None:
        return 0.0
    return 1.0 if rec_a == rec_b else 0.0


def recommendation_consistency_loose(run_a: dict, run_b: dict) -> float:
    rec_a = extract_recommendation_loose(run_a)
    rec_b = extract_recommendation_loose(run_b)
    if rec_a is None or rec_b is None:
        return 0.0
    return 1.0 if rec_a == rec_b else 0.0


def compute_stability(runs: list[dict]) -> dict:
    """Compute stability metrics for a set of runs."""
    if len(runs) < 2:
        return {"score": 100.0, "approach_canonical": 1.0, "runs": len(runs)}

    # Original (strict) approach Jaccard
    pairwise_jaccards_orig = []
    # Canonical (loose) approach Jaccard
    pairwise_jaccards_canonical = []
    # Applicability strict
    pairwise_applicability_strict = []
    # Applicability loose
    pairwise_applicability_loose = []
    # Recommendation strict
    pairwise_recommendation_strict = []
    # Recommendation loose
    pairwise_recommendation_loose = []

    for run_a, run_b in combinations(runs, 2):
        pairwise_jaccards_orig.append(
            jaccard_similarity(
                extract_original_labels(run_a),
                extract_original_labels(run_b),
            )
        )
        pairwise_jaccards_canonical.append(
            jaccard_similarity(
                extract_canonical_labels(run_a),
                extract_canonical_labels(run_b),
            )
        )
        pairwise_applicability_strict.append(applicability_consistency_strict(run_a, run_b))
        pairwise_applicability_loose.append(applicability_consistency_loose(run_a, run_b))
        pairwise_recommendation_strict.append(recommendation_consistency_strict(run_a, run_b))
        pairwise_recommendation_loose.append(recommendation_consistency_loose(run_a, run_b))

    avg_jaccard_orig = (
        sum(pairwise_jaccards_orig) / len(pairwise_jaccards_orig) if pairwise_jaccards_orig else 1.0
    )
    avg_jaccard_canonical = (
        sum(pairwise_jaccards_canonical) / len(pairwise_jaccards_canonical)
        if pairwise_jaccards_canonical
        else 1.0
    )
    avg_applicability_strict = (
        sum(pairwise_applicability_strict) / len(pairwise_applicability_strict)
        if pairwise_applicability_strict
        else 1.0
    )
    avg_applicability_loose = (
        sum(pairwise_applicability_loose) / len(pairwise_applicability_loose)
        if pairwise_applicability_loose
        else 1.0
    )
    avg_recommendation_strict = (
        sum(pairwise_recommendation_strict) / len(pairwise_recommendation_strict)
        if pairwise_recommendation_strict
        else 1.0
    )
    avg_recommendation_loose = (
        sum(pairwise_recommendation_loose) / len(pairwise_recommendation_loose)
        if pairwise_recommendation_loose
        else 1.0
    )

    # Strict score (original approach + strict applicability + strict recommendation)
    strict_score = (
        35.0 * avg_jaccard_orig
        + 30.0 * avg_applicability_strict
        + 20.0 * avg_recommendation_strict
        + 15.0  # structural validity assumed 1.0
    )
    strict_score = max(0, min(100, strict_score))

    # Loose score (canonical approach + loose applicability + loose recommendation)
    loose_score = (
        35.0 * avg_jaccard_canonical
        + 30.0 * avg_applicability_loose
        + 20.0 * avg_recommendation_loose
        + 15.0
    )
    loose_score = max(0, min(100, loose_score))

    return {
        "score_strict": strict_score,
        "score_loose": loose_score,
        "approach_original": avg_jaccard_orig,
        "approach_canonical": avg_jaccard_canonical,
        "applicability_strict": avg_applicability_strict,
        "applicability_loose": avg_applicability_loose,
        "recommendation_strict": avg_recommendation_strict,
        "recommendation_loose": avg_recommendation_loose,
        "runs": len(runs),
    }


def analyze_question(exp_dir: Path, question: str) -> dict:
    """Analyze a single question across all its runs."""
    run_dirs = sorted(
        [d for d in exp_dir.iterdir() if d.is_dir() and d.name.startswith(f"{question}_k=")]
    )

    if not run_dirs:
        return {"error": "No runs found"}

    # Get top/low scores from first run
    first_run = run_dirs[0]
    prompt_file = first_run / "A-prompt.txt"

    if not prompt_file.exists():
        return {"error": "No prompt file"}

    chunks = extract_chunks(prompt_file)
    retrieval = [(d, s, float(sc)) for d, s, sc in chunks if float(sc) > 0]
    expansion = [(d, s) for d, s, sc in chunks if float(sc) == 0]

    # Group by doc
    retrieval_by_doc = defaultdict(list)
    for doc, sec, sc in retrieval:
        retrieval_by_doc[doc].append((sec, sc))

    # Get top score (max) and low score (min of top 5)
    all_scores = [sc for d, sec, sc in retrieval]
    top_score = max(all_scores) if all_scores else 0
    sorted_scores = sorted(all_scores, reverse=True)
    low_score = sorted_scores[-1] if sorted_scores else 0

    # Get all sections (alphabetical) with scores - keep as list of tuples
    retrieval_sections_with_scores = defaultdict(list)
    for doc, sec, sc in retrieval:
        retrieval_sections_with_scores[doc].append((sec, sc))

    all_expansion_sections = defaultdict(set)
    for doc, sec in expansion:
        all_expansion_sections[doc].add(sec)

    # Load B-responses for stability
    b_responses = []
    for rd in run_dirs:
        br = load_b_response(rd)
        if br:
            b_responses.append(br)

    stability = (
        compute_stability(b_responses)
        if b_responses
        else {"score": 0, "approach_canonical": 0, "runs": 0}
    )

    return {
        "question": question,
        "runs": len(run_dirs),
        "top_score": top_score,
        "low_score": low_score,
        "retrieval_sections": {
            doc: sorted(sections) for doc, sections in retrieval_sections_with_scores.items()
        },
        "expansion_sections": {
            doc: sorted(sections) for doc, sections in all_expansion_sections.items()
        },
        "stability_score": stability.get("score", 0),
        "approach_canonical": stability.get("approach_canonical", 0),
    }


def generate_markdown_table(questions_data: list[dict]) -> str:
    """Generate markdown table for all questions with non-expansion chunk scores."""
    lines = []
    lines.append("## Retrieval Analysis\n")
    lines.append("\n### Top Retrieval Chunks by Question\n")
    lines.append("| Question | Runs | Top Score | Low Score |")
    lines.append("|----------|------|-----------|-----------|")

    for q in questions_data:
        if "error" in q:
            continue
        lines.append(
            f"| {q['question']} | {q['runs']} | {q['top_score']:.4f} | {q['low_score']:.4f} |"
        )

    lines.append("\n### IFRS 9 Retrieval Sections (alphabetical, with scores)\n")
    lines.append("| Question | Section | Score |")
    lines.append("|----------|---------|-------|")
    for q in questions_data:
        if "error" in q:
            continue
        sections = q["retrieval_sections"].get("ifrs-9-financial-instruments 2025 required", [])
        for sec, sc in sorted(sections, key=lambda x: x[0]):
            lines.append(f"| {q['question']} | {sec} | {sc:.4f} |")

    lines.append("\n### IFRIC 16 Retrieval Sections (alphabetical, with scores)\n")
    lines.append("| Question | Section | Score |")
    lines.append("|----------|---------|-------|")
    for q in questions_data:
        if "error" in q:
            continue
        sections = q["retrieval_sections"].get(
            "ifric-16-hedges-of-a-net-investment-in-a-foreign-operation", []
        )
        for sec, sc in sorted(sections, key=lambda x: x[0]):
            lines.append(f"| {q['question']} | {sec} | {sc:.4f} |")

    return "\n".join(lines)


def generate_expansion_table(questions_data: list[dict]) -> str:
    """Generate markdown table for expansion sections."""
    lines = []
    lines.append("\n## Expansion Sections\n")
    lines.append("| Question | Document | Sections |")
    lines.append("|----------|----------|----------|")

    for q in questions_data:
        if "error" in q:
            continue
        for doc, sections in q["expansion_sections"].items():
            doc_short = doc.split()[0]  # Shorten document name
            lines.append(f"| {q['question']} | {doc_short} | {', '.join(sections)} |")

    return "\n".join(lines)


def generate_expansion_table(questions_data: list[dict]) -> str:
    """Generate markdown table for expansion sections."""
    lines = []
    lines.append("\n## Expansion Sections\n")
    lines.append("| Question | IFRS 9 Expansion | IFRIC 16 Expansion |")
    lines.append("|----------|------------------|--------------------|")

    for q in questions_data:
        if "error" in q:
            continue

        ifrs9_exp = ", ".join(
            q["expansion_sections"].get("ifrs-9-financial-instruments 2025 required", [])
        )
        ifric_exp = ", ".join(
            q["expansion_sections"].get(
                "ifric-16-hedges-of-a-net-investment-in-a-foreign-operation", []
            )
        )

        lines.append(f"| {q['question']} | {ifrs9_exp} | {ifric_exp} |")

    return "\n".join(lines)


def compute_aggregate_metrics(questions_data: list[dict]) -> dict:
    """Compute aggregate metrics across ALL runs of ALL questions (treating each run equally)."""
    # Collect all runs across all questions
    all_runs_data = []  # Each element is a (question_id, run_data) tuple

    for q in questions_data:
        if "error" in q:
            continue
        question = q["question"]
        # Get all runs for this question
        exp_dir = Path("experiments/07_betterbetter_2_stage_processing_json_output")
        run_dirs = sorted(
            [d for d in exp_dir.iterdir() if d.is_dir() and d.name.startswith(f"{question}_k=")]
        )

        for rd in run_dirs:
            br = load_b_response(rd)
            if br:
                all_runs_data.append((question, br))

    if len(all_runs_data) < 2:
        return {"error": "Not enough runs"}

    # Extract all labels/applicability/recommendation
    all_original_labels = [extract_original_labels(br) for q, br in all_runs_data]
    all_canonical_labels = [extract_canonical_labels(br) for q, br in all_runs_data]
    all_applicability_strict = [extract_applicability_strict(br) for q, br in all_runs_data]
    all_applicability_loose = [extract_applicability_loose(br) for q, br in all_runs_data]
    all_recommendation_strict = [extract_recommendation_strict(br) for q, br in all_runs_data]
    all_recommendation_loose = [extract_recommendation_loose(br) for q, br in all_runs_data]

    # Compute all pairwise comparisons (strict)
    pairwise_approach_orig = []
    pairwise_applicability_strict = []
    pairwise_recommendation_strict = []
    # Compute all pairwise comparisons (loose)
    pairwise_approach_canonical = []
    pairwise_applicability_loose = []
    pairwise_recommendation_loose = []

    for i in range(len(all_runs_data)):
        for j in range(i + 1, len(all_runs_data)):
            # Strict
            pairwise_approach_orig.append(
                jaccard_similarity(all_original_labels[i], all_original_labels[j])
            )
            # Loose
            pairwise_approach_canonical.append(
                jaccard_similarity(all_canonical_labels[i], all_canonical_labels[j])
            )
            # Applicability strict
            shared = set(all_applicability_strict[i].keys()) & set(
                all_applicability_strict[j].keys()
            )
            if shared:
                matches = sum(
                    1
                    for k in shared
                    if all_applicability_strict[i][k] == all_applicability_strict[j][k]
                )
                pairwise_applicability_strict.append(matches / len(shared))
            else:
                pairwise_applicability_strict.append(
                    1.0
                    if (not all_applicability_strict[i] and not all_applicability_strict[j])
                    else 0.0
                )
            # Applicability loose
            shared = set(all_applicability_loose[i].keys()) & set(all_applicability_loose[j].keys())
            if shared:
                matches = sum(
                    1
                    for k in shared
                    if all_applicability_loose[i][k] == all_applicability_loose[j][k]
                )
                pairwise_applicability_loose.append(matches / len(shared))
            else:
                pairwise_applicability_loose.append(
                    1.0
                    if (not all_applicability_loose[i] and not all_applicability_loose[j])
                    else 0.0
                )
            # Recommendation strict
            if all_recommendation_strict[i] and all_recommendation_strict[j]:
                pairwise_recommendation_strict.append(
                    1.0 if all_recommendation_strict[i] == all_recommendation_strict[j] else 0.0
                )
            else:
                pairwise_recommendation_strict.append(0.0)
            # Recommendation loose
            if all_recommendation_loose[i] and all_recommendation_loose[j]:
                pairwise_recommendation_loose.append(
                    1.0 if all_recommendation_loose[i] == all_recommendation_loose[j] else 0.0
                )
            else:
                pairwise_recommendation_loose.append(0.0)

    # Compute averages
    avg_approach_orig = (
        sum(pairwise_approach_orig) / len(pairwise_approach_orig) if pairwise_approach_orig else 1.0
    )
    avg_approach_canonical = (
        sum(pairwise_approach_canonical) / len(pairwise_approach_canonical)
        if pairwise_approach_canonical
        else 1.0
    )
    avg_applicability_strict = (
        sum(pairwise_applicability_strict) / len(pairwise_applicability_strict)
        if pairwise_applicability_strict
        else 1.0
    )
    avg_applicability_loose = (
        sum(pairwise_applicability_loose) / len(pairwise_applicability_loose)
        if pairwise_applicability_loose
        else 1.0
    )
    avg_recommendation_strict = (
        sum(pairwise_recommendation_strict) / len(pairwise_recommendation_strict)
        if pairwise_recommendation_strict
        else 1.0
    )
    avg_recommendation_loose = (
        sum(pairwise_recommendation_loose) / len(pairwise_recommendation_loose)
        if pairwise_recommendation_loose
        else 1.0
    )

    # Strict score
    strict_score = (
        35.0 * avg_approach_orig
        + 30.0 * avg_applicability_strict
        + 20.0 * avg_recommendation_strict
        + 15.0
    )
    strict_score = max(0, min(100, strict_score))

    # Loose score
    loose_score = (
        35.0 * avg_approach_canonical
        + 30.0 * avg_applicability_loose
        + 20.0 * avg_recommendation_loose
        + 15.0
    )
    loose_score = max(0, min(100, loose_score))

    # Get all retrieval scores
    all_top_scores = [q["top_score"] for q in questions_data if "error" not in q]
    all_low_scores = [q["low_score"] for q in questions_data if "error" not in q]

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


def main():
    exp_dir = Path("experiments/07_betterbetter_2_stage_processing_json_output")

    # Analyze all questions (extract question IDs from run directories)
    run_dirs = [d for d in exp_dir.iterdir() if d.is_dir() and "__run" in d.name]
    question_ids = sorted(set(d.name.split("_k=")[0] for d in run_dirs))

    print(f"Analyzing {len(question_ids)} questions...")

    questions_data = []
    for qid in question_ids:
        result = analyze_question(exp_dir, qid)
        questions_data.append(result)
        print(
            f"  {qid}: top={result.get('top_score', 0):.4f}, low={result.get('low_score', 0):.4f}, runs={result.get('runs', 0)}"
        )

    # Generate markdown output
    print("\n" + "=" * 80)
    print("MARKDOWN OUTPUT")
    print("=" * 80)

    print(generate_markdown_table(questions_data))
    print(generate_expansion_table(questions_data))

    # Aggregate metrics - computed across ALL runs (each run treated equally)
    agg = compute_aggregate_metrics(questions_data)
    print(f"\n## Aggregate Metrics (across all {agg['total_runs']} runs)")
    print(f"| Metric | Strict | Loose |")
    print(f"|--------|--------|------|")
    print(f"| Score | {agg['score_strict']:.1f} | {agg['score_loose']:.1f} |")
    print(f"| Approach | {agg['approach_original']:.4f} | {agg['approach_canonical']:.4f} |")
    print(
        f"| Applicability | {agg['applicability_strict']:.4f} | {agg['applicability_loose']:.4f} |"
    )
    print(
        f"| Recommendation | {agg['recommendation_strict']:.4f} | {agg['recommendation_loose']:.4f} |"
    )
    print(f"|")
    print(f"| Avg Top Score | {agg['avg_top_score']:.4f} |")
    print(f"| Avg Low Score | {agg['avg_low_score']:.4f} |")


if __name__ == "__main__":
    main()
