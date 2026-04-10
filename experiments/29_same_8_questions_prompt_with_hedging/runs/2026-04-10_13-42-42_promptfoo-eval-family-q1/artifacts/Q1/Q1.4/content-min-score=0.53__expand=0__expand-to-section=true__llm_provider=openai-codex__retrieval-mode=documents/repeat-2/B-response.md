# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs10`
   - `ifrs12`
   - `ifrs19`
   - `ias24`
   - `ifrs9`
   - `ias7`
   - `ifric17`
   - `ias27`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric2`

## Hypothèses
   - L’analyse est effectuée au niveau des états financiers consolidés.
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance libellée en devise entre entités du groupe.
   - La créance et la dette correspondante constituent un poste monétaire intragroupe et les entités concernées ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une désignation de couverture peut être envisageable sur le risque de change d’une créance intragroupe reconnue seulement via l’exception visant les postes monétaires intragroupe dont les écarts de change ne sont pas totalement éliminés. En revanche, le modèle de cash flow hedge n’est pas le bon dès lors qu’une créance est déjà reconnue.

## Points Opérationnels

   - Le point clé de timing est la reconnaissance de la créance: avant reconnaissance, on raisonnerait sur une transaction prévue; après reconnaissance, sur un poste monétaire.
   - En consolidation, il faut vérifier que l’exposition de change subsiste malgré l’élimination intragroupe, ce qui suppose des monnaies fonctionnelles différentes.
   - La base IFRS fournie soutient surtout l’éligibilité de l’élément couvert en consolidation; la documentation devra rester alignée sur cette exception étroite.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un poste monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- le risque de change génère des écarts non totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un poste monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - le risque de change génère des écarts non totalement éliminés en consolidation

**Raisonnment**:
Dans cette situation, l’élément visé est une créance déjà comptabilisée, donc la famille pertinente est celle d’un actif reconnu. En consolidation, les transactions intragroupe sont en principe exclues des éléments couverts, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés. Cela peut donc permettre une documentation de couverture sur la composante change de la créance de dividende reconnue.

**Implications pratiques**: La documentation doit viser la composante change de la créance intragroupe reconnue, et non le dividende comme flux futur abstrait.

**Référence**:
 - 6.3.5
    >not in the consolidated financial statements of the group
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - B86(c)
    >eliminate in full intragroup assets and liabilities

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise les transactions prévues, alors que la question précise qu’une créance a déjà été reconnue. À ce stade, on n’est plus face à un flux futur hautement probable mais à un actif intragroupe comptabilisé. En consolidation, IFRS 9 n’ouvre une exception explicite pour l’intragroupe qu’aux postes monétaires intragroupe et à certaines transactions intragroupe hautement probables; ici le fait déclencheur est précisément la reconnaissance de la créance.

**Implications pratiques**: Une fois la créance de dividende comptabilisée, il ne faut pas documenter la relation comme une couverture de flux de trésorerie.

**Référence**:
 - 6.3.1
    >a forecast transaction
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item