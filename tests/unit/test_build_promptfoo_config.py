"""Tests for Promptfoo config generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    """Return repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return Promptfoo config generator path."""
    return _repo_root() / "scripts" / "build_promptfoo_config.py"


def _load_module() -> ModuleType:
    """Load scripts/build_promptfoo_config.py as module."""
    spec = importlib.util.spec_from_file_location("tests_build_promptfoo_config_module", _script_path())
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_builder_renders_family_anchor_and_alias(tmp_path: Path) -> None:
    """Builder should anchor family assertions once and reuse alias."""
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
      policy-config: '../../../../config/policy.default.yaml'
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

    module = _load_module()
    builder = module.PromptfooConfigBuilder(project_root=tmp_path)

    output_path = tmp_path / "experiments" / "promptfoo_regression" / "runs" / "latest" / "promptfooconfig.yaml"
    output_path.parent.mkdir(parents=True)
    output = builder.build_text(output_path=output_path)

    assert "assert: &q1_assertions" in output
    assert output.count("&q1_assertions") == 1
    assert "assert: *q1_assertions" in output
    assert "family: 'Q1¤'" in output
    assert "variant: 'Q1.0¤'" in output


def test_builder_writes_requested_output_path(tmp_path: Path) -> None:
    """Builder should render config relative to requested output path."""
    module = _load_module()
    builder = module.PromptfooConfigBuilder(project_root=_repo_root())

    output_path = tmp_path / "experiments" / "promptfoo_regression" / "runs" / "demo" / "promptfooconfig.yaml"
    output_path.parent.mkdir(parents=True)

    generated = builder.build_text(output_path=output_path)
    builder.write_output(output_path=output_path)
    written = output_path.read_text(encoding="utf-8")

    assert written == generated
    assert "tests:" in generated
    assert "file://" in generated


def test_builder_includes_policy_config_reference(tmp_path: Path) -> None:
    """Generated config should carry policy-config provider option."""
    module = _load_module()
    builder = module.PromptfooConfigBuilder(project_root=_repo_root())

    output_path = tmp_path / "experiments" / "promptfoo_regression" / "runs" / "demo" / "promptfooconfig.yaml"
    output_path.parent.mkdir(parents=True)
    generated = builder.build_text(output_path=output_path)

    assert "policy-config" in generated
    assert "effective/policy.default.yaml" in generated
