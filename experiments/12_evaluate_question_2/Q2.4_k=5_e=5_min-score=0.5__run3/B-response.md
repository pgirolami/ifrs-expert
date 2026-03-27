# Analyse d'une question comptable

**Date**: 2026-03-27T09:20:15.891848+00:00
**Question**:
>Question not provided

**Documentation consultée**
   - (documentation non disponible)

## Hypothèses
La question porte sur la classification d’un actif financier selon IFRS 9, car le critère SPPI est examiné dans ce cadre.
La condition relative au modèle économique est distincte de la question SPPI et n’est pas tranchée ici.

## Recommandation

**oui_sous_conditions**
Oui, une telle clause n’exclut pas automatiquement le critère SPPI. Il faut analyser les flux possibles avant et après le déclenchement et vérifier que la clause reste dans une logique de prêt basique; sinon, l’actif relève de la juste valeur par résultat.

## Approches évaluées

### Coût amorti
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - La clause produit seulement des variations cohérentes avec un prêt basique, par exemple un prépaiement ou une extension avec compensation raisonnable.
   - Le déclencheur ne fait pas dépendre les flux d’un indice actions, d’une marchandise ou d’actifs / flux de trésorerie spécifiques.

**Raisonnment**:
Dans cette situation, la seule présence d’une clause modifiant l’échéancier ou le montant des flux n’écarte pas d’emblée le coût amorti.
Il faut apprécier les flux susceptibles de naître avant et après le déclenchement; si la clause reste dans une logique de principal, d’intérêt et, le cas échéant, de compensation raisonnable, l’actif peut encore satisfaire SPPI.

**Implications pratiques**: Le coût amorti reste ouvert si l’analyse contractuelle confirme que la clause ne fait pas sortir l’actif du périmètre SPPI.

**Référence**:
 - B4.1.10
    >whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest
 - B4.1.11
    >the prepayment amount substantially represents unpaid amounts of principal and interest on the principal amount outstanding

### Juste valeur par OCI
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - La modification contractuelle se limite à des flux de principal et d’intérêt, avec compensation raisonnable le cas échéant.
   - Le modèle économique requis pour la FVOCI est satisfait séparément.

**Raisonnment**:
Dans cette situation, la FVOCI n’est envisageable que si la même analyse conduit d’abord à conclure que la clause déclenchante ne fait pas perdre le caractère SPPI.
Le contexte fourni ne tranche pas le modèle économique; la FVOCI reste donc possible, mais seulement sous cette double réserve.

**Implications pratiques**: Si la clause reste compatible avec SPPI, la FVOCI demeure disponible sous réserve du modèle économique applicable.

**Référence**:
 - B4.1.10
    >The entity may also need to assess the nature of any contingent event
 - B4.1.11
    >the terms of the extension option result in contractual cash flows during the extension period that are solely payments of principal and interest

### Juste valeur par résultat
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - La clause expose l’instrument à des risques ou à une variabilité non compatibles avec un prêt basique, par exemple un indice actions ou la performance d’un actif spécifique.
   - L’effet de la clause n’est ni de minimis ni non genuine.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat s’impose seulement si la clause déclenchante fait varier les flux selon un facteur étranger à un prêt basique.
Le contexte vise notamment un taux lié à un indice actions ou des flux dépendant d’actifs spécifiques; dans ce cas, l’actif ne peut pas être classé au coût amorti ni en FVOCI.

**Implications pratiques**: Si la clause sort du schéma de prêt basique, le traitement de repli est la juste valeur par résultat.

**Référence**:
 - B4.1.10
    >if a specified equity index reaches a particular level
 - B4.1.16
    >those contractual cash flows are inconsistent with a basic lending arrangement.
 - B4.1.18
    >could have only a de minimis effect
