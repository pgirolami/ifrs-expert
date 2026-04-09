# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs19`
   - `ias32`
   - `ifric17`
   - `ifrs17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ifrs9`
   - `ifric19`
   - `ias37`
   - `ifric16`

## Hypothèses
   - La question vise les comptes consolidés IFRS et une créance de dividende intragroupe déjà comptabilisée.
   - Seule la composante de risque de change est envisagée pour la relation de couverture.
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, une documentation de couverture est envisageable en consolidation principalement via une couverture de juste valeur de la composante change de la créance intragroupe. La couverture de flux de trésorerie n’est pas adaptée à une créance déjà reconnue, et la couverture d’investissement net ne s’applique que si l’exposition couverte est celle d’un investissement net dans une activité à l’étranger.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que les écarts de change sur la créance intragroupe affectent bien le résultat consolidé.
   - La documentation doit être mise en place sur la composante change du poste monétaire intragroupe, avec identification claire de l’instrument de couverture et du risque couvert.
   - Si le dividende n’était pas encore reconnu mais seulement prévu, l’analyse aurait pu être différente; ici, le fait qu’il soit déjà en créance oriente vers la couverture de juste valeur.
   - Il faut vérifier la cohérence entre la devise de la créance, les monnaies fonctionnelles des entités concernées et le traitement des écarts de change en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un poste monétaire exposé au risque de change.<br>- Les écarts de change sur ce poste doivent affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminés en consolidation.<br>- La documentation de couverture doit viser uniquement la composante change de la créance. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un poste monétaire exposé au risque de change.
   - Les écarts de change sur ce poste doivent affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminés en consolidation.
   - La documentation de couverture doit viser uniquement la composante change de la créance.

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance, donc il s’agit d’un actif reconnu. En consolidation, IFRS 9 permet de désigner le risque de change d’un poste monétaire intragroupe comme élément couvert s’il crée des écarts de change qui ne sont pas totalement éliminés en consolidation. Cette mécanique est cohérente avec une couverture de juste valeur d’un actif reconnu au titre du seul risque de change.

**Implications pratiques**: C’est l’approche la plus directement compatible avec une créance de dividende déjà reconnue en comptes consolidés.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite ne porte pas sur un flux futur hautement probable, mais sur un dividende déjà comptabilisé en créance. Une couverture de flux de trésorerie vise une variabilité de flux de trésorerie d’un élément reconnu ou d’une transaction future hautement probable. Ici, le fait générateur a déjà eu lieu et l’exposition est celle d’un poste monétaire reconnu.

**Implications pratiques**: Cette approche n’est pas appropriée une fois le dividende intragroupe reconnu en créance.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas présenté concerne la composante change d’une créance de dividende intragroupe, pas une exposition de change sur un investissement net dans une activité à l’étranger. La couverture d’investissement net répond à un autre objet économique et documentaire. En l’absence d’éléments montrant que le risque couvert est celui de l’investissement net lui-même, cette voie ne correspond pas à la situation décrite.

**Implications pratiques**: À défaut de viser formellement un investissement net dans une activité à l’étranger, cette documentation ne convient pas au dividende en créance.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.