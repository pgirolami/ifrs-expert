# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - La créance et la dette de dividende intragroupe sont libellées dans une devise étrangère.
   - Le dividende intragroupe, une fois comptabilisé en créance/dette, constitue un poste monétaire intragroupe.
   - La question porte sur les comptes consolidés IFRS et sur la possibilité de documenter une couverture du risque de change attaché à cette créance déjà comptabilisée.
   - Le risque de change sur ce poste monétaire n’est pas intégralement éliminé en consolidation et peut donc affecter le résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la couverture de juste valeur, sous réserve que la créance/dette de dividende soit bien un poste monétaire intragroupe dont l’effet de change affecte le résultat consolidé. La couverture de flux de trésorerie n’est pas adaptée à une créance déjà reconnue, et la couverture d’investissement net ne vise pas ce dividende en tant que tel.

## Points Opérationnels

   - En consolidation, le point clé est de démontrer que le dividende intragroupe constitue bien un poste monétaire intragroupe dont les écarts de change affectent le résultat consolidé.
   - La documentation de couverture doit être formalisée dès l’origine de la relation de couverture.
   - Si le dividende n’était qu’un flux intragroupe futur avant comptabilisation, la logique de couverture de flux de trésorerie pourrait être analysée ; ce n’est pas le cas ici selon les faits donnés.
   - La couverture d’investissement net doit être réservée au risque de change de l’investissement net dans l’entité étrangère, pas à la créance de dividende elle-même.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende comptabilisé doit constituer un poste monétaire intragroupe en devise.<br>- Les écarts de change sur ce poste doivent affecter le résultat consolidé.<br>- La relation de couverture doit satisfaire à la désignation et à la documentation IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité étrangère | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende comptabilisé doit constituer un poste monétaire intragroupe en devise.
   - Les écarts de change sur ce poste doivent affecter le résultat consolidé.
   - La relation de couverture doit satisfaire à la désignation et à la documentation IFRS 9.

**Raisonnment**:
Ici, le dividende intragroupe est déjà comptabilisé en créance/dette : on est donc face à un poste reconnu, et non à un flux futur. En consolidation, un poste monétaire intragroupe en devise peut rester exposé au change si les écarts ne sont pas totalement éliminés ; dans ce cas, la logique de couverture de juste valeur est la plus cohérente avec le fait générateur décrit.

**Implications pratiques**: La documentation doit viser le risque de change du poste reconnu et démontrer son effet en résultat consolidé.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une variabilité de flux de trésorerie sur un poste ou une transaction future hautement probable. Or, dans les faits donnés, le dividende a déjà été comptabilisé en créance : le sujet n’est plus un flux futur hautement probable, mais un poste monétaire reconnu exposé au change.

**Implications pratiques**: Cette voie ne convient pas pour couvrir la partie change d’une créance de dividende déjà enregistrée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’un investissement net dans une activité étrangère
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette documentation couvre le risque de change sur l’investissement net dans une activité étrangère, c’est-à-dire sur les actifs nets de l’opération étrangère. Le cas décrit porte sur une créance de dividende intragroupe déjà comptabilisée ; ce n’est pas, en tant que tel, l’objet d’une couverture d’investissement net.

**Implications pratiques**: Cette documentation ne cible pas la créance de dividende ; elle viserait l’investissement net dans l’entité étrangère.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation