# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ias24`
   - `ifrs9`
   - `ifric17`
   - `ifrs19`
   - `ifric16`
   - `ifrs12`
   - `ifrs18`
   - `ifric1`
   - `ias27`
   - `sic25`
   - `ias37`
   - `ifric19`
   - `ifric21`
   - `sic29`
   - `ias26`

## Hypothèses
   - La créance de dividendes et la dette correspondante naissent entre entités d’un même groupe consolidé.
   - L’exposition visée est un risque de change sur un solde intragroupe identifié dans l’analyse de consolidation.
   - Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur cet élément monétaire ne sont pas intégralement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une exposition de change sur une créance de dividendes intragroupe n’est éligible que si elle correspond à un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés. Dans ce cas, la voie pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’un investissement net.

## Points Opérationnels

   - Vérifier d’abord si la créance/dette sur dividendes est bien un élément monétaire intragroupe et si les monnaies fonctionnelles diffèrent.
   - Confirmer que les écarts de change sur ce solde affectent effectivement le résultat consolidé et ne sont pas entièrement éliminés à la consolidation.
   - Ne pas confondre cette exposition distincte sur dividende déclaré avec le risque de change sur l’investissement net dans l’opération étrangère.
   - En consolidation, l’élimination des soldes intragroupe n’empêche pas, par exception, l’éligibilité du seul risque de change sur un élément monétaire intragroupe lorsque IFRS 9.6.3.6 est satisfait.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette sur dividendes constitue un élément monétaire intragroupe.<br>- Les écarts de change sur cet élément ne sont pas entièrement éliminés en consolidation.<br>- Le risque couvert est bien le risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette sur dividendes constitue un élément monétaire intragroupe.
   - Les écarts de change sur cet élément ne sont pas entièrement éliminés en consolidation.
   - Le risque couvert est bien le risque de change affectant le résultat consolidé.

**Raisonnment**:
Dans cette situation, la créance sur dividendes est un poste reconnu et l’exposition identifiée est un risque de change sur un solde intragroupe. IFRS 9 admet, en consolidation, l’éligibilité du risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés ; cela cadre avec une couverture d’un actif/passif reconnu affectant le résultat.

**Implications pratiques**: La documentation de couverture doit viser le risque de change sur la créance intragroupe reconnue, au niveau des comptes consolidés.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 4
    >Intragroup related party transactions and outstanding balances are eliminated

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis réservent explicitement l’exception intragroupe, en consolidation, aux éléments monétaires intragroupe et à certaines transactions intragroupe hautement probables en devise. Ici, la question porte sur une créance de dividendes déjà comptabilisée, donc sur un solde reconnu distinct, et non sur une transaction future hautement probable.

**Implications pratiques**: La créance sur dividendes reconnue ne doit pas être traitée comme une couverture de flux de trésorerie dans ce cas.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une exposition de change distincte née de la comptabilisation d’une créance de dividendes intragroupe. Or la couverture d’investissement net vise le risque de change sur les actifs nets d’une opération étrangère ; une créance de dividendes reconnue séparément n’est pas, dans ce cas, l’investissement net lui-même.

**Implications pratiques**: Il ne faut pas documenter cette créance sur dividendes comme instrument ou élément couvert d’une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency