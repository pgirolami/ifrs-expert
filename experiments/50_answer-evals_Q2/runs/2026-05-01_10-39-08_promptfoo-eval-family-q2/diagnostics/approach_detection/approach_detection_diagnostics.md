# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `50_answer-evals_Q2`
- Run: `2026-05-01_10-39-08_promptfoo-eval-family-q2`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 10

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| amortised_cost | no | 10/10 | 5 |
| fair_value_oci | no | 5/10 | 4 |
| fair_value_profit | no | 1/10 | 1 |
| fair_value_profit_loss | no | 4/10 | 3 |
| fair_value_through_oci | no | 1/10 | 1 |
| fair_value_through_profit_or_loss | no | 1/10 | 1 |
| fvoci | no | 2/10 | 2 |
| fvoci_debt | no | 2/10 | 2 |
| fvtpl | no | 4/10 | 3 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q2.0 | 2 | 72.0 | 72.0 | 0 | 6 |
| Q2.1 | 2 | 72.0 | 72.0 | 0 | 6 |
| Q2.2 | 2 | 100.0 | 100.0 | 0 | 6 |
| Q2.3 | 2 | 72.0 | 72.0 | 0 | 6 |
| Q2.4 | 2 | 82.5 | 82.5 | 0 | 6 |

## Authority Categorization by Run

### Q2.0 / 0

- Question: Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?
- Embedded question: Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.65-0.70 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.67-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.68 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.4.1-B5.4.7 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:1 |
| IAS 39 | g102D-102D | 🗑️ dropped | 0.58 | D:1 |
| IAS 39 | g102E-102E | 🗑️ dropped | 0.58 | D:1 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.62 | D:6 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.59 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | — | D:8 |
| IAS 39 | g81-81A | 🗑️ dropped | — | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.58 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:1 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:1 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.59 | D:3 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.58-0.58 | D:13 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:19 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.62 | D:2 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.59 | D:5 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:2 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB49-B53 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB54-B60 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IFRS 17 | gB72-B85 | 🖼️ peripheral | 0.61-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 2 | g15-18 | 🖼️ peripheral | 0.53-0.61 | D:0 |
| IAS 2 | g6-8 | 🖼️ peripheral | 0.53 | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g102D-102D / 102D / dropped
- IAS 39 / g102E-102E / 102E / dropped
- IAS 39 / g102P-102U / 102P / dropped
- IAS 39 / g102P-102U / 102Q / dropped
- IAS 39 / g102P-102U / 102R / dropped
- IAS 39 / g102P-102U / 102S / dropped
- IAS 39 / g102P-102U / 102T / dropped
- IAS 39 / g102P-102U / 102U / dropped
- IAS 39 / g102W-102X / 102W / dropped
- IAS 39 / g102W-102X / 102X / dropped
- IAS 39 / g74-77 / 74 / dropped
- IAS 39 / g74-77 / 75 / dropped
- IAS 39 / g74-77 / 76 / dropped
- IAS 39 / g74-77 / 77 / dropped
- IAS 39 / g74-77 / E1 / dropped
- IAS 39 / g74-77 / E2 / dropped
- IAS 39 / g74-77 / E3 / dropped
- IAS 39 / g74-77 / E4 / dropped
- IAS 39 / g81-81A / 81 / dropped
- IAS 39 / g81-81A / 81A / dropped
- IAS 39 / g85-102 / 85 / dropped
- IAS 39 / g85-102 / 86 / dropped
- IAS 39 / g85-102 / 87 / dropped
- IAS 39 / g85-102 / 88 / dropped
- IAS 39 / g85-102 / E6 / dropped
- IAS 39 / g85-102 / E7 / dropped
- IAS 39 / g85-102 / E8 / dropped
- IAS 39 / g85-102 / E9 / dropped
- IAS 39 / g89-94 / 89 / dropped
- IAS 39 / g89-94 / 89A / dropped
- IAS 39 / g89-94 / 90 / dropped
- IAS 39 / g89-94 / 91 / dropped
- IAS 39 / g89-94 / 92 / dropped
- IAS 39 / g89-94 / 93 / dropped
- IAS 39 / g89-94 / 94 / dropped
- IAS 39 / g95-101 / 95 / dropped
- IAS 39 / g95-101 / 96 / dropped
- IAS 39 / g95-101 / 97 / dropped
- IAS 39 / g95-101 / 98 / dropped
- IAS 39 / g95-101 / 99 / dropped
- IAS 39 / g95-101 / 100 / dropped
- IAS 39 / g95-101 / 101 / dropped
- IAS 39 / gAG100-AG100 / AG100 / dropped
- IAS 39 / gAG101-AG101 / AG101 / dropped
- IAS 39 / gAG102-AG132 / AG102 / dropped
- IAS 39 / gAG102-AG132 / AG103 / dropped
- IAS 39 / gAG102-AG132 / AG104 / dropped
- IAS 39 / gAG105-AG113A / AG105 / dropped
- IAS 39 / gAG105-AG113A / AG106 / dropped
- IAS 39 / gAG105-AG113A / AG107 / dropped
- IAS 39 / gAG105-AG113A / AG107A / dropped
- IAS 39 / gAG105-AG113A / AG108 / dropped
- IAS 39 / gAG105-AG113A / AG109 / dropped
- IAS 39 / gAG105-AG113A / AG110 / dropped
- IAS 39 / gAG105-AG113A / AG110A / dropped
- IAS 39 / gAG105-AG113A / AG110B / dropped
- IAS 39 / gAG105-AG113A / AG111 / dropped
- IAS 39 / gAG105-AG113A / AG112 / dropped
- IAS 39 / gAG105-AG113A / AG113 / dropped
- IAS 39 / gAG105-AG113A / AG113A / dropped
- IAS 39 / gAG114-AG132 / AG114 / dropped
- IAS 39 / gAG114-AG132 / AG115 / dropped
- IAS 39 / gAG114-AG132 / AG116 / dropped
- IAS 39 / gAG114-AG132 / AG117 / dropped
- IAS 39 / gAG114-AG132 / AG118 / dropped
- IAS 39 / gAG114-AG132 / AG119 / dropped
- IAS 39 / gAG114-AG132 / AG120 / dropped
- IAS 39 / gAG114-AG132 / AG121 / dropped
- IAS 39 / gAG114-AG132 / AG122 / dropped
- IAS 39 / gAG114-AG132 / AG123 / dropped
- IAS 39 / gAG114-AG132 / AG124 / dropped
- IAS 39 / gAG114-AG132 / AG125 / dropped
- IAS 39 / gAG114-AG132 / AG126 / dropped
- IAS 39 / gAG114-AG132 / AG127 / dropped
- IAS 39 / gAG114-AG132 / AG128 / dropped
- IAS 39 / gAG114-AG132 / AG129 / dropped
- IAS 39 / gAG114-AG132 / AG130 / dropped
- IAS 39 / gAG114-AG132 / AG131 / dropped
- IAS 39 / gAG114-AG132 / AG132 / dropped
- IAS 39 / gAG98-AG101 / AG99E / dropped
- IAS 39 / gAG98-AG101 / AG99F / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped
- IAS 39 / gAG99C-AG99D / AG99C / dropped
- IAS 39 / gAG99C-AG99D / AG99D / dropped

### Q2.0 / 1

- Question: Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?
- Embedded question: Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.65-0.70 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.67-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.68 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.4.1-B5.4.7 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g102E-102E | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.58-0.58 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB49-B53 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB54-B60 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.62-0.63 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.61-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 2 | g15-18 | 🖼️ peripheral | 0.53-0.61 | D:0 |
| IAS 2 | g6-8 | 🖼️ peripheral | 0.53 | D:0 |

### Q2.1 / 0

- Question: Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?
- Embedded question: Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.64-0.68 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.65-0.67 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.4.1-B5.4.7 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g102P-102U | 🖼️ peripheral | 0.60 | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.56-0.56 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.57-0.61 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 19 | g165-165 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g166-166 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 19 | g167-168 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 19 | g243-245 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g42-73 | 🔎 secondary | 0.62 | D:0 |
| IFRS 19 | g44-44 | 🖼️ peripheral | — | D:0 |
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
| IFRS 19 | g65-67 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g68-71 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g72-72 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g73-73 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g84-87 | 🗑️ dropped | 0.54 | D:0 |

### Q2.1 / 1

- Question: Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?
- Embedded question: Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.64-0.68 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.65-0.67 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.4.1-B5.4.7 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g102P-102U | 🖼️ peripheral | 0.60 | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g74-77 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.56-0.56 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.57-0.61 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 19 | g165-165 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g166-166 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 19 | g167-168 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 19 | g243-245 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g42-73 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 19 | g44-44 | 🖼️ peripheral | — | D:0 |
| IFRS 19 | g45-46 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g47-48 | 🗑️ dropped | — | D:0 |
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
| IFRS 19 | g65-67 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g68-71 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g72-72 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g73-73 | 🗑️ dropped | — | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g84-87 | 🗑️ dropped | 0.54 | D:0 |

### Q2.2 / 0

- Question: Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?
- Embedded question: Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.66-0.68 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.67 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102E-102E | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102F-102G | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.61 | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.56-0.60 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.56 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g53-59 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.59-0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.61-0.61 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.64 | D:0 |
| IAS 33 | g12-18 | 🗑️ dropped | — | D:0 |
| IAS 33 | g19-29 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IAS 33 | g33-35 | 🗑️ dropped | — | D:0 |
| IAS 33 | g45-48 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 33 | g49-51 | 🖼️ peripheral | — | D:0 |
| IAS 33 | g5-8 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 33 | g52-57 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IAS 33 | g58-61 | 🗑️ dropped | 0.54-0.56 | D:0 |
| IAS 33 | g70-73A | 🗑️ dropped | 0.61 | D:0 |
| IAS 33 | gA6-A9 | 🗑️ dropped | 0.56 | D:0 |

### Q2.2 / 1

- Question: Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?
- Embedded question: Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.66-0.68 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.65-0.69 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.67-0.67 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102E-102E | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102F-102G | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.61 | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.56-0.60 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.56 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g53-59 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.59-0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.61-0.61 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.64 | D:0 |
| IAS 33 | g12-18 | 🗑️ dropped | — | D:0 |
| IAS 33 | g19-29 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IAS 33 | g33-35 | 🖼️ peripheral | — | D:0 |
| IAS 33 | g45-48 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 33 | g49-51 | 🗑️ dropped | — | D:0 |
| IAS 33 | g5-8 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 33 | g52-57 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IAS 33 | g58-61 | 🗑️ dropped | 0.54-0.56 | D:0 |
| IAS 33 | g70-73A | 🗑️ dropped | 0.61 | D:0 |
| IAS 33 | gA6-A9 | 🗑️ dropped | 0.56 | D:0 |

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
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
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
| IAS 32 | g11-14 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 32 | g15-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | — | D:0 |
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
| IFRS 9 | gB4.1.20-B4.1.26 | 🔎 secondary | 0.69-0.70 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
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
| IAS 32 | g11-14 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 32 | g15-27 | 🖼️ peripheral | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | — | D:0 |
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

### Q2.4 / 0

- Question: Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?
- Embedded question: Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🔎 secondary | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.66-0.69 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.66-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.68-0.70 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | g72-73 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 39 | g74-77 | 🗑️ dropped | — | D:0 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.58-0.63 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.57 | D:0 |
| IAS 39 | sgAG94-AG97 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB61-B71 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.60-0.62 | D:0 |
| IFRS 17 | gB72-B85 | 🗑️ dropped | 0.61-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🗑️ dropped | 0.64 | D:0 |
| IAS 33 | g12-18 | 🗑️ dropped | — | D:0 |
| IAS 33 | g19-29 | 🗑️ dropped | 0.55 | D:0 |
| IAS 33 | g33-35 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 33 | g45-48 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 33 | g49-51 | 🖼️ peripheral | — | D:0 |
| IAS 33 | g5-8 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 33 | g52-57 | 🗑️ dropped | 0.54-0.54 | D:0 |
| IAS 33 | g58-61 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IAS 33 | g70-73A | 🗑️ dropped | 0.63 | D:0 |
| IAS 33 | gA13-A14 | 🗑️ dropped | — | D:0 |
| IAS 33 | gA6-A9 | 🗑️ dropped | 0.57 | D:0 |

### Q2.4 / 1

- Question: Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?
- Embedded question: Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?
cash flow

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.4.5-5.4.9 | 🗑️ dropped | 0.66-0.69 | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.66-0.71 | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | 0.68-0.70 | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🔎 secondary | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:1 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.62 | D:6 |
| IAS 39 | g72-73 | 🗑️ dropped | 0.57 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | — | D:8 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.57 | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.58 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:1 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:1 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.58 | D:3 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.57 | D:13 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:19 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.58-0.63 | D:2 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.59 | D:5 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | 0.57 | D:2 |
| IAS 39 | sgAG94-AG97 | 🗑️ dropped | — | D:3 |
| IFRS 17 | g33-35 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 17 | g36-36 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 17 | g43-46 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB101-B118 | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 17 | gB115-B118 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | gB61-B71 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | 0.60-0.62 | D:0 |
| IFRS 17 | gB72-B85 | 🖼️ peripheral | 0.61-0.63 | D:0 |
| IFRS 17 | gB96-B100 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 33 | g12-18 | 🗑️ dropped | — | D:0 |
| IAS 33 | g19-29 | 🗑️ dropped | 0.55 | D:0 |
| IAS 33 | g33-35 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 33 | g45-48 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 33 | g49-51 | 🖼️ peripheral | — | D:0 |
| IAS 33 | g5-8 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 33 | g52-57 | 🖼️ peripheral | 0.54-0.54 | D:0 |
| IAS 33 | g58-61 | 🖼️ peripheral | 0.56-0.58 | D:0 |
| IAS 33 | g70-73A | 🖼️ peripheral | 0.63 | D:0 |
| IAS 33 | gA13-A14 | 🗑️ dropped | — | D:0 |
| IAS 33 | gA6-A9 | 🗑️ dropped | 0.57 | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g102P-102U / 102P / dropped
- IAS 39 / g102P-102U / 102Q / dropped
- IAS 39 / g102P-102U / 102R / dropped
- IAS 39 / g102P-102U / 102S / dropped
- IAS 39 / g102P-102U / 102T / dropped
- IAS 39 / g102P-102U / 102U / dropped
- IAS 39 / g72-73 / 72 / dropped
- IAS 39 / g72-73 / 73 / dropped
- IAS 39 / g74-77 / 74 / dropped
- IAS 39 / g74-77 / 75 / dropped
- IAS 39 / g74-77 / 76 / dropped
- IAS 39 / g74-77 / 77 / dropped
- IAS 39 / g74-77 / E1 / dropped
- IAS 39 / g74-77 / E2 / dropped
- IAS 39 / g74-77 / E3 / dropped
- IAS 39 / g74-77 / E4 / dropped
- IAS 39 / g81-81A / 81 / dropped
- IAS 39 / g81-81A / 81A / dropped
- IAS 39 / g85-102 / 85 / dropped
- IAS 39 / g85-102 / 86 / dropped
- IAS 39 / g85-102 / 87 / dropped
- IAS 39 / g85-102 / 88 / dropped
- IAS 39 / g85-102 / E6 / dropped
- IAS 39 / g85-102 / E7 / dropped
- IAS 39 / g85-102 / E8 / dropped
- IAS 39 / g85-102 / E9 / dropped
- IAS 39 / g89-94 / 89 / dropped
- IAS 39 / g89-94 / 89A / dropped
- IAS 39 / g89-94 / 90 / dropped
- IAS 39 / g89-94 / 91 / dropped
- IAS 39 / g89-94 / 92 / dropped
- IAS 39 / g89-94 / 93 / dropped
- IAS 39 / g89-94 / 94 / dropped
- IAS 39 / g95-101 / 95 / dropped
- IAS 39 / g95-101 / 96 / dropped
- IAS 39 / g95-101 / 97 / dropped
- IAS 39 / g95-101 / 98 / dropped
- IAS 39 / g95-101 / 99 / dropped
- IAS 39 / g95-101 / 100 / dropped
- IAS 39 / g95-101 / 101 / dropped
- IAS 39 / gAG100-AG100 / AG100 / dropped
- IAS 39 / gAG101-AG101 / AG101 / dropped
- IAS 39 / gAG102-AG132 / AG102 / dropped
- IAS 39 / gAG102-AG132 / AG103 / dropped
- IAS 39 / gAG102-AG132 / AG104 / dropped
- IAS 39 / gAG105-AG113A / AG105 / dropped
- IAS 39 / gAG105-AG113A / AG106 / dropped
- IAS 39 / gAG105-AG113A / AG107 / dropped
- IAS 39 / gAG105-AG113A / AG107A / dropped
- IAS 39 / gAG105-AG113A / AG108 / dropped
- IAS 39 / gAG105-AG113A / AG109 / dropped
- IAS 39 / gAG105-AG113A / AG110 / dropped
- IAS 39 / gAG105-AG113A / AG110A / dropped
- IAS 39 / gAG105-AG113A / AG110B / dropped
- IAS 39 / gAG105-AG113A / AG111 / dropped
- IAS 39 / gAG105-AG113A / AG112 / dropped
- IAS 39 / gAG105-AG113A / AG113 / dropped
- IAS 39 / gAG105-AG113A / AG113A / dropped
- IAS 39 / gAG114-AG132 / AG114 / dropped
- IAS 39 / gAG114-AG132 / AG115 / dropped
- IAS 39 / gAG114-AG132 / AG116 / dropped
- IAS 39 / gAG114-AG132 / AG117 / dropped
- IAS 39 / gAG114-AG132 / AG118 / dropped
- IAS 39 / gAG114-AG132 / AG119 / dropped
- IAS 39 / gAG114-AG132 / AG120 / dropped
- IAS 39 / gAG114-AG132 / AG121 / dropped
- IAS 39 / gAG114-AG132 / AG122 / dropped
- IAS 39 / gAG114-AG132 / AG123 / dropped
- IAS 39 / gAG114-AG132 / AG124 / dropped
- IAS 39 / gAG114-AG132 / AG125 / dropped
- IAS 39 / gAG114-AG132 / AG126 / dropped
- IAS 39 / gAG114-AG132 / AG127 / dropped
- IAS 39 / gAG114-AG132 / AG128 / dropped
- IAS 39 / gAG114-AG132 / AG129 / dropped
- IAS 39 / gAG114-AG132 / AG130 / dropped
- IAS 39 / gAG114-AG132 / AG131 / dropped
- IAS 39 / gAG114-AG132 / AG132 / dropped
- IAS 39 / gAG98-AG101 / AG99E / dropped
- IAS 39 / gAG98-AG101 / AG99F / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped
- IAS 39 / gAG99C-AG99D / AG99C / dropped
- IAS 39 / gAG99C-AG99D / AG99D / dropped
- IAS 39 / sgAG94-AG97 / AG94 / dropped
- IAS 39 / sgAG94-AG97 / AG95 / dropped
- IAS 39 / sgAG94-AG97 / AG97 / dropped

