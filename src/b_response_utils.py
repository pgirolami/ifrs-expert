"""Shared utilities for B-response markdown conversion."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias

from src.models.document import infer_document_kind, infer_exact_document_type

JSONValue: TypeAlias = "str | int | float | bool | None | list[JSONValue] | dict[str, JSONValue]"


def _format_applicability(value: str) -> str:
    """Format applicability value to be user-friendly.

    Converts 'oui_sous_conditions' -> 'OUI SOUS CONDITIONS'
    """
    return value.replace("_", " ").upper()


def _group_by_family(doc_uids: list[str]) -> dict[str, list[str]]:
    """Group document UIDs by exact document_type with document_kind labels."""
    families: dict[str, list[str]] = defaultdict(list)
    other_docs: list[str] = []

    for doc_uid in doc_uids:
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        if document_type is not None:
            bucket = f"{document_type} ({document_kind})" if document_kind is not None else document_type
            families[bucket].append(doc_uid)
            continue
        other_docs.append(doc_uid)

    if other_docs:
        families["Autres"].extend(other_docs)

    return dict(families)


def _build_header(
    question: str | None,
    doc_uids: list[str] | None,
    authority_doc_uids: list[str] | None = None,
    primary_accounting_issue: str | None = None,
) -> list[str]:
    """Build the header section with question, documentation consulted, and reformulation."""
    now = datetime.now().astimezone().strftime("%Y-%m-%d")
    lines = [
        "# Analyse d'une question comptable",
        "",
        f"**Date**: {now}",
        "",
        "## Question",
        "",
        "**Utilisateur**:",
        f">{question}",
        "",
    ]

    # Add reformulation section if primary_accounting_issue is available
    if primary_accounting_issue:
        lines.extend(
            [
                "**Reformulation**:",
                f">{primary_accounting_issue}",
                "",
            ]
        )

    # Documentation consultée - all documents, grouped by family
    lines.append("## Documentation")
    lines.append("**Consultée**")
    if doc_uids:
        grouped = _group_by_family(doc_uids)
        for family_name, family_docs in sorted(grouped.items()):
            if family_name == "Autres":
                # For "Autres", list each doc individually
                lines.extend(f"   - `{doc_uid}`" for doc_uid in family_docs)
            else:
                # For standard families, show family name and all docs on one line
                doc_list = ", ".join(f"`{uid}`" for uid in family_docs)
                lines.append(f"   - {family_name} ({doc_list})")
    else:
        lines.append("   - (documentation non disponible)")

    # Documentation retenue pour l'analyse - only authority-filtered docs
    if authority_doc_uids:
        lines.extend(["", "**Retenue pour l'analyse**"])
        grouped_authority = _group_by_family(authority_doc_uids)
        for family_name, family_docs in sorted(grouped_authority.items()):
            if family_name == "Autres":
                lines.extend(f"   - `{doc_uid}`" for doc_uid in family_docs)
            else:
                doc_list = ", ".join(f"`{uid}`" for uid in family_docs)
                lines.append(f"   - {family_name} ({doc_list})")

    return lines


def _build_assumptions(assumptions: list[str]) -> list[str]:
    """Build the assumptions section."""
    lines = [
        "",
        "## Hypothèses",
    ]
    lines.extend(f"   - {line}" for line in assumptions)
    return lines


def _build_recommendation(recommendation: dict) -> list[str]:
    """Build the recommendation section."""
    answer = _format_applicability(recommendation.get("answer", "N/A"))
    justification = recommendation.get("justification", "")

    return [
        "",
        "## Recommandation",
        "",
        f"**{answer}**",
        "",
        f"{justification}",
        "",
    ]


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


def _bold_excerpt_in_chunk(chunk_text: str, excerpt: str) -> str:
    """Replace the excerpt in chunk text with a bold version.

    Does case-insensitive matching and preserves the original case.
    """
    if not excerpt or not chunk_text:
        return chunk_text

    excerpt_lower = excerpt.lower()
    chunk_lower = chunk_text.lower()

    position = chunk_lower.find(excerpt_lower)
    if position == -1:
        return chunk_text

    # Get the original case excerpt
    original_excerpt = chunk_text[position : position + len(excerpt)]
    return chunk_text.replace(original_excerpt, f"**{original_excerpt}**")


def _truncate_chunk_with_highlight(
    chunk_text: str,
    excerpt: str,
    max_chunk_length: int = 2000,
    context_chars: int = 500,
) -> str:
    """Truncate chunk text while keeping the excerpt visible with context.

    If chunk is longer than max_chunk_length:
    - Show context_chars before and after the excerpt
    - Truncate the middle portion with "..."
    - Put the excerpt in **bold**

    Args:
        chunk_text: The full chunk text
        excerpt: The relevant excerpt to highlight
        max_chunk_length: Maximum allowed chunk length (default 2000)
        context_chars: Characters to show before/after when truncating (default 500)

    Returns:
        Truncated chunk text with excerpt highlighted in bold
    """
    # Find the excerpt position in the chunk
    excerpt_lower = excerpt.lower()
    chunk_lower = chunk_text.lower()

    position = chunk_lower.find(excerpt_lower)
    if position == -1:
        # Excerpt not found - return truncated chunk without bold
        return chunk_text[:max_chunk_length] + "..." if len(chunk_text) > max_chunk_length else chunk_text

    # If chunk is short enough, just bold the excerpt and return
    if len(chunk_text) <= max_chunk_length:
        return _bold_excerpt_in_chunk(chunk_text, excerpt)

    # Calculate the position for the excerpt
    excerpt_start = position
    excerpt_end = position + len(excerpt)

    # Calculate context boundaries
    context_start = max(0, excerpt_start - context_chars)
    context_end = min(len(chunk_text), excerpt_end + context_chars)

    # Build the truncated text
    parts: list[str] = []

    # Add leading context with ellipsis if there's more content before
    if context_start > 0:
        parts.append("..." + chunk_text[context_start:excerpt_start])
    else:
        parts.append(chunk_text[0:excerpt_start])

    # Add the excerpt in bold
    original_excerpt = chunk_text[excerpt_start:excerpt_end]
    parts.append(f"**{original_excerpt}**")

    # Add trailing context with ellipsis if there's more content after
    if context_end < len(chunk_text):
        parts.append(chunk_text[excerpt_end:context_end] + "...")
    else:
        parts.append(chunk_text[excerpt_end:])

    return "".join(parts)


def _build_approach_detail(idx: int, approach: dict, chunk_data: dict[str, str] | None = None) -> list[str]:
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
        "",
        f"**Applicabilité**: {applicability}",
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
            "**Raisonnement**:",
            reasoning or "(raisonnement non disponible)",
            "",
            f"**Implications pratiques**: {practical_implication or '(implications non spécifiées)'}",
            "",
        ]
    )

    # References section
    if references:
        lines.append("**Référence**:")
        for ref in references:
            document = ref.get("document", "")
            section = ref.get("section", "")
            excerpt = ref.get("excerpt", "")

            # Build section reference with document name
            section_ref = f"{document} {section}" if document else section

            lines.append(f" - {section_ref}")
            lines.append("")

            # Get full chunk text if available
            if chunk_data:
                chunk_key = f"{document}/{section}"
                full_chunk = chunk_data.get(chunk_key) or chunk_data.get(section)
                if full_chunk:
                    formatted_chunk = _truncate_chunk_with_highlight(full_chunk, excerpt)
                    lines.append(f"    >{formatted_chunk}")
                else:
                    lines.append(f"    >{excerpt}")
            else:
                # Fallback: just show the excerpt
                lines.append(f"    >{excerpt}")
    else:
        lines.append("   - (référence non disponible)")

    return lines


@dataclass
class MarkdownOptions:
    """Options for converting B-response JSON to markdown."""

    question: str | None = None
    doc_uids: list[str] | None = None
    authority_doc_uids: list[str] | None = None
    primary_accounting_issue: str | None = None
    chunk_data: dict[str, str] | None = None


def convert_json_to_markdown(
    b_json: dict,
    question: str | None = None,
    doc_uids: list[str] | None = None,
    authority_doc_uids: list[str] | None = None,
    primary_accounting_issue: str | None = None,
) -> str:
    """Convert B-response JSON to French markdown format.

    Args:
        b_json: Parsed JSON response
        question: The original question (optional)
        doc_uids: List of document UIDs consulted (optional)
        authority_doc_uids: List of document UIDs used in Prompt B after authority filtering (optional)
        primary_accounting_issue: The reformulated primary accounting issue from Prompt A (optional)

    Returns:
        Markdown formatted string in French
    """
    options = MarkdownOptions(
        question=question,
        doc_uids=doc_uids,
        authority_doc_uids=authority_doc_uids,
        primary_accounting_issue=primary_accounting_issue,
    )
    return _convert_json_to_markdown_with_options(b_json, options)


def convert_json_to_markdown_full(b_json: dict, options: MarkdownOptions) -> str:
    """Convert B-response JSON to French markdown format with full options.

    Args:
        b_json: Parsed JSON response
        options: Markdown conversion options including chunk_data

    Returns:
        Markdown formatted string in French
    """
    return _convert_json_to_markdown_with_options(b_json, options)


def _convert_json_to_markdown_with_options(b_json: dict, options: MarkdownOptions) -> str:
    """Convert B-response JSON to markdown using options object.

    Args:
        b_json: Parsed JSON response
        options: Markdown conversion options

    Returns:
        Markdown formatted string in French
    """
    assumptions = b_json.get("assumptions_fr", [])
    recommendation = b_json.get("recommendation", {})
    approaches = b_json.get("approaches", [])

    lines: list[str] = []
    lines.extend(
        _build_header(
            options.question,
            options.doc_uids,
            options.authority_doc_uids,
            options.primary_accounting_issue,
        )
    )
    lines.extend(_build_assumptions(assumptions))
    lines.extend(_build_recommendation(recommendation))
    lines.extend(_build_approaches_summary(approaches))

    for idx, approach in enumerate(approaches, start=1):
        lines.extend(_build_approach_detail(idx, approach, options.chunk_data))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# FAQ-style markdown conversion
# ---------------------------------------------------------------------------

IFRS_URL_TEMPLATE = "https://www.ifrs.org/issued-standards/list-of-standards/{slug}/content/dam/ifrs/publications/html-standards/english/2026/issued/{slug}/#/{anchor}"

IFRS_DOCUMENT_SLUGS: dict[str, str] = {
    "ifrs9": "ifrs-9-financial-instruments",
    "ifric16": "ifric-16-hedges-of-a-net-investment-in-a-foreign-operation",
    "ias21": "ias-21-the-effects-of-changes-in-foreign-exchange-rates",
}


def _build_faq_url(document: str, section: str) -> str:
    """Build the IFRS.org URL for a document reference."""
    slug = IFRS_DOCUMENT_SLUGS.get(document.lower(), document.lower())
    anchor = f"{document.upper()}_{section.replace('.', '')}"
    return IFRS_URL_TEMPLATE.format(slug=slug, anchor=anchor)


def _format_faq_answer(answer: str) -> str:
    """Format answer value for FAQ display."""
    if answer == "oui_sous_conditions":
        return "Oui"
    return answer.capitalize()


def _format_approach_inline_refs(references: list[dict]) -> str:
    """Format inline section references from a list of references.

    Produces strings like '(IFRS 9 6.3.1, IFRS 9 6.3.5, IFRIC 16 10)'.
    """
    if not references:
        return ""
    parts = []
    for ref in references:
        doc = ref.get("document", "")
        section = ref.get("section", "")
        if doc and section:
            parts.append(f"{_humanise_doc_label(doc)} {section}")
    if not parts:
        return ""
    return "(" + ", ".join(parts) + ")"


def _humanise_doc_label(doc_uid: str) -> str:
    """Humanise a document UID into a display label.

    'ifrs9' -> 'IFRS 9'
    'ifric16' -> 'IFRIC 16'
    'ias12' -> 'IAS 12'
    'sic13' -> 'SIC 13'
    """
    if doc_uid.startswith("ifrs"):
        suffix = doc_uid[4:]
        return f"IFRS {suffix}" if suffix else "IFRS"
    if doc_uid.startswith("ifric"):
        suffix = doc_uid[5:]
        return f"IFRIC {suffix}" if suffix else "IFRIC"
    if doc_uid.startswith("ias"):
        suffix = doc_uid[3:]
        return f"IAS {suffix}" if suffix else "IAS"
    if doc_uid.startswith("sic"):
        suffix = doc_uid[3:]
        return f"SIC {suffix}" if suffix else "SIC"
    return doc_uid


def _build_faq_approaches(approaches: list[dict]) -> list[str]:
    """Build inline reasoning paragraphs for each approach."""
    lines: list[str] = []
    for approach in approaches:
        applicability = approach.get("applicability", "non")
        reasoning = approach.get("reasoning_fr", "")
        label_fr = approach.get("label_fr", "")
        refs = approach.get("references", [])
        inline_ref = _format_approach_inline_refs(refs)

        if applicability in ("oui", "oui_sous_conditions"):
            # Full paragraph: reasoning + inline refs
            ref_suffix = inline_ref
            reasoning_stripped = reasoning.rstrip().removesuffix(".")
            lines.append(f"{reasoning_stripped}{ref_suffix}.")
        elif applicability == "non":
            # Brief one-liner: label + inline refs
            ref_suffix = f" {inline_ref}" if inline_ref else ""
            lines.append(f"{label_fr} ne s'applique donc pas{ref_suffix}.")

    return lines


def _build_faq_citations(approaches: list[dict]) -> list[str]:
    """Build the Citations section from all unique references across approaches."""
    seen_refs: set[tuple[str, str]] = set()
    all_citations: list[dict] = []
    for approach in approaches:
        for ref in approach.get("references", []):
            key = (ref.get("document", ""), ref.get("section", ""))
            if key in seen_refs:
                continue
            seen_refs.add(key)
            doc = ref.get("document", "")
            section = ref.get("section", "")
            excerpt = ref.get("excerpt", "")
            all_citations.append({"document": doc, "section": section, "excerpt": excerpt})

    if not all_citations:
        return []

    lines = ["**Citations**:"]
    for ref in all_citations:
        doc = ref["document"]
        section = ref["section"]
        excerpt = ref["excerpt"]
        url = _build_faq_url(doc, section)
        label = _humanise_doc_label(doc)
        lines.append(f" - [{label} {section}]({url})")
        lines.append("")
        lines.append(f"    >{excerpt}")
        lines.append("")

    return lines


def convert_json_to_faq_markdown(
    b_json: dict,
    primary_accounting_issue: str | None = None,
) -> str:
    """Convert B-response JSON to FAQ-style French markdown.

    Format:
        >primary_accounting_issue

        Pour cette réponse, on considère que
        - assumptions...

        **Answer**, justification

        inline reasoning per approach (non-applicable approaches are
        noted briefly, applicable ones get a full paragraph with refs)

        **Citations**:
        - [DOC SECTION](url)

            >full excerpt
    """
    assumptions: list[str] = b_json.get("assumptions_fr", [])
    recommendation: dict = b_json.get("recommendation", {})
    approaches: list[dict] = b_json.get("approaches", [])

    lines: list[str] = []

    # ---- Reformulation
    if primary_accounting_issue:
        lines.extend([f">{primary_accounting_issue}", ""])

    # ---- Assumptions
    lines.append("Pour cette réponse, on considère que")
    lines.extend(f"  - {a}" for a in assumptions)
    lines.append("")

    # ---- Recommendation
    rec_answer = _format_faq_answer(recommendation.get("answer", ""))
    rec_justification = recommendation.get("justification", "")
    if rec_justification:
        lines.append(f"**{rec_answer}**, {rec_justification}")
    else:
        lines.append(f"**{rec_answer}**")
    lines.append("")

    # ---- Approaches inline
    lines.extend(_build_faq_approaches(approaches))
    lines.append("")

    # ---- Citations
    lines.extend(_build_faq_citations(approaches))

    return "\n".join(lines)
