# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - L’instrument est un actif financier relevant du modèle de classement et d’évaluation d’IFRS 9.
   - La question porte sur les conséquences, en matière de classement, de la condition SPPI lorsque les flux contractuels peuvent changer à la suite d’un événement déclencheur.

## Recommandation

**OUI SOUS CONDITIONS**

Oui. La seule présence d’une clause modifiant l’échéancier ou le montant des flux n’empêche pas, à elle seule, le respect du critère SPPI. Il faut toutefois vérifier, dans cette situation, les flux possibles avant et après le déclencheur et s’assurer que le déclencheur n’introduit pas une exposition étrangère à un prêt basique.

## Points Opérationnels

   - Identifier tous les flux contractuels possibles avant et après la survenance du déclencheur.
   - Documenter la nature du déclencheur: un déclencheur lié à la détérioration du crédit est plus compatible avec SPPI qu’un déclencheur indexé sur des variables de marché de type actions.
   - Si l’analyse conclut que la clause fait sortir l’instrument de SPPI, exclure le coût amorti et la JV par OCI et retenir la juste valeur par résultat.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le déclencheur ne crée pas d’exposition à un indice actions ou à un autre facteur non cohérent avec un prêt basique.<br>- Les flux après déclenchement restent cohérents avec une rémunération du temps, du risque de crédit et d’une marge de prêt. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - La clause de variation n’introduit pas de volatilité ou de risque étranger à une relation de prêt basique.<br>- L’analyse des flux potentiels avant et après déclenchement ne met pas en évidence de mécanisme assimilable à une exposition de type actions. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le déclencheur modifie les flux d’une manière incompatible avec un prêt basique.<br>- La clause introduit un facteur de rendement ou de risque non lié au temps, au crédit ou aux coûts de prêt de base. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le déclencheur ne crée pas d’exposition à un indice actions ou à un autre facteur non cohérent avec un prêt basique.
   - Les flux après déclenchement restent cohérents avec une rémunération du temps, du risque de crédit et d’une marge de prêt.

**Raisonnment**:
Dans cette situation, le coût amorti n’est envisageable que si la clause de déclenchement ne fait pas sortir l’actif du périmètre SPPI. Le texte impose d’examiner les flux susceptibles de survenir avant et après la modification, et indique que la nature du déclencheur peut être un indicateur important. Une clause liée à des impayés est plus compatible qu’une clause liée à un indice actions.

**Implications pratiques**: Le coût amorti reste possible seulement après une analyse documentée des flux contractuels potentiels avant et après le déclencheur.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.10
    >it may be an indicator
 - B4.1.10
    >more likely in the former case

### 2. Juste valeur par autres éléments du résultat global
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause de variation n’introduit pas de volatilité ou de risque étranger à une relation de prêt basique.
   - L’analyse des flux potentiels avant et après déclenchement ne met pas en évidence de mécanisme assimilable à une exposition de type actions.

**Raisonnment**:
Dans cette situation, la juste valeur par OCI n’est possible que si la même analyse conclut que la clause de variation des flux reste compatible avec SPPI. Le fait qu’un événement déclencheur existe n’est pas décisif en soi; ce qui compte est l’effet des flux potentiels sur toute la durée de l’instrument. Si la clause demeure compatible avec un prêt basique, cette base de mesure reste ouverte.

**Implications pratiques**: La JV par OCI n’est envisageable qu’après la même revue contractuelle détaillée que pour le coût amorti.

**Référence**:
 - B4.1.10
    >whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest
 - B4.1.11
    >a variable interest rate that consists of consideration for the time value of money

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le déclencheur modifie les flux d’une manière incompatible avec un prêt basique.
   - La clause introduit un facteur de rendement ou de risque non lié au temps, au crédit ou aux coûts de prêt de base.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat devient la voie pertinente si l’analyse de la clause montre que les flux après déclenchement ne sont plus ceux d’un prêt basique. Le contexte illustre qu’un déclencheur fondé sur un indice actions est un signal défavorable, contrairement à un ajustement lié à des défauts de paiement. Ainsi, ce traitement s’applique si la clause fait échouer le test SPPI.

**Implications pratiques**: Si la clause échoue au test SPPI, il faut écarter le coût amorti et la JV par OCI au profit de la JV par résultat.

**Référence**:
 - B4.1.10
    >compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments
 - B4.1.10
    >to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level
 - B4.1.15
    >those cash flows do not represent the payment of principal and interest
