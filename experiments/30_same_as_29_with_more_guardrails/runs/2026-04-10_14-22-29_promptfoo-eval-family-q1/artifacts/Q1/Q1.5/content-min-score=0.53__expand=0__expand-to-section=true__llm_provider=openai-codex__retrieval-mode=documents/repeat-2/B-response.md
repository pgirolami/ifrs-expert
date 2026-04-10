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
   - Le dividende intragroupe a été déclaré et comptabilisé en créance à recevoir chez une entité du groupe et en dette correspondante chez une autre entité du groupe.
   - La créance/dette de dividende est un élément monétaire libellé dans une devise différente de la monnaie fonctionnelle d'au moins une des entités concernées.
   - Au niveau consolidé, les écarts de change sur cet élément monétaire intragroupe ne sont pas entièrement éliminés, conformément à IAS 21 lorsque les entités ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique via une couverture de juste valeur du risque de change sur la créance intragroupe, si l'élément monétaire génère des écarts de change non totalement éliminés en consolidation. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà comptabilisée, et la couverture d'investissement net ne vise pas ce type d'exposition.

## Points Opérationnels

   - Le point décisif est le niveau de reporting : l'analyse doit être faite dans les états financiers consolidés, pas seulement dans les comptes individuels.
   - Le facteur clé est la nature monétaire de la créance de dividende et la persistance d'écarts de change en consolidation entre entités à monnaies fonctionnelles différentes.
   - Si le dividende n'était pas encore comptabilisé mais seulement attendu, la logique pourrait relever d'une transaction prévue; ce n'est pas le cas décrit ici.
   - La documentation formelle doit identifier le risque couvert comme le risque de change de l'élément monétaire intragroupe reconnu.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe reconnu.<br>- Les écarts de change sur cet élément ne doivent pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée au niveau consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe reconnu.
   - Les écarts de change sur cet élément ne doivent pas être totalement éliminés en consolidation.
   - La relation de couverture doit être formellement désignée et documentée au niveau consolidé.

**Raisonnment**:
Ici, le dividende intragroupe comptabilisé en créance à recevoir constitue un élément monétaire reconnu. IFRS 9 permet, au niveau consolidé, de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert lorsque les écarts de change ne sont pas totalement éliminés en consolidation. C'est précisément le cas visé pour une créance/dette intragroupe entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture peut viser le risque de change de la créance de dividende intragroupe dans les comptes consolidés si l'exposition subsiste en résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 45
    >such an exchange difference is recognised in profit or loss

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction prévue hautement probable, y compris, par exception, certaines transactions intragroupe prévues en devise. Or la question porte sur des dividendes déjà comptabilisés en créance à recevoir, donc sur une exposition existante et non sur un flux futur seulement prévu. Le fait générateur n'est plus une transaction forecast mais un poste monétaire reconnu.

**Implications pratiques**: La relation de couverture ne devrait pas être documentée comme cash flow hedge pour une créance de dividende déjà reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net vise le risque de change attaché à une participation nette dans une activité étrangère, c'est-à-dire aux net assets de l'opération étrangère inclus dans les états financiers consolidés. Une créance de dividende intragroupe est un poste monétaire distinct, pas un montant de net assets d'une activité étrangère. Ce n'est donc pas l'exposition visée par ce modèle.

**Implications pratiques**: Il ne faut pas qualifier la couverture du risque de change d'un dividende intragroupe en hedge de net investment.

**Référence**:
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency