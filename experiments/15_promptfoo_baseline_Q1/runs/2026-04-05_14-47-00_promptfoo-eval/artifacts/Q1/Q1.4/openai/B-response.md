# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur des états financiers consolidés soumis à IFRS 9.
   - Le dividende intragroupe et la créance correspondante sont libellés dans une devise étrangère.
   - La créance/dividende intragroupe existe entre des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui en consolidation si, une fois la créance de dividende reconnue, elle constitue un élément monétaire intragroupe dont le risque de change génère des écarts non entièrement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point de départ pertinent est la date de reconnaissance de la créance de dividende, pas la simple intention de distribuer.
   - En consolidation, il faut démontrer que l’écart de change sur la créance/dette intragroupe n’est pas entièrement éliminé, ce qui suppose des monnaies fonctionnelles différentes entre les entités concernées.
   - La documentation de couverture doit viser explicitement le risque de change de la créance intragroupe reconnue et satisfaire aux exigences formelles d’IFRS 9 sur la désignation et l’efficacité.
   - Si le dividende n’a pas encore donné lieu à une créance reconnue, la qualification en cash flow hedge intragroupe n’est pas étayée ici par les textes fournis.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change sur cette créance génère des gains ou pertes non entièrement éliminés en consolidation.<br>- Les entités concernées ont des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change sur cette créance génère des gains ou pertes non entièrement éliminés en consolidation.
   - Les entités concernées ont des monnaies fonctionnelles différentes.

**Raisonnment**:
Dans cette situation, la créance de dividende déjà reconnue est un actif comptabilisé. IFRS 9 permet, par exception en consolidation, de désigner le risque de change d’un élément monétaire intragroupe s’il crée des écarts de change non totalement éliminés. Cela correspond au modèle de couverture d’un actif reconnu pour un risque pouvant affecter le résultat.

**Implications pratiques**: La documentation peut être mise en place à partir de la reconnaissance de la créance, en visant son risque de change dans les comptes consolidés.

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
Ici, le fait générateur visé est un dividende intragroupe déjà constaté en créance, non une transaction future hautement probable. En consolidation, l’exception IFRS 9 pour transactions intragroupe futures vise seulement les risques de change qui affecteront le résultat consolidé; le texte cite comme non qualifiantes des flux intragroupe de type redevances, intérêts ou management fees, sauf lien avec une transaction externe. Le dividende intragroupe ne ressort pas comme un flux futur éligible dans ce cas.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une cash flow hedge du dividende intragroupe dans ce scénario.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise la composante change d’un dividende intragroupe et la créance correspondante, pas le risque de change d’un investissement net dans une activité à l’étranger. IFRIC 16 réserve ce modèle à la couverture du risque de change lié aux net assets d’une opération étrangère inclus dans les états financiers.

**Implications pratiques**: Le dividende intragroupe à recevoir ne doit pas être documenté comme hedge de net investment.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations