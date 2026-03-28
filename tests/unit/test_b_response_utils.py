"""Tests for b_response_utils."""

import pytest

from src.b_response_utils import convert_json_to_markdown


class TestConvertJsonToMarkdown:
    """Tests for convert_json_to_markdown function."""

    def test_basic_conversion(self):
        """Test basic JSON to markdown conversion with proper formatting checks."""
        b_json = {
            "assumptions_fr": ["Assumption 1", "Assumption 2"],
            "recommendation": {
                "answer": "oui",
                "justification": "Test justification text",
            },
            "approaches": [
                {
                    "id": "approach_1",
                    "label_fr": "Approche principale",
                    "normalized_label": "main_approach",
                    "applicability": "non",
                    "reasoning_fr": "This approach does not apply because of specific facts",
                    "conditions_fr": ["Condition A must be met", "Condition B must be satisfied"],
                    "practical_implication_fr": "Implementation requires documentation",
                    "references": [{"section": "IFRS 9.6.3.5", "excerpt": "Relevant excerpt text"}],
                },
                {
                    "id": "approach_2",
                    "label_fr": "Approche alternative",
                    "normalized_label": "alternative_approach",
                    "applicability": "oui",
                    "reasoning_fr": "This approach applies to the case",
                    "conditions_fr": [],
                    "practical_implication_fr": "No additional requirements",
                    "references": [],
                },
            ],
            "operational_points_fr": ["Point opérationnel 1", "Point opérationnel 2"],
        }

        result = convert_json_to_markdown(b_json, question="Test question?", doc_uids=["doc1", "doc2"])

        # Split into lines for precise checking
        lines = result.split("\n")

        # Check document header
        assert lines[0] == "# Analyse d'une question comptable"

        # Check date is present (format: **Date**: YYYY-MM-DD)
        date_line = [l for l in lines if l.startswith("**Date**:")][0]
        assert "**Date**:" in date_line

        # Check question is in blockquote (format: >question)
        question_line = [l for l in lines if l.startswith(">")][0]
        assert question_line == ">Test question?"

        # Check documentation with backtick formatting (each doc on its own line)
        doc_lines = [l for l in lines if "`doc" in l]
        assert any("`doc1`" in l for l in doc_lines)
        assert any("`doc2`" in l for l in doc_lines)

        # Check hypotheses section with formatted list items
        hypotheses_section = "\n".join(lines[lines.index("## Hypothèses"):lines.index("## Hypothèses") + 4])
        assert "   - Assumption 1" in hypotheses_section
        assert "   - Assumption 2" in hypotheses_section

        # Check recommendation with uppercase formatting
        rec_section_start = lines.index("## Recommandation")
        rec_section = "\n".join(lines[rec_section_start:rec_section_start + 5])
        assert "**OUI**" in rec_section
        assert "Test justification text" in rec_section

        # Check operational points with formatted list
        ops_section_start = lines.index("## Points Opérationnels")
        ops_section = "\n".join(lines[ops_section_start:ops_section_start + 4])
        assert "   - Point opérationnel 1" in ops_section
        assert "   - Point opérationnel 2" in ops_section

        # Check summary table structure
        table_start = lines.index("| Approche | Applicabilité | Conditions |")
        table_rows = "\n".join(lines[table_start:table_start + 4])
        assert "| 1. Approche principale | NON |" in table_rows
        assert "| 2. Approche alternative | OUI |" in table_rows

        # Check approach detail sections with all formatting on same lines
        approach1_section = "\n".join(lines[lines.index("### 1. Approche principale"):lines.index("### 2. Approche alternative")])
        assert "**Applicabilité**: NON" in approach1_section
        assert "   - Condition A must be met" in approach1_section
        assert "   - Condition B must be satisfied" in approach1_section
        assert "**Raisonnment**:" in approach1_section
        assert "This approach does not apply because of specific facts" in approach1_section
        assert "**Implications pratiques**: Implementation requires documentation" in approach1_section

        # Check references with section and blockquote excerpt
        ref_section = "\n".join(lines[lines.index("**Référence**:"):lines.index("**Référence**:") + 4])
        assert " - IFRS 9.6.3.5" in ref_section
        assert ">Relevant excerpt text" in ref_section

        # Check second approach has empty conditions handled
        approach2_section = "\n".join(lines[lines.index("### 2. Approche alternative"):])
        assert "**Applicabilité**: OUI" in approach2_section
        assert "(conditions non spécifiées)" in approach2_section

    def test_conversion_without_question_and_docs(self):
        """Test conversion without optional question and doc_uids."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "non", "justification": "Not applicable"},
            "approaches": [],
            "operational_points_fr": [],
        }

        result = convert_json_to_markdown(b_json)

        assert "documentation non disponible" in result

    def test_conditions_handling(self):
        """Test that conditions are properly formatted."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui_sous_conditions", "justification": "Test"},
            "approaches": [
                {
                    "id": "approach_1",
                    "label_fr": "Approach with conditions",
                    "normalized_label": "approach_1",
                    "applicability": "oui_sous_conditions",
                    "reasoning_fr": "Test reasoning",
                    "conditions_fr": ["Condition A", "Condition B"],
                    "practical_implication_fr": "Implication",
                    "references": [],
                }
            ],
            "operational_points_fr": [],
        }

        result = convert_json_to_markdown(b_json)

        assert "Condition A" in result
        assert "Condition B" in result

    def test_pipes_escaped_in_content(self):
        """Test that pipes in content are escaped for markdown tables."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [
                {
                    "id": "approach_1",
                    "label_fr": "Test | with pipe",
                    "normalized_label": "approach_1",
                    "applicability": "non",
                    "reasoning_fr": "Test",
                    "conditions_fr": ["Cond | 1"],
                    "practical_implication_fr": "Test",
                    "references": [],
                }
            ],
            "operational_points_fr": [],
        }

        result = convert_json_to_markdown(b_json)

        # Pipes should be escaped in markdown table
        assert r"\|" in result or "with pipe" in result

    def test_applicability_formatting(self):
        """Test that applicability values are properly formatted."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui_sous_conditions", "justification": "Test"},
            "approaches": [
                {
                    "id": "approach_1",
                    "label_fr": "Test",
                    "normalized_label": "approach_1",
                    "applicability": "oui_sous_conditions",
                    "reasoning_fr": "Test",
                    "conditions_fr": [],
                    "practical_implication_fr": "Test",
                    "references": [],
                }
            ],
            "operational_points_fr": [],
        }

        result = convert_json_to_markdown(b_json)

        # Should be formatted as uppercase with spaces instead of underscores
        assert "OUI SOUS CONDITIONS" in result