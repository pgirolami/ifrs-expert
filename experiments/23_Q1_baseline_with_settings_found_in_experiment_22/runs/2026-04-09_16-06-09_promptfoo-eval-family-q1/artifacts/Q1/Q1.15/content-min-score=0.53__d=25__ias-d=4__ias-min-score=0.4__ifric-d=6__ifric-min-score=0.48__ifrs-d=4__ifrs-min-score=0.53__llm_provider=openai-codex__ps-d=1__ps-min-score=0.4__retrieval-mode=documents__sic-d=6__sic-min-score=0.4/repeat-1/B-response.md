# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ias32`
   - `ifric2`
   - `ifrs19`
   - `ifrs7`
   - `ifric17`
   - `ifrs9`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ias24`
   - `ifric16`
   - `ifric19`
   - `sic29`
   - `ifric21`
   - `ps1`
   - `ias37`

## Hypothèses
   - La question est analysée dans le cadre des états financiers consolidés et de la comptabilité de couverture selon IFRS 9.
   - La créance de dividende intragroupe est libellée dans une devise différente de la devise fonctionnelle de l’entité qui la comptabilise et crée donc une exposition de change.
   - Cette créance constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende intragroupe constitue un élément monétaire générant des écarts de change non totalement éliminés en consolidation. Dans ce cas, la désignation pertinente est en principe une couverture de juste valeur, et non une couverture de flux de trésorerie ni une couverture d’investissement net.

## Points Opérationnels

   - Vérifier d’abord que la créance de dividende est bien un élément monétaire intragroupe et que ses écarts de change ne sont pas totalement éliminés en consolidation.
   - La désignation doit être appréciée au niveau des états financiers consolidés, car la règle générale exclut les éléments intragroupe sauf exception spécifique sur le risque de change.
   - La documentation de couverture doit être en place dès l’origine de la relation et satisfaire aux critères d’IFRS 9.
   - Si l’exposition correspond à une créance déjà reconnue, la modélisation la plus cohérente est en pratique une couverture de juste valeur.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un élément monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes qui ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture doit satisfaire aux critères de désignation et de documentation d’IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un élément monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes qui ne sont pas totalement éliminés en consolidation.
   - La relation de couverture doit satisfaire aux critères de désignation et de documentation d’IFRS 9.

**Raisonnment**:
Dans cette situation, la créance de dividende déjà comptabilisée est un actif reconnu. IFRS 9 permet de couvrir un actif reconnu en juste valeur, et prévoit une exception pour le risque de change d’un élément monétaire intragroupe en consolidation lorsque les gains/pertes de change ne sont pas totalement éliminés. La désignation n’est donc possible que si cette condition est remplie dans les faits.

**Implications pratiques**: Si ces conditions sont remplies, l’exposition de change sur la créance peut être désignée comme élément couvert en couverture de juste valeur.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, l’exposition décrite porte sur une créance de dividende déjà reconnue, donc sur un montant monétaire déterminé. Le risque visé est celui de change affectant la valeur d’un actif comptabilisé, ce qui correspond à une logique de juste valeur dans ce cas, et non à une variabilité de flux de trésorerie futurs au sens de la couverture de flux.

**Implications pratiques**: Cette exposition ne devrait pas être documentée comme une couverture de flux de trésorerie dans les faits décrits.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe reconnue n’est pas, dans les faits décrits, un investissement net dans une activité à l’étranger. La couverture d’investissement net vise l’exposition de change sur les net assets d’une activité étrangère, pas sur un dividende à recevoir intragroupe isolé.

**Implications pratiques**: La relation ne doit pas être structurée comme une couverture d’investissement net sur la base de cette seule créance de dividende.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency