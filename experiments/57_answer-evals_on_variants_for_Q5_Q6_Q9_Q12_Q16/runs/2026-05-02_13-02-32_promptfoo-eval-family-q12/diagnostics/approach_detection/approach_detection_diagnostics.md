# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16`
- Run: `2026-05-02_13-02-32_promptfoo-eval-family-q12`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 10

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| expense_recognition_for_short_term_leases | no | 1/10 | 1 |
| general_lessee_accounting | no | 1/10 | 1 |
| general_lessee_lease_accounting | no | 1/10 | 1 |
| general_lessee_lease_model | no | 1/10 | 1 |
| recognition_of_a_right_of_use_asset_and_lease_liability | no | 1/10 | 1 |
| right_of_use_asset_and_lease_liability | no | 4/10 | 3 |
| right_of_use_model | yes | 2/10 | 1 |
| short_term_lease_exemption | yes | 9/10 | 5 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q12.0 | 2 | 35.0 | 35.0 | 3 | 3 |
| Q12.1 | 2 | 100.0 | 100.0 | 2 | 2 |
| Q12.2 | 2 | 100.0 | 100.0 | 0 | 0 |
| Q12.3 | 2 | 76.7 | 76.7 | 2 | 2 |
| Q12.4 | 2 | 56.7 | 56.7 | 2 | 2 |

## Authority Categorization by Run

### Q12.0 / 0

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
| IFRS 16 | g36-43 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.61-0.61 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.59-0.63 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IAS 38 | g100-103 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g118-123 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🖼️ peripheral | 0.53-0.62 | D:0 |
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

### Q12.0 / 1

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
| IAS 38 | g100-103 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g118-123 | 🗑️ dropped | 0.53 | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🖼️ peripheral | 0.53-0.62 | D:0 |
| IFRS 15 | g22-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g24-25 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g26-30 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g35-37 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g84-86 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | g9-16 | 🖼️ peripheral | 0.55-0.60 | D:0 |
| IFRS 15 | g91-94 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 15 | gB39-B43 | 🗑️ dropped | 0.55-0.58 | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB70-B76 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 15 | gB9-B13 | 🗑️ dropped | 0.56 | D:0 |

### Q12.1 / 0

- Question: Un contrat de location sans option d’achat, conclu pour une durée d’un an ou moins mais renouvelable tacitement ou à durée indéterminée, peut-il entrer dans l’exemption IFRS 16 applicable aux contrats de courte durée ?
- Embedded question: Un contrat de location sans option d’achat, conclu pour une durée d’un an ou moins mais renouvelable tacitement ou à durée indéterminée, peut-il entrer dans l’exemption IFRS 16 applicable aux contrats de courte durée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g100-102 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 16 | g22-22 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g23-25 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g26-28 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g29-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g3-4 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 16 | g30-33 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.59-0.59 | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 16 | gB20-B20 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.57-0.64 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.65 | D:0 |
| IFRS 3 | g18-20 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g28A-28B_V2 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IAS 16 | g16-22A | 🖼️ peripheral | 0.53 | D:0 |
| IAS 16 | g29-66 | 🗑️ dropped | 0.53 | D:0 |
| IAS 16 | g30-30 | 🗑️ dropped | — | D:0 |
| IAS 16 | g31-42 | 🗑️ dropped | — | D:0 |
| IAS 16 | g43-62A | 🗑️ dropped | — | D:0 |
| IAS 16 | g50-59 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 16 | g60-62A | 🗑️ dropped | — | D:0 |
| IAS 16 | g63-64 | 🗑️ dropped | — | D:0 |
| IAS 16 | g65-66 | 🗑️ dropped | — | D:0 |
| IAS 37 | g1-9 | 🖼️ peripheral | 0.63 | D:0 |

### Q12.1 / 1

- Question: Un contrat de location sans option d’achat, conclu pour une durée d’un an ou moins mais renouvelable tacitement ou à durée indéterminée, peut-il entrer dans l’exemption IFRS 16 applicable aux contrats de courte durée ?
- Embedded question: Un contrat de location sans option d’achat, conclu pour une durée d’un an ou moins mais renouvelable tacitement ou à durée indéterminée, peut-il entrer dans l’exemption IFRS 16 applicable aux contrats de courte durée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g100-102 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 16 | g22-22 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g23-25 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g26-28 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g29-35 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g3-4 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 16 | g30-33 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.59-0.59 | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 16 | gB20-B20 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.57-0.64 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 3 | g18-20 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g28A-28B_V2 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IAS 16 | g16-22A | 🗑️ dropped | 0.53 | D:0 |
| IAS 16 | g29-66 | 🗑️ dropped | 0.53 | D:0 |
| IAS 16 | g30-30 | 🗑️ dropped | — | D:0 |
| IAS 16 | g31-42 | 🗑️ dropped | — | D:0 |
| IAS 16 | g43-62A | 🗑️ dropped | — | D:0 |
| IAS 16 | g50-59 | 🗑️ dropped | 0.63 | D:0 |
| IAS 16 | g60-62A | 🗑️ dropped | — | D:0 |
| IAS 16 | g63-64 | 🗑️ dropped | — | D:0 |
| IAS 16 | g65-66 | 🗑️ dropped | — | D:0 |
| IAS 37 | g1-9 | 🖼️ peripheral | 0.63 | D:0 |

### Q12.2 / 0

- Question: Le preneur dispose d’un contrat sans option d’achat dont la période initiale n’excède pas douze mois, avec tacite reconduction ou durée indéterminée. Peut-il ne pas reconnaître le droit d’utilisation et la dette de loyers au titre de l’exemption pour contrats courts ?
- Embedded question: Le preneur dispose d’un contrat sans option d’achat dont la période initiale n’excède pas douze mois, avec tacite reconduction ou durée indéterminée. Peut-il ne pas reconnaître le droit d’utilisation et la dette de loyers au titre de l’exemption pour contrats courts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.61-0.62 | D:0 |
| IFRS 16 | g22-22 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g23-25 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g26-28 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g29-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g30-33 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.60-0.62 | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.61-0.63 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IAS 12 | 0011 | 🗑️ dropped | — | D:0 |
| IAS 12 | g1-4 | 🗑️ dropped | — | D:0 |
| IAS 12 | g12-14 | 🗑️ dropped | — | D:0 |
| IAS 12 | g15-23 | 🗑️ dropped | 0.54-0.54 | D:0 |
| IAS 12 | g19-19 | 🗑️ dropped | — | D:0 |
| IAS 12 | g20-20 | 🗑️ dropped | — | D:0 |
| IAS 12 | g21-21B | 🗑️ dropped | — | D:0 |
| IAS 12 | g22-23 | 🗑️ dropped | 0.58-0.64 | D:0 |
| IAS 12 | g24-33 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g32A-32A | 🗑️ dropped | — | D:0 |
| IAS 12 | g33-33 | 🗑️ dropped | — | D:0 |
| IAS 12 | g34-36 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g37-37 | 🗑️ dropped | — | D:0 |
| IAS 12 | g38-45 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g46-56 | 🗑️ dropped | — | D:0 |
| IAS 12 | g5-11 | 🗑️ dropped | — | D:0 |
| IAS 12 | g57-68C | 🗑️ dropped | — | D:0 |
| IAS 12 | g58-60 | 🗑️ dropped | — | D:0 |
| IAS 12 | g61-65A | 🗑️ dropped | — | D:0 |
| IAS 12 | g66-68 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g68A-68C | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g7-11 | 🗑️ dropped | — | D:0 |
| IAS 12 | g71-76 | 🗑️ dropped | — | D:0 |
| IAS 12 | g77-77A | 🗑️ dropped | — | D:0 |
| IAS 12 | g78-78 | 🗑️ dropped | — | D:0 |
| IAS 12 | g79-88 | 🗑️ dropped | — | D:0 |
| IAS 12 | g88A-88D | 🗑️ dropped | — | D:0 |
| IAS 12 | TI0002 | 🗑️ dropped | 0.56 | D:0 |
| IAS 38 | g11-12 | 🗑️ dropped | — | D:0 |
| IAS 38 | g118-123 | 🗑️ dropped | 0.55 | D:0 |
| IAS 38 | g129-132 | 🗑️ dropped | 0.54 | D:0 |
| IAS 38 | g13-16 | 🗑️ dropped | 0.56 | D:0 |
| IAS 38 | g131-131 | 🗑️ dropped | — | D:0 |
| IAS 38 | g132-132 | 🗑️ dropped | — | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g18-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g25-32 | 🗑️ dropped | — | D:0 |
| IAS 38 | g33-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g35-38-41 | 🗑️ dropped | — | D:0 |
| IAS 38 | g42-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | 0.55 | D:0 |
| IAS 38 | g45-47 | 🗑️ dropped | — | D:0 |
| IAS 38 | g48-50 | 🗑️ dropped | — | D:0 |
| IAS 38 | g51-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g54-56 | 🗑️ dropped | — | D:0 |
| IAS 38 | g57-64 | 🗑️ dropped | — | D:0 |
| IAS 38 | g65-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g68-71 | 🗑️ dropped | 0.54 | D:0 |
| IAS 38 | g71-71 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🗑️ dropped | 0.54-0.61 | D:0 |
| IAS 38 | g9-17 | 🗑️ dropped | 0.54 | D:0 |
| IAS 38 | g97-99 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | g10-17 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | g11-14 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 3 | g18-20 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g28A-28B_V2 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 3 | g29-29 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB42-B42 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | gB51-B53 | 🗑️ dropped | 0.55-0.58 | D:0 |
| IFRS 3 | gB54-B55 | 🗑️ dropped | 0.56 | D:0 |

