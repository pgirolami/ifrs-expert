# Experiment 38: Q1 target recall tuning with IAS-S TOC representation

## Goal

Mirror experiment 36, but with IAS-S routed to a dedicated `toc` similarity representation, then tune:

- `IAS-S` (`d`, `min_score`)
- `IFRS-S` (`d`, `min_score`)
- `IFRIC` (`d`, `min_score`)
- `global_d`

Target documents that must appear in `document_hits` for every Q1 variant:

- `ias39`
- `ifrs9`
- `ifric16`

Command used for saved runs:

```bash
uv run python -m src.cli retrieve --policy-config <policy> --json
```

Queries:

- `experiments/00_QUESTIONS/Q1/Q1.0.txt` ... `Q1.22.txt` (23 queries)

## Policies

- Baseline: `policies/policy.baseline.yaml`
- Optimal: `policies/policy.optimal.yaml`

### Baseline (key settings)

- `IAS-S`: `similarity_representation=toc`, `d=6`, `min_score=0.4`
- `IFRS-S`: `d=4`, `min_score=0.53`
- `IFRIC`: `d=6`, `min_score=0.48`
- `global_d=25`

### Optimal found

- `IAS-S`: `similarity_representation=toc`, `d=12`, `min_score=0.44`
- `IFRS-S`: `d=10`, `min_score=0.53`
- `IFRIC`: `d=4`, `min_score=0.50`
- `global_d=35`

## Results

### Baseline

- all 3 targets present together: **5 / 23**
- per target presence:
  - `ias39`: **8 / 23**
  - `ifrs9`: **17 / 23**
  - `ifric16`: **23 / 23**

### Optimal

- all 3 targets present together: **23 / 23**
- per target presence:
  - `ias39`: **23 / 23**
  - `ifrs9`: **23 / 23**
  - `ifric16`: **23 / 23**

## Takeaways

1. For this Q1 family, IAS-S with `toc` representation is substantially better than prior IAS routing for consistently surfacing `ias39`.
2. Compared to experiment 36, the required `global_d` drops from 80 to 35 while reaching full 23/23 target recall.
3. The selected operating point keeps `IAS-S d` moderate (12) and `IAS-S min_score` relatively high (0.44).

## Artifacts

- `runs/baseline/*.retrieve.json` (23 outputs)
- `runs/optimal/*.retrieve.json` (23 outputs)
- `runs/summary.json`
- `policies/policy.baseline.yaml`
- `policies/policy.optimal.yaml`
