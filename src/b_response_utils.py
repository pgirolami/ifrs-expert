"""Shared utilities for B-response markdown conversion."""

from datetime import datetime


def _format_applicability(value: str) -> str:
    """Format applicability value to be user-friendly.

    Converts 'oui_sous_conditions' -> 'OUI SOUS CONDITIONS'
    """
    return value.replace("_", " ").upper()


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
    # Get date in YYYY-MM-DD format (local timezone)
    now = datetime.now().astimezone().strftime("%Y-%m-%d")

    # Get assumptions
    assumptions = b_json.get("assumptions_fr", [])

    # Get recommendation
    recommendation = b_json.get("recommendation", {})
    answer = _format_applicability(recommendation.get("answer", "N/A"))
    justification = recommendation.get("justification", "")

    # Get approaches
    approaches = b_json.get("approaches", [])

    # Build markdown
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

    # Add document UIDs if provided
    if doc_uids:
        lines.extend(f"   - `{uid}`" for uid in doc_uids)
    else:
        lines.append("   - (documentation non disponible)")

    lines.extend(
        [
            "",
            "## Hypothèses",
        ]
    )

    # Add assumptions
    lines.extend(f"   - {line}" for line in assumptions)

    # Get operational points
    operational_points = b_json.get("operational_points_fr", [])

    lines.extend(
        [
            "",
            "## Recommandation",
            "",
            f"**{answer}**",
            "",
            f"{justification}",
            "",
        ]
    )

    # Add operational points if available
    if operational_points:
        lines.extend(["## Points Opérationnels", ""])
        lines.extend(f"   - {point}" for point in operational_points)
        lines.append("")

    lines.extend(["## Approches évaluées", ""])

    # Build summary table
    lines.append("| Approche | Applicabilité | Conditions |")
    lines.append("| --- | --- | --- |")

    for idx, approach in enumerate(approaches, start=1):
        label_fr = approach.get("label_fr", "N/A")
        applicability = _format_applicability(approach.get("applicability", "N/A"))
        conditions = approach.get("conditions_fr", [])

        # Format conditions as bullet points
        conditions_text = "<br>".join(f"- {c}" for c in conditions) if conditions else "- (non spécifiées)"

        # Escape pipes in content for markdown table
        label_escaped = label_fr.replace("|", "\\|")
        conditions_escaped = conditions_text.replace("|", "\\|")

        lines.append(f"| {idx}. {label_escaped} | {applicability} | {conditions_escaped} |")

    lines.append("")

    # Iterate over approaches (detail sections)
    for idx, approach in enumerate(approaches, start=1):
        label_fr = approach.get("label_fr", "N/A")
        applicability = _format_applicability(approach.get("applicability", "N/A"))
        conditions = approach.get("conditions_fr", [])
        reasoning = approach.get("reasoning_fr", "")
        practical_implication = approach.get("practical_implication_fr", "")
        references = approach.get("references", [])

        lines.append(f"### {idx}. {label_fr}")
        lines.append(f"**Applicabilité**: {_format_applicability(applicability)}")
        lines.append("")
        lines.append("**Conditions**:")
        if conditions:
            lines.extend(f"   - {c}" for c in conditions)
        else:
            lines.append("   - (conditions non spécifiées)")
        lines.append("")
        lines.append("**Raisonnment**:")
        lines.append(reasoning or "(raisonnement non disponible)")
        lines.append("")
        lines.append(f"**Implications pratiques**: {practical_implication or '(implications non spécifiées)'}")
        lines.append("")
        lines.append("**Référence**:")

        if references:
            for ref in references:
                section = ref.get("section", "")
                excerpt = ref.get("excerpt", "")
                lines.append(f" - {section}")
                lines.append(f"    >{excerpt}")
        else:
            lines.append("   - (référence non disponible)")

        lines.append("")

    return "\n".join(lines)