### Q12.2 / 1

- Question: Le preneur dispose d’un contrat sans option d’achat dont la période initiale n’excède pas douze mois, avec tacite reconduction ou durée indéterminée. Peut-il ne pas reconnaître le droit d’utilisation et la dette de loyers au titre de l’exemption pour contrats courts ?
- Embedded question: Le preneur dispose d’un contrat sans option d’achat dont la période initiale n’excède pas douze mois, avec tacite reconduction ou durée indéterminée. Peut-il ne pas reconnaître le droit d’utilisation et la dette de loyers au titre de l’exemption pour contrats courts ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.61-0.62 | D:0 |
| IFRS 16 | g22-22 | 🎯 authoritative | — | D:0 |
| IFRS 16 | g23-25 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g26-28 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g29-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g30-33 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g34-35 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g44-46 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.60-0.62 | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 16 | gB3-B8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.61-0.63 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IAS 12 | 0011 | 🗑️ dropped | — | D:0 |
| IAS 12 | g1-4 | 🗑️ dropped | — | D:0 |
| IAS 12 | g12-14 | 🗑️ dropped | — | D:0 |
| IAS 12 | g15-23 | 🗑️ dropped | 0.54-0.54 | D:0 |
| IAS 12 | g19-19 | 🗑️ dropped | — | D:0 |
| IAS 12 | g20-20 | 🗑️ dropped | — | D:0 |
| IAS 12 | g21-21B | 🗑️ dropped | — | D:0 |
| IAS 12 | g22-23 | 🖼️ peripheral | 0.58-0.64 | D:0 |
| IAS 12 | g24-33 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g32A-32A | 🗑️ dropped | — | D:0 |
| IAS 12 | g33-33 | 🗑️ dropped | — | D:0 |
| IAS 12 | g34-36 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g37-37 | 🗑️ dropped | — | D:0 |
| IAS 12 | g38-45 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g46-56 | 🗑️ dropped | — | D:0 |
| IAS 12 | g5-11 | 🗑️ dropped | — | D:0 |
| IAS 12 | g57-68C | 🗑️ dropped | — | D:0 |
| IAS 12 | g58-60 | 🗑️ dropped | — | D:0 |
| IAS 12 | g61-65A | 🗑️ dropped | — | D:0 |
| IAS 12 | g66-68 | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g68A-68C | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g7-11 | 🗑️ dropped | — | D:0 |
| IAS 12 | g71-76 | 🗑️ dropped | — | D:0 |
| IAS 12 | g77-77A | 🗑️ dropped | — | D:0 |
| IAS 12 | g78-78 | 🗑️ dropped | — | D:0 |
| IAS 12 | g79-88 | 🗑️ dropped | — | D:0 |
| IAS 12 | g88A-88D | 🗑️ dropped | — | D:0 |
| IAS 12 | TI0002 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 38 | g11-12 | 🗑️ dropped | — | D:0 |
| IAS 38 | g118-123 | 🗑️ dropped | 0.55 | D:0 |
| IAS 38 | g129-132 | 🗑️ dropped | 0.54 | D:0 |
| IAS 38 | g13-16 | 🗑️ dropped | 0.56 | D:0 |
| IAS 38 | g131-131 | 🗑️ dropped | — | D:0 |
| IAS 38 | g132-132 | 🗑️ dropped | — | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g18-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g25-32 | 🗑️ dropped | — | D:0 |
| IAS 38 | g33-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g35-38-41 | 🗑️ dropped | — | D:0 |
| IAS 38 | g42-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | 0.55 | D:0 |
| IAS 38 | g45-47 | 🗑️ dropped | — | D:0 |
| IAS 38 | g48-50 | 🗑️ dropped | — | D:0 |
| IAS 38 | g51-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g54-56 | 🗑️ dropped | — | D:0 |
| IAS 38 | g57-64 | 🗑️ dropped | — | D:0 |
| IAS 38 | g65-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g68-71 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 38 | g71-71 | 🗑️ dropped | — | D:0 |
| IAS 38 | g74-74 | 🗑️ dropped | — | D:0 |
| IAS 38 | g75-87 | 🗑️ dropped | — | D:0 |
| IAS 38 | g88-96 | 🗑️ dropped | 0.54-0.61 | D:0 |
| IAS 38 | g9-17 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 38 | g97-99 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | g10-17 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | g11-14 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g15-17 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 3 | g18-20 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g28A-28B_V2 | 🖼️ peripheral | 0.65 | D:0 |
| IFRS 3 | g29-29 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB42-B42 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | gB51-B53 | 🗑️ dropped | 0.55-0.58 | D:0 |
| IFRS 3 | gB54-B55 | 🗑️ dropped | 0.56 | D:0 |

### Q12.3 / 0

- Question: Pour un contrat sans option d’achat renouvelable par tacite reconduction, ou conclu sans terme défini, comment apprécier si la durée de location permet l’application de l’exemption de courte durée ?
- Embedded question: Pour un contrat sans option d’achat renouvelable par tacite reconduction, ou conclu sans terme défini, comment apprécier si la durée de location permet l’application de l’exemption de courte durée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.62 | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.62-0.66 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IAS 12 | g15-23 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g19-19 | 🗑️ dropped | — | D:0 |
| IAS 12 | g20-20 | 🗑️ dropped | — | D:0 |
| IAS 12 | g21-21B | 🗑️ dropped | — | D:0 |
| IAS 12 | g22-23 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 12 | g24-33 | 🖼️ peripheral | 0.53 | D:0 |
| IAS 12 | g32A-32A | 🗑️ dropped | — | D:0 |
| IAS 12 | g33-33 | 🗑️ dropped | — | D:0 |
| IAS 12 | g46-56 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g5-11 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g58-60 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g68A-68C | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g7-11 | 🗑️ dropped | — | D:0 |
| IAS 16 | g50-59 | 🖼️ peripheral | 0.60 | D:0 |

### Q12.3 / 1

- Question: Pour un contrat sans option d’achat renouvelable par tacite reconduction, ou conclu sans terme défini, comment apprécier si la durée de location permet l’application de l’exemption de courte durée ?
- Embedded question: Pour un contrat sans option d’achat renouvelable par tacite reconduction, ou conclu sans terme défini, comment apprécier si la durée de location permet l’application de l’exemption de courte durée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g18-21 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.62 | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.62-0.66 | D:0 |
| IFRS 16 | gB42-B42 | 🗑️ dropped | — | D:0 |
| IAS 12 | g15-23 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g19-19 | 🗑️ dropped | — | D:0 |
| IAS 12 | g20-20 | 🗑️ dropped | — | D:0 |
| IAS 12 | g21-21B | 🗑️ dropped | — | D:0 |
| IAS 12 | g22-23 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 12 | g24-33 | 🖼️ peripheral | 0.53 | D:0 |
| IAS 12 | g32A-32A | 🗑️ dropped | — | D:0 |
| IAS 12 | g33-33 | 🗑️ dropped | — | D:0 |
| IAS 12 | g46-56 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g5-11 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g58-60 | 🖼️ peripheral | — | D:0 |
| IAS 12 | g68A-68C | 🗑️ dropped | 0.55 | D:0 |
| IAS 12 | g7-11 | 🗑️ dropped | — | D:0 |
| IAS 16 | g50-59 | 🖼️ peripheral | 0.60 | D:0 |

### Q12.4 / 0

- Question: Un bail sans option d’achat prévoit une durée initiale inférieure ou égale à un an, mais peut se poursuivre automatiquement. Cette caractéristique empêche-t-elle de le qualifier de contrat de courte durée au sens d’IFRS 16 ?
- Embedded question: Un bail sans option d’achat prévoit une durée initiale inférieure ou égale à un an, mais peut se poursuivre automatiquement. Cette caractéristique empêche-t-elle de le qualifier de contrat de courte durée au sens d’IFRS 16 ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g100-102 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 16 | g3-4 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.56 | D:0 |
| IFRS 16 | gB14-B19 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 16 | gB20-B20 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | gB24-B31 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | gB25-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB28-B29 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB30-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.58-0.61 | D:0 |
| IFRS 16 | gB42-B42 | 🖼️ peripheral | — | D:0 |
| IAS 16 | g50-59 | 🖼️ peripheral | 0.62 | D:0 |

### Q12.4 / 1

- Question: Un bail sans option d’achat prévoit une durée initiale inférieure ou égale à un an, mais peut se poursuivre automatiquement. Cette caractéristique empêche-t-elle de le qualifier de contrat de courte durée au sens d’IFRS 16 ?
- Embedded question: Un bail sans option d’achat prévoit une durée initiale inférieure ou égale à un an, mais peut se poursuivre automatiquement. Cette caractéristique empêche-t-elle de le qualifier de contrat de courte durée au sens d’IFRS 16 ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 16 | g100-102 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 16 | g3-4 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 16 | g5-8 | 🎯 authoritative | 0.56 | D:0 |
| IFRS 16 | gB14-B19 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 16 | gB20-B20 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | gB24-B31 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | gB25-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB28-B29 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB30-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB34-B41 | 🎯 authoritative | 0.58-0.61 | D:0 |
| IFRS 16 | gB42-B42 | 🖼️ peripheral | — | D:0 |
| IAS 16 | g50-59 | 🖼️ peripheral | 0.62 | D:0 |

