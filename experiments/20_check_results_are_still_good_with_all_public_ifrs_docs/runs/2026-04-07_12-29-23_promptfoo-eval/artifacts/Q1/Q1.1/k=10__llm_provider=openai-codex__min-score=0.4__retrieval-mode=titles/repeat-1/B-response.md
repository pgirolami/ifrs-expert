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
   - La créance de dividende intragroupe et la dette correspondante sont libellées dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance/dette, de sorte qu’il ne s’agit plus d’une transaction future simplement prévue.
   - En consolidation, la question vise uniquement la composante de risque de change et suppose qu’un instrument de couverture externe au groupe peut être désigné.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la documentation de couverture peut être appliquée en consolidation principalement via une couverture de juste valeur du risque de change, sous réserve que la créance intragroupe soit un poste monétaire dont l’écart de change n’est pas totalement éliminé en consolidation. La couverture de flux de trésorerie n’est pas adaptée ici, et la couverture d’investissement net ne viserait pas la créance de dividende elle-même.

## Points Opérationnels

   - En consolidation, il faut d’abord vérifier si la créance de dividende intragroupe est bien un poste monétaire générant un écart de change non totalement éliminé.
   - La documentation doit être mise en place selon IFRS 9 avec désignation explicite du risque couvert, de l’instrument de couverture et de la méthode d’évaluation de l’efficacité.
   - Si le dividende a été déclaré après la clôture, IAS 10 indique qu’il n’est pas comptabilisé en dette à la date de clôture ; l’analyse de couverture ne serait alors pas la même.
   - La couverture d’investissement net doit rester réservée aux expositions de conversion liées à l’investissement net dans l’activité étrangère, et non aux dividendes intragroupe à recevoir.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un poste monétaire intragroupe.<br>- Le risque de change sur ce poste doit affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminé en consolidation.<br>- La relation de couverture doit satisfaire aux conditions formelles de désignation et de documentation IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe.
   - Le risque de change sur ce poste doit affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminé en consolidation.
   - La relation de couverture doit satisfaire aux conditions formelles de désignation et de documentation IFRS 9.

**Raisonnment**:
Dans les comptes consolidés, un poste intragroupe n’est en principe pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Une créance de dividende déjà comptabilisée est un actif reconnu ; la couverture de juste valeur est donc la voie IFRS pertinente pour ce risque spécifique dans ce cas.

**Implications pratiques**: La variation de change de l’instrument de couverture et celle de la créance au titre du risque couvert seraient reconnues en résultat consolidé selon la mécanique de la couverture de juste valeur.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 32
    >such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance : le sujet n’est plus une transaction future hautement probable mais un poste monétaire existant. Le risque porte alors sur la réévaluation de la créance en devise, ce qui correspond à une logique de juste valeur/réévaluation en résultat plutôt qu’à une variabilité de flux futurs à couvrir.

**Implications pratiques**: Cette approche n’est pas adaptée pour documenter le change d’une créance de dividende intragroupe déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.
 - 28
    >Exchange differences arising on the settlement of monetary items or on translating monetary items ... shall be recognised in profit or loss

### 3. Couverture d’investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette méthode vise le risque de change sur un investissement net dans une activité à l’étranger, non sur une créance de dividende déclarée et comptabilisée. Le dividende intragroupe traduit en pratique une intention de règlement/distribution ; il ne constitue donc pas, dans les faits décrits, l’élément de couverture d’un investissement net au sens IFRS.

**Implications pratiques**: La créance de dividende ne doit pas être documentée comme couverture d’investissement net ; ce modèle concerne l’investissement net lui-même.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity