# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance sur dividendes est une créance intragroupe libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - La question vise les comptes consolidés et l’exposition de change provient de cette créance intragroupe elle-même, non d’un investissement net dans une activité étrangère.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une exposition de change sur une créance intragroupe n’est éligible que par exception pour le risque de change d’un élément monétaire intragroupe qui n’est pas totalement éliminé en consolidation. Dans ce cas, la couverture peut être envisagée; sinon, non.

## Points Opérationnels

   - Le point décisif est de vérifier si les écarts de change sur la créance de dividendes intragroupe subsistent en résultat consolidé après éliminations.
   - Si l’exposition est totalement éliminée en consolidation, aucun des modèles de couverture fondés sur cette créance ne s’applique au niveau consolidé.
   - Si l’exposition subsiste, la relation de couverture doit être formellement désignée et documentée dès l’origine selon IFRS 9 6.4.1.
   - La qualification en couverture d’investissement net doit être écartée sauf si l’élément couvert est effectivement un montant de net assets d’une activité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance sur dividendes doit constituer un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance sur dividendes doit être un élément monétaire intragroupe exposé au risque de change.<br>- Le risque de change doit affecter le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance sur dividendes doit constituer un élément monétaire intragroupe.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance sur dividendes est un actif reconnu, donc la mécanique de couverture de juste valeur peut viser son risque de change. Mais au niveau consolidé, un poste intragroupe n’est éligible que si, en tant qu’élément monétaire intragroupe, il crée des écarts de change non totalement éliminés en consolidation.

**Implications pratiques**: Il faut démontrer que l’exposition de change subsiste réellement dans le résultat consolidé malgré les éliminations intragroupe.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance sur dividendes doit être un élément monétaire intragroupe exposé au risque de change.
   - Le risque de change doit affecter le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation.

**Raisonnment**:
Le modèle de couverture de flux peut viser la variabilité de flux d’un actif reconnu attribuable à un risque particulier. Pour cette créance intragroupe, cela n’est recevable au niveau consolidé que dans le cadre de l’exception IFRS 9 sur le risque de change d’un élément monétaire intragroupe non totalement éliminé.

**Implications pratiques**: La documentation doit relier la variabilité des flux en monnaie fonctionnelle au risque de change restant dans les comptes consolidés.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability
 - B6.3.4
    >provided that ... the foreign currency risk will affect consolidated profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, l’exposition identifiée provient d’une créance sur dividendes intragroupe, donc d’un solde intragroupe distinct. Le modèle de couverture d’investissement net vise le risque de change attaché à un montant de net assets d’une activité étrangère, pas une créance de dividendes.

**Implications pratiques**: Cette exposition ne doit pas être documentée comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 1
    >The item being hedged ... may be an amount of net assets
 - ifric-16 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation