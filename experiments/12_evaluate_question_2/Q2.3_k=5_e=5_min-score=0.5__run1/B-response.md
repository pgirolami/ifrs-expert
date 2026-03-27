# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - On suppose que la question porte sur le classement et l’évaluation ultérieure d’un actif financier selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, sous conditions : la seule présence d’un terme déclenché par un événement n’exclut pas le critère SPPI. Il faut apprécier les flux possibles avant et après le déclenchement ; si le mécanisme reste cohérent avec un prêt basique, le SPPI peut être respecté, sinon l’actif relève de la juste valeur par résultat.

## Points Opérationnels

   - Analyser les flux contractuels susceptibles de naître avant et après le déclenchement, sur toute la durée de vie de l’instrument.
   - Qualifier précisément la nature du trigger : lié au risque de crédit/au prêt basique, ou au contraire à un indice, à des actifs déterminés ou à une autre exposition non basique.
   - Tenir compte qu’un effet seulement de minimis ou non genuine n’affecte pas le classement.
   - Une fois le SPPI établi ou écarté, le choix entre coût amorti et FVOCI dépend du modèle économique ; à défaut de SPPI, la juste valeur par résultat s’applique.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le déclencheur et ses effets restent compatibles avec une logique de prêt basique, sans exposition à un indice d’actions, à des actifs spécifiques ou à une variabilité étrangère au crédit/temps/risques et coûts de base.<br>- Le modèle économique est de détenir l’actif pour encaisser les flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - Le déclencheur et les flux potentiels avant/après modification restent compatibles avec un prêt basique.<br>- Le modèle économique est de détenir l’actif pour encaisser les flux contractuels et vendre. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le déclencheur crée une variabilité de flux non cohérente avec un prêt basique, par exemple liée à un indice d’actions ou à la performance d’actifs déterminés.<br>- L’effet du terme n’est pas seulement de minimis ou non genuine. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le déclencheur et ses effets restent compatibles avec une logique de prêt basique, sans exposition à un indice d’actions, à des actifs spécifiques ou à une variabilité étrangère au crédit/temps/risques et coûts de base.
   - Le modèle économique est de détenir l’actif pour encaisser les flux contractuels.

**Raisonnment**:
Dans cette situation, un terme contractuel qui modifie l’échéancier ou le montant des flux n’empêche pas automatiquement le SPPI.
Le coût amorti n’est possible que si l’analyse des flux avant et après le déclencheur montre une logique de prêt basique, et si l’actif est détenu pour encaisser les flux contractuels.

**Implications pratiques**: Documenter l’analyse du trigger et des flux sur toute la durée de vie avant de conclure au coût amorti.

**Référence**:
 - B4.1.10
    >must assess the contractual cash flows that could arise both before, and after, the change
 - B4.1.11
    >a contractual term that permits the issuer (ie the debtor) to prepay a debt instrument

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le déclencheur et les flux potentiels avant/après modification restent compatibles avec un prêt basique.
   - Le modèle économique est de détenir l’actif pour encaisser les flux contractuels et vendre.

**Raisonnment**:
Dans cette situation, le même test SPPI s’applique : un mécanisme déclenché par événement peut encore être compatible avec un prêt basique.
La FVOCI n’est envisageable que si ce terme ne fait pas sortir l’instrument du SPPI et si le modèle économique combine encaissement des flux contractuels et vente.

**Implications pratiques**: Vérifier d’abord le SPPI au niveau contractuel, puis confirmer que le modèle économique correspond à une gestion 'collecte et vente'.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument
 - B4.1.11
    >The following are examples of contractual terms that result in contractual cash flows that are solely payments of principal and interest

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le déclencheur crée une variabilité de flux non cohérente avec un prêt basique, par exemple liée à un indice d’actions ou à la performance d’actifs déterminés.
   - L’effet du terme n’est pas seulement de minimis ou non genuine.

**Raisonnment**:
Dans cette situation, la JV résultat s’impose si le terme déclenché par l’événement introduit une exposition incompatible avec un prêt basique.
Ce sera le cas si le trigger fait dépendre les flux d’éléments comme un indice d’actions ou des actifs/cash flows spécifiques, plutôt que d’éléments usuels d’un prêt.

**Implications pratiques**: Si le trigger fait sortir l’instrument du SPPI, l’actif ne peut pas être classé au coût amorti ni en FVOCI.

**Référence**:
 - B4.1.10
    >interest rate is reset to a higher rate if a specified equity index reaches a particular level
 - B4.1.16
    >cash flows increase as more automobiles use a particular toll road
 - B4.1.18
    >could have only a de minimis effect on the contractual cash flows
