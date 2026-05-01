# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `51_answer-evals_Q3`
- Run: `2026-05-01_13-49-24_promptfoo-eval-family-q3`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 22

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| amortised_cost | no | 22/22 | 11 |
| fair_value_through_other_comprehensive_income | no | 22/22 | 11 |
| fair_value_through_profit_or_loss | no | 22/22 | 11 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q3.0 | 2 | 90.0 | 90.0 | 0 | 6 |
| Q3.1 | 2 | 80.0 | 100.0 | 0 | 6 |
| Q3.2 | 2 | 100.0 | 100.0 | 0 | 6 |
| Q3.3 | 2 | 80.0 | 100.0 | 0 | 6 |
| Q3.4 | 2 | 100.0 | 100.0 | 0 | 6 |
| Q3.5 | 2 | 90.0 | 90.0 | 0 | 6 |
| Q3.6 | 2 | 100.0 | 100.0 | 0 | 6 |
| Q3.7 | 2 | 90.0 | 100.0 | 0 | 6 |
| Q3.8 | 2 | 70.0 | 100.0 | 0 | 6 |
| Q3.9 | 2 | 90.0 | 100.0 | 0 | 6 |
| Q3.10 | 2 | 80.0 | 100.0 | 0 | 6 |

## Authority Categorization by Run

### Q3.0 / 0

- Question: Qu'est-ce qu'un actif dont les termes contractuels donnent droit uniquement au paiement du principal et des intérêts ?
- Embedded question: Qu'est-ce qu'un actif dont les termes contractuels donnent droit uniquement au paiement du principal et des intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | gB3.2.10-B3.2.11 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.56-0.64 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.59 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.61-0.61 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |

### Q3.0 / 1

- Question: Qu'est-ce qu'un actif dont les termes contractuels donnent droit uniquement au paiement du principal et des intérêts ?
- Embedded question: Qu'est-ce qu'un actif dont les termes contractuels donnent droit uniquement au paiement du principal et des intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | gB3.2.10-B3.2.11 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.56-0.64 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.59 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |

### Q3.1 / 0

- Question: Comment définit-on un actif financier dont les flux contractuels se limitent au remboursement du principal et au paiement d’intérêts ?
- Embedded question: Comment définit-on un actif financier dont les flux contractuels se limitent au remboursement du principal et au paiement d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.63 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.67 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.66 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | — | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.67 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.62-0.65 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 19 | g116-119 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g123-126 | 🗑️ dropped | 0.55-0.57 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.53-0.53 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.59 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.54-0.61 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.53 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

### Q3.1 / 1

- Question: Comment définit-on un actif financier dont les flux contractuels se limitent au remboursement du principal et au paiement d’intérêts ?
- Embedded question: Comment définit-on un actif financier dont les flux contractuels se limitent au remboursement du principal et au paiement d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.63 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.67 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.66 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | — | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.67 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.62-0.65 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 19 | g116-119 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g123-126 | 🖼️ peripheral | 0.55-0.57 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🖼️ peripheral | 0.56-0.57 | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.53-0.53 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.59 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.54-0.61 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.53 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

### Q3.2 / 0

- Question: Quelle est la nature d’un actif dont les conditions contractuelles prévoient exclusivement des encaissements de principal et d’intérêts ?
- Embedded question: Quelle est la nature d’un actif dont les conditions contractuelles prévoient exclusivement des encaissements de principal et d’intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.58-0.64 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.59-0.64 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |

### Q3.2 / 1

- Question: Quelle est la nature d’un actif dont les conditions contractuelles prévoient exclusivement des encaissements de principal et d’intérêts ?
- Embedded question: Quelle est la nature d’un actif dont les conditions contractuelles prévoient exclusivement des encaissements de principal et d’intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.58-0.64 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.59-0.64 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |

### Q3.3 / 0

- Question: Peut-on expliquer ce qu’est un actif financier caractérisé par des flux contractuels composés uniquement de principal et d’intérêts ?
- Embedded question: Peut-on expliquer ce qu’est un actif financier caractérisé par des flux contractuels composés uniquement de principal et d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.68 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.64-0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.63 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | — | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.61-0.65 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG28-AG28 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 7 | g13-15 | 🖼️ peripheral | 0.58-0.60 | D:0 |
| IAS 7 | g16-16 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 7 | g21-21 | 🗑️ dropped | 0.57 | D:0 |
| IAS 7 | g22-24 | 🗑️ dropped | 0.58 | D:0 |
| IAS 7 | g31-34 | 🖼️ peripheral | 0.58-0.59 | D:0 |
| IAS 7 | g43-44 | 🖼️ peripheral | 0.57-0.58 | D:0 |
| IAS 7 | g7-9 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g15-17 | 🔎 secondary | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g58-58 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.58 | D:0 |
| IFRIC 12 | g15-19 | 🗑️ dropped | 0.58 | D:0 |
| IFRIC 12 | g23-25 | 🔎 secondary | — | D:0 |

### Q3.3 / 1

- Question: Peut-on expliquer ce qu’est un actif financier caractérisé par des flux contractuels composés uniquement de principal et d’intérêts ?
- Embedded question: Peut-on expliquer ce qu’est un actif financier caractérisé par des flux contractuels composés uniquement de principal et d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.68 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.64-0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.63 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | — | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.61-0.65 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG28-AG28 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🔎 secondary | 0.62-0.63 | D:0 |
| IAS 7 | g13-15 | 🖼️ peripheral | 0.58-0.60 | D:0 |
| IAS 7 | g16-16 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 7 | g21-21 | 🗑️ dropped | 0.57 | D:0 |
| IAS 7 | g22-24 | 🗑️ dropped | 0.58 | D:0 |
| IAS 7 | g31-34 | 🗑️ dropped | 0.58-0.59 | D:0 |
| IAS 7 | g43-44 | 🗑️ dropped | 0.57-0.58 | D:0 |
| IAS 7 | g7-9 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.58 | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.58 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | — | D:0 |

### Q3.4 / 0

- Question: Comment interpréter un instrument financier dont les paiements contractuels se limitent au principal et aux intérêts ?
- Embedded question: Comment interpréter un instrument financier dont les paiements contractuels se limitent au principal et aux intérêts ?
financial instrument

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.64-0.70 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.66-0.69 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | g42-95 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.69 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.64-0.68 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.67 | D:0 |
| IAS 32 | gAG38-AG40 | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | gAG38A-AG38D_V1 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG38E-AG38F_V1 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g72-73 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | 0.61 | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.58-0.59 | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | sgAG94-AG97 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | g105-109 | 🖼️ peripheral | 0.57-0.59 | D:0 |
| IFRS 15 | g113-122 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g114-115 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g116-118 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g119-119 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g120-122 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g26-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g31-45 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 15 | g35-37 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g46-90 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | 0.59-0.62 | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g73-86 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g81-83 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g84-86 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g87-90 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB6-B8 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | 0.59-0.59 | D:0 |

### Q3.4 / 1

- Question: Comment interpréter un instrument financier dont les paiements contractuels se limitent au principal et aux intérêts ?
- Embedded question: Comment interpréter un instrument financier dont les paiements contractuels se limitent au principal et aux intérêts ?
financial instrument

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.64-0.70 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.66-0.69 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | g11-14 | 🖼️ peripheral | 0.68 | D:0 |
| IAS 32 | g15-27 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 32 | g21-24 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 32 | g25-25 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g26-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | g42-95 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🖼️ peripheral | 0.69 | D:0 |
| IAS 32 | gAG20-AG24 | 🖼️ peripheral | 0.64-0.68 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🖼️ peripheral | 0.67 | D:0 |
| IAS 32 | gAG38-AG40 | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | gAG38A-AG38D_V1 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG38E-AG38F_V1 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g72-73 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | 0.61 | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.58-0.59 | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG98-AG99BA | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | sgAG94-AG97 | 🖼️ peripheral | 0.57 | D:0 |
| IFRS 15 | g105-109 | 🖼️ peripheral | 0.57-0.59 | D:0 |
| IFRS 15 | g113-122 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g114-115 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g116-118 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g119-119 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g120-122 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g26-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g31-45 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 15 | g35-37 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g46-90 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.59-0.62 | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g73-86 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g81-83 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g84-86 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g87-90 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB6-B8 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB66-B69 | 🖼️ peripheral | 0.59-0.59 | D:0 |

