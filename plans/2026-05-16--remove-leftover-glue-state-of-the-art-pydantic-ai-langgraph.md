# Plan — Remove leftover glue and finish the Pydantic AI + LangGraph shape

## Goal

Turn the repo from a mostly migrated codebase into a clean, state-of-the-art implementation of:

- Pydantic AI as the LLM application layer
- LangGraph as the workflow/control layer
- typed domain objects as the canonical internal contract

This plan targets leftover glue, compatibility shims, and thin adapters that still make the code read like a transition state.

## Scan findings

The scan found these leftover glue patterns:

- `src/commands/answer.py`
  - legacy CLI command layer that should be removed or merged into the real application entry point
  - the config/validation/engine wiring it performs is still split from the app layer itself

- `src/ai/pydantic_client.py`
  - repeatable `run_sync` wrapper pattern for text and structured agents
  - still exposes a completion-style API instead of a stronger app boundary

- `src/ui/follow_up_agent.py`
  - another thin Pydantic AI adapter with the same run pattern
  - text wrapper sits on top of structured output instead of being part of a shared agent layer

- `src/cli.py`
  - legacy/back-compat helpers remain
  - raw `llm` stdin path should be removed if it is only serving as an escape hatch

- `src/policy.py`
  - compatibility views and aliases still support old shapes

- `src/commands/__init__.py`
  - compatibility exports should be deleted; callers should import concrete modules directly

These are not bugs by themselves, but they are glue seams that keep the repo from reading like a final architecture.

## Non-goals

- Do not change corpus/schema/storage formats unless a milestone explicitly requires it.
- Do not rewrite retrieval semantics just to remove wrappers.
- Do not add framework machinery that only moves code around.

## Milestones

### Milestone 1 — Inventory and delete glue

**Objective:** identify migration leftovers and remove them from the core path.

**Done when:**
- every thin adapter, compatibility view, and backward-compat path is either removed or moved behind a clearly temporary legacy boundary
- any remaining boundary modules are explicitly documented as temporary and are not used by the main app path
- tests exist for the intended public contract of those boundary modules

### Milestone 2 — Collapse Pydantic AI wrappers into one app-facing layer

**Objective:** make Pydantic AI usage look native, not layered through repeated completion adapters.

**Done when:**
- one canonical agent/app layer owns model selection, deps, run controls, and output contracts
- structured and text generation share the same underlying agent construction path
- no duplicate wrapper logic remains across `pydantic_client.py`, follow-up generation, and related adapters
- agent usage stays typed end-to-end with `deps_type`, `RunContext`, instructions, tools, and structured outputs
- core call sites no longer need wrapper-specific knowledge to get a result

### Milestone 3 — Make LangGraph the real workflow boundary

**Objective:** move case-analysis orchestration from a mostly linear pipeline into a graph-native execution model.

**Done when:**
- graph state is typed and expresses real workflow state, not just transient plumbing
- nodes own workflow transitions instead of a higher-level adapter stitching stages together
- interruptions/branching/clarification paths are first-class graph behavior
- tool use is bounded by graph stage, not scattered through wrappers
- the answer path can be read as a graph, not as a chain of glue methods

### Milestone 4 — Introduce a typed LangGraph state model

**Objective:** remove the remaining graph boundary casts by making the case-analysis state strongly typed end to end.

**Done when:**
- the LangGraph state is represented by a `TypedDict` or equivalent strongly typed state contract
- graph nodes read and write the typed state directly instead of relying on `dict[str, object]` plus boundary casts
- the graph runner boundary no longer needs broad `cast(...)` calls to rebuild state snapshots
- tests continue to cover the graph contract and the typed state shape
- the graph state remains practical for partial updates and LangGraph integration

### Milestone 5 — Remove compatibility shims entirely

**Objective:** delete legacy support code that exists only to keep old call sites alive, unless a short-lived transition wrapper is absolutely required.

**Done when:**
- compatibility views in `src/policy.py` are removed from the main path, with no new core code depending on them
- `src/commands/__init__.py` compatibility exports are removed
- CLI back-compat helpers are removed
- tests stop depending on implementation-era wrappers and instead assert stable behavior
- the public surface is small, intentional, and documented without compatibility shims

### Milestone 6 — Tighten docs, tests, and acceptance criteria

**Objective:** make the final architecture obvious to contributors and reviewers.

**Done when:**
- docs describe the repo as a typed Pydantic AI + LangGraph application, not a migration
- tests cover the public boundaries, graph transitions, and agent contracts
- no core module reads like a temporary bridge
- search for `compatibility`, `backward compatibility`, `thin adapter`, or `wrapper` in core code finds only deliberate boundary code

## Suggested order

1. Inventory glue and mark keep/remove boundaries
2. Consolidate Pydantic AI agent construction
3. Rework the LangGraph workflow boundary
4. Introduce a typed LangGraph state model
5. Remove compatibility shims and legacy CLI surface
6. Update docs and tests to match the final shape

## Acceptance bar

The repo is done when:

- Pydantic AI usage is centralized, typed, and intentional
- LangGraph owns orchestration, branching, and state transitions
- graph state is strongly typed and boundary casts are minimized or eliminated
- compatibility code is eliminated from the main code path
- core modules no longer contain migration glue
- the codebase reads like a final architecture, not a halfway point
