# Experiment 36: Q1 target-document recall tuning (d + min_score)

## Goal

Find `d` and `min_score` parameters for:

- `IAS-S` (target: `ias39`)
- `IFRS-S` (target: `ifrs9`)
- `IFRIC` (target: `ifric16`)

so these three documents are retrieved as `document_hits` across the full Q1 variant set (`Q1.0` … `Q1.22`) using:

```bash
uv run python -m src.cli retrieve --policy-config ...
```

## Setup

- Query set: `experiments/00_QUESTIONS/Q1/*.txt` (23 variants)
- Retrieval command used for saved outputs:
  - `uv run python -m src.cli retrieve --policy-config <policy> --json`
- Similarity representations were kept as configured in current policy (only `d` + `min_score` were tuned for the three target types).
- `global_d` remained `25`.

Policies used in this experiment:

- Baseline: `policies/policy.baseline.yaml`
- Best found with only per-type tuning ("optimal"): `policies/policy.optimal.yaml`
- Best found after also tuning `global_d` ("optimal_global_d"): `policies/policy.optimal_global_d.yaml`

## Best parameters found (per-type only)

```yaml
IAS-S:
  d: 15
  min_score: 0.45

IFRS-S:
  d: 5
  min_score: 0.53

IFRIC:
  d: 3
  min_score: 0.50

global_d: 25  # unchanged
```

## Best parameters found (including global_d)

```yaml
IAS-S:
  d: 25
  min_score: 0.45

IFRS-S:
  d: 10
  min_score: 0.53

IFRIC:
  d: 8
  min_score: 0.50

global_d: 80
```

## Results

### Baseline

- All three targets present in same retrieval: **1 / 23** queries
- Per-target presence:
  - `ias39`: 2 / 23
  - `ifrs9`: 17 / 23
  - `ifric16`: 23 / 23

### Best found with per-type tuning only (policy.optimal.yaml)

- All three targets present in same retrieval: **16 / 23** queries
- Per-target presence:
  - `ias39`: 20 / 23
  - `ifrs9`: 19 / 23
  - `ifric16`: 20 / 23

Missing cases:

- `Q1.0`: missing `ifric16`
- `Q1.1`: missing `ias39`, `ifric16`
- `Q1.2`: missing `ias39`, `ifric16`
- `Q1.10`: missing `ifrs9`
- `Q1.15`: missing `ifrs9`
- `Q1.16`: missing `ias39`, `ifrs9`
- `Q1.18`: missing `ifrs9`

### Best found with global_d tuning (policy.optimal_global_d.yaml)

- All three targets present in same retrieval: **23 / 23** queries
- Per-target presence:
  - `ias39`: 23 / 23
  - `ifrs9`: 23 / 23
  - `ifric16`: 23 / 23

## Conclusion

With the current document representations:

- tuning only per-type `d` + `min_score` improves recall but stops at **16/23**;
- adding `global_d` tuning enables **23/23** simultaneous retrieval of `ias39`, `ifrs9`, and `ifric16` on Q1 variants.

Trade-off: the successful configuration uses a much larger candidate set (`global_d=80`), so downstream prompt context and competition/noise should be evaluated before adopting it as default.

## Human conclusion

These parameters are too lax: we can't send chunks for 80 documents through prompt A. In experiment 34, we optimized for IFRS 9 and IFRIC 16, let's now optimize for IAS.

## Artifacts

- Baseline retrieval outputs (23 files): `runs/baseline/*.retrieve.json`
- Best-found retrieval outputs with per-type-only tuning (23 files): `runs/optimal/*.retrieve.json`
- Best-found retrieval outputs with global_d tuning (23 files): `runs/optimal_global_d/*.retrieve.json`
- Execution summary: `runs/summary.json`
