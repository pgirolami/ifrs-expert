# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance de dividende est un élément monétaire intragroupe reconnu, libellé en devise étrangère.
   - La question porte sur l'éligibilité de cette exposition comme élément couvert dans les comptes consolidés au titre d'IFRS 9.
   - L'exposition de change sur cette créance affecte les comptes consolidés, donc les écarts de change ne sont pas entièrement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, l'exposition de change sur une créance intragroupe reconnue peut être désignée comme élément couvert si, dans ce cas précis, les écarts de change ne sont pas entièrement éliminés à la consolidation. Le fondement est l'exception IFRS 9 pour le risque de change des éléments monétaires intragroupe.

## Points Opérationnels

   - En comptes consolidés, la règle de base exclut les éléments intragroupe; il faut donc documenter précisément pourquoi l'exception de l'élément monétaire intragroupe s'applique.
   - La documentation initiale doit identifier l'instrument de couverture, la créance de dividende, le risque de change couvert et la méthode d'évaluation de l'efficacité.
   - Le point décisif est de démontrer que les écarts de change sur la créance affectent bien le résultat consolidé et ne sont pas entièrement éliminés lors de la consolidation.
   - Le modèle de couverture d'investissement net doit être écarté car il ne vise pas une créance de dividende intragroupe reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit constituer un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne doivent pas être entièrement éliminés en consolidation.<br>- Le risque couvert doit être le risque de change pouvant affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité couverte doit être celle des flux de trésorerie liée au risque de change de la créance reconnue.<br>- Les écarts de change doivent affecter le résultat consolidé et ne pas être entièrement éliminés.<br>- La relation de couverture doit être formellement documentée à l'origine. |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit constituer un élément monétaire intragroupe.
   - Les écarts de change correspondants ne doivent pas être entièrement éliminés en consolidation.
   - Le risque couvert doit être le risque de change pouvant affecter le résultat consolidé.

**Raisonnment**:
La créance de dividende est un actif reconnu, ce qui entre dans le périmètre d'une couverture de juste valeur. En consolidation, un élément intragroupe n'est normalement pas éligible, sauf exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés. Si c'est bien le cas ici, cette exposition peut être désignée comme élément couvert.

**Implications pratiques**: Le groupe peut documenter une relation de couverture de juste valeur sur le risque de change de la créance, sous réserve de démontrer l'effet en résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité couverte doit être celle des flux de trésorerie liée au risque de change de la créance reconnue.
   - Les écarts de change doivent affecter le résultat consolidé et ne pas être entièrement éliminés.
   - La relation de couverture doit être formellement documentée à l'origine.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie d'un actif reconnu pour un risque particulier. Dans cette situation, la créance de dividende reconnue expose le groupe à une variabilité des flux en monnaie fonctionnelle liée au change. Toutefois, l'éligibilité en consolidation repose toujours sur l'exception visant le risque de change d'un élément monétaire intragroupe non entièrement éliminé.

**Implications pratiques**: Une désignation en cash flow hedge est envisageable si le groupe documente la variabilité des encaissements futurs en devise fonctionnelle liée au change.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >at the inception ... there is formal designation and documentation

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite concerne une créance de dividende intragroupe reconnue, et non un investissement net dans une activité à l'étranger. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change sur un investissement net dans une activité étrangère. Ce traitement ne correspond donc pas au fait générateur décrit.

**Implications pratiques**: Le groupe ne doit pas retenir le modèle de couverture d'investissement net pour une créance de dividende intragroupe.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations