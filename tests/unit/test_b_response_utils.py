"""Tests for b_response_utils."""

from __future__ import annotations

from src.b_response_utils import (
    _bold_excerpt_in_chunk,
    _build_approach_detail,
    _group_by_family,
    _truncate_chunk_with_highlight,
    convert_json_to_markdown,
)


class TestDocumentFamilyGrouping:
    """Tests for document family grouping functionality."""

    def test_group_by_family_ifrs(self) -> None:
        """Test grouping IFRS documents."""
        doc_uids = ["ifrs15", "ifrs9", "ias21"]
        grouped = _group_by_family(doc_uids)

        assert "IFRS-S (standard)" in grouped
        assert grouped["IFRS-S (standard)"] == ["ifrs15", "ifrs9"]
        assert "IAS (standard)" in grouped
        assert grouped["IAS (standard)"] == ["ias21"]

    def test_group_by_family_mixed_documents(self) -> None:
        """Test grouping a mix of IFRS, IAS, and unknown documents."""
        doc_uids = ["ifrs15", "ifrs9", "ias21", "unknown_doc", "ias12"]
        grouped = _group_by_family(doc_uids)

        assert "IFRS-S (standard)" in grouped
        assert grouped["IFRS-S (standard)"] == ["ifrs15", "ifrs9"]
        assert "IAS (standard)" in grouped
        assert grouped["IAS (standard)"] == ["ias21", "ias12"]
        assert "Autres" in grouped
        assert grouped["Autres"] == ["unknown_doc"]

    def test_group_by_family_only_unknown(self) -> None:
        """Test grouping with only unknown documents."""
        doc_uids = ["custom1", "custom2"]
        grouped = _group_by_family(doc_uids)

        assert "Autres" in grouped
        assert grouped["Autres"] == ["custom1", "custom2"]

    def test_group_by_family_empty(self) -> None:
        """Test grouping with empty list."""
        grouped = _group_by_family([])
        assert grouped == {}

    def test_group_by_family_single_family(self) -> None:
        """Test grouping documents from the same family."""
        doc_uids = ["ifrs15", "ifrs16", "ifrs17"]
        grouped = _group_by_family(doc_uids)

        assert "IFRS-S (standard)" in grouped
        assert grouped["IFRS-S (standard)"] == ["ifrs15", "ifrs16", "ifrs17"]
        assert "Autres" not in grouped


class TestCitationFormatting:
    """Tests for citation/chunk formatting in markdown output."""

    def test_truncate_chunk_with_highlight_short_chunk(self) -> None:
        """Short chunks (< 2000 chars) are returned with excerpt bolded, not truncated."""
        chunk = "This is a short chunk with some relevant content that should be highlighted."
        excerpt = "relevant content"
        result = _truncate_chunk_with_highlight(chunk, excerpt)

        assert "**relevant content**" in result
        assert "This is a short chunk with some" in result

    def test_truncate_chunk_with_highlight_long_chunk(self) -> None:
        """Long chunks are truncated with context before/after excerpt."""
        # Create a chunk longer than 2000 characters
        prefix = "A" * 1000
        middle = "B" * 500
        relevant = "RELEVANT TEXT"
        suffix = "C" * 1000
        chunk = prefix + middle + relevant + suffix

        result = _truncate_chunk_with_highlight(chunk, relevant)

        assert "**RELEVANT TEXT**" in result
        # Should have ellipsis since we truncate
        assert "..." in result

    def test_truncate_chunk_with_highlight_excerpt_not_found(self) -> None:
        """When excerpt not found in chunk, returns truncated chunk."""
        chunk = "A" * 3000
        excerpt = "not found"
        result = _truncate_chunk_with_highlight(chunk, excerpt)

        # Should be truncated since chunk is > 2000
        assert len(result) <= 2003  # 2000 + "..."
        assert "..." in result
        # Excerpt not found, so not bolded
        assert "**" not in result

    def test_truncate_chunk_with_highlight_context_chars(self) -> None:
        """Verifies context characters are included before/after excerpt."""
        chunk = "X" * 500 + "TARGET EXCERPT" + "Y" * 500
        excerpt = "TARGET EXCERPT"
        result = _truncate_chunk_with_highlight(chunk, excerpt)

        # Since chunk is ~1025 chars and we limit to 2000, it should be returned with excerpt bolded
        assert "**TARGET EXCERPT**" in result

    def test_bold_excerpt_in_chunk(self) -> None:
        """Test that excerpt is wrapped in **bold** markers."""
        chunk = "The hedged item must be a recognised asset or liability."
        excerpt = "recognised asset or liability"
        result = _bold_excerpt_in_chunk(chunk, excerpt)

        assert "**recognised asset or liability**" in result
        assert "The hedged item must be a" in result

    def test_bold_excerpt_in_chunk_case_insensitive(self) -> None:
        """Bold excerpt works case-insensitively."""
        chunk = "The key requirement is FAIR VALUE measurement."
        excerpt = "fair value"
        result = _bold_excerpt_in_chunk(chunk, excerpt)

        assert "**FAIR VALUE**" in result

    def test_bold_excerpt_not_found(self) -> None:
        """When excerpt not found, returns original chunk."""
        chunk = "Some text without the excerpt"
        excerpt = "missing"
        result = _bold_excerpt_in_chunk(chunk, excerpt)

        assert result == chunk

    def test_build_approach_detail_with_chunk_data(self) -> None:
        """Test that approach detail includes full chunk with excerpt bolded."""
        approach = {
            "id": "approach_1",
            "label_fr": "Couverture de juste valeur",
            "normalized_label": "fair_value_hedge",
            "applicability": "oui",
            "reasoning_fr": "Applicable because...",
            "conditions_fr": ["Condition 1"],
            "practical_implication_fr": "Update records",
            "references": [
                {
                    "document": "ifrs9",
                    "section": "6.3.1",
                    "excerpt": "recognised asset or liability",
                }
            ],
        }

        chunk_data = {
            "ifrs9/6.3.1": "A hedged item can be a recognised asset or liability that is a firm commitment.",
        }

        lines = _build_approach_detail(1, approach, chunk_data)

        # Check that document is included in reference
        assert any("ifrs9 6.3.1" in line for line in lines)
        # Check that chunk with bold excerpt is included
        assert any("**recognised asset or liability**" in line for line in lines)

    def test_build_approach_detail_without_chunk_data(self) -> None:
        """Test that approach detail falls back to excerpt when no chunk data."""
        approach = {
            "id": "approach_1",
            "label_fr": "Test Approach",
            "normalized_label": "test",
            "applicability": "oui",
            "reasoning_fr": "Because...",
            "conditions_fr": [],
            "practical_implication_fr": "Test",
            "references": [
                {
                    "document": "ifrs9",
                    "section": "6.3.1",
                    "excerpt": "recognised asset",
                }
            ],
        }

        lines = _build_approach_detail(1, approach, None)

        # Should fall back to showing just the excerpt
        assert any("ifrs9 6.3.1" in line for line in lines)
        assert any(">recognised asset" in line for line in lines)

    def test_build_approach_detail_without_document(self) -> None:
        """Test that references without document still show section."""
        approach = {
            "id": "approach_1",
            "label_fr": "Test",
            "normalized_label": "test",
            "applicability": "oui",
            "reasoning_fr": "Because",
            "conditions_fr": [],
            "practical_implication_fr": "Test",
            "references": [
                {
                    "section": "5.1",
                    "excerpt": "some text",
                }
            ],
        }

        lines = _build_approach_detail(1, approach, None)

        assert any("5.1" in line and "ifrs9" not in line for line in lines)


class TestConvertJsonToMarkdown:
    """Tests for convert_json_to_markdown function."""

    def test_basic_conversion(self) -> None:
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
        }

        result = convert_json_to_markdown(b_json, question="Test question?", doc_uids=["doc1", "doc2"])

        # Split into lines for precise checking
        lines = result.split("\n")

        # Check document header
        assert lines[0] == "# Analyse d'une question comptable"

        # Check date is present (format: **Date**: YYYY-MM-DD)
        date_line = [l for l in lines if l.startswith("**Date**:")][0]
        assert "**Date**:" in date_line

        # Check question section with Utilisateur label
        assert any("**Utilisateur**" in l for l in lines)

        # Check question blockquote comes after Utilisateur label (on separate line)
        user_idx = next(i for i, l in enumerate(lines) if "**Utilisateur**" in l)
        question_line = lines[user_idx + 1]
        assert question_line == ">Test question?"

        # Check documentation with backtick formatting (each doc on its own line)
        doc_lines = [l for l in lines if "`doc" in l]
        assert any("`doc1`" in l for l in doc_lines)
        assert any("`doc2`" in l for l in doc_lines)

        # Check hypotheses section with formatted list items
        hypotheses_section = "\n".join(lines[lines.index("## Hypothèses") : lines.index("## Hypothèses") + 4])
        assert "   - Assumption 1" in hypotheses_section
        assert "   - Assumption 2" in hypotheses_section

        # Check recommendation with uppercase formatting
        rec_section_start = lines.index("## Recommandation")
        rec_section = "\n".join(lines[rec_section_start : rec_section_start + 5])
        assert "**OUI**" in rec_section
        assert "Test justification text" in rec_section

        # Check summary table structure
        table_start = lines.index("| Approche | Applicabilité | Conditions |")
        table_rows = "\n".join(lines[table_start : table_start + 4])
        assert "| 1. Approche principale | NON |" in table_rows
        assert "| 2. Approche alternative | OUI |" in table_rows

        # Check approach detail sections with all formatting on same lines
        approach1_section = "\n".join(lines[lines.index("### 1. Approche principale") : lines.index("### 2. Approche alternative")])
        assert "**Applicabilité**: NON" in approach1_section
        assert "   - Condition A must be met" in approach1_section
        assert "   - Condition B must be satisfied" in approach1_section
        assert "**Raisonnement**:" in approach1_section
        assert "This approach does not apply because of specific facts" in approach1_section
        assert "**Implications pratiques**: Implementation requires documentation" in approach1_section

        # Check references with section and blockquote excerpt
        ref_section = "\n".join(lines[lines.index("**Référence**:") : lines.index("**Référence**:") + 4])
        assert " - IFRS 9.6.3.5" in ref_section
        assert ">Relevant excerpt text" in ref_section

        # Check second approach has empty conditions handled
        approach2_section = "\n".join(lines[lines.index("### 2. Approche alternative") :])
        assert "**Applicabilité**: OUI" in approach2_section
        assert "(conditions non spécifiées)" in approach2_section

    def test_conversion_without_question_and_docs(self) -> None:
        """Test conversion without optional question and doc_uids."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "non", "justification": "Not applicable"},
            "approaches": [],
        }

        result = convert_json_to_markdown(b_json)

        assert "documentation non disponible" in result

    def test_conditions_handling(self) -> None:
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
        }

        result = convert_json_to_markdown(b_json)

        assert "Condition A" in result
        assert "Condition B" in result

    def test_pipes_escaped_in_content(self) -> None:
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
        }

        result = convert_json_to_markdown(b_json)

        assert r"\|" in result or "with pipe" in result

    def test_applicability_formatting(self) -> None:
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
        }

        result = convert_json_to_markdown(b_json)

        # Should be formatted as uppercase with spaces instead of underscores
        assert "OUI SOUS CONDITIONS" in result

    def test_grouped_documentation_consultee(self) -> None:
        """Test that documentation consultée groups documents by family."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(
            b_json,
            question="Test?",
            doc_uids=["ifrs15", "ifrs9", "ias21", "ias12", "custom_doc"],
        )

        lines = result.split("\n")

        # Find documentation section
        doc_section_idx = lines.index("## Documentation")

        # IFRS documents should be grouped together
        assert any("IFRS" in l and "ifrs15" in l and "ifrs9" in l for l in lines[doc_section_idx:])

        # IAS documents should be grouped together
        assert any("IAS" in l and "ias21" in l and "ias12" in l for l in lines[doc_section_idx:])

        # Unknown documents should be listed individually
        assert any("`custom_doc`" in l for l in lines[doc_section_idx:])

    def test_documentation_retenue_section(self) -> None:
        """Test that documentation retenue pour l'analyse section is present when authority_doc_uids provided."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(
            b_json,
            question="Test?",
            doc_uids=["ifrs15", "ias21", "ifrs9"],
            authority_doc_uids=["ifrs15", "ias21"],
        )

        lines = result.split("\n")

        # Documentation retenue section should be present
        assert "**Retenue pour l'analyse**" in lines

        # Only authority-filtered docs should appear here
        retenue_idx = lines.index("**Retenue pour l'analyse**")
        retenue_section = "\n".join(lines[retenue_idx:])
        assert "IFRS" in retenue_section
        assert "IAS" in retenue_section
        assert "ifrs9" not in retenue_section  # ifrs9 should not appear (not in authority_doc_uids)

    def test_reformulation_section(self) -> None:
        """Test that reformulation section with primary_accounting_issue is present."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(
            b_json,
            question="How to account for X?",
            primary_accounting_issue="The primary issue is whether X should be recognized as revenue under IFRS 15.",
        )

        lines = result.split("\n")

        # Reformulation section should be present
        assert "**Reformulation**:" in lines

        # The reformulated question should be in blockquote
        reformulation_idx = lines.index("**Reformulation**:")
        reformulation_content = lines[reformulation_idx + 1]
        assert reformulation_content.startswith(">")
        assert "primary issue" in reformulation_content

    def test_no_reformulation_without_issue(self) -> None:
        """Test that reformulation section is not present when primary_accounting_issue is None."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(
            b_json,
            question="How to account for X?",
        )

        lines = result.split("\n")

        # Reformulation section should NOT be present
        assert "**Reformulation**:" not in lines

    def test_utilisateur_label_before_question(self) -> None:
        """Test that **Utilisateur** label appears before the question blockquote."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(b_json, question="Test question?")

        lines = result.split("\n")

        # Find the Utilisateur label and the question
        user_idx = lines.index("**Utilisateur**:")
        question_line = lines[user_idx + 1]

        assert question_line.startswith(">")
        assert "Test question?" in question_line

    def test_empty_authority_doc_uids_no_retenue_section(self) -> None:
        """Test that documentation retenue section is not present when authority_doc_uids is empty."""
        b_json = {
            "assumptions_fr": [],
            "recommendation": {"answer": "oui", "justification": "Test"},
            "approaches": [],
        }

        result = convert_json_to_markdown(
            b_json,
            question="Test?",
            doc_uids=["ifrs15"],
            authority_doc_uids=[],
        )

        lines = result.split("\n")

        # Documentation retenue section should NOT be present with empty list
        assert "**Documentation retenue pour l'analyse**" not in lines
