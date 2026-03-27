# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question porte sur la classification d’un actif financier au sens d’IFRS 9, pour lequel le test SPPI est pertinent.
   - Aucun fait supplémentaire n’est fourni sur la nature précise de l’événement déclencheur ni sur la forme exacte des flux modifiés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un instrument avec une clause modifiant l’échéancier ou le montant des flux peut encore respecter le critère SPPI. Il faut toutefois que l’analyse des flux avant et après le déclenchement montre qu’ils restent des paiements de principal et d’intérêts compatibles avec un prêt basique; sinon, le test SPPI échoue.

## Points Opérationnels

   - Analyser et documenter les flux contractuels susceptibles de naître avant et après l’événement déclencheur, pas seulement le flux actuellement attendu.
   - Examiner la nature du trigger: un événement lié au risque de crédit est plus compatible avec le SPPI qu’un déclencheur lié à un indice d’actions.
   - Si la clause affecte la composante de valeur temps de l’argent, apprécier si les flux contractuels pourraient être significativement différents des flux de référence sur la durée de vie de l’instrument.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’analyse de la clause conclut que les flux avant et après déclenchement restent compatibles avec des paiements de principal et d’intérêts.<br>- Le modèle économique pertinent est la détention pour encaisser les flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - L’analyse de la clause conclut que les flux avant et après déclenchement restent compatibles avec des paiements de principal et d’intérêts.<br>- Le modèle économique pertinent est la détention pour encaisser les flux contractuels et vendre. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - L’analyse conclut que les flux pouvant naître du terme contractuel ne respectent pas le critère SPPI. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’analyse de la clause conclut que les flux avant et après déclenchement restent compatibles avec des paiements de principal et d’intérêts.
   - Le modèle économique pertinent est la détention pour encaisser les flux contractuels.

**Raisonnment**:
Dans cette situation, la seule présence d’une clause pouvant modifier les flux n’exclut pas le SPPI. Le coût amorti peut donc rester possible si l’analyse des flux susceptibles de naître avant et après le déclenchement montre qu’ils demeurent des paiements de principal et d’intérêts, et si le modèle économique est la détention pour encaisser.

**Implications pratiques**: Le coût amorti n’est envisageable qu’après documentation de l’effet réel du trigger sur les flux contractuels.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument
 - B4.1.10
    >are solely payments of principal and interest on the principal amount outstanding
 - B4.1.11
    >contractual terms that result in contractual cash flows that are solely payments of principal and interest

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’analyse de la clause conclut que les flux avant et après déclenchement restent compatibles avec des paiements de principal et d’intérêts.
   - Le modèle économique pertinent est la détention pour encaisser les flux contractuels et vendre.

**Raisonnment**:
Dans cette situation, la clause de modification des flux n’empêche pas à elle seule une classification en FVOCI. Cette voie reste ouverte si le terme contractuel passe l’analyse SPPI avant et après l’événement déclencheur, et si le modèle économique correspond à l’encaissement et à la vente.

**Implications pratiques**: La FVOCI n’est possible que si la clause reste compatible avec un prêt basique et si le modèle économique adéquat est démontré.

**Référence**:
 - B4.1.10
    >the entity must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >a contractual term that permits the issuer or the holder to extend the contractual term
 - B4.1.11
    >cash flows during the extension period that are solely payments of principal and interest

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’analyse conclut que les flux pouvant naître du terme contractuel ne respectent pas le critère SPPI.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat devient la réponse si l’analyse montre que la clause fait naître des flux incompatibles avec un prêt basique. Le texte indique qu’un trigger lié à des impayés peut être plus compatible avec le SPPI, tandis qu’un trigger lié à un indice d’actions est un indicateur contraire.

**Implications pratiques**: Cette classification s’impose si la clause fait échouer le test SPPI.

**Référence**:
 - B4.1.10
    >It is more likely in the former case
 - B4.1.10
    >if a specified equity index reaches a particular level
 - B4.1.9D
    >cannot be measured at amortised cost or fair value through other comprehensive income
