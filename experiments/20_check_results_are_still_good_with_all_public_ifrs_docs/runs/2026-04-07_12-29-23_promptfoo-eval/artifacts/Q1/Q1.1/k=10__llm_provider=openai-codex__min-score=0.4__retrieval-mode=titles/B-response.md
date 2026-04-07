# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ifric17`
   - `ifrs18`
   - `ifrs2`
   - `ifrs10`
   - `ifric5`
   - `ias8`
   - `ias32`
   - `ifrs11`
   - `ias7`
   - `ifrs19`
   - `ifrs17`
   - `ifrs9`
   - `ifrs8`
   - `ias19`
   - `ifrs3`
   - `ifrs7`
   - `ias37`
   - `ias10`
   - `ias29`
   - `ifrs1`
   - `ifrs13`
   - `ias28`
   - `ias27`
   - `ias26`
   - `ias12`
   - `ias39`
   - `ias34`
   - `ifrs16`
   - `ifrs15`
   - `ps1`
   - `ias36`
   - `ias23`
   - `ifrs5`
   - `ifric23`
   - `ias20`
   - `ps2`
   - `ifrs14`
   - `ifrs6`
   - `ias38`
   - `ias33`
   - `ias21`
   - `ifrs12`
   - `ias40`
   - `ifric2`
   - `ias2`
   - `ias24`
   - `ifric14`
   - `ifric16`
   - `ifric12`
   - `ifric20`
   - `ias16`
   - `ias41`
   - `ifric19`
   - `ifric10`
   - `ifric22`
   - `ifric21`
   - `ifric7`
   - `ifric6`
   - `ifric1`

## Hypothèses
   - Le dividende intragroupe a été déclaré et comptabilisé en créance, donc il existe une position monétaire intragroupe exposée au change.
   - Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur cette créance/dette intragroupe ne sont pas intégralement éliminés en consolidation.
   - La question vise les comptes consolidés IFRS et la possibilité de documenter une couverture de change sur cette position.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture de change est envisageable sur une créance de dividende intragroupe seulement si cette créance est un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé. Dans ce cas, une documentation de fair value hedge ou de cash flow hedge peut être envisagée ; la net investment hedge n’est pertinente que si la position relève d’un investissement net dans une activité étrangère.

## Points Opérationnels

   - En consolidation, vérifier d’abord que la créance de dividende est bien un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes.
   - Si les écarts de change sur la créance/dette sont totalement éliminés en consolidation, il n’y a pas d’élément couvert éligible sur lequel documenter la couverture.
   - La documentation doit identifier le risque de change couvert, l’instrument de couverture, la méthode d’efficacité et le traitement retenu (fair value hedge ou cash flow hedge).
   - Le dividende lui-même reste une transaction entre propriétaires présentée en capitaux propres ; le sujet ici porte uniquement sur la composante change de la créance/dette intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe.<br>- Les écarts de change doivent ne pas être totalement éliminés en consolidation.<br>- La relation de couverture doit satisfaire aux critères de désignation et d’efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit être libellée dans une devise étrangère par rapport à la monnaie fonctionnelle de l’entité qui la porte.<br>- Les écarts de change doivent pouvoir affecter le résultat consolidé.<br>- Les critères de hedge accounting d’IFRS 9 doivent être remplis. |
| 3. Couverture d’un investissement net dans une activité étrangère | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe.
   - Les écarts de change doivent ne pas être totalement éliminés en consolidation.
   - La relation de couverture doit satisfaire aux critères de désignation et d’efficacité d’IFRS 9.

**Raisonnment**:
Dans cette situation, la créance de dividende intragroupe est une position reconnue et exposée au change. En comptes consolidés, un poste monétaire intragroupe peut être désigné comme élément couvert si les écarts de change ne sont pas totalement éliminés ; la couverture de juste valeur est donc possible sur ce risque spécifique, sous réserve de la documentation IFRS 9.

**Implications pratiques**: La variation de valeur du dérivé et la variation de la créance attribuable au risque de change seraient comptabilisées en résultat selon le modèle de fair value hedge.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.5.8
    >the gain or loss on the hedging instrument shall be recognised in profit or loss

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être libellée dans une devise étrangère par rapport à la monnaie fonctionnelle de l’entité qui la porte.
   - Les écarts de change doivent pouvoir affecter le résultat consolidé.
   - Les critères de hedge accounting d’IFRS 9 doivent être remplis.

**Raisonnment**:
La créance de dividende en devise génère des flux futurs dont la contre-valeur dans la monnaie fonctionnelle varie avec le change. Dès lors que le poste monétaire intragroupe qualifie en consolidation et que le risque de change affecte le résultat, une documentation de cash flow hedge peut aussi être envisagée dans ce cas précis.

**Implications pratiques**: La part efficace de la couverture serait comptabilisée en autres éléments du résultat global puis recyclée selon les règles IFRS 9 applicables.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.11
    >the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge ... shall be recognised in other comprehensive income

### 3. Couverture d’un investissement net dans une activité étrangère
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe ne correspond pas, dans les faits décrits, à la couverture d’un investissement net dans une activité étrangère. Cette approche vise le risque de conversion lié aux net assets d’une activité étrangère, non une créance de dividende née d’une distribution intragroupe.

**Implications pratiques**: Cette voie n’est pas la bonne pour documenter le change d’une créance de dividende intragroupe, sauf si la position relevait en substance d’un investissement net, ce qui n’est pas décrit ici.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity