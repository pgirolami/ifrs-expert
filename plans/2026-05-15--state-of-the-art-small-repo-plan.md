# Plan — State-of-the-art cleanup for a small repo

## Goal

Raise IFRS Expert to a standard that feels **state-of-the-art for a small, focused codebase**: clear architecture, idiomatic framework usage, strong typing, and low accidental complexity.

This plan is intentionally a **problem statement**, not a solution design. It lists what is still structurally off in the repo and what must be true before the codebase can be considered clean and modern.

## What “state-of-the-art” means here

For a repo this size, the target is not “more abstraction” or “more framework.” The target is:

- framework usage that follows the framework’s intended mental model;
- clear ownership of orchestration vs domain logic vs rendering;
- small modules with real boundaries, not shallow pass-through layers;
- typed data flow instead of JSON/string glue;
- fewer transitional patterns and compatibility shims in the core path;
- code that is easy to test, inspect, and extend without rereading multiple large files.

## 1. Problems blocking a full Pydantic AI app design

Pydantic AI is present, but the repo still does not yet read like a full Pydantic AI application.

### Current problems

- **Agents are created ad hoc inside wrapper methods.**
  The code calls `Agent(...)` directly in small helper methods instead of having a clear app-level agent layer with stable ownership.

- **The app still treats Pydantic AI as a thin completion wrapper.**
  The current usage is mostly “run prompt in, get model out,” which leaves out the deeper app design Pydantic AI is meant to support: explicit agent boundaries, dependency injection, reusable instructions, tool boundaries, and richer lifecycle hooks.

- **Typed outputs exist, but typed app structure is incomplete.**
  The code has typed output models, but the boundaries around agents, dependencies, and runtime state are still loose and partially transitional.

- **JSON bridges still leak through the core flow.**
  Some paths still serialize typed outputs back to JSON for downstream compatibility instead of keeping typed objects as the canonical application boundary.

- **Provider/model resolution is centralized, but not yet a full app contract.**
  The repo resolves models from environment variables, but there is not yet a single explicit application configuration surface that makes the agent stack feel intentional rather than patched together.

- **The follow-up agent is only partially shaped like a real app component.**
  The grounded follow-up path exists, but its structure still looks like an auxiliary wrapper rather than a first-class agent module with a clear contract.

### What this means in practice

The repo currently uses Pydantic AI **correctly enough to work**, but not yet **cleanly enough to feel designed around it**.

## 2. Problems blocking “advanced LangGraph” usage

LangGraph is present, but the current use is still the minimal deterministic orchestration pattern.

### Current problems

- **The graph is shallow and linear.**
  The workflow has explicit nodes and conditional failure routing, but it still behaves like a simple pipeline with graph syntax rather than a graph-shaped execution model.

- **The state model is too small for advanced graph work.**
  The graph state carries the minimum necessary fields, which is fine for a linear flow but not enough for real graph-native behavior such as branching analysis, resumable state, interrupts, or staged tool use.

- **There is no checkpointing or resume story.**
  Advanced LangGraph usage usually makes persistence and continuation part of the design. This repo currently has no such runtime model.

- **No interrupt/human-in-the-loop boundary exists.**
  The graph cannot pause for clarification, inspection, or resumption in a first-class way.

- **Tool use is not graph-bounded yet.**
  The plan for tool-calling is conceptually present, but the actual runtime pattern is still “deterministic steps around LLM calls,” not “graph-managed stages with bounded agent autonomy.”

- **The graph is not yet a real state machine for case analysis.**
  It does not yet express alternative paths, loop-backs, or stage-specific state evolution in a way that would justify LangGraph over a simpler orchestrator.

### What this means in practice

The current LangGraph usage is **acceptable**, but it is not yet **advanced**. It is mostly a control-flow wrapper, not yet a graph-native workflow runtime.

## 3. Problems blocking architecture-level cleanliness

The repo is functional, but several parts still feel like a codebase in transition.

### Current problems

- **Large files still own too much behavior.**
  Some high-traffic modules remain very large and mix several responsibilities in one place.

- **Orchestration, transformation, and rendering are still too close together.**
  The answer path especially still has places where workflow control, prompt construction, context shaping, validation, and output rendering are tightly adjacent.

- **There are too many transitional adapters.**
  The repo contains compatibility layers and bridge methods that are understandable during migration but make the architecture feel less final.

- **The module structure is deeper than it needs to be in some areas and too shallow in others.**
  Some files are mostly pass-throughs, while other files are overloaded with domain and orchestration logic.

- **The naming of layers is not always consistent with responsibility.**
  Some modules are named like services but behave like mixed orchestration utilities; some helpers are hidden inside engine classes instead of living at the boundary they actually own.

- **There is still evidence of historical layering.**
  The repo carries old paths, new paths, and migration artifacts at the same time, which is reasonable for a transition but not yet a clean final architecture.

- **Tests reflect implementation shape too closely in some places.**
  Some tests verify intermediate plumbing rather than stable behavior, which makes refactors more expensive than necessary.

### What this means in practice

The architecture is **good for a growing project**, but not yet **minimal, crisp, and obviously well-owned**.

## 4. What should be true after cleanup

The repo should be able to satisfy these statements:

- Pydantic AI is used as a first-class app layer, not just a typed completion wrapper.
- LangGraph is used as a real workflow runtime, not just a node-shaped function chain.
- Each major module has one obvious owner and one obvious reason to exist.
- The answer path can be understood without jumping through several large files.
- Transitional compatibility code is reduced to the minimum necessary surface.
- The codebase reads as intentionally designed, not incrementally assembled.

## 5. Areas to audit before any implementation

If this plan is followed through, the first audit targets should be:

- `src/ai/`
- `src/case_analysis/`
- `src/commands/answer.py`
- `src/ui/follow_up_agent.py`
- the largest retrieval and ingestion modules
- tests that assert plumbing instead of behavior

## 6. Out of scope for this plan

- changing the corpus schema;
- changing FAISS/vector-store formats;
- rewriting retrieval semantics for their own sake;
- adding framework machinery that does not reduce complexity;
- optimizing for maximum abstraction over maximum clarity.

## 7. Intended outcome

This plan should lead to a repo that is small enough to stay understandable, but modern enough that its framework choices and module boundaries feel deliberate rather than historical.

## 8. Phasing and milestones

> The first phase should stabilize the Pydantic AI application design. The second phase should use that design to simplify the repo architecture. LangGraph cleanup should only be expanded when the Pydantic AI boundary is stable enough to support it.

### Phase 1 — Full Pydantic AI app design

> Goal: make the LLM layer feel like a real Pydantic AI application rather than a set of agent wrappers.

#### Milestone 1.1 — Define the Pydantic AI app boundary
- Problem: agent ownership is scattered across helper methods and call sites.
- Problem: typed outputs exist, but the application layer is not clearly modeled as a first-class Pydantic AI app.
- Problem: provider/model resolution is centralized only at the environment-variable level, not at the application-contract level.
- Done when the repo has one clearly named place where Pydantic AI app ownership lives, instead of scattered agent construction across wrappers and call sites.
- Done when provider/model resolution is described as part of the app contract, not just as environment-variable parsing.
- Done when the boundary is documented well enough that a new contributor can tell where Pydantic AI begins and ends without reading multiple unrelated files.
- Status: done.

#### Milestone 1.2 — Make dependencies and outputs canonical
- Problem: some flows still serialize typed output back into JSON before the next stage consumes it.
- Problem: Pydantic AI outputs are not yet treated as the stable internal contract across the app boundary.
- Problem: the code still relies on compatibility bridges instead of a clean typed handoff between stages.
- Done when the primary LLM flow keeps typed objects as the canonical internal contract instead of repeatedly round-tripping through JSON for convenience.
- Done when the main app path can validate output shape as part of the contract rather than as an after-the-fact compatibility step.
- Done when the code no longer needs obvious transitional parsing bridges in the core path just to keep stages talking to each other.
- Status: done.

#### Milestone 1.3 — Make follow-up generation a first-class app component
- Problem: follow-up generation exists, but it still behaves like an auxiliary adapter rather than part of the same app design.
- Problem: grounded follow-up behavior is not yet represented by a clear, intentional agent boundary.
- Done when grounded follow-up generation has a stable, explicit home in the app structure and is no longer just an auxiliary helper.
- Done when its inputs, outputs, and responsibility are clear from the module boundary itself.
- Done when follow-up behavior can be reasoned about as part of the same application model as the main answer flow.
- Status: done.

#### Milestone 1.4 — Remove transitional LLM glue from the core path
- Problem: the core answer path still contains migration-era seams that make the framework usage look improvised.
- Problem: the repo is still mixing model orchestration, parsing, and compatibility logic in ways that obscure the intended app design.
- Done when the main answer path no longer depends on migration-era compatibility seams to explain how prompts, outputs, and rendering connect.
- Done when orchestration, parsing, and compatibility logic are no longer visibly mixed in the core LLM flow.
- Done when the Pydantic AI layer feels intentional rather than bolted onto an older pipeline.
- Status: done.

#### Milestone 2.1 — Separate orchestration from domain logic
- Problem: the answer path still mixes workflow control, prompt construction, retrieval shaping, validation, and rendering too closely.
- Problem: some modules own more than one architectural concern.
- Done when workflow control, prompt construction, retrieval shaping, validation, and rendering are no longer tightly interleaved in the same path.
- Done when each major module has one obvious architectural responsibility.
- Done when reading the answer path no longer requires mentally untangling mixed concerns.
- Status: done.

#### Milestone 2.2 — Remove large mixed-responsibility modules
- Problem: several high-traffic files are still too large to be comfortably readable in one sitting.
- Problem: some files are mostly glue, while others are overloaded with unrelated responsibilities.
- Done when the worst high-traffic modules are materially smaller and no longer contain several unrelated workflows in one file.
- Done when the codebase has fewer large files that must be treated as special cases during review or refactoring.
- Done when the remaining large files are large for a clear reason, not because they accumulated unrelated behavior.
- Status: done.

#### Milestone 2.3 — Eliminate shallow abstractions
- Problem: some classes and modules exist mainly to forward data without hiding meaningful complexity.
- Problem: the module tree contains too many transitional wrappers for a codebase of this size.
- Done when modules and classes that only forward data without hiding complexity are removed, merged, or clearly justified.
- Done when the module tree is easier to navigate because each layer earns its existence.
- Done when the repo has fewer transitional wrappers that exist mainly because of historical refactors.
- Status: done.

#### Milestone 2.4 — Make tests track behavior instead of plumbing
- Problem: some tests are coupled to implementation details and internal sequencing.
- Problem: that coupling makes architectural cleanup harder than it should be.
- Done when the test suite relies less on internal sequencing and more on stable externally meaningful behavior.
- Done when refactors can happen without rewriting tests that only asserted implementation shape.
- Done when the tests are obviously protecting the architecture rather than fossilizing it.
- Status: done.

#### Milestone 3.1 — Expand graph state meaningfully
- Problem: the current graph state is too small for graph-native workflows.
- Problem: the workflow does not yet have enough state to support branching, interrupt/resume, or stage-specific persistence.
- Done when the graph state can represent more than the minimum happy-path fields and is suitable for real workflow branching.
- Done when the state model supports interruption, continuation, or stage-specific persistence without feeling retrofitted.
- Done when the graph no longer looks like a linear function chain with a `StateGraph` wrapper.
- Status: done.

#### Milestone 3.2 — Introduce real graph-native control points
- Problem: the current graph is still mostly a linear pipeline with graph syntax.
- Problem: it lacks the control points needed for clarification, continuation, and bounded autonomy.
- Done when the graph has explicit control points for alternate paths such as clarification, continuation, or loop-back behavior.
- Done when the workflow can express graph-native state transitions instead of only pass/fail routing.
- Done when the graph is obviously the right abstraction for the workflow, not just one possible implementation.
- Status: done.

#### Milestone 3.3 — Bounded tool use inside graph stages
- Problem: tool-calling is not yet an explicit graph-bounded capability.
- Problem: the runtime currently does not express where autonomy begins and ends.
- Done when tool use is clearly scoped to graph-managed stages and the limits of autonomy are visible in the design.
- Done when the runtime makes it clear which stages are deterministic and which stages may call tools.
- Done when tool-calling is an explicit part of the graph contract rather than an implied behavior layered on top.
- Status: done.
