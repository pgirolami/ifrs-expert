# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifrs9`
   - `ias32`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ifric2`
   - `ifric17`
   - `sic25`
   - `ifrs12`
   - `ps1`
   - `ias37`
   - `ifric23`
   - `sic29`

## Hypothèses
   - La créance de dividendes est un élément monétaire comptabilisé, libellé en devise étrangère.
   - La question est appréciée au niveau des états financiers consolidés.
   - L’exposition visée est le risque de change sur une créance intragroupe existante.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’un élément monétaire intragroupe peut être désigné comme élément couvert si les écarts de change ne sont pas totalement éliminés à la consolidation. En pratique, cela suppose typiquement des entités du groupe ayant des monnaies fonctionnelles différentes.

## Points Opérationnels

   - Le point décisif est la condition d’IFRS 9.6.3.6 : les écarts de change sur la créance intragroupe doivent ne pas être totalement éliminés en consolidation.
   - IAS 21.45 confirme qu’un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes peut laisser subsister un effet de change en consolidation.
   - Si cette condition n’est pas remplie, la créance de dividendes intragroupe ne peut pas être désignée comme élément couvert dans les comptes consolidés.
   - La couverture d’investissement net n’est pas adaptée à une créance de dividendes normale, car son règlement est en principe attendu.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit générer des écarts de change non totalement éliminés en consolidation.<br>- Le risque couvert doit être le seul risque de change sur la créance reconnue. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance intragroupe doit générer des écarts de change non totalement éliminés en consolidation.<br>- La relation de couverture doit viser la variabilité des flux de trésorerie due au risque de change sur la créance reconnue. |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit générer des écarts de change non totalement éliminés en consolidation.
   - Le risque couvert doit être le seul risque de change sur la créance reconnue.

**Raisonnment**:
La créance de dividendes est, selon l’hypothèse retenue, un actif reconnu. IFRS 9 permet qu’un élément monétaire intragroupe soit un élément couvert en consolidation pour le seul risque de change si ce risque génère des écarts de change non totalement éliminés. Dans ce cas, une désignation en fair value hedge est envisageable pour ce risque particulier.

**Implications pratiques**: Vérifier d’abord que la créance de dividendes produit bien un effet de change résiduel en résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit générer des écarts de change non totalement éliminés en consolidation.
   - La relation de couverture doit viser la variabilité des flux de trésorerie due au risque de change sur la créance reconnue.

**Raisonnment**:
IFRS 9 permet une cash flow hedge sur la variabilité des flux de trésorerie d’un actif reconnu attribuable à un risque particulier. Comme la question vise une créance de dividendes existante en devise, cette voie n’est recevable que si l’entité documente que l’exposition couverte est bien la variabilité des flux en monnaie fonctionnelle résultant du change, et que l’élément intragroupe remplit l’exception de consolidation.

**Implications pratiques**: La documentation de couverture doit être particulièrement précise sur la nature ‘cash flow’ de l’exposition de change couverte.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 45
    >the monetary item represents a commitment to convert one currency into another

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividendes intragroupe ne correspond pas, dans les faits décrits, à un investissement net dans une activité étrangère. IAS 21 réserve cette notion à un élément monétaire dont le règlement n’est ni planifié ni probable dans un avenir prévisible, ce qui ne cadre pas avec une créance de dividendes à encaisser. Cette approche ne s’applique donc pas à la situation décrite.

**Implications pratiques**: Ne pas traiter la créance de dividendes comme un élément d’investissement net sauf faits très différents de ceux posés.

**Référence**:
 - 15
    >settlement is neither planned nor likely to occur in the foreseeable future
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.