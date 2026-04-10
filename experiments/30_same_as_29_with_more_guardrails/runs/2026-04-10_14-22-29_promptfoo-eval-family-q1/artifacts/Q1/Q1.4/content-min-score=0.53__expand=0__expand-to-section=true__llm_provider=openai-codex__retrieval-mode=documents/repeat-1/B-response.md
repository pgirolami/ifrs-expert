# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs10`
   - `ifrs12`
   - `ifrs19`
   - `ias24`
   - `ifrs9`
   - `ias7`
   - `ifric17`
   - `ias27`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric2`

## Hypothèses
   - La question vise des états financiers consolidés au sens d’IFRS 10.
   - Le dividende intragroupe a été déclaré et une créance/dette intragroupe a été comptabilisée dans les comptes individuels concernés.
   - La créance intragroupe est un élément monétaire libellé dans une devise qui génère un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation et affectent donc le résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, une désignation de couverture est possible si la créance de dividende reconnue constitue un élément monétaire intragroupe exposé à un risque de change non totalement éliminé et affectant le résultat consolidé. Dans ce cas, la voie pertinente est la couverture de juste valeur; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à cette situation.

## Points Opérationnels

   - Le point clé est le niveau de reporting: l’analyse doit être faite en consolidation, où les soldes intragroupe sont éliminés sauf effet de change non totalement neutralisé.
   - Le moment pertinent pour documenter la couverture est celui où la créance est reconnue, sous réserve que le risque de change subsiste dans le résultat consolidé.
   - Si la créance de dividende est dans la même monnaie fonctionnelle que les entités concernées, ou si les écarts de change sont intégralement éliminés, la désignation ne fonctionne pas.
   - La documentation doit viser la composante change du poste monétaire intragroupe reconnu, et non le dividende intragroupe en tant que tel.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe<br>- Le risque de change doit affecter le résultat consolidé car il n’est pas entièrement éliminé en consolidation<br>- La désignation est à apprécier au niveau consolidé, et non sur la seule base des comptes individuels |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe
   - Le risque de change doit affecter le résultat consolidé car il n’est pas entièrement éliminé en consolidation
   - La désignation est à apprécier au niveau consolidé, et non sur la seule base des comptes individuels

**Raisonnment**:
La situation porte sur une créance déjà reconnue, donc sur un poste monétaire existant et non sur un flux futur. En consolidation, les éléments intragroupe sont en principe éliminés, mais IFRS 9 admet l’exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Dans ce cas précis, la documentation de couverture peut viser cette composante change.

**Implications pratiques**: La documentation peut être mise en place à partir de la reconnaissance de la créance, si le risque de change subsiste au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - B86
    >eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows
 - 12
    >Dividends from a subsidiary ... are recognised ... when the entity’s right to receive the dividend is established

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe pour lequel une créance a déjà été reconnue. On n’est donc plus face à une transaction future hautement probable, qui est le terrain naturel du cash flow hedge, mais face à un poste reconnu. L’exception IFRS 9 sur les transactions intragroupe futures concerne des flux qui affecteront le résultat consolidé, pas une créance déjà constatée.

**Implications pratiques**: Le modèle de cash flow hedge n’est pas le bon véhicule une fois la créance de dividende déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question ne porte pas sur le risque de change d’un investissement net dans une opération étrangère, mais sur une créance de dividende intragroupe née après déclaration. IFRIC 16 réserve ce modèle aux couvertures de net investment en foreign operations. Il ne vise pas un dividende intragroupe reconnu comme créance.

**Implications pratiques**: La relation de couverture ne doit pas être documentée comme couverture d’investissement net pour ce cas.

**Référence**:
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 8
    >it should not be applied by analogy to other types of hedge accounting
 - 6.3.1
    >A hedged item can be a recognised asset or liability ... or a net investment in a foreign operation