# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Peut-on appliquer la comptabilité de couverture en consolidation à l’exposition de change résultant de dividendes intragroupe dès lors que ceux-ci ont été comptabilisés en créance à recevoir ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question porte sur des états financiers consolidés établis selon les IFRS.
   - Les dividendes intragroupe sont libellés dans une devise créant une exposition de change entre des entités du groupe.
   - L’exposition visée est celle sur une créance/dette intragroupe née après comptabilisation du dividende à recevoir.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la couverture peut viser l’exposition de change d’une créance intragroupe déjà comptabilisée si cette créance est un poste monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, le modèle pertinent est le fair value hedge, pas le cash flow hedge.

## Points Opérationnels

   - Le point clé est le moment : dès que le dividende est comptabilisé en créance, l’analyse porte sur un poste monétaire reconnu, non sur une transaction future.
   - En consolidation, vérifier si les deux entités ont des monnaies fonctionnelles différentes ; sinon l’exception de l’item monétaire intragroupe ne joue pas.
   - La couverture n’est recevable que pour le risque de change qui affecte effectivement le résultat consolidé.
   - La documentation initiale au titre d’IFRS 9 doit identifier l’instrument de couverture, la créance couverte, le risque de change et l’évaluation de l’efficacité.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe.<br>- Les écarts de change sur cette créance affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert est bien le risque de change sur l’actif reconnu. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe.
   - Les écarts de change sur cette créance affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation.
   - Le risque couvert est bien le risque de change sur l’actif reconnu.

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance à recevoir : il s’agit donc d’un actif reconnu. En consolidation, un élément intragroupe n’est en principe pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés parce que les entités ont des monnaies fonctionnelles différentes. Dans cette situation précise, une couverture de juste valeur de ce risque de change peut entrer dans le champ.

**Implications pratiques**: Documenter la relation comme une couverture du risque de change sur la créance intragroupe reconnue, sous réserve que l’effet de change remonte bien en résultat consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis réservent le cash flow hedge à la variabilité de flux de trésorerie d’un élément reconnu ou d’une transaction future hautement probable. Or la question vise une exposition de change née une fois le dividende déjà comptabilisé en créance à recevoir, donc un poste monétaire reconnu. Dans ces faits, le sujet est celui du risque de change sur une créance existante, ce qui renvoie au traitement d’un actif reconnu plutôt qu’à une transaction future intragroupe.

**Implications pratiques**: Ne pas retenir le modèle cash flow hedge pour la créance de dividende déjà constatée en consolidation.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify