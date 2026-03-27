# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question porte sur le classement et l’évaluation d’un actif financier selon IFRS 9.
   - L’enjeu est de savoir si des clauses contractuelles pouvant modifier l’échéancier ou le montant des flux affectent l’éligibilité à des catégories de mesure fondées sur le critère SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Une telle clause n’exclut pas automatiquement le critère SPPI. Elle ne le respecte que si, avant et après l’événement déclencheur, tous les flux possibles restent compatibles avec un prêt basique; à défaut, l’actif relève de la juste valeur par résultat.

## Points Opérationnels

   - Analyser la clause sur la base de tous les flux contractuels possibles avant et après l’événement déclencheur, et non seulement dans le scénario jugé le plus probable.
   - Documenter si le déclencheur et ses effets restent liés à une logique de prêt basique ou s’ils introduisent une exposition externe (indice, actif, performance spécifique).
   - Évaluer l’effet de la clause sur chaque période de reporting et cumulativement sur la durée de vie de l’instrument, en tenant compte du seuil de minimis.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - La clause ne doit pas créer, après déclenchement, une exposition à un indice, un actif ou un risque étranger à un prêt basique.<br>- Les flux possibles avant et après modification doivent rester assimilables à principal et intérêts, avec au plus une compensation raisonnable si le contrat est interrompu ou ajusté. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - La clause ne doit pas pouvoir produire des flux sensiblement différents de ceux d’un instrument de prêt basique.<br>- Si la caractéristique n’a qu’un effet de minimis sur les flux, cet effet doit rester limité sur chaque période et cumulativement. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - L’analyse montre que certains flux possibles issus de la clause ne sont pas assimilables à principal et intérêts d’un prêt basique.<br>- L’effet potentiel de la clause sur les flux est plus que de minimis sur une période ou cumulativement. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause ne doit pas créer, après déclenchement, une exposition à un indice, un actif ou un risque étranger à un prêt basique.
   - Les flux possibles avant et après modification doivent rester assimilables à principal et intérêts, avec au plus une compensation raisonnable si le contrat est interrompu ou ajusté.

**Raisonnment**:
Dans cette situation, le coût amorti n’est envisageable que si la clause susceptible d’altérer les flux est examinée avant et après son déclenchement. Si tous les flux possibles restent des remboursements de principal et d’intérêts compatibles avec un prêt basique, la clause ne fait pas obstacle à cette mesure; sinon, elle l’exclut.

**Implications pratiques**: Le coût amorti reste possible seulement si l’analyse contractuelle documentée soutient que la clause conserve des flux de type prêt basique.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows
 - B4.1.11
    >reasonable compensation for the early termination of the contract

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause ne doit pas pouvoir produire des flux sensiblement différents de ceux d’un instrument de prêt basique.
   - Si la caractéristique n’a qu’un effet de minimis sur les flux, cet effet doit rester limité sur chaque période et cumulativement.

**Raisonnment**:
Dans cette situation, la JVOCI suit le même filtre SPPI que le coût amorti pour la clause visée. Elle n’est donc possible que si les flux pouvant résulter du déclencheur, sur toute la durée de vie de l’instrument, demeurent cohérents avec un prêt basique.

**Implications pratiques**: La JVOCI n’est préservée que si la revue SPPI de la clause conclut à des flux toujours compatibles avec principal et intérêts.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest
 - B4.1.18
    >could have only a de minimis effect on the contractual cash flows

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’analyse montre que certains flux possibles issus de la clause ne sont pas assimilables à principal et intérêts d’un prêt basique.
   - L’effet potentiel de la clause sur les flux est plus que de minimis sur une période ou cumulativement.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat devient le traitement pertinent si la clause déclenchée peut faire varier les flux d’une manière incompatible avec un prêt basique. C’est notamment le cas si elle expose l’instrument à des actifs, indices ou rendements spécifiques plutôt qu’à du principal et des intérêts.

**Implications pratiques**: Si la clause échoue au test SPPI, l’actif doit être orienté vers la juste valeur par résultat.

**Référence**:
 - B4.1.16
    >those contractual cash flows are inconsistent with a basic lending arrangement
 - B4.1.18
    >if a contractual cash flow characteristic could have an effect on the contractual cash flows that is more than de minimis
