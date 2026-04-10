# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question porte sur l’application de la comptabilité de couverture selon IFRS 9 dans des comptes consolidés.
   - La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - La créance à recevoir est déjà comptabilisée à la date de désignation envisagée.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, une documentation de couverture peut viser le risque de change d’une créance intragroupe déjà comptabilisée si ce risque génère des écarts de change non totalement éliminés en consolidation. En revanche, dans cette situation, la voie pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie.

## Points Opérationnels

   - Le point clé est le niveau de reporting : l’analyse doit être faite en comptes consolidés, pas dans les comptes individuels.
   - Le moment de la désignation est déterminant : une fois la créance comptabilisée, on parle d’un élément reconnu et non d’une transaction future.
   - Il faut vérifier que le dividende intragroupe crée bien un élément monétaire en devise donnant lieu à des écarts de change non entièrement éliminés en consolidation.
   - La documentation de couverture doit être calibrée sur le seul risque de change couvert de la créance intragroupe concernée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé au risque de change.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.<br>- La désignation doit être faite dans les comptes consolidés sur l’élément reconnu concerné. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé au risque de change.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.
   - La désignation doit être faite dans les comptes consolidés sur l’élément reconnu concerné.

**Raisonnment**:
Dans votre situation, il existe une créance de dividende intragroupe déjà comptabilisée : c’est donc un élément reconnu pouvant servir d’élément couvert. En comptes consolidés, IFRS 9 admet par exception qu’un élément monétaire intragroupe soit couvert pour le risque de change si ce risque crée des écarts de change qui ne sont pas entièrement éliminés en consolidation. Cela peut donc s’appliquer à la créance de dividende, sous cette condition de risque résiduel en consolidation.

**Implications pratiques**: Si ces conditions sont remplies, la documentation de couverture peut viser le risque de change de la créance de dividende déjà comptabilisée au niveau consolidé.

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
Cette approche vise des transactions prévues hautement probables. Or, dans votre cas, la créance de dividende intragroupe est déjà comptabilisée : on n’est plus au stade d’une transaction future prévue mais d’un actif reconnu. La couverture de flux de trésorerie n’est donc pas la bonne qualification pour cette situation précise.

**Implications pratiques**: Une documentation en cash flow hedge ne convient pas pour une créance de dividende déjà enregistrée.

**Référence**:
 - 6.3.1
    >The hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.5
    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements ... not in the consolidated financial statements