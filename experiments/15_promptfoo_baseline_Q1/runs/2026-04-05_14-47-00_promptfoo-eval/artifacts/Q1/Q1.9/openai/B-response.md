# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur la comptabilité de couverture dans des états financiers consolidés selon IFRS 9.
   - Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe monétaire.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende intragroupe crée un risque de change qui n’est pas intégralement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie.

## Points Opérationnels

   - Vérifier au moment de la désignation que la créance de dividende est bien un élément monétaire intragroupe encore exposé au change en consolidation.
   - Confirmer que les entités concernées ont des monnaies fonctionnelles différentes, faute de quoi l’exception de 6.3.6 ne joue pas.
   - La documentation de couverture doit montrer que le risque couvert est le risque de change affectant le résultat consolidé.
   - Si l’exposition est déjà reconnue en créance, l’analyse doit être menée en couverture de juste valeur plutôt qu’en couverture de flux de trésorerie.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette intragroupe est libellée dans une monnaie générant des écarts de change non totalement éliminés en consolidation.<br>- Le risque de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette intragroupe est libellée dans une monnaie générant des écarts de change non totalement éliminés en consolidation.
   - Le risque de change affecte le résultat consolidé.

**Raisonnment**:
Ici, le dividende déclaré est une créance intragroupe monétaire reconnue. IFRS 9 prévoit une exception permettant de désigner le risque de change d’un élément monétaire intragroupe dans les comptes consolidés s’il génère des écarts de change non totalement éliminés en consolidation; cette exposition sur une créance reconnue relève de la logique d’une couverture de juste valeur car elle affecte le résultat.

**Implications pratiques**: Il faut documenter la relation de couverture sur la créance de dividende reconnue et démontrer que l’exposition de change subsiste au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende n’est plus une transaction intragroupe future hautement probable mais une créance déjà reconnue. La question vise le risque de change porté par cet élément monétaire reconnu; le contexte IFRS fourni traite ce cas via l’exception sur les éléments monétaires intragroupe, pas comme une couverture de flux de trésorerie.

**Implications pratiques**: Une désignation en couverture de flux de trésorerie ne correspond pas au fait qu’un dividende a déjà été déclaré et comptabilisé en créance.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - B6.3.5
    >royalty payments, interest payments or management charges ... unless there is a related external transaction