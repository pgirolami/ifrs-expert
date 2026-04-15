"""Tests that CLI parser defaults align with command option defaults."""

from __future__ import annotations

import argparse
from dataclasses import fields

from src.cli import _build_parser
from src.commands.answer import AnswerOptions
from src.commands.constants import (
    DEFAULT_D,
    DEFAULT_D_FOR_IAS_DOCUMENTS,
    DEFAULT_D_FOR_IFRIC_DOCUMENTS,
    DEFAULT_D_FOR_IFRS_DOCUMENTS,
    DEFAULT_D_FOR_NAVIS_DOCUMENTS,
    DEFAULT_D_FOR_PS_DOCUMENTS,
    DEFAULT_D_FOR_SIC_DOCUMENTS,
    DEFAULT_EXPAND,
    DEFAULT_FULL_DOC_THRESHOLD,
    DEFAULT_MIN_SCORE,
    DEFAULT_MIN_SCORE_FOR_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS,
    DEFAULT_QUERY_TITLES_MIN_SCORE,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVE_CONTENT_MIN_SCORE,
    DEFAULT_RETRIEVE_DOCUMENT_D,
    DEFAULT_RETRIEVE_EXPAND,
    DEFAULT_RETRIEVE_EXPAND_TO_SECTION,
    DEFAULT_RETRIEVAL_MODE,
    DEFAULT_SCOPE,
)
from src.commands.query import QueryOptions
from src.commands.query_documents import QueryDocumentsOptions
from src.commands.query_titles import QueryTitlesOptions
from src.commands.retrieve import RetrieveOptions


def _get_subparser(name: str) -> argparse.ArgumentParser:
    parser = _build_parser()
    subparsers_action = next(
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)  # noqa: SLF001
    )
    return subparsers_action.choices[name]


def _get_action_default(subparser: argparse.ArgumentParser, dest: str) -> object:
    for action in subparser._actions:  # noqa: SLF001
        if action.dest == dest:
            return action.default
    msg = f"Missing parser action for {dest}"
    raise AssertionError(msg)


def test_options_dataclass_defaults_remain_constant_backed() -> None:
    """Option dataclasses should expose expected constant-backed defaults."""
    query_defaults = QueryOptions()
    assert query_defaults.k == DEFAULT_RETRIEVAL_K
    assert query_defaults.min_score == DEFAULT_MIN_SCORE
    assert query_defaults.expand == DEFAULT_EXPAND
    assert query_defaults.full_doc_threshold == DEFAULT_FULL_DOC_THRESHOLD

    query_documents_defaults = QueryDocumentsOptions(document_type="IFRS")
    assert query_documents_defaults.d == DEFAULT_D
    assert query_documents_defaults.min_score == DEFAULT_MIN_SCORE_FOR_DOCUMENTS

    query_titles_defaults = QueryTitlesOptions()
    assert query_titles_defaults.k == DEFAULT_RETRIEVAL_K
    assert query_titles_defaults.min_score == DEFAULT_QUERY_TITLES_MIN_SCORE

    retrieve_defaults = RetrieveOptions()
    assert retrieve_defaults.k == DEFAULT_RETRIEVAL_K
    assert retrieve_defaults.d == DEFAULT_RETRIEVE_DOCUMENT_D
    assert retrieve_defaults.expand == DEFAULT_RETRIEVE_EXPAND
    assert retrieve_defaults.expand_to_section == DEFAULT_RETRIEVE_EXPAND_TO_SECTION
    assert retrieve_defaults.retrieval_mode == DEFAULT_RETRIEVAL_MODE
    assert retrieve_defaults.navis_d == DEFAULT_D_FOR_NAVIS_DOCUMENTS
    assert retrieve_defaults.navis_min_score == DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS

    answer_defaults = AnswerOptions()
    assert answer_defaults.k == DEFAULT_RETRIEVAL_K
    assert answer_defaults.d == DEFAULT_RETRIEVE_DOCUMENT_D
    assert answer_defaults.min_score == DEFAULT_RETRIEVE_CONTENT_MIN_SCORE
    assert answer_defaults.content_min_score == DEFAULT_RETRIEVE_CONTENT_MIN_SCORE
    assert answer_defaults.expand == DEFAULT_RETRIEVE_EXPAND
    assert answer_defaults.expand_to_section == DEFAULT_RETRIEVE_EXPAND_TO_SECTION
    assert answer_defaults.retrieval_mode == DEFAULT_RETRIEVAL_MODE
    assert answer_defaults.navis_d == DEFAULT_D_FOR_NAVIS_DOCUMENTS
    assert answer_defaults.navis_min_score == DEFAULT_MIN_SCORE_FOR_NAVIS_DOCUMENTS

    retrieve_option_fields = {field.name for field in fields(RetrieveOptions)}
    answer_option_fields = {field.name for field in fields(AnswerOptions)}
    assert "navis_d" in retrieve_option_fields
    assert "navis_min_score" in retrieve_option_fields
    assert "navis_d" in answer_option_fields
    assert "navis_min_score" in answer_option_fields


