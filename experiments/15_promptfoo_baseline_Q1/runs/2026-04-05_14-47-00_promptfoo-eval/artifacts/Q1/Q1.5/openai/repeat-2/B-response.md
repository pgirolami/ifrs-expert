# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question porte sur l’application de la comptabilité de couverture selon IFRS 9 dans des états financiers consolidés.
   - Les dividendes intragroupe ont été comptabilisés en créance à recevoir, donc il existe un poste monétaire intragroupe reconnu.
   - La créance de dividendes est libellée dans une devise qui crée un risque de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, le risque de change d’une créance intragroupe reconnue peut être désigné dans une relation de couverture uniquement via l’exception visant les postes monétaires intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation. Dans cette situation, le modèle pertinent est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’un investissement net.

## Points Opérationnels

   - La désignation formelle doit être faite au niveau consolidé, en identifiant la créance intragroupe, le risque de change couvert et l’instrument de couverture.
   - Le point clé d’éligibilité est de démontrer que les écarts de change sur la créance intragroupe ne sont pas entièrement éliminés en consolidation.
   - Si cette condition n’est pas remplie, la réponse devient non au niveau des états financiers consolidés.
   - Le modèle de couverture d’investissement net ne doit pas être utilisé pour requalifier un risque portant en réalité sur un dividende intragroupe à recevoir.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividendes est un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Le risque de change sur cette créance donne lieu à des gains ou pertes non entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividendes est un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Le risque de change sur cette créance donne lieu à des gains ou pertes non entièrement éliminés en consolidation.

**Raisonnment**:
La créance de dividendes est, dans les faits décrits, un actif reconnu. IFRS 9 permet qu’un poste monétaire intragroupe soit un élément couvert en consolidation pour son risque de change si ce risque génère des écarts de change non entièrement éliminés en consolidation. Dans ce cas, la logique de couverture de juste valeur d’un actif reconnu exposé à un risque particulier est cohérente avec la situation.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change de la créance intragroupe reconnue au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation posée, le dividende a déjà donné lieu à une créance à recevoir reconnue ; il ne s’agit donc pas d’une transaction future hautement probable. En outre, IFRS 9 limite en consolidation les éléments couverts intragroupe, et l’exception pertinente vise ici le poste monétaire intragroupe reconnu plutôt qu’un flux futur de dividende.

**Implications pratiques**: Le modèle de cash flow hedge ne correspond pas au fait générateur décrit, qui est une créance intragroupe déjà comptabilisée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé concerne une créance intragroupe de dividendes, non un investissement net dans une activité à l’étranger. Le modèle de net investment hedge traite le risque de change attaché aux net assets d’une opération étrangère ; il ne vise pas une créance de dividendes intragroupe reconnue.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir le change sur une créance de dividendes intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations