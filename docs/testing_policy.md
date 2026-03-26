## Testing and Mocking Policy

### Core rule

Prefer explicit dependency injection, narrow interfaces, and small fakes over `MagicMock` and monkey-patching.

Tests must verify behavior through clear seams in the code, not by patching internal implementation details.

### Required defaults

1. **Inject dependencies explicitly**
   - Pass external collaborators through constructors, function parameters, or small factories.
   - Do not instantiate network clients, SDK clients, repositories, clocks, or other side-effecting dependencies deep inside business logic unless there is a compelling reason.

2. **Define stable interfaces at boundaries**
   - Use small, explicit interfaces for external dependencies.
   - In Python, prefer `typing.Protocol` for these interfaces.
   - Business logic should depend on these interfaces, not directly on vendor SDKs or process-global modules.

3. **Prefer fakes, stubs, and spies over mocks**
   - Use lightweight in-memory fakes for repositories, gateways, and service clients where practical.
   - Use stubs for fixed responses.
   - Use spies only when call recording is required.
   - Prefer these to `MagicMock` because they are easier to read, reason about, and statically analyze.

4. **Mock only true boundaries**
   - Acceptable mock targets include:
     - network access
     - filesystem access
     - subprocess execution
     - clocks and time sources
     - randomness
     - environment access
     - third-party SDK adapters
     - message bus / queue adapters
   - Avoid mocking domain objects, internal helpers, or other application code under active development.

5. **Do not monkey-patch internal application dependencies**
   - Monkey-patching is a last resort for legacy containment or unavoidable global/process boundaries.
   - It must not be the default mechanism for unit testing business logic.
   - Repeated patching of internal imports is a design smell and should trigger refactoring toward injected dependencies.

6. **Wrap third-party libraries**
   - Create thin adapters around external SDKs and libraries.
   - Application code should depend on the adapter interface, not directly on the SDK.
   - Unit tests should exercise the application against a fake adapter.
   - Separate integration tests should cover the real adapter.

7. **Assert outcomes before interactions**
   - Prefer assertions on returned values, state changes, persisted records, and emitted domain events.
   - Use call-based assertions only when the interaction itself is the behavior being tested.

### Rules for `unittest.mock`

1. `MagicMock` must not be used by default.
2. If mocking is necessary, use `create_autospec(...)` or `spec_set=...`.
3. Bare, unconstrained mocks are discouraged because they hide interface drift and allow invalid calls.
4. Mock assertions must stay narrow and behavior-relevant. Do not assert incidental internal call structure.

### Rules for pytest monkeypatch / patch

1. Allowed uses:
   - environment variables
   - time sources
   - randomness
   - process-global facilities
   - unavoidable legacy seams
2. Disallowed as a routine practice:
   - patching internal services, repositories, helpers, or domain functions to make tests pass
   - patching multiple internals of the same unit under test instead of introducing a seam
3. If a test requires more than two non-global patches, treat that as a refactoring candidate.

### Test design guidance

When writing or updating tests, use this preference order:

1. real value objects
2. in-memory fake implementations
3. simple stubs or spies
4. autospecced mocks at external boundaries
5. monkey-patching only for unavoidable global or legacy cases

### Refactoring guidance

When encountering brittle tests with many patches or mocks:

1. identify the real side-effect boundary
2. extract a small interface for that boundary
3. inject the dependency explicitly
4. replace repeated mocks with a fake implementation
5. keep integration coverage for the concrete adapter

### Review checklist

A test should be flagged for redesign if any of the following are true:

- it patches more than two dependencies
- it mocks internal application code
- it primarily asserts `assert_called_*` rather than outcomes
- small production refactors break tests without changing behavior
- setup is dominated by patching and mock wiring
- the dependency structure of the unit is not obvious from the constructor or function signature

### Expected architectural style

This codebase should favor:
- explicit construction over hidden globals
- typed interfaces over implicit runtime coupling
- small adapters around side-effecting systems
- unit tests based on fakes
- integration tests for real external implementations

This is closer to dependency injection than dynamic monkey-patching, and should be treated as the default design approach.