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
    exp_07_dir = exp_dir / "07_betterbetter_2_stage_processing_json_output"

    if not exp_07_dir.exists():
        print(f"Experiment directory not found: {exp_07_dir}")
        return

    # Collect all unique normalized labels
    all_labels: set[str] = set()

    run_dirs = sorted([d for d in exp_07_dir.iterdir() if d.is_dir() and "__run" in d.name])

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

    # Now let's rerun the stability scoring with canonical labels
    print("\n" + "=" * 80)
    print("RECALCULATING WITH CANONICAL LABELS")
    print("=" * 80)


if __name__ == "__main__":
    main()
