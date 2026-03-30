# Analyse d'une question comptable

**Date**: 2026-03-30

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question vise les comptes consolidés.
   - Les dividendes intragroupe ont donné lieu à la comptabilisation d'une créance/dette intragroupe monétaire libellée en devise.
   - La question porte sur la possibilité d'appliquer la comptabilité de couverture IFRS 9 à ce risque de change en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la couverture de flux de trésorerie n'est pas disponible car les dividendes intragroupe n'affectent généralement pas le résultat consolidé. Une couverture de juste valeur pourrait seulement être envisageable si la créance monétaire intragroupe crée des écarts de change non totalement éliminés en consolidation.

## Points Opérationnels

   - Le point clé est de distinguer le dividende intragroupe en tant que flux intragroupe du poste monétaire de créance/dette une fois comptabilisé.
   - Si vous visez la créance comptabilisée, documentez uniquement le risque de change du poste monétaire intragroupe et démontrez qu'il n'est pas totalement éliminé en consolidation.
   - La documentation doit être formalisée dès l'origine de la relation de couverture avec identification de l'instrument, de l'élément couvert, du risque couvert et du test d'efficacité.
   - En pratique, pour des dividendes intragroupe, la réponse est donc non comme couverture des flux intragroupe; éventuellement oui sous conditions seulement comme fair value hedge du poste monétaire reconnu.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe est un poste monétaire reconnu.<br>- Le risque de change génère des écarts de change non totalement éliminés en consolidation.<br>- La relation de couverture satisfait aux critères de documentation et d'efficacité d'IFRS 9. |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En consolidation, IFRS 9 n'admet les transactions intragroupe comme élément couvert que par exception pour certains risques de change, à condition qu'ils affectent le résultat consolidé. Le texte précise que c'est généralement exclu pour les dividendes, comme pour les redevances, intérêts ou management fees entre sociétés du groupe.

**Implications pratiques**: Vous ne pouvez pas documenter en cash flow hedge le change sur des dividendes intragroupe dans les comptes consolidés.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe est un poste monétaire reconnu.
   - Le risque de change génère des écarts de change non totalement éliminés en consolidation.
   - La relation de couverture satisfait aux critères de documentation et d'efficacité d'IFRS 9.

**Raisonnment**:
La créance à recevoir comptabilisée est, selon l'hypothèse, un poste monétaire intragroupe reconnu. IFRS 9 permet en consolidation, par exception, de désigner le risque de change d'un poste monétaire intragroupe comme élément couvert si les gains/pertes de change ne sont pas totalement éliminés selon IAS 21, notamment entre entités ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: Une documentation de fair value hedge peut être envisagée seulement si la créance de dividende crée un vrai risque de change résiduel au niveau consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 3. Couverture d'un investissement net à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change sur un investissement net dans une activité étrangère, c'est-à-dire sur des actifs nets de l'opération étrangère. Une créance de dividende intragroupe comptabilisée n'est pas, dans les faits décrits, un investissement net mais un poste monétaire distinct.

**Implications pratiques**: Cette voie n'est pas adaptée à une créance de dividende intragroupe déjà comptabilisée.

**Référence**:
 - 1162
    >the item being hedged ... may be an amount of net assets
 - 1170
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 1171
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Si les conditions de l'exception relative aux postes monétaires intragroupe ne sont pas remplies, la solution IFRS 9 en consolidation est l'absence de hedge accounting. C'est aussi la conclusion pour une tentative de couverture des dividendes intragroupe en tant que flux intragroupe, qui ne qualifie pas ici.

**Implications pratiques**: À défaut de qualification en fair value hedge sur le poste monétaire, les écarts de change suivent leur traitement normal sans documentation de couverture.

**Référence**:
 - 6.3.5
    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements
 - 6.3.6
    >However, as an exception to paragraph 6.3.5
