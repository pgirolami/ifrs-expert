"""Shared utilities for B-response markdown conversion."""

from datetime import datetime


def _format_applicability(value: str) -> str:
    """Format applicability value to be user-friendly.

    Converts 'oui_sous_conditions' -> 'OUI SOUS CONDITIONS'
    """
    return value.replace("_", " ").upper()


def _build_header(question: str | None, doc_uids: list[str] | None) -> list[str]:
    """Build the header section."""
    now = datetime.now().astimezone().strftime("%Y-%m-%d")
    lines = [
        "# Analyse d'une question comptable",
        "",
        f"**Date**: {now}",
        "",
        "**Question**:",
        f">{question}",
        "",
        "**Documentation consultée**",
    ]

    if doc_uids:
        lines.extend(f"   - `{uid}`" for uid in doc_uids)
    else:
        lines.append("   - (documentation non disponible)")

    return lines


def _build_assumptions(assumptions: list[str]) -> list[str]:
    """Build the assumptions section."""
    lines = [
        "",
        "## Hypothèses",
    ]
    lines.extend(f"   - {line}" for line in assumptions)
    return lines


def _build_recommendation(recommendation: dict, operational_points: list[str]) -> list[str]:
    """Build the recommendation section."""
    answer = _format_applicability(recommendation.get("answer", "N/A"))
    justification = recommendation.get("justification", "")

    lines = [
        "",
        "## Recommandation",
        "",
        f"**{answer}**",
        "",
        f"{justification}",
        "",
    ]

    if operational_points:
        lines.extend(["## Points Opérationnels", ""])
        lines.extend(f"   - {point}" for point in operational_points)
        lines.append("")

    return lines


def _build_approaches_summary(approaches: list[dict]) -> list[str]:
    """Build the approaches summary table."""
    lines = [
        "",
        "## Approches évaluées",
        "",
        "| Approche | Applicabilité | Conditions |",
        "| --- | --- | --- |",
    ]

    for idx, approach in enumerate(approaches, start=1):
        label_fr = approach.get("label_fr", "N/A")
        applicability = _format_applicability(approach.get("applicability", "N/A"))
        conditions = approach.get("conditions_fr", [])

        conditions_text = "<br>".join(f"- {c}" for c in conditions) if conditions else "- (non spécifiées)"
        label_escaped = label_fr.replace("|", "\\|")
        conditions_escaped = conditions_text.replace("|", "\\|")

        lines.append(f"| {idx}. {label_escaped} | {applicability} | {conditions_escaped} |")

    return lines


def _build_approach_detail(idx: int, approach: dict) -> list[str]:
    """Build detail section for a single approach."""
    label_fr = approach.get("label_fr", "N/A")
    applicability = _format_applicability(approach.get("applicability", "N/A"))
    conditions = approach.get("conditions_fr", [])
    reasoning = approach.get("reasoning_fr", "")
    practical_implication = approach.get("practical_implication_fr", "")
    references = approach.get("references", [])

    lines = [
        "",
        f"### {idx}. {label_fr}",
        f"**Applicabilité**: {_format_applicability(applicability)}",
        "",
        "**Conditions**:",
    ]

    if conditions:
        lines.extend(f"   - {c}" for c in conditions)
    else:
        lines.append("   - (conditions non spécifiées)")

    lines.extend(
        [
            "",
            "**Raisonnment**:",
            reasoning or "(raisonnement non disponible)",
            "",
            f"**Implications pratiques**: {practical_implication or '(implications non spécifiées)'}",
            "",
            "**Référence**:",
        ]
    )

    if references:
        for ref in references:
            section = ref.get("section", "")
            excerpt = ref.get("excerpt", "")
            lines.append(f" - {section}")
            lines.append(f"    >{excerpt}")
    else:
        lines.append("   - (référence non disponible)")

    return lines


def convert_json_to_markdown(
    b_json: dict,
    question: str | None = None,
    doc_uids: list[str] | None = None,
) -> str:
    """Convert B-response JSON to French markdown format.

    Args:
        b_json: Parsed JSON response
        question: The original question (optional)
        doc_uids: List of document UIDs consulted (optional)

    Returns:
        Markdown formatted string in French
    """
    assumptions = b_json.get("assumptions_fr", [])
    recommendation = b_json.get("recommendation", {})
    operational_points = b_json.get("operational_points_fr", [])
    approaches = b_json.get("approaches", [])

    lines = []
    lines.extend(_build_header(question, doc_uids))
    lines.extend(_build_assumptions(assumptions))
    lines.extend(_build_recommendation(recommendation, operational_points))
    lines.extend(_build_approaches_summary(approaches))

    for idx, approach in enumerate(approaches, start=1):
        lines.extend(_build_approach_detail(idx, approach))

    return "\n".join(lines)
