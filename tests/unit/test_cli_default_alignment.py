"""Tests for CLI defaults after policy-driven migration."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.cli import _build_answer_options, _build_parser, _load_policy
from src.commands.answer import AnswerOptions


def _get_subparser(name: str) -> argparse.ArgumentParser:
    parser = _build_parser()
    subparsers_action = next(
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)  # noqa: SLF001
    )
    return subparsers_action.choices[name]


def _has_required_argument(subparser: argparse.ArgumentParser, dest: str) -> bool:
    for action in subparser._actions:  # noqa: SLF001
        if action.dest == dest:
            return action.required
    msg = f"Missing parser action for {dest}"
    raise AssertionError(msg)


def test_policy_config_required_for_retrieval_commands() -> None:
    """All retrieval-family commands should require --policy-config."""
    for command in ["query", "query-documents", "query-titles", "retrieve", "answer"]:
        subparser = _get_subparser(command)
        assert _has_required_argument(subparser, "policy_config") is True


def test_answer_options_builder_loads_policy_and_passthrough_values() -> None:
    """CLI builder should set policy and optional overrides on AnswerOptions."""
    parser = _build_parser()
    args = parser.parse_args(
        [
            "answer",
            "--policy-config",
            "config/policy.default.yaml",
            "--output-dir",
            "tmp/out",
        ]
    )

    options = _build_answer_options(args, _load_policy(args))

    assert isinstance(options, AnswerOptions)
    assert options.output_dir == Path("tmp/out")
    assert options.policy.k > 0
