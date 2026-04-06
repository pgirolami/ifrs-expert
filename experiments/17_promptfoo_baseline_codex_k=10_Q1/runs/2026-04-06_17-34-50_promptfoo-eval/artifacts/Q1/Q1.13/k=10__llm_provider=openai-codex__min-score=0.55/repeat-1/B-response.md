# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Dans les comptes consolidés, des dividendes intragroupe ont été décidés et une créance à recevoir a été comptabilisée. Dans ce contexte, la composante de risque de change associée à cette créance peut-elle être intégrée dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La créance de dividende intragroupe est un élément monétaire intragroupe déjà comptabilisé.
   - La créance et la dette correspondante sont libellées dans une devise générant un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - L'analyse est faite au niveau des comptes consolidés et porte uniquement sur l'éligibilité au hedge accounting selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une relation de couverture du risque de change d'un élément monétaire intragroupe lorsque ce risque n'est pas totalement éliminé en consolidation. Dans cette situation, l'approche pertinente est la couverture de juste valeur; les autres approches ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Vérifier que la créance de dividende est bien un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.
   - Confirmer que les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation; sinon l'élément n'est pas éligible.
   - La documentation de couverture doit identifier l'instrument de couverture, la créance couverte, le risque de change désigné et la manière d'évaluer l'efficacité.
   - L'exception IFRS 9 pour les éléments intragroupe vise le seul risque de change; elle ne généralise pas l'éligibilité des transactions intragroupe en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit créer une exposition de change donnant lieu à des gains ou pertes non totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée dès l'origine conformément à IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit créer une exposition de change donnant lieu à des gains ou pertes non totalement éliminés en consolidation.
   - La relation de couverture doit être formellement désignée et documentée dès l'origine conformément à IFRS 9.

**Raisonnment**:
La créance de dividende est un actif reconnu; IFRS 9 permet qu'un actif reconnu soit un élément couvert en juste valeur. En consolidation, un élément monétaire intragroupe peut exceptionnellement être désigné pour son risque de change si les écarts de change ne sont pas totalement éliminés. C'est le cas visé par l'hypothèse retenue.

**Implications pratiques**: La créance de dividende peut être incluse comme élément couvert pour son risque de change dans une documentation de fair value hedge, sous réserve de l'exception intragroupe.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.4.1
    >at the inception ... there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrivent une créance de dividende déjà constatée, donc un montant de devise à recevoir déterminé. Le sujet est le risque de change rattaché à un actif reconnu, ce qui renvoie ici à une exposition de valeur de la créance, non à une variabilité de flux d'une transaction future hautement probable.

**Implications pratiques**: Cette approche ne doit pas être retenue pour documenter la couverture de cette créance de dividende déjà comptabilisée.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.1
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise la composante de change d'une créance de dividende intragroupe, non le risque de change découlant d'un investissement net dans une activité à l'étranger. Le modèle de net investment hedge est réservé à l'exposition sur les net assets d'une foreign operation incluse dans les états financiers.

**Implications pratiques**: La créance de dividende ne doit pas être documentée comme élément couvert au titre d'une couverture d'investissement net.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 1
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - ifric-16 2
    >the item being hedged ... may be an amount of net assets