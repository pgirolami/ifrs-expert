# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans un schéma où des dividendes intragroupe ont déjà été reconnus en créance à recevoir, la question se pose du traitement du risque de change associé en consolidation. Ce risque peut-il être formellement documenté dans une relation de couverture ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance de dividende intragroupe est un élément monétaire reconnu, libellé en devise étrangère.
   - La question vise les états financiers consolidés et le risque de change attaché à cette position intragroupe reconnue.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via l’exception IFRS 9 applicable au risque de change d’un élément monétaire intragroupe en consolidation. Il faut que les écarts de change ne soient pas totalement éliminés en consolidation, typiquement parce que les entités concernées ont des monnaies fonctionnelles différentes.

## Points Opérationnels

   - En consolidation, partir de la règle générale d’exclusion des postes intragroupe puis documenter explicitement l’exception de l’élément monétaire intragroupe.
   - Le point décisif est de démontrer que les écarts de change sur la créance de dividende ne sont pas totalement éliminés en consolidation.
   - La documentation doit être mise en place dans une relation de couverture répondant aux critères généraux d’IFRS 9, y compris la désignation formelle et l’identification du risque couvert.
   - Si les écarts de change sont entièrement éliminés en consolidation, la réponse devient non pour cette créance intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.<br>- Le risque de change doit créer des gains ou pertes de change non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - Le risque de change doit créer des gains ou pertes de change non totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu et la question porte sur son risque de change en consolidation. IFRS 9 pose une interdiction générale pour les postes intragroupe, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il génère des écarts non totalement éliminés en consolidation. Si cette condition est remplie, une documentation formelle de couverture est possible.

**Implications pratiques**: La documentation de couverture est envisageable en consolidation si l’exception relative aux éléments monétaires intragroupe est démontrée.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis réservent la couverture de flux de trésorerie, pour les situations intragroupe en consolidation, à la devise d’une transaction intragroupe hautement probable. Ici, le dividende a déjà été reconnu en créance à recevoir : il ne s’agit plus d’une transaction future hautement probable mais d’un poste monétaire existant. Le cas décrit ne correspond donc pas au modèle visé.

**Implications pratiques**: Le risque de change de la créance déjà constatée ne doit pas être documenté comme cash flow hedge dans ce schéma.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.4
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe déjà comptabilisée, non sur le risque de change lié à un investissement net dans une activité à l’étranger. Le modèle IFRIC 16 vise les écarts de change sur des net assets de foreign operation, pas un receivable intragroupe isolé. Ce traitement n’est donc pas celui de la situation décrite.

**Implications pratiques**: Il ne faut pas qualifier cette créance de dividende comme hedge de net investment.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets