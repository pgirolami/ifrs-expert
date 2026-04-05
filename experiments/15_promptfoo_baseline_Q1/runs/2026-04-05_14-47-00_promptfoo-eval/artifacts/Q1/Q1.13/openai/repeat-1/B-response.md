# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans les comptes consolidés, des dividendes intragroupe ont été décidés et une créance à recevoir a été comptabilisée. Dans ce contexte, la composante de risque de change associée à cette créance peut-elle être intégrée dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La créance de dividende intragroupe est un élément monétaire intragroupe reconnu.
   - L’analyse est faite du point de vue des comptes consolidés et du risque de change au sens d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais en pratique seulement via une relation de couverture de juste valeur, si la créance intragroupe crée en consolidation une exposition de change non totalement éliminée. Les modèles de cash flow hedge et de net investment hedge ne correspondent pas à cette situation.

## Points Opérationnels

   - Vérifier en priorité si les écarts de change sur la créance intragroupe subsistent en résultat consolidé après éliminations.
   - La documentation de couverture doit identifier l’instrument de couverture, la créance couverte et le risque de change désigné.
   - Si la créance est libellée dans une devise différente des monnaies fonctionnelles des entités concernées, l’analyse IAS 21 des écarts non éliminés est déterminante.
   - Le choix praticable dans cette situation est la couverture de juste valeur, pas la couverture de flux ni la couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance doit générer des gains ou pertes de change non totalement éliminés en consolidation<br>- les entités concernées doivent avoir des monnaies fonctionnelles différentes<br>- la relation de couverture doit être formellement désignée et documentée dès l’origine |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance doit générer des gains ou pertes de change non totalement éliminés en consolidation
   - les entités concernées doivent avoir des monnaies fonctionnelles différentes
   - la relation de couverture doit être formellement désignée et documentée dès l’origine

**Raisonnment**:
Ici, il s’agit d’une créance intragroupe reconnue, donc d’un actif déjà comptabilisé exposé au risque de change. IFRS 9 admet, en comptes consolidés, qu’un élément monétaire intragroupe soit un élément couvert pour son risque de change si les écarts de change ne sont pas totalement éliminés à la consolidation. Dans ce cas, la logique pertinente est celle d’une couverture de juste valeur d’un actif reconnu affectant le résultat.

**Implications pratiques**: Documenter la créance de dividende comme élément couvert pour son seul risque de change, sous réserve que ce risque affecte le résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance déjà reconnue après décision du dividende, et non sur une transaction future hautement probable. IFRS 9 réserve le cash flow hedge à la variabilité de flux de trésorerie d’éléments reconnus ou de transactions futures, mais, dans ce cas précis, l’exception explicite visant les éléments monétaires intragroupe en consolidation renvoie à leur qualification comme élément couvert, non à un dividende déjà constaté comme flux futur à couvrir.

**Implications pratiques**: Ne pas retenir le modèle de cash flow hedge pour une créance de dividende déjà comptabilisée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La créance de dividende intragroupe n’est pas un investissement net dans une activité à l’étranger, mais un poste monétaire intragroupe distinct. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change attaché aux net assets d’une activité étrangère inclus dans les états financiers, ce qui ne correspond pas au fait décrit.

**Implications pratiques**: Écarter la couverture d’investissement net pour cette créance de dividende intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations