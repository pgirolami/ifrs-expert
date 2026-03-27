# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - La question porte sur la classification IFRS 9 d’un actif financier comportant une clause contractuelle pouvant modifier l’échéancier ou le montant des flux de trésorerie.
   - Aucune autre caractéristique contractuelle ni information de modèle de gestion n’est fournie ; l’analyse se limite donc à l’effet de cette clause sur le critère SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Oui. Une clause déclenchante peut coexister avec le critère SPPI si les flux possibles avant et après le déclencheur restent ceux d’un prêt basique. Si la clause introduit une exposition non basique ou des écarts significatifs par rapport aux flux de référence, le test SPPI échoue et l’actif relève alors de la juste valeur par résultat.

## Points Opérationnels

   - Tester explicitement les flux contractuels possibles avant et après l’événement déclencheur ; la nature du trigger est un indicateur, mais pas le seul critère.
   - Comparer, si nécessaire, les flux possibles aux flux de référence pour déterminer s’ils peuvent devenir significativement différents sur la durée de vie de l’instrument.
   - Documenter séparément les cas où l’effet de la clause est seulement de minimis ou non genuine, car ils n’affectent pas la conclusion de classification.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - la clause ne doit pas indexer les flux sur des actions, des matières premières, des actifs spécifiques ou des flux d’actifs spécifiques<br>- la condition supplémentaire de 4.1.2(a) doit aussi être satisfaite |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - la clause ne doit pas indexer les flux sur des actions, des matières premières, des actifs spécifiques ou des flux d’actifs spécifiques<br>- la condition supplémentaire de 4.1.2A(a) doit aussi être satisfaite |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - la clause introduit une exposition à des variables non compatibles avec un prêt basique<br>- les flux possibles peuvent devenir significativement différents des flux de référence |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la clause ne doit pas indexer les flux sur des actions, des matières premières, des actifs spécifiques ou des flux d’actifs spécifiques
   - la condition supplémentaire de 4.1.2(a) doit aussi être satisfaite

**Raisonnment**:
Dans cette situation, la seule présence d’une clause modifiant le calendrier ou le montant des flux n’exclut pas le coût amorti. L’actif peut encore y être éligible si l’analyse des flux pouvant survenir avant et après le déclencheur montre qu’ils restent compatibles avec un prêt basique, y compris pour des clauses de prépaiement ou d’extension avec compensation raisonnable.

**Implications pratiques**: Documenter les flux possibles avant et après déclenchement avant de conclure au coût amorti.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >prepayment amount substantially represents unpaid amounts of principal and interest
 - B4.1.18
    >could have only a de minimis effect

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la clause ne doit pas indexer les flux sur des actions, des matières premières, des actifs spécifiques ou des flux d’actifs spécifiques
   - la condition supplémentaire de 4.1.2A(a) doit aussi être satisfaite

**Raisonnment**:
Dans cette situation, une clause déclenchante n’exclut pas à elle seule la juste valeur par OCI. Si les flux potentiels avant et après le déclencheur restent compatibles avec un prêt basique, le motif SPPI ne ferme pas cette catégorie ; en revanche, une clause non basique fait sortir l’actif du coût amorti et de la juste valeur par OCI.

**Implications pratiques**: Ne retenir la juste valeur par OCI qu’après validation du caractère basique de la clause déclenchante.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.12
    >subject to meeting the condition in paragraph 4.1.2(a) or the condition in paragraph 4.1.2A(a)
 - B4.1.9D
    >cannot be measured at amortised cost or fair value through other comprehensive income

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la clause introduit une exposition à des variables non compatibles avec un prêt basique
   - les flux possibles peuvent devenir significativement différents des flux de référence

**Raisonnment**:
Dans cette situation, la juste valeur par résultat devient le traitement applicable si la clause déclenchante fait dépendre les flux d’un facteur étranger à un prêt basique ou peut produire des flux significativement différents des flux de référence. C’est notamment le cas d’une indexation sur un indice actions ou sur des actifs ou flux spécifiques.

**Implications pratiques**: Si l’analyse SPPI échoue, classer l’actif en juste valeur par résultat.

**Référence**:
 - B4.1.10
    >it may be an indicator
 - B4.1.16
    >those contractual cash flows are inconsistent with a basic lending arrangement
 - B4.1.9D
    >cannot be measured at amortised cost or fair value through other comprehensive income
