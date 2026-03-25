#!/usr/bin/env python3
"""Analyze experiment 4 results."""

import re
from pathlib import Path

BASE = Path(__file__).parent

# Determine which questions have been run
questions = []
for f in sorted(BASE.glob("Q1.*__run1/B-response.md")):
    q = f.parent.name.split("_k=")[0]
    questions.append(q)

print(f"Found {len(questions)} questions: {questions}")

TITLE_MAP = {
    "interdiction": "A1_General_Exclusion",
    "exclusion": "A1_General_Exclusion",
    "règle générale": "A1_General_Exclusion",
    "non-éligibilité": "A1_General_Exclusion",
    "monétaire": "A2_Monetary_Item",
    "juste valeur": "A2_Monetary_Item",
    "risque de change": "A2_Monetary_Item",
    "transaction future": "A3_CF_Future",
    "transaction intragroupe prévu": "A3_CF_Future",
    "dividende futur": "A3_CF_Future",
    "prévue": "A3_CF_Future",
    "investissement net": "A4_Net_Investment",
    "activité étrangère": "A4_Net_Investment",
    "activité à l'étranger": "A4_Net_Investment",
}


def get_canonical_approach(title):
    title_lower = title.lower()
    for key, canonical in TITLE_MAP.items():
        if key in title_lower:
            return canonical
    return "Other"


def find_applicability_and_title(text):
    """Find applicability and extract title from line."""
    text = text.strip()

    # Case 1: **Applicability — Approche N : Title** (bold inline, like Q1.10 run 3)
    # Pattern: **word** - Approche N : title
    match = re.search(r"\*\*([^*]+?)\s*[-—]\s*Approche\s*\d+\s*:\s*(.+?)\*\*$", text)
    if match:
        applicability = match.group(1).strip()
        title = match.group(2).strip()
        return applicability, title

    # Try without trailing **
    match2 = re.search(r"\*\*([^*]+?)\s*[-—]\s*Approche\s*\d+\s*:\s*(.+)", text)
    if match2:
        applicability = match2.group(1).strip()
        title = match2.group(2).strip()
        title = title.rstrip("*").strip()  # Remove trailing *
        return applicability, title

    return None, None


def find_applicability(text):
    """Find applicability in text."""
    text = text.strip()

    # Case 1: Bold at START: **Non — Approche**
    if text.startswith("**Non") and "—" in text:
        return "Non"
    if text.startswith("**Oui sous conditions"):
        return "Oui sous conditions"
    if text.startswith("**Oui") and "Oui sous conditions" not in text:
        return "Oui"

    # Case 2: Bold in middle
    if "**Non**" in text or "**Non." in text:
        return "Non"
    if "**Oui sous conditions**" in text:
        return "Oui sous conditions"
    if "**Oui**" in text or "**Oui." in text:
        return "Oui"

    # Case 3: Plain text at end
    if "Non" in text and (text.endswith("Non") or text.endswith("Non.") or text.endswith("Non —")):
        return "Non"
    if "Oui sous conditions" in text:
        return "Oui sous conditions"
    if "Oui" in text and (text.endswith("Oui") or text.endswith("Oui.")):
        return "Oui"

    return None


def extract_title_from_line(line):
    title = line.replace("###", "").strip()
    title = re.sub(r"^[\d\)]+\s*", "", title)
    title = re.sub(r"\*\*.*\*\*", "", title)
    title = title.split("—")[-1].strip()
    return title


def parse_file(filepath):
    results = {}
    if not filepath.exists():
        return results

    lines = filepath.read_text().split("\n")
    current_title = None

    for i, line in enumerate(lines):
        # Check for inline format **Applicability — Approche N : Title**
        applicability, title = find_applicability_and_title(line)
        if applicability and title:
            canonical = get_canonical_approach(title)
            results[canonical] = applicability
            continue

        # Check for ### prefix format
        if "###" in line and ("Approche" in line or re.search(r"^###\s*\d+", line)):
            applicability = find_applicability(line)

            if applicability:
                title = extract_title_from_line(line)
                canonical = get_canonical_approach(title)
                results[canonical] = applicability
            else:
                current_title = extract_title_from_line(line)
            continue

        # Check next line for applicability
        if current_title:
            applicability = find_applicability(line)
            if applicability:
                canonical = get_canonical_approach(current_title)
                results[canonical] = applicability
                current_title = None

    return results


# Parse all files
all_results = {}
for q in questions:
    all_results[q] = {}
    for run in [1, 2, 3]:
        f = BASE / f"{q}_k=5_e=5_min-score=0.5__run{run}/B-response.md"
        all_results[q][run] = parse_file(f)

# Print table
print(
    "\n| Q | Run | A1 (General Exclusion) | A2 (Monetary Item) | A3 (CF Future) | A4 (Net Investment) |"
)
print(
    "|---|-----|-------------------------|-------------------|-----------------|---------------------|"
)

for q in questions:
    for run in [1, 2, 3]:
        r = all_results[q][run]
        a1 = r.get("A1_General_Exclusion", "-")
        a2 = r.get("A2_Monetary_Item", "-")
        a3 = r.get("A3_CF_Future", "-")
        a4 = r.get("A4_Net_Investment", "-")

        a1_marker = " ⚠️" if a1 == "Oui" else ""
        print(f"| {q} | {run} | {a1}{a1_marker:20} | {a2:17} | {a3:15} | {a4:19} |")

# Write ANALYSIS.md
analysis = """# Experiment 4 Analysis

## Unique Approaches Identified

### Approach 1: General Intragroup Exclusion
**Summary:** Default rule that intragroup items cannot be hedged in consolidation (IFRS 9.6.3.5)

**Typical Applicability:** usually Non

---

### Approach 2: Intragroup Monetary Item Exception  
**Summary:** The key exception - hedge FX risk on intragroup monetary item (IFRS 9.6.3.6)

**Typical Applicability:** usually Oui sous conditions

---

### Approach 3: Cash Flow Hedge on Future Transaction

**Typical Applicability:** usually Non

---

### Approach 4: Net Investment Hedge

**Typical Applicability:** varies

---

## Summary Table

| Q | Run | A1 (General Exclusion) | A2 (Monetary Item) | A3 (CF Future) | A4 (Net Investment) |
|---|-----|-------------------------|-------------------|-----------------|---------------------|
"""

for q in questions:
    for run in [1, 2, 3]:
        r = all_results[q][run]
        a1 = r.get("A1_General_Exclusion", "-")
        a2 = r.get("A2_Monetary_Item", "-")
        a3 = r.get("A3_CF_Future", "-")
        a4 = r.get("A4_Net_Investment", "-")
        a1_str = f"**{a1}** ⚠️" if a1 == "Oui" else a1
        analysis += f"| {q} | {run} | {a1_str:23} | {a2:17} | {a3:15} | {a4:19} |\n"

analysis += """**Note:** "-" means the approach wasn't listed

---

## Key Findings
- A1 (General Exclusion): usually Non ✓
- A2 (Monetary Item): usually Oui sous conditions ✓  
- A3 (CF Future): usually Non ✓
- A4 (Net Investment): varies
"""

(BASE / "ANALYSIS.md").write_text(analysis)
print("\nAnalysis written to ANALYSIS.md")
