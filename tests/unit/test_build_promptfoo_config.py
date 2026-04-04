"""Tests for the Promptfoo config generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return the Promptfoo config generator path."""
    return _repo_root() / "scripts" / "build_promptfoo_config.py"


def _load_build_promptfoo_module() -> ModuleType:
    """Load scripts/build_promptfoo_config.py as a module for unit tests."""
    spec = importlib.util.spec_from_file_location("tests_build_promptfoo_config_module", _script_path())
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_promptfoo_config_builder_renders_family_anchor_and_alias(tmp_path: Path) -> None:
    """The builder should anchor family assertions once and reuse them for later variants."""
    base_path = tmp_path / "promptfoo_src" / "base.yaml"
    base_path.parent.mkdir(parents=True)
    base_path.write_text(
        """
evaluateOptions:
  cache: false
prompts:
  - '{{question}}'
providers:
  - id: 'exec:test'
    label: 'Provider'
    config:
      llm_provider: 'openai'
readme: |
  Demo suite
""".lstrip(),
        encoding="utf-8",
    )

    family_dir = tmp_path / "experiments" / "00_QUESTIONS" / "Q1"
    family_dir.mkdir(parents=True)
    (family_dir / "Q1.0.txt").write_text("Question 0", encoding="utf-8")
    (family_dir / "Q1.1.txt").write_text("Question 1", encoding="utf-8")
    (family_dir / "family.yaml").write_text(
        """
family_id: Q1
defaults:
  options:
    mode: live
assert:
  - type: is-json
    value: file://./prompts/schema.json
    description: JSON schema
variants:
  - id: Q1.0
    file: Q1.0.txt
    description: Variant zero
  - id: Q1.1
    file: Q1.1.txt
    description: Variant one
""".lstrip(),
        encoding="utf-8",
    )

    build_promptfoo_config = _load_build_promptfoo_module()
    builder = build_promptfoo_config.PromptfooConfigBuilder(project_root=tmp_path)

    output = builder.build_text()

    assert "assert: &q1_assertions" in output
    assert output.count("&q1_assertions") == 1, "Expected one Q1 assertion anchor"
    assert "assert: *q1_assertions" in output
    assert "family: 'Q1'" in output
    assert "variant: 'Q1.0'" in output
    assert "description: 'Q1.0 - Variant zero'" in output


def test_promptfoo_config_builder_omits_options_when_family_has_no_defaults(tmp_path: Path) -> None:
    """The builder should omit test options when a family does not define them."""
    base_path = tmp_path / "promptfoo_src" / "base.yaml"
    base_path.parent.mkdir(parents=True)
    base_path.write_text(
        """
evaluateOptions:
  cache: false
prompts:
  - '{{question}}'
providers:
  - id: 'exec:test'
    label: 'Provider'
    config:
      llm_provider: 'openai'
readme: |
  Demo suite
""".lstrip(),
        encoding="utf-8",
    )

    family_dir = tmp_path / "experiments" / "00_QUESTIONS" / "Q2"
    family_dir.mkdir(parents=True)
    (family_dir / "Q2.0.txt").write_text("Question 0", encoding="utf-8")
    (family_dir / "family.yaml").write_text(
        """
family_id: Q2
assert:
  - type: is-json
    value: file://./prompts/schema.json
    description: JSON schema
variants:
  - id: Q2.0
    file: Q2.0.txt
    description: Variant zero
""".lstrip(),
        encoding="utf-8",
    )

    build_promptfoo_config = _load_build_promptfoo_module()
    builder = build_promptfoo_config.PromptfooConfigBuilder(project_root=tmp_path)

    output = builder.build_text()

    assert "options:" not in output
    assert "description: 'Q2.0 - Variant zero'" in output


def test_promptfoo_config_builder_matches_checked_in_config() -> None:
    """The checked-in Promptfoo config should match the generated output."""
    build_promptfoo_config = _load_build_promptfoo_module()
    builder = build_promptfoo_config.PromptfooConfigBuilder(project_root=_repo_root())

    generated = builder.build_text()
    checked_in = (_repo_root() / "promptfooconfig.yaml").read_text(encoding="utf-8")

    assert generated == checked_in
