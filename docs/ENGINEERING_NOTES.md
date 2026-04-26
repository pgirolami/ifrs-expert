### 2026-04-26 : Getting to the same result faster next time
Reached a much clearer view of the development process in hindsight.

**Key lesson:**
> evaluate the evidence layer directly before optimizing reasoning on top of it

**1. Early work implicitly simulated document routing**
- In the initial prototype with only `IFRS 9` and `IFRIC 16`, document routing had effectively been done manually by preselecting the relevant standards
- That shortcut was useful because it allowed a fast end-to-end demo for the SME
- But it also hid a major future problem: once the corpus became realistic, authority routing and noisy retrieval became the blocker

**2. Retrieval should have been instrumented earlier**
- A number of experiments were spent trying to improve approach stability before it was fully understood that part of the instability came from retrieval inconsistency
- Earlier paragraph / chunk-level diagnostics would likely have made the project move faster

**Learning:**

A better order for next time would be:
1. prove the question is answerable in principle (done)
2. build a minimal end-to-end demo for SME feedback (done)
3. instrument retrieval deeply (late)
4. stabilize document routing and chunk evidence (done)
5. only then optimize approach identification and applicability behavior (too early)
