# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - La question porte sur le classement d’un actif financier selon IFRS 9.
   - Aucun fait supplémentaire n’est donné sur la clause précise; l’analyse est donc limitée à l’existence d’un terme contractuel pouvant modifier les flux en cas d’événement déclencheur.

## Recommandation

**OUI SOUS CONDITIONS**

Oui. Un terme contractuel qui modifie l’échéancier ou le montant des flux n’exclut pas, à lui seul, le critère SPPI. Il faut analyser les flux possibles avant et après le déclenchement; un déclencheur cohérent avec un prêt basique peut rester compatible, contrairement à une exposition de type indice actions ou autre risque non basique.

## Points Opérationnels

   - Analyser les flux contractuels possibles avant et après l’événement déclencheur, et pas seulement le scénario attendu.
   - Examiner la nature du déclencheur: un lien avec le risque de crédit est plus compatible avec un prêt basique qu’un lien avec un indice actions.
   - Vérifier si la caractéristique est seulement de minimis ou non genuine avant de conclure qu’elle affecte le test SPPI.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’analyse des flux avant et après déclenchement conclut qu’ils restent des paiements de principal et d’intérêts.<br>- Le déclencheur ne crée pas une exposition à une variable étrangère à un prêt basique, par exemple un indice actions. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - La clause déclenchée ne fait pas dériver les flux vers une exposition non basique.<br>- Les flux susceptibles de naître avant et après l’événement restent des paiements de principal et d’intérêts. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le terme déclencheur produit des flux qui ne sont pas uniquement du principal et des intérêts.<br>- L’effet potentiel de la caractéristique est plus que de minimis. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’analyse des flux avant et après déclenchement conclut qu’ils restent des paiements de principal et d’intérêts.
   - Le déclencheur ne crée pas une exposition à une variable étrangère à un prêt basique, par exemple un indice actions.

**Raisonnment**:
Dans cette situation, le coût amorti reste envisageable au regard du seul enjeu posé, à savoir le test SPPI. La présence d’un événement déclencheur n’est pas disqualifiante en soi; il faut apprécier les flux avant et après le déclenchement et vérifier qu’ils restent assimilables à du principal et des intérêts d’un prêt basique.

**Implications pratiques**: Documenter le test SPPI sur les scénarios contractuels pertinents avant de retenir le coût amorti.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >result in contractual cash flows that are solely payments of principal and interest

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause déclenchée ne fait pas dériver les flux vers une exposition non basique.
   - Les flux susceptibles de naître avant et après l’événement restent des paiements de principal et d’intérêts.

**Raisonnment**:
Pour cette situation, le filtre SPPI fonctionne de la même manière pour la FVOCI. Ainsi, un instrument avec clause déclenchée peut encore entrer dans cette catégorie si, malgré la modification potentielle des flux, ceux-ci demeurent compatibles avec un prêt basique après examen de toutes les issues contractuelles pertinentes.

**Implications pratiques**: La conclusion SPPI positive maintient la FVOCI comme option possible au regard de ce critère.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument
 - B4.1.11
    >The following are examples of contractual terms that result in contractual cash flows

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le terme déclencheur produit des flux qui ne sont pas uniquement du principal et des intérêts.
   - L’effet potentiel de la caractéristique est plus que de minimis.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat devient le traitement pertinent si la clause déclenchée conduit à des flux qui ne correspondent plus à un prêt basique. Le contexte IFRS 9 illustre précisément qu’un déclencheur lié à un indice actions est un signal fort d’échec du test SPPI, sauf si l’effet de la caractéristique est seulement de minimis ou non genuine.

**Implications pratiques**: Si le test SPPI échoue, l’instrument ne reste pas dans les catégories fondées sur SPPI et doit être traité à la juste valeur par résultat.

**Référence**:
 - B4.1.10
    >if a specified equity index reaches a particular level
 - B4.1.18
    >could have only a de minimis effect
