# Analyse d'une question comptable

**Date**: 2026-03-27T09:20:15.886221+00:00
**Question**:
>Question not provided

**Documentation consultée**
   - (documentation non disponible)

## Hypothèses
La question porte sur le classement d’un actif financier selon IFRS 9.
L’analyse est limitée aux traitements comptables liés au fait que les flux contractuels sont, ou non, compatibles avec un prêt basique (SPPI).

## Recommandation

**oui_sous_conditions**
Un terme contractuel qui modifie l’échéancier ou le montant des flux n’exclut pas, à lui seul, le critère SPPI. Il faut apprécier les flux possibles avant et après le déclenchement ; s’ils restent compatibles avec principal et intérêts d’un prêt basique, le SPPI peut être respecté, sinon l’actif relève de la juste valeur par résultat.

## Approches évaluées

### Coût amorti
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - Le terme déclencheur ne doit pas introduire une exposition étrangère à un prêt basique, telle qu’un index actions ou des flux pouvant devenir significativement différents d’un benchmark de prêt.
   - Le modèle économique doit être la détention pour encaissement des flux contractuels.

**Raisonnment**:
Dans cette situation, la simple présence d’un événement déclencheur ne disqualifie pas automatiquement l’actif. Le coût amorti n’est possible que si l’analyse des flux avant et après le changement montre que le terme reste compatible avec un prêt basique, puis si le modèle économique correspond à une détention pour encaissement.

**Implications pratiques**: Documenter dès l’origine l’analyse du trigger et classer au coût amorti seulement si cette analyse reste compatible avec un prêt basique.

**Référence**:
 - B4.1.10
    >assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >prepayment amount substantially represents unpaid amounts of principal and interest

### Juste valeur par OCI
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - Le terme déclencheur doit laisser subsister des flux assimilables à principal et intérêts malgré l’événement.
   - Le modèle économique doit combiner encaissement des flux contractuels et vente.

**Raisonnment**:
Dans cette même situation, un instrument avec terme déclenché peut encore satisfaire le SPPI et donc rester éligible à la FVOCI. Cela suppose que les flux potentiels, y compris après déclenchement, restent ceux d’un prêt basique, et que le modèle économique combine encaissement et vente.

**Implications pratiques**: Si l’analyse du terme déclenché confirme le SPPI, la FVOCI reste envisageable selon le modèle économique retenu.

**Référence**:
 - B4.1.10
    >whether the contractual cash flows that could arise over the life of the instrument are solely payments of principal and interest
 - B4.1.11
    >extension option result in contractual cash flows during the extension period that are solely payments

### Juste valeur par résultat
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - L’analyse du terme déclencheur montre des flux non compatibles avec un prêt basique ou pouvant devenir significativement différents du benchmark.
   - L’effet du terme n’est ni de minimis ni non genuine.

**Raisonnment**:
Cette approche s’applique dans cette situation si le terme déclencheur fait sortir l’instrument d’un prêt basique. C’est le cas lorsque le changement de flux expose l’actif à autre chose que principal et intérêts, ou lorsque les flux possibles peuvent devenir significativement différents d’un benchmark pertinent.

**Implications pratiques**: Si le trigger fait échouer le SPPI, l’actif ne peut pas être classé au coût amorti ni en FVOCI et doit être mesuré en juste valeur par résultat.

**Référence**:
 - B4.1.9D
    >cannot be measured at amortised cost or fair value through other comprehensive income
 - B4.1.18
    >could have only a de minimis effect