def test_parser_defaults_align_for_all_commands() -> None:
    """Parser defaults should align with command defaults and shared constants."""
    chunk_parser = _get_subparser("chunk")
    assert _get_action_default(chunk_parser, "pdf") is None

    store_parser = _get_subparser("store")
    assert _get_action_default(store_parser, "source") is None
    assert _get_action_default(store_parser, "doc_uid") is None
    assert _get_action_default(store_parser, "scope") == DEFAULT_SCOPE

    ingest_parser = _get_subparser("ingest")
    assert _get_action_default(ingest_parser, "scope") == DEFAULT_SCOPE

    list_parser = _get_subparser("list")
    assert _get_action_default(list_parser, "doc_uid") is None

    query_parser = _get_subparser("query")
    assert _get_action_default(query_parser, "k") == QueryOptions().k
    assert _get_action_default(query_parser, "min_score") == QueryOptions().min_score
    assert _get_action_default(query_parser, "expand") == QueryOptions().expand
    assert _get_action_default(query_parser, "full_doc_threshold") == QueryOptions().full_doc_threshold
    assert _get_action_default(query_parser, "json") is False

    query_documents_parser = _get_subparser("query-documents")
    query_documents_defaults = QueryDocumentsOptions(document_type="IFRS")
    assert _get_action_default(query_documents_parser, "document_type") is None
    assert _get_action_default(query_documents_parser, "d") == query_documents_defaults.d
    assert _get_action_default(query_documents_parser, "json") is False
    assert _get_action_default(query_documents_parser, "min_score") == query_documents_defaults.min_score

    retrieve_parser = _get_subparser("retrieve")
    retrieve_defaults = RetrieveOptions()
    assert _get_action_default(retrieve_parser, "k") == retrieve_defaults.k
    assert _get_action_default(retrieve_parser, "d") == retrieve_defaults.d
    assert _get_action_default(retrieve_parser, "doc_min_score") == retrieve_defaults.doc_min_score
    assert _get_action_default(retrieve_parser, "ifrs_d") == DEFAULT_D_FOR_IFRS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ias_d") == DEFAULT_D_FOR_IAS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ifric_d") == DEFAULT_D_FOR_IFRIC_DOCUMENTS
    assert _get_action_default(retrieve_parser, "sic_d") == DEFAULT_D_FOR_SIC_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ps_d") == DEFAULT_D_FOR_PS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "navis_d") == retrieve_defaults.navis_d
    assert _get_action_default(retrieve_parser, "ifrs_min_score") == DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ias_min_score") == DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ifric_min_score") == DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS
    assert _get_action_default(retrieve_parser, "sic_min_score") == DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS
    assert _get_action_default(retrieve_parser, "ps_min_score") == DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS
    assert _get_action_default(retrieve_parser, "navis_min_score") == retrieve_defaults.navis_min_score
    assert _get_action_default(retrieve_parser, "content_min_score") == retrieve_defaults.content_min_score
    assert _get_action_default(retrieve_parser, "expand_to_section") == retrieve_defaults.expand_to_section
    assert _get_action_default(retrieve_parser, "expand") == retrieve_defaults.expand
    assert _get_action_default(retrieve_parser, "full_doc_threshold") == retrieve_defaults.full_doc_threshold
    assert _get_action_default(retrieve_parser, "retrieval_mode") == retrieve_defaults.retrieval_mode
    assert _get_action_default(retrieve_parser, "json") is False

    query_titles_parser = _get_subparser("query-titles")
    query_titles_defaults = QueryTitlesOptions()
    assert _get_action_default(query_titles_parser, "k") == query_titles_defaults.k
    assert _get_action_default(query_titles_parser, "json") is False
    assert _get_action_default(query_titles_parser, "min_score") == query_titles_defaults.min_score

    answer_parser = _get_subparser("answer")
    answer_defaults = AnswerOptions()
    assert _get_action_default(answer_parser, "expand") == answer_defaults.expand
    assert _get_action_default(answer_parser, "full_doc_threshold") == answer_defaults.full_doc_threshold
    assert _get_action_default(answer_parser, "k") == answer_defaults.k
    assert _get_action_default(answer_parser, "min_score") == answer_defaults.min_score
    assert _get_action_default(answer_parser, "d") == answer_defaults.d
    assert _get_action_default(answer_parser, "doc_min_score") == answer_defaults.doc_min_score
    assert _get_action_default(answer_parser, "ifrs_d") == answer_defaults.ifrs_d
    assert _get_action_default(answer_parser, "ias_d") == answer_defaults.ias_d
    assert _get_action_default(answer_parser, "ifric_d") == answer_defaults.ifric_d
    assert _get_action_default(answer_parser, "sic_d") == answer_defaults.sic_d
    assert _get_action_default(answer_parser, "ps_d") == answer_defaults.ps_d
    assert _get_action_default(answer_parser, "navis_d") == answer_defaults.navis_d
    assert _get_action_default(answer_parser, "ifrs_min_score") == answer_defaults.ifrs_min_score
    assert _get_action_default(answer_parser, "ias_min_score") == answer_defaults.ias_min_score
    assert _get_action_default(answer_parser, "ifric_min_score") == answer_defaults.ifric_min_score
    assert _get_action_default(answer_parser, "sic_min_score") == answer_defaults.sic_min_score
    assert _get_action_default(answer_parser, "ps_min_score") == answer_defaults.ps_min_score
    assert _get_action_default(answer_parser, "navis_min_score") == answer_defaults.navis_min_score
    assert _get_action_default(answer_parser, "content_min_score") == DEFAULT_RETRIEVE_CONTENT_MIN_SCORE
    assert _get_action_default(answer_parser, "expand_to_section") == answer_defaults.expand_to_section
    assert _get_action_default(answer_parser, "retrieval_mode") == answer_defaults.retrieval_mode
    assert _get_action_default(answer_parser, "output_dir") is None
    assert _get_action_default(answer_parser, "save_all") is False

    llm_parser = _get_subparser("llm")
    assert isinstance(llm_parser, argparse.ArgumentParser)


def test_help_text_defaults_are_constant_backed() -> None:
    """Help text should surface the same default constants shown by parser values."""
    query_help = _get_subparser("query").format_help()
    assert f"Default: {DEFAULT_MIN_SCORE}" in query_help

    query_documents_help = _get_subparser("query-documents").format_help()
    assert f"Default: {DEFAULT_MIN_SCORE_FOR_DOCUMENTS}" in query_documents_help

    query_titles_help = _get_subparser("query-titles").format_help()
    assert f"Default: {DEFAULT_QUERY_TITLES_MIN_SCORE}" in query_titles_help

    retrieve_help = _get_subparser("retrieve").format_help()
    assert f"default: {DEFAULT_RETRIEVAL_MODE}" in retrieve_help
    assert "--navis-d" in retrieve_help
    assert "--navis-min-score" in retrieve_help

    answer_help = _get_subparser("answer").format_help()
    assert f"Default: {DEFAULT_RETRIEVE_CONTENT_MIN_SCORE}" in answer_help
    assert "--navis-d" in answer_help
    assert "--navis-min-score" in answer_help