### Q3.5 / 0

- Question: À quoi correspond un actif dont les flux de trésorerie contractuels ne comprennent que le principal et les intérêts ?
- Embedded question: À quoi correspond un actif dont les flux de trésorerie contractuels ne comprennent que le principal et les intérêts ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.68 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 7 | g10-17 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 7 | g13-15 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 7 | g16-16 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 7 | g17-17 | 🖼️ peripheral | — | D:0 |
| IAS 7 | g31-34 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 7 | g37-38 | 🗑️ dropped | 0.59 | D:0 |
| IAS 7 | g39-42B | 🗑️ dropped | 0.61 | D:0 |
| IAS 7 | g43-44 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 7 | g6-9 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 7 | g7-9 | 🖼️ peripheral | 0.70 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g103-108F | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.54 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | 0.53-0.60 | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.54 | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.55 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.58 | D:0 |
| IFRS 17 | g1-2 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g10-13 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | g28A-28F | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | g38-39 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g63-68 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g78-79 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB119-B119 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB44-B48 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 17 | gB61-B71 | 🖼️ peripheral | 0.56-0.62 | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.57 | D:0 |

### Q3.5 / 1

- Question: À quoi correspond un actif dont les flux de trésorerie contractuels ne comprennent que le principal et les intérêts ?
- Embedded question: À quoi correspond un actif dont les flux de trésorerie contractuels ne comprennent que le principal et les intérêts ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.68 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 7 | g10-17 | 🗑️ dropped | 0.62 | D:0 |
| IAS 7 | g13-15 | 🗑️ dropped | 0.62 | D:0 |
| IAS 7 | g16-16 | 🗑️ dropped | 0.64 | D:0 |
| IAS 7 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 7 | g31-34 | 🗑️ dropped | 0.59 | D:0 |
| IAS 7 | g37-38 | 🗑️ dropped | 0.59 | D:0 |
| IAS 7 | g39-42B | 🗑️ dropped | 0.61 | D:0 |
| IAS 7 | g43-44 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 7 | g6-9 | 🗑️ dropped | 0.62 | D:0 |
| IAS 7 | g7-9 | 🗑️ dropped | 0.70 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g103-108F | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | g74-77 | 🗑️ dropped | — | D:0 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.54 | D:0 |
| IAS 39 | g85-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:0 |
| IAS 39 | g95-101 | 🗑️ dropped | 0.53-0.60 | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.54 | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.55 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.58 | D:0 |
| IFRS 17 | g1-2 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g10-13 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g28A-28F | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g38-39 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g63-68 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g78-79 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB119-B119 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB44-B48 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | 0.56-0.62 | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.57 | D:0 |

### Q3.6 / 0

- Question: Quelle définition donner à un actif financier respectant le critère des paiements uniquement constitués de principal et d’intérêts ?
- Embedded question: Quelle définition donner à un actif financier respectant le critère des paiements uniquement constitués de principal et d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.1.1-3.1.2 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g3.1.2-3.1.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.63-0.69 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.1-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.3.3-4.3.7 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.2.1-5.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.1-B3.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.2A-B3.1.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.3-B3.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.65 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65-0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 32 | g1-3 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.68 | D:0 |
| IAS 32 | g15-27 | 🔎 secondary | 0.64 | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🔎 secondary | 0.62 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.63-0.65 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🖼️ peripheral | 0.57-0.58 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g131-132 | 🗑️ dropped | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🖼️ peripheral | 0.56-0.58 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g55-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g56-60 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.56-0.61 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 3 | g18-20 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | g24-25 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g27-28 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g29-29 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | g30-30 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g31-31 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g31A-31A | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g8-9 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB1-B4 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.54-0.54 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB43-B43 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB5-B6 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7-B12 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.57 | D:0 |

### Q3.6 / 1

- Question: Quelle définition donner à un actif financier respectant le critère des paiements uniquement constitués de principal et d’intérêts ?
- Embedded question: Quelle définition donner à un actif financier respectant le critère des paiements uniquement constitués de principal et d’intérêts ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.1.1-3.1.2 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g3.1.2-3.1.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.63-0.69 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | g4.2.1-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.3.3-4.3.7 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.2.1-5.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.1-B3.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.2A-B3.1.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.1.3-B3.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.65-0.65 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🔎 secondary | 0.63 | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65-0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 32 | g1-3 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.65 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.66 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.63-0.65 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🖼️ peripheral | 0.57-0.58 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g131-132 | 🗑️ dropped | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🖼️ peripheral | 0.56-0.58 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g55-152 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g56-60 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🖼️ peripheral | 0.56-0.61 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 3 | g18-20 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g24-25 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g26-26 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g27-28 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g29-29 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g3-3 | 🖼️ peripheral | 0.53 | D:0 |
| IFRS 3 | g30-30 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g31-31 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g31A-31A | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g8-9 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB1-B4 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.54-0.54 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB43-B43 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB5-B6 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7-B12 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | gB8-B11 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🖼️ peripheral | 0.57 | D:0 |

### Q3.7 / 0

- Question: En IFRS, comment qualifie-t-on un actif dont les termes contractuels donnent droit seulement à des flux de principal et d’intérêts ?
- Embedded question: En IFRS, comment qualifie-t-on un actif dont les termes contractuels donnent droit seulement à des flux de principal et d’intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.61-0.65 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.61-0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.62-0.64 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |

### Q3.7 / 1

- Question: En IFRS, comment qualifie-t-on un actif dont les termes contractuels donnent droit seulement à des flux de principal et d’intérêts ?
- Embedded question: En IFRS, comment qualifie-t-on un actif dont les termes contractuels donnent droit seulement à des flux de principal et d’intérêts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.61-0.65 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.61-0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.62-0.64 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |

### Q3.8 / 0

- Question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
- Embedded question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🖼️ peripheral | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64-0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🖼️ peripheral | 0.64-0.67 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.69 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.66-0.66 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🗑️ dropped | 0.58-0.60 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g131-132 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🖼️ peripheral | 0.56-0.57 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g155-157 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g55-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g56-60 | 🗑️ dropped | — | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g54-58 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB13-B18 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB63-B63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.57 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g12-13 | 🗑️ dropped | 0.53 | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.55-0.63 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

### Q3.8 / 1

- Question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
- Embedded question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64-0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🔎 secondary | 0.64-0.67 | D:0 |
| IAS 32 | gAG20-AG24 | 🔎 secondary | 0.69 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.66-0.66 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🖼️ peripheral | 0.58-0.60 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g131-132 | 🗑️ dropped | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🖼️ peripheral | 0.56-0.57 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g155-157 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g55-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g56-60 | 🗑️ dropped | — | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g54-58 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB13-B18 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB63-B63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.57 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g12-13 | 🗑️ dropped | 0.53 | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.55-0.63 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

### Q3.9 / 0

- Question: Un actif financier peut être caractérisé par des flux de trésorerie limités au principal et aux intérêts.
Comment définit-on précisément ce type d’actif dont les termes contractuels ne prévoient que ces paiements ?
- Embedded question: Un actif financier peut être caractérisé par des flux de trésorerie limités au principal et aux intérêts.
Comment définit-on précisément ce type d’actif dont les termes contractuels ne prévoient que ces paiements ?
cash flow
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.68-0.72 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.69 | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🔎 secondary | 0.69 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.69-0.69 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 7 | g13-15 | 🖼️ peripheral | 0.66 | D:0 |
| IAS 7 | g16-16 | 🖼️ peripheral | 0.70 | D:0 |
| IAS 7 | g22-24 | 🖼️ peripheral | 0.66-0.67 | D:0 |
| IAS 7 | g31-34 | 🖼️ peripheral | 0.66 | D:0 |
| IAS 7 | g35-36 | 🗑️ dropped | 0.67 | D:0 |
| IAS 7 | g39-42B | 🖼️ peripheral | 0.67 | D:0 |
| IAS 7 | g43-44 | 🖼️ peripheral | 0.68-0.68 | D:0 |
| IAS 7 | g7-9 | 🖼️ peripheral | 0.71 | D:0 |
| IAS 36 | g100-103 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 36 | g33-38 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.63-0.67 | D:0 |
| IAS 36 | g66-73 | 🖼️ peripheral | 0.67 | D:0 |
| IAS 36 | gA1-A2 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 19 | g165-165 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 19 | g167-168 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g169-170 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g171-171 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g206-210 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IFRS 19 | g250-256 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 19 | g254-256 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g42-73 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 19 | g44-44 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 19 | g45-46 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g47-48 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g49-50 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g51-51 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g52-52 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g53-53 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g54-55 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g56-56 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g58-63 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g64-64 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g64A-64C | 🗑️ dropped | — | D:0 |
| IFRS 19 | g65-67 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g68-71 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g72-72 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g73-73 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.57 | D:0 |

### Q3.9 / 1

- Question: Un actif financier peut être caractérisé par des flux de trésorerie limités au principal et aux intérêts.
Comment définit-on précisément ce type d’actif dont les termes contractuels ne prévoient que ces paiements ?
- Embedded question: Un actif financier peut être caractérisé par des flux de trésorerie limités au principal et aux intérêts.
Comment définit-on précisément ce type d’actif dont les termes contractuels ne prévoient que ces paiements ?
cash flow
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🔎 secondary | 0.68-0.72 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.69 | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🔎 secondary | 0.69 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🔎 secondary | 0.69-0.69 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 7 | g13-15 | 🖼️ peripheral | 0.66 | D:0 |
| IAS 7 | g16-16 | 🖼️ peripheral | 0.70 | D:0 |
| IAS 7 | g22-24 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IAS 7 | g31-34 | 🗑️ dropped | 0.66 | D:0 |
| IAS 7 | g35-36 | 🗑️ dropped | 0.67 | D:0 |
| IAS 7 | g39-42B | 🗑️ dropped | 0.67 | D:0 |
| IAS 7 | g43-44 | 🗑️ dropped | 0.68-0.68 | D:0 |
| IAS 7 | g7-9 | 🖼️ peripheral | 0.71 | D:0 |
| IAS 36 | g100-103 | 🗑️ dropped | 0.64 | D:0 |
| IAS 36 | g33-38 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.63-0.67 | D:0 |
| IAS 36 | g66-73 | 🖼️ peripheral | 0.67 | D:0 |
| IAS 36 | gA1-A2 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 19 | g165-165 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 19 | g167-168 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g169-170 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g171-171 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g206-210 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IFRS 19 | g250-256 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 19 | g254-256 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g42-73 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 19 | g44-44 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 19 | g45-46 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g47-48 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g49-50 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g51-51 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g52-52 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g53-53 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g54-55 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g56-56 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g58-63 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g64-64 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g64A-64C | 🗑️ dropped | — | D:0 |
| IFRS 19 | g65-67 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g68-71 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g72-72 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g73-73 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.57 | D:0 |

### Q3.10 / 0

- Question: Certains actifs ne génèrent contractuellement que des paiements de principal et d’intérêts.
Quelle est la définition exacte d’un tel actif dans ce contexte ?
- Embedded question: Certains actifs ne génèrent contractuellement que des paiements de principal et d’intérêts.
Quelle est la définition exacte d’un tel actif dans ce contexte ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB3.2.10-B3.2.11 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.60-0.65 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.63 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |

### Q3.10 / 1

- Question: Certains actifs ne génèrent contractuellement que des paiements de principal et d’intérêts.
Quelle est la définition exacte d’un tel actif dans ce contexte ?
- Embedded question: Certains actifs ne génèrent contractuellement que des paiements de principal et d’intérêts.
Quelle est la définition exacte d’un tel actif dans ce contexte ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB3.2.10-B3.2.11 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.60-0.65 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | 0.61 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.63 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🎯 authoritative | — | D:0 |

