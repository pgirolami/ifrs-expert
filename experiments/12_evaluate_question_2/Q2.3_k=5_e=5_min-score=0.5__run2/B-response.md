# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - La question porte sur le classement d’un actif financier selon IFRS 9.
   - L’analyse est limitée aux traitements comptables liés au fait que les flux contractuels sont, ou non, compatibles avec un prêt basique (SPPI).

## Recommandation

**OUI SOUS CONDITIONS**

Un terme contractuel qui modifie l’échéancier ou le montant des flux n’exclut pas, à lui seul, le critère SPPI. Il faut apprécier les flux possibles avant et après le déclenchement ; s’ils restent compatibles avec principal et intérêts d’un prêt basique, le SPPI peut être respecté, sinon l’actif relève de la juste valeur par résultat.

## Points Opérationnels

   - Analyser à la date de comptabilisation initiale les flux contractuels possibles avant et après l’événement déclencheur.
   - Documenter la nature du trigger : un déclencheur lié au défaut ou au risque de crédit est plus compatible avec un prêt basique qu’un déclencheur lié à un indice actions.
   - Vérifier si l’effet du terme est de minimis ou non genuine ; dans ce cas, il n’affecte pas le classement.
   - Une fois le SPPI conclu, le choix entre coût amorti et FVOCI dépend encore du modèle économique applicable.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le terme déclencheur ne doit pas introduire une exposition étrangère à un prêt basique, telle qu’un index actions ou des flux pouvant devenir significativement différents d’un benchmark de prêt.<br>- Le modèle économique doit être la détention pour encaissement des flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - Le terme déclencheur doit laisser subsister des flux assimilables à principal et intérêts malgré l’événement.<br>- Le modèle économique doit combiner encaissement des flux contractuels et vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - L’analyse du terme déclencheur montre des flux non compatibles avec un prêt basique ou pouvant devenir significativement différents du benchmark.<br>- L’effet du terme n’est ni de minimis ni non genuine. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

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

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

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

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

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
