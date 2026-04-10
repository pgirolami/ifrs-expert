# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifric17`
   - `ifrs9`
   - `ifrs18`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic25`
   - `ifric16`
   - `sic29`
   - `ifric19`

## Hypothèses
   - La question vise les comptes consolidés IFRS.
   - La créance de dividende intragroupe est déjà comptabilisée et libellée dans une devise pouvant générer un risque de change.
   - La relation de couverture envisagée porte uniquement sur le risque de change de cette créance intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture n’est envisageable ici que via le modèle de couverture d’un élément monétaire intragroupe reconnu, si le risque de change n’est pas entièrement éliminé en consolidation. En revanche, la couverture de flux futurs de dividendes intragroupe et la couverture d’investissement net ne correspondent pas à cette situation.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que la créance de dividende constitue bien un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé.
   - Si la créance est déjà reconnue, l’analyse doit se faire comme couverture d’un élément existant, pas comme couverture d’une transaction future.
   - La documentation doit circonscrire la relation au seul risque de change sur le solde intragroupe concerné.
   - Les dividendes, en tant que distributions aux propriétaires, relèvent par nature de l’equity/presentation et ne soutiennent pas à eux seuls un modèle de cash flow hedge en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un élément monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un élément monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation

**Raisonnment**:
La créance de dividende déjà comptabilisée est un élément reconnu, ce qui correspond au modèle de couverture d’un actif/passif existant. En consolidation, un élément intragroupe est en principe exclu, sauf pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Donc cela peut s’appliquer ici, mais seulement dans ce cas précis.

**Implications pratiques**: Possible en consolidation uniquement en ciblant le risque de change résiduel de la créance intragroupe reconnue.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise notamment une transaction future hautement probable. Or votre fait générateur est un dividende intragroupe déjà comptabilisé en créance, donc on n’est plus sur un flux futur non reconnu. En outre, l’exception intragroupe en consolidation exige que le risque de change affecte le résultat consolidé, ce qui n’est pas la logique d’un dividende intragroupe.

**Implications pratiques**: Ce n’est pas le bon modèle pour une créance de dividende déjà reconnue en comptes consolidés.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >a highly probable forecast intragroup transaction may qualify ... and the foreign currency risk will affect consolidated profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net vise l’exposition de change sur les net assets d’une activité étrangère. Votre question porte sur une créance de dividende intragroupe déjà comptabilisée, donc sur un solde intragroupe spécifique et non sur l’investissement net dans l’entité étrangère. Ce modèle ne correspond donc pas à la situation décrite.

**Implications pratiques**: Ne pas documenter cette créance de dividende comme couverture d’investissement net.

**Référence**:
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity