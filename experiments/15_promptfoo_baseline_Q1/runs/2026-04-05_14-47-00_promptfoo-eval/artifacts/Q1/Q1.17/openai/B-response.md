# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - L’analyse est faite au niveau des états financiers consolidés.
   - La créance de dividende intragroupe est un poste monétaire libellé dans une devise différente de la monnaie fonctionnelle d’au moins l’une des entités concernées, de sorte que l’écart de change n’est pas totalement éliminé en consolidation selon IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe via une couverture de juste valeur de la seule composante de change du dividende intragroupe à recevoir. Cela n’est possible en consolidation que si le poste monétaire intragroupe crée bien une exposition de change non entièrement éliminée ; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à ce cas.

## Points Opérationnels

   - Vérifier d’abord si le dividende intragroupe à recevoir est bien un poste monétaire en devise dont les écarts de change ne sont pas totalement éliminés en consolidation.
   - Si cette condition est remplie, la désignation la plus cohérente est une fair value hedge de la seule composante de change de la créance reconnue.
   - La documentation doit identifier précisément l’élément couvert, la composante de risque de change et la manière d’apprécier l’efficacité de la couverture.
   - Si l’exposition de change est entièrement éliminée en consolidation, aucune relation de couverture ne peut être mise en place sur ce poste au niveau consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe doit constituer un poste monétaire dont le risque de change n’est pas totalement éliminé en consolidation.<br>- La relation doit porter uniquement sur la composante de change, séparément identifiable et mesurable de façon fiable. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe doit constituer un poste monétaire dont le risque de change n’est pas totalement éliminé en consolidation.
   - La relation doit porter uniquement sur la composante de change, séparément identifiable et mesurable de façon fiable.

**Raisonnment**:
Ici, il existe une créance intragroupe déjà comptabilisée ; ce n’est donc pas une transaction future mais un actif reconnu. IFRS 9 autorise, en consolidation, la couverture du risque de change d’un poste monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés ; en outre, une composante de risque spécifique peut être désignée si elle est identifiable et mesurable.

**Implications pratiques**: La documentation de couverture doit désigner la créance reconnue et uniquement son risque de change comme élément couvert.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk or risks
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas décrit porte sur des dividendes intragroupe déjà comptabilisés à recevoir, donc sur une créance reconnue et non sur une transaction future hautement probable. Dans le contexte intragroupe en consolidation, IFRS 9 vise l’exception cash flow hedge pour des transactions intragroupe futures hautement probables affectant le résultat consolidé, ce qui ne correspond pas au fait décrit.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir la créance de dividende déjà reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Un dividende intragroupe à recevoir n’est pas un investissement net dans une activité à l’étranger mais une créance intragroupe distincte. Le modèle de net investment hedge vise l’exposition de change sur les net assets d’une activité étrangère, pas l’encaissement d’un dividende intragroupe isolé.

**Implications pratiques**: La couverture d’investissement net n’est pas adaptée à ce poste de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16.10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - ifric-16.12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity