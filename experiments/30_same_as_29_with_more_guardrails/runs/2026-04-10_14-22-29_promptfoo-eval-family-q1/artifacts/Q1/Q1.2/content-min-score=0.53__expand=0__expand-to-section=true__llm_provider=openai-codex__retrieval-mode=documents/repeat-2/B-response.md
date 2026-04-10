# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - Le dividende intragroupe est libellé dans une devise différente de la devise fonctionnelle d'au moins une des entités concernées.
   - La créance de dividende est déjà comptabilisée à la date d'analyse dans les comptes individuels et est éliminée en consolidation.
   - La question vise la comptabilité de couverture dans les comptes consolidés, et non les comptes individuels.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie la plus pertinente est la fair value hedge, mais seulement si la créance intragroupe expose le groupe à un risque de change qui n'est pas totalement éliminé en consolidation. La cash flow hedge ne correspond en principe pas à une créance déjà comptabilisée, et la net investment hedge ne vise pas la partie change de ce dividende en tant que tel.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si la créance de dividende est un élément monétaire intragroupe dont le risque de change subsiste au niveau du groupe.
   - La temporalité est clé : avant comptabilisation, une logique de transaction future pourrait être envisagée ; après comptabilisation en créance, l'analyse bascule vers un élément reconnu.
   - La documentation de couverture doit être posée au niveau consolidé en cohérence avec la devise fonctionnelle retenue pour mesurer le risque couvert.
   - Si les écarts de change sont intégralement éliminés en consolidation, la justification d'un hedged item au niveau du groupe devient insuffisante.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un élément monétaire intragroupe exposé au change.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation du fait de devises fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un élément monétaire intragroupe exposé au change.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation du fait de devises fonctionnelles différentes.

**Raisonnment**:
La créance de dividende est un élément reconnu, ce qui cadre avec un hedged item de type actif reconnu. En consolidation, les éléments intragroupe ne sont en principe pas éligibles, sauf pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Donc cette approche peut s'appliquer ici si la créance de dividende a bien cette nature et cet effet en consolidation.

**Implications pratiques**: La documentation devrait viser le risque de change de la créance intragroupe reconnue au niveau consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise notamment une transaction future hautement probable. Or, dans votre cas, le dividende intragroupe a déjà été comptabilisé en créance : on n'est plus au stade d'un flux futur non reconnu, mais d'un actif reconnu. L'exception IFRS 9 pour les transactions intragroupe hautement probables ne répond donc pas au fait décrit.

**Implications pratiques**: Cette documentation n'est en principe pas adaptée une fois la créance de dividende déjà reconnue.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La net investment hedge est un modèle distinct pour couvrir le risque de change d'un investissement net dans une activité à l'étranger. Votre question porte sur la partie change d'un dividende intragroupe déjà comptabilisé en créance, pas sur l'investissement net lui-même. Sur les faits donnés, cette désignation ne cible pas l'objet couvert pertinent.

**Implications pratiques**: Ce modèle ne traite pas directement la créance de dividende intragroupe comme élément couvert.

**Référence**:
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation
 - 6.3.1
    >a net investment in a foreign operation