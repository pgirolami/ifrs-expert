# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Reformulation**:
>Eligibility of an intragroup dividend receivable for designation as a hedged item in a hedge accounting relationship under IFRS.

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias24`, `ias37`)
   - IFRIC (`ifric2`, `ifric17`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias24`, `ias37`)
   - IFRIC (`ifric2`, `ifric17`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`)

## Hypothèses
   - Le dividende intragroupe est constaté comme une créance (actif financier) dans les états financiers consolidés du groupe.
   - La créance est libellée dans une monnaie étrangère autre que la monnaie fonctionnelle de l'entité consolidante.
   - Le dividende représente une transaction monétaire intragroupe, le contrepartie étant une entité du même groupe.

## Recommandation

**NON**

En IFRS, un élément couvert doit correspondre à un actif ou passif avec une partie externe (IFRS 9, §6.3.5). Un dividende intragroupe est un actif interne, et aucun texte ne prévoit d'exception pour les créances de dividendes intragroupe. L'exception d'IFRIC 16 ne s'applique qu'aux couvertures d'investissements nets dans des opérations étrangères, ce qui n'est pas le cas ici.

## Points Opérationnels

   - Documenter la position de change du dividende intragroupe et évaluer si elle affecte le résultat consolidé (IAS 21).
   - Envisager la comptabilisation des écarts de change directement en autres éléments du résultat全局 (OCI) si l'exposition n'est pas éliminée par consolidation.
   - Le cas échéant, utiliser les instruments dérivés intragroupe pour couvrir le risque de change au niveau des comptes individuels des entités, puis éliminer les effets en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture en cash flow du risque de change | NON | - (non spécifiées) |
| 2. Couverture en juste valeur du risque de change | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture en cash flow du risque de change

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La couverture en cash flow exige que l'élément couvert soit un actif ou passif avec une partie externe. La créance de dividende intragroupe a pour contrepartie une entité du groupe, donc elle ne peut être désignée comme élément couvert en vertu d'IFRS 9 §6.3.5.

**Implications pratiques**: Aucun enregistrement de couverture de flux de change ne peut être appliqué à cette créance intragroupe.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 2. Couverture en juste valeur du risque de change

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Même raisonnement que pour la couverture en cash flow : la juste valeur d'un élément couvert doit refléter un risque de change avec un tiers externe. La créance de dividende intragroupe ne répond pas au critère d'externalité exigé par IFRS 9 §6.3.5.

**Implications pratiques**: Aucune désignation en couverture en juste valeur n'est possible pour ce dividende.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 3. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRIC 16 limite expressément son champ aux couvertures du risque de change lié à un investissement net dans une opération étrangère. Une créance de dividende intragroupe ne constitue pas un investissement net et ne peut être traitée comme tel selon IFRS 9 §6.3.1.

**Implications pratiques**: L'approche de couverture d'investissement net ne s'applique pas à la créance de dividende.

**Référence**:
 - IFRS 9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation.
 - IFRIC 16 8

    >This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting.