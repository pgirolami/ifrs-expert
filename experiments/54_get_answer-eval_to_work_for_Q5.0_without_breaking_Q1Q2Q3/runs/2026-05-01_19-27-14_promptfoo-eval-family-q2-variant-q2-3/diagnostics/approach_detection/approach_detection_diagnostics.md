# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `54_get_answer-eval_to_work_for_Q5.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-01_19-27-14_promptfoo-eval-family-q2-variant-q2-3`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| amortised_cost | yes | 2/2 | 1 |
| fair_value_through_other_comprehensive_income | yes | 2/2 | 1 |
| fair_value_through_profit_or_loss | yes | 2/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q2.3 | 2 | 100.0 | 100.0 | 0 | 0 |

## Authority Categorization by Run

### Q2.3 / 0

- Question: Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?
- Embedded question: Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.67-0.70 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.66-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.69-0.70 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 32 | g11-14 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 32 | g15-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g21-24 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.62-0.65 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG28-AG28 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.61 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.61-0.64 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.59 | D:0 |
| IFRS 17 | g10-13 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | g33-35 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 17 | g36-36 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB49-B53 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB54-B60 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.62-0.64 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.66 | D:0 |

### Q2.3 / 1

- Question: Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?
- Embedded question: Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.67-0.70 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.66-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.69-0.70 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 32 | g15-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g21-24 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g25-25 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g26-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | 0.63 | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG15-AG19 | 🗑️ dropped | 0.62-0.65 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG28-AG28 | 🗑️ dropped | 0.62 | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | g102-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.61 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.61-0.64 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.59 | D:0 |
| IFRS 17 | g10-13 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | g33-35 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 17 | g36-36 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB49-B53 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB54-B60 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.62-0.64 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.66 | D:0 |

