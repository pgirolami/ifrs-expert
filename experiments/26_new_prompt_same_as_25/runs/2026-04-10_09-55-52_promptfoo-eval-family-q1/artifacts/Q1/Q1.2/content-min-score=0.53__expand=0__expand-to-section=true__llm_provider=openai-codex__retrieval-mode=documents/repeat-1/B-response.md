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
   - La question vise le risque de change, dans les comptes consolidés, sur un dividende intragroupe libellé dans une devise générant des écarts de change.
   - Le dividende intragroupe a déjà été comptabilisé en créance ; il ne s'agit donc plus, à la date considérée, d'une transaction intragroupe future.
   - La créance de dividende est un élément monétaire intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, une documentation de couverture en comptes consolidés peut viser la partie change via une couverture de juste valeur de la créance intragroupe, si le risque de change n'est pas totalement éliminé en consolidation. En revanche, la couverture de flux de trésorerie ne convient pas pour une créance déjà comptabilisée.

## Points Opérationnels

   - Le point déterminant est le timing : une fois le dividende comptabilisé en créance, l'analyse se fait sur un élément monétaire reconnu, pas sur une transaction future.
   - En consolidation, la possibilité de couvrir un poste intragroupe est une exception limitée au risque de change ; il faut donc bien circonscrire la documentation à cette composante.
   - Il faut vérifier que l'exposition de change sur la créance n'est pas entièrement éliminée en consolidation, notamment lorsque les entités du groupe ont des monnaies fonctionnelles différentes.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est libellée dans une devise exposant le groupe à des écarts de change en consolidation.<br>- Les gains et pertes de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est libellée dans une devise exposant le groupe à des écarts de change en consolidation.
   - Les gains et pertes de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Ici, le dividende intragroupe a déjà été enregistré en créance : on est donc face à un élément monétaire intragroupe reconnu. Le contexte IFRS 9 prévoit qu'en comptes consolidés, le risque de change d'un élément monétaire intragroupe peut être désigné comme élément couvert, mais seulement s'il crée des écarts de change qui ne sont pas totalement éliminés en consolidation.

**Implications pratiques**: La documentation peut porter sur le risque de change de la créance de dividende déjà reconnue dans les comptes consolidés.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette voie vise une transaction intragroupe future hautement probable. Or, dans votre cas, le dividende intragroupe a déjà été comptabilisé en créance : l'exposition n'est plus celle d'un flux futur à documenter avant reconnaissance, mais celle d'un poste monétaire déjà reconnu.

**Implications pratiques**: Cette documentation ne correspond pas au stade actuel du dividende, déjà enregistré en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item