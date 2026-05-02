# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16`
- Run: `2026-05-02_12-57-25_promptfoo-eval-family-q9`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 10

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| right_to_access | no | 2/10 | 2 |
| right_to_access_intellectual_property | no | 7/10 | 5 |
| right_to_access_the_entitys_intellectual_property | no | 1/10 | 1 |
| right_to_use | no | 2/10 | 2 |
| right_to_use_intellectual_property | no | 7/10 | 5 |
| right_to_use_the_entitys_intellectual_property | no | 1/10 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q9.0 | 2 | 35.0 | 35.0 | 0 | 4 |
| Q9.1 | 2 | 100.0 | 100.0 | 0 | 4 |
| Q9.2 | 2 | 100.0 | 100.0 | 0 | 4 |
| Q9.3 | 2 | 35.0 | 35.0 | 0 | 4 |
| Q9.4 | 2 | 35.0 | 35.0 | 0 | 4 |

## Authority Categorization by Run

### Q9.0 / 0

- Question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?
- Embedded question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g31-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.55-0.56 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.60 | D:0 |

### Q9.0 / 1

- Question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?
- Embedded question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g31-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.55-0.56 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.60 | D:0 |

### Q9.1 / 0

- Question: Pour une licence de propriété intellectuelle, le revenu doit-il être reconnu à un moment précis ou progressivement sur la période pendant laquelle le client bénéficie du droit ?
- Embedded question: Pour une licence de propriété intellectuelle, le revenu doit-il être reconnu à un moment précis ou progressivement sur la période pendant laquelle le client bénéficie du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g26-30 | 🔎 secondary | 0.60 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.60-0.60 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.63 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.60-0.65 | D:0 |
| IFRS 15 | gB63-B63B | 🖼️ peripheral | 0.67 | D:0 |
| IFRS 16 | g100-102 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 16 | g36-43 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | g39-43 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | g47-50 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 16 | g71-74 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 16 | g75-80 | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 16 | g79-80 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g81-87 | 🖼️ peripheral | 0.57 | D:0 |
| IFRS 16 | g87-87 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | g93-94 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 16 | gB13-B20 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | gB14-B19 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | gB20-B20 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB21-B23 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB24-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB25-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB28-B29 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB30-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB9-B31 | 🖼️ peripheral | 0.56 | D:0 |

### Q9.1 / 1

- Question: Pour une licence de propriété intellectuelle, le revenu doit-il être reconnu à un moment précis ou progressivement sur la période pendant laquelle le client bénéficie du droit ?
- Embedded question: Pour une licence de propriété intellectuelle, le revenu doit-il être reconnu à un moment précis ou progressivement sur la période pendant laquelle le client bénéficie du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g26-30 | 🔎 secondary | 0.60 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.60-0.60 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.63 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.60-0.65 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.67 | D:0 |
| IFRS 16 | g100-102 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 16 | g36-43 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g47-50 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 16 | g71-74 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 16 | g75-80 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 16 | g79-80 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g81-87 | 🖼️ peripheral | 0.57 | D:0 |
| IFRS 16 | g87-87 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g93-94 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 16 | gB13-B20 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 16 | gB20-B20 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB21-B23 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB24-B31 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB25-B31 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB28-B29 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB30-B31 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB9-B31 | 🗑️ dropped | 0.56 | D:0 |

### Q9.2 / 0

- Question: Une entité concède une licence de propriété intellectuelle à un client. Comment déterminer si le chiffre d’affaires correspondant est comptabilisé à une date donnée ou sur la durée du droit concédé ?
- Embedded question: Une entité concède une licence de propriété intellectuelle à un client. Comment déterminer si le chiffre d’affaires correspondant est comptabilisé à une date donnée ou sur la durée du droit concédé ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g24-25 | 🔎 secondary | — | D:0 |
| IFRS 15 | g31-45 | 🔎 secondary | 0.60 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | — | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.61-0.69 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.62-0.66 | D:0 |
| IFRS 15 | gB63-B63B | 🗑️ dropped | 0.63 | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g18-20 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g21A-21C | 🗑️ dropped | 0.58 | D:0 |
| IFRS 3 | g32-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g34-36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g37-40 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g39-40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g41-42A | 🗑️ dropped | — | D:0 |
| IFRS 3 | g51-53 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g53-53 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g56-56 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g59-63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g8-9 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | gB31-B40 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB42-B42 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 3 | gB46-B46 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB47-B49 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB64-B67 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | — | D:0 |

### Q9.2 / 1

- Question: Une entité concède une licence de propriété intellectuelle à un client. Comment déterminer si le chiffre d’affaires correspondant est comptabilisé à une date donnée ou sur la durée du droit concédé ?
- Embedded question: Une entité concède une licence de propriété intellectuelle à un client. Comment déterminer si le chiffre d’affaires correspondant est comptabilisé à une date donnée ou sur la durée du droit concédé ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g24-25 | 🔎 secondary | — | D:0 |
| IFRS 15 | g31-45 | 🔎 secondary | 0.60 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | — | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.61-0.69 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.62-0.66 | D:0 |
| IFRS 15 | gB63-B63B | 🗑️ dropped | 0.63 | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g18-20 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g21A-21C | 🗑️ dropped | 0.58 | D:0 |
| IFRS 3 | g32-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g34-36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g37-40 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g41-42A | 🗑️ dropped | — | D:0 |
| IFRS 3 | g51-53 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g53-53 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 3 | g59-63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g8-9 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB42-B42 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 3 | gB46-B46 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB47-B49 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB64-B67 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | — | D:0 |

### Q9.3 / 0

- Question: Le traitement du revenu issu d’une licence de propriété intellectuelle dépend de la nature du droit transféré. Quels critères IFRS permettent de choisir entre une reconnaissance ponctuelle et une reconnaissance étalée ?
- Embedded question: Le traitement du revenu issu d’une licence de propriété intellectuelle dépend de la nature du droit transféré. Quels critères IFRS permettent de choisir entre une reconnaissance ponctuelle et une reconnaissance étalée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g105-109 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 15 | g26-30 | 🔎 secondary | 0.58 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.57-0.58 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g41-43 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g44-45 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.60 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.58-0.59 | D:0 |
| IFRS 15 | gB63-B63B | 🖼️ peripheral | 0.60 | D:0 |

### Q9.3 / 1

- Question: Le traitement du revenu issu d’une licence de propriété intellectuelle dépend de la nature du droit transféré. Quels critères IFRS permettent de choisir entre une reconnaissance ponctuelle et une reconnaissance étalée ?
- Embedded question: Le traitement du revenu issu d’une licence de propriété intellectuelle dépend de la nature du droit transféré. Quels critères IFRS permettent de choisir entre une reconnaissance ponctuelle et une reconnaissance étalée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g105-109 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 15 | g26-30 | 🔎 secondary | 0.58 | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.57-0.58 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.60 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.58-0.59 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.60 | D:0 |

### Q9.4 / 0

- Question: Dans le cadre d’une licence de propriété intellectuelle, faut-il comptabiliser le revenu lorsque le droit est mis à disposition ou l’étaler pendant toute la période d’utilisation autorisée ?
- Embedded question: Dans le cadre d’une licence de propriété intellectuelle, faut-il comptabiliser le revenu lorsque le droit est mis à disposition ou l’étaler pendant toute la période d’utilisation autorisée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g35-37 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g56-58 | 🔎 secondary | 0.57 | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.56-0.60 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.57-0.62 | D:0 |

### Q9.4 / 1

- Question: Dans le cadre d’une licence de propriété intellectuelle, faut-il comptabiliser le revenu lorsque le droit est mis à disposition ou l’étaler pendant toute la période d’utilisation autorisée ?
- Embedded question: Dans le cadre d’une licence de propriété intellectuelle, faut-il comptabiliser le revenu lorsque le droit est mis à disposition ou l’étaler pendant toute la période d’utilisation autorisée ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g35-37 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g41-43 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g44-45 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🔎 secondary | 0.57 | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.56-0.60 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.57-0.62 | D:0 |

