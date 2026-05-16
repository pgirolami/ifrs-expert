# Idiomatic Pydantic AI Plan

## Goal
Make the Pydantic AI usage in this repo idiomatic, not just functional.

## What "idiomatic" means here
- Agents are the primary abstraction, not a thin `Agent(...).run_sync(...)` wrapper.
- Dependencies use `deps_type` and `RunContext` where runtime state matters.
- Model behavior is shaped with `instructions` / `system_prompt` / dynamic instruction functions.
- Tools and reusable capabilities are explicit when the model needs runtime access.
- Structured output stays typed end-to-end.
- Run settings, metadata, and usage limits are applied at the right layer.
- Agent specs are considered where config should live outside code.

## Non-goals
- No novelty for novelty's sake.
- No replacing working code with abstract layers that do not buy anything.
- No mixing unrelated cleanup into this pass.

## Milestones

### Milestone 1 — Normalize agent shape
**Problem:** current agents are minimal wrappers around `Agent.run_sync()`.

**Done when:**
- core agent entry points use explicit agent classes/factories with typed dependencies
- `RunContext` is used where runtime state is needed
- agent construction is centralized instead of repeated ad hoc
- tests cover the new agent contract
- Status: done.

### Milestone 2 — Move prompt shaping into agent instructions
**Problem:** prompt shaping is still mostly external string assembly.

**Done when:**
- stable instructions move into `instructions` / `system_prompt`
- runtime-dependent prompt shaping moves into decorated instruction functions
- prompt assembly helpers are reduced to true formatting concerns
- redundant prompt glue is removed
- Status: done.

### Milestone 3 — Introduce real tools and capabilities
**Problem:** the project has model calls, but not enough explicit agent tools/capabilities.

**Done when:**
- repeated model-side concerns become explicit tools
- reusable tool/instruction bundles become capabilities where useful
- tool boundaries are visible in the agent contract
- tool tests verify allow-listing, retries, and typed context
- Status: done.

### Milestone 4 — Add run-level controls
**Problem:** model behavior is still under-specified at the run boundary.

**Done when:**
- `model_settings` are used intentionally
- `metadata` is passed through for observability / tracing
- `usage_limits` are applied where needed
- concurrency or retry controls are set intentionally, not by default

### Milestone 5 — Consider agent specs for stable configuration
**Problem:** some agent config may belong in code, some in spec.

**Done when:**
- we decide which agents should be code-defined vs spec-defined
- any stable agent config that fits a spec moves to YAML/JSON
- tests cover the spec path if adopted

### Milestone 6 — Remove leftover non-idiomatic glue
**Problem:** the repo still contains transitional patterns from older agent shapes.

**Done when:**
- thin wrappers are removed or justified
- duplicated agent construction disappears
- docs and tests match the final agent style
- the remaining Pydantic AI code reads like a native usage example

## Suggested implementation order
1. core agent factory + deps model
2. instructions/system prompts
3. tools/capabilities
4. run settings/metadata/limits
5. spec-driven config if it still adds value
6. cleanup and test tightening

## Acceptance bar
- `Agent`, `RunContext`, instructions, tools, and capabilities are used where they earn their keep.
- The code reads like a Pydantic AI app, not a generic wrapper around LLM calls.
- Existing behavior stays covered by tests.
- No unnecessary abstractions are introduced.
