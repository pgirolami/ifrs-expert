# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `56_get_answer-eval_to_work_for_Q12.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-02_12-10-17_promptfoo-eval-family-q12`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| contingent_liability | yes | 0/2 | 0 |
| provision | yes | 0/2 | 0 |
| right_of_use_model | no | 2/2 | 1 |
| short_term_lease_exemption | no | 2/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q12.0 | 2 | 100.0 | 100.0 | 4 | 4 |

## Authority Categorization by Run

### Q12.0 / 0

- Question: Un contrat (sans option d'achat) d'une durée inférieure ou égale à un an renouvelable par tacite reconduction ou à durée indéterminée peut-il être qualifié de contrat de courte durée pour lequel le preneur peut bénéficier de l'exemption optionnelle de reconnaissance du droit d'utilisation et de la dette de loyers ?
- Embedded question: Un contrat (sans option d'achat) d'une durée inférieure ou égale à un an renouvelable par tacite reconduction ou à durée indéterminée peut-il être qualifié de contrat de courte durée pour lequel le preneur peut bénéficier de l'exemption optionnelle de reconnaissance du droit d'utilisation et de la dette de loyers ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 16 | g22-22 | 🔎 secondary | — | D:0 |
| IFRS 16 | g23-25 | 🔎 secondary | — | D:0 |
| IFRS 16 | g26-28 | 🔎 secondary | — | D:0 |
| IFRS 16 | g29-35 | 🔎 secondary | — | D:0 |
| IFRS 16 | g30-33 | 🔎 secondary | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🔎 secondary | — | D:0 |
| IFRS 16 | g39-43 | 🔎 secondary | — | D:0 |
| IFRS 16 | g44-46 | 🔎 secondary | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.59-0.63 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g22-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g24-25 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g26-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g35-37 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g84-86 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | g9-16 | 🖼️ peripheral | 0.55-0.60 | D:0 |
| IFRS 15 | g91-94 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 15 | gB39-B43 | 🗑️ dropped | 0.55-0.58 | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB70-B76 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 15 | gB9-B13 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 38 | g100-103 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g118-123 | 🖼️ peripheral | 0.53 | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🖼️ peripheral | 0.53-0.62 | D:0 |

### Q12.0 / 1

- Question: Un contrat (sans option d'achat) d'une durée inférieure ou égale à un an renouvelable par tacite reconduction ou à durée indéterminée peut-il être qualifié de contrat de courte durée pour lequel le preneur peut bénéficier de l'exemption optionnelle de reconnaissance du droit d'utilisation et de la dette de loyers ?
- Embedded question: Un contrat (sans option d'achat) d'une durée inférieure ou égale à un an renouvelable par tacite reconduction ou à durée indéterminée peut-il être qualifié de contrat de courte durée pour lequel le preneur peut bénéficier de l'exemption optionnelle de reconnaissance du droit d'utilisation et de la dette de loyers ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 16 | g22-22 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g23-25 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g26-28 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g29-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g30-33 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.59-0.63 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g22-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g24-25 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g26-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g35-37 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g84-86 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | g9-16 | 🖼️ peripheral | 0.55-0.60 | D:0 |
| IFRS 15 | g91-94 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 15 | gB39-B43 | 🗑️ dropped | 0.55-0.58 | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB70-B76 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 15 | gB9-B13 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 38 | g100-103 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g118-123 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🖼️ peripheral | 0.53-0.62 | D:0 |

