# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric17`
   - `ifric2`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic7`

## Hypothèses
   - Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que la créance/dette monétaire génère des écarts de change dans les comptes consolidés.

## Recommandation

**OUI**

Dans cette situation, le risque de change sur la créance de dividende intragroupe peut être désigné dans une relation de couverture au niveau consolidé, car il s'agit d'un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Le modèle pertinent est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d'investissement net.

## Points Opérationnels

   - La possibilité de couverture existe au niveau des états financiers consolidés, pas parce que l'élément est intragroupe en soi, mais parce que les écarts de change sur l'élément monétaire subsistent en consolidation.
   - Le point décisif est le moment de déclaration du dividende : une fois la créance comptabilisée, l'analyse bascule vers un actif monétaire reconnu.
   - La documentation de couverture doit viser spécifiquement le risque de change de la créance de dividende intragroupe reconnue.
   - Le traitement de base reste IAS 21 ; la couverture IFRS 9 vient en surcouche si elle est formellement désignée et documentée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI | - La créance/dette de dividende doit constituer un élément monétaire intragroupe.<br>- Les écarts de change doivent affecter le résultat consolidé, donc ne pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation IAS 21 du change | OUI | - La créance/dette doit être un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes. |

### 1. Couverture de juste valeur
**Applicabilité**: OUI

**Conditions**:
   - La créance/dette de dividende doit constituer un élément monétaire intragroupe.
   - Les écarts de change doivent affecter le résultat consolidé, donc ne pas être totalement éliminés en consolidation.

**Raisonnment**:
Ici, le dividende déclaré a déjà donné naissance à une créance intragroupe comptabilisée, donc à un actif reconnu. IFRS 9 permet, en consolidation, qu'un élément monétaire intragroupe exposé à des écarts de change non totalement éliminés soit un élément couvert ; c'est précisément le cas décrit.

**Implications pratiques**: Une documentation formelle de couverture au niveau consolidé est possible sur le risque de change de la créance de dividende reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les hypothèses indiquent que le dividende intragroupe est déjà déclaré et comptabilisé en créance à recevoir. On n'est donc plus face à une transaction future hautement probable, mais à un poste monétaire déjà reconnu ; le modèle de couverture de flux de trésorerie ne correspond pas à ce fait précis.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir le risque de change d'une créance de dividende déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change d'un dividende intragroupe reconnu en créance, et non le risque de change attaché à un investissement net dans une activité à l'étranger. Le champ IFRIC 16/IFRS 9 relatif aux couvertures d'investissement net ne correspond donc pas à cette exposition spécifique.

**Implications pratiques**: Il ne faut pas documenter cette exposition comme une couverture d'investissement net.

**Référence**:
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 8
    >it should not be applied by analogy to other types of hedge accounting
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation

### 4. Comptabilisation IAS 21 du change
**Applicabilité**: OUI

**Conditions**:
   - La créance/dette doit être un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.

**Raisonnment**:
IAS 21 constitue ici le traitement de base de l'exposition : un poste monétaire intragroupe entre entités de monnaies fonctionnelles différentes génère des écarts de change visibles en consolidation. Cette base comptable explique précisément pourquoi l'élément peut ensuite être couvert au niveau consolidé.

**Implications pratiques**: À défaut de couverture, les écarts de change sur la créance de dividende sont comptabilisés selon IAS 21 dans les comptes consolidés.

**Référence**:
 - 45
    >such an exchange difference is recognised in profit or loss
 - 3
    >This Standard shall be applied ... in accounting for transactions and balances in foreign currencies
 - 6.3.6
    >if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation