# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question porte sur le classement et l’évaluation d’un actif financier selon IFRS 9.
   - L’instrument est apprécié au regard du critère SPPI afin de déterminer sa base d’évaluation ultérieure admissible.

## Recommandation

**OUI SOUS CONDITIONS**

Une clause qui peut modifier l’échéancier ou le montant des flux n’exclut pas automatiquement le critère SPPI. Dans cette situation, il faut vérifier les flux possibles avant et après le déclencheur; s’ils restent compatibles avec un prêt basique, le SPPI peut être respecté, sinon l’actif relève du FVPL.

## Points Opérationnels

   - Analyser les flux contractuels possibles avant et après le déclenchement, et non seulement le scénario attendu.
   - Examiner la nature du déclencheur: un lien avec le risque de crédit est plus compatible avec le SPPI qu’un lien avec un indice d’actions ou la performance d’actifs spécifiques.
   - Si la clause n’a qu’un effet de minimis ou n’est pas genuine, elle ne modifie pas la conclusion de classement.
   - La conclusion SPPI détermine ensuite si le coût amorti ou le FVOCI restent ouverts; à défaut, l’actif est mesuré au FVPL.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Après examen des flux avant et après déclenchement, la clause ne crée pas d’exposition étrangère à un prêt basique<br>- Le modèle économique est la détention pour encaissement |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - Les flux susceptibles d’apparaître avant et après l’événement déclencheur restent compatibles avec un prêt basique<br>- Le modèle économique combine encaissement des flux et cession |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause introduit une variabilité ou un déclencheur non cohérent avec un prêt basique |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Après examen des flux avant et après déclenchement, la clause ne crée pas d’exposition étrangère à un prêt basique
   - Le modèle économique est la détention pour encaissement

**Raisonnment**:
Dans cette situation, le seul fait qu’une clause puisse modifier les flux ne ferme pas la voie du coût amorti. Cette base reste possible seulement si les flux pouvant naître avant et après le déclenchement demeurent des paiements de principal et d’intérêts cohérents avec un prêt basique; sinon le SPPI échoue.

**Implications pratiques**: Il faut documenter l’analyse de la clause déclenchante avant de conclure au coût amorti.

**Référence**:
 - B4.1.10
    >assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >contractual terms that result in contractual cash flows that are solely payments of principal and interest

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux susceptibles d’apparaître avant et après l’événement déclencheur restent compatibles avec un prêt basique
   - Le modèle économique combine encaissement des flux et cession

**Raisonnment**:
Dans cette situation, le FVOCI n’est envisageable que si la clause reste compatible avec le SPPI malgré le possible changement de flux. Si le déclencheur ou ses effets introduisent autre chose qu’une logique de prêt basique, cette option tombe comme le coût amorti.

**Implications pratiques**: Le FVOCI n’est ouvert que si l’analyse SPPI de la clause est positive et que le modèle économique pertinent est établi.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument
 - B4.1.18
    >does not affect the classification of the financial asset if it could have only a de minimis effect

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause introduit une variabilité ou un déclencheur non cohérent avec un prêt basique

**Raisonnment**:
Dans cette situation, le FVPL s’applique si la clause fait dépendre les flux d’un facteur incompatible avec un prêt basique ou si les flux potentiels deviennent significativement différents de flux de principal et d’intérêts de référence. L’exemple d’un déclencheur lié à un indice d’actions va dans ce sens.

**Implications pratiques**: Si la clause échoue au test SPPI, exclure le coût amorti et le FVOCI et retenir le FVPL.

**Référence**:
 - B4.1.10
    >a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level
 - B4.1.16
    >those contractual cash flows are inconsistent with a basic lending arrangement
