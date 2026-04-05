# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur la comptabilité de couverture dans des états financiers consolidés au titre d’IFRS 9.
   - Les dividendes intragroupe ont déjà été comptabilisés en créance/dette intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance intragroupe est un élément monétaire entre entités ayant des monnaies fonctionnelles différentes et si le risque de change génère des écarts non totalement éliminés en consolidation. Dans cette situation, le modèle pertinent est en pratique la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point décisif en consolidation est l’exception d’IFRS 9 pour le risque de change d’un élément monétaire intragroupe.
   - Il faut vérifier factuellement que la créance de dividende est bien monétaire et qu’elle existe entre entités à monnaies fonctionnelles différentes.
   - Si les écarts de change sont totalement éliminés en consolidation, la désignation comme élément couvert n’est pas admise dans cette situation.
   - La documentation de couverture doit être établie à l’origine de la relation et démontrer que le risque couvert est bien celui qui affecte le résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un élément monétaire intragroupe.<br>- Les deux entités ont des monnaies fonctionnelles différentes.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un élément monétaire intragroupe.
   - Les deux entités ont des monnaies fonctionnelles différentes.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Ici, la créance de dividende est déjà reconnue. En consolidation, les éléments intragroupe sont en principe exclus, sauf exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans ce cas précis, l’exposition porte sur un actif reconnu et le modèle de couverture de juste valeur est celui qui correspond le mieux à ce risque de change affectant le résultat.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé en visant le risque de change de la créance intragroupe reconnue.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende n’est plus une transaction intragroupe future mais une créance déjà comptabilisée. Le sujet est donc la réévaluation de change d’un élément monétaire reconnu, et non la variabilité de flux futurs d’une transaction hautement probable. Le modèle de cash flow hedge ne correspond pas au fait décrit.

**Implications pratiques**: Ne pas structurer la désignation comme couverture de flux de trésorerie pour cette créance déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende intragroupe reconnue, pas un montant de net assets d’une activité étrangère. Le modèle de couverture d’investissement net vise le risque de change sur un investissement net dans une activité à l’étranger, avec comptabilisation en OCI, ce qui ne correspond pas au fait pattern décrit.

**Implications pratiques**: Ne pas traiter la créance de dividende comme un investissement net couvert.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets