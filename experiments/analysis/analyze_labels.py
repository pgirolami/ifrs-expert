"""Analyze approach labels and create canonical mapping table."""

import json
from pathlib import Path


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


# Semantic groupings - which normalized labels are semantically equivalent
CANONICAL_MAPPING = {
    # Fair value hedge variations
    "fair_value_hedge": "fair_value_hedge",
    # Cash flow hedge variations
    "cash_flow_hedge": "cash_flow_hedge",
    # Net investment hedge variations
    "net_investment_hedge": "net_investment_hedge",
    # These are all semantically similar - hedging the FX risk on an intragroup monetary item
    "foreign_currency_hedge": "intragroup_monetary_hedge",
    "foreign_currency_component_hedge": "intragroup_monetary_hedge",
    "intragroup_monetary_hedge": "intragroup_monetary_hedge",
    "monetary_item_hedge": "intragroup_monetary_hedge",
    # These are specific analysis approaches, not hedge accounting routes
    "cartographie_des_entites_et_devises_fonctionnelles": "analysis_only",
    "choix_entre_creance_de_dividende_et_couverture_d_investissement_net": "analysis_only",
    "qualification_du_solde_comme_reglement_proche_ou_investissement_net": "analysis_only",
}


def main():
    exp_dir = Path("experiments")
    # Analyze experiment 08
    exp_08_dir = exp_dir / "08_treatment_only_approaches"

    if not exp_08_dir.exists():
        print(f"Experiment directory not found: {exp_08_dir}")
        return

    # Collect all unique normalized labels
    all_labels: set[str] = set()

    run_dirs = sorted([d for d in exp_08_dir.iterdir() if d.is_dir() and "__run" in d.name])

    for run_dir in run_dirs:
        b_response = load_b_response(run_dir)
        if not b_response:
            continue

        approaches = b_response.get("approaches", [])
        for approach in approaches:
            norm_label = approach.get("normalized_label", "")
            if norm_label:
                all_labels.add(norm_label)

    # Build mapping table
    print("| normalized_label | canonical_label |")
    print("|------------------|-----------------|")

    for label in sorted(all_labels):
        canonical = CANONICAL_MAPPING.get(label, label)
        print(f"| {label} | {canonical} |")

    print(f"\n**Total unique normalized labels: {len(all_labels)}**")

    # Now collect label frequency by question
    print("\n" + "=" * 80)
    print("LABEL FREQUENCY BY QUESTION")
    print("=" * 80)

    # Group runs by question
    runs_by_question: dict[str, list[Path]] = {}
    for run_dir in run_dirs:
        parts = run_dir.name.split("__run")
        if len(parts) >= 2:
            question_id = parts[0]
            if question_id not in runs_by_question:
                runs_by_question[question_id] = []
            runs_by_question[question_id].append(run_dir)

    # Collect label counts by question
    label_counts: dict[str, dict[str, int]] = {}
    for question_id, run_paths in sorted(runs_by_question.items()):
        label_counts[question_id] = {}
        for run_path in run_paths:
            b_response = load_b_response(run_path)
            if not b_response:
                continue
            approaches = b_response.get("approaches", [])
            for approach in approaches:
                norm_label = approach.get("normalized_label", "")
                if norm_label:
                    label_counts[question_id][norm_label] = label_counts[question_id].get(norm_label, 0) + 1

    # Get all unique labels across all questions
    all_unique_labels = set()
    for counts in label_counts.values():
        all_unique_labels.update(counts.keys())

    # Print table
    print(f"\n| normalized_label | ", end="")
    for q in sorted(label_counts.keys(), key=lambda x: (int(x.split('.')[1].split('_')[0]) if '.' in x and x.split('.')[1].split('_')[0].isdigit() else 999, x)):
        print(f"{q} | ", end="")
    print("Total |")
    print(f"|------------------|", end="")
    for _ in label_counts:
        print("------|", end="")
    print("------|")

    for label in sorted(all_unique_labels):
        print(f"| {label} | ", end="")
        total = 0
        for q in sorted(label_counts.keys(), key=lambda x: (int(x.split('.')[1].split('_')[0]) if '.' in x and x.split('.')[1].split('_')[0].isdigit() else 999, x)):
            count = label_counts[q].get(label, 0)
            print(f"{count} | ", end="")
            total += count
        print(f"{total} |")


if __name__ == "__main__":
    main()
