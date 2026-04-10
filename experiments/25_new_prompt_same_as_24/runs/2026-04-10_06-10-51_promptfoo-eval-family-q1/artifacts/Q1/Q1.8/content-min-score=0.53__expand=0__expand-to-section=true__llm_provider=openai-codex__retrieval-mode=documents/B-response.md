# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Peut-on appliquer la comptabilité de couverture en consolidation à l’exposition de change résultant de dividendes intragroupe dès lors que ceux-ci ont été comptabilisés en créance à recevoir ?

**Documentation consultée**
   - `ifrs9`
   - `ifric17`
   - `ias32`
   - `ifrs18`
   - `ias7`
   - `ifric2`
   - `ifrs19`
   - `ifric16`
   - `ifrs7`
   - `ias37`
   - `sic25`

## Hypothèses
   - Le dividende intragroupe déclaré a donné lieu à une créance et à une dette intragroupe comptabilisées, constituant un élément monétaire libellé en devise.
   - La question vise les états financiers consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la comptabilité de couverture peut viser l’exposition de change d’une créance de dividende intragroupe déjà comptabilisée si cette créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, le modèle pertinent est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si les écarts de change sur la créance/dette intragroupe de dividende ne sont pas totalement éliminés.
   - Le moment est important : avant comptabilisation du dividende, on serait dans la logique d’une transaction prévisionnelle ; après comptabilisation en créance, l’analyse bascule vers un poste reconnu.
   - La réponse vaut pour les comptes consolidés ; IFRS 9 distingue expressément ce cadre des comptes individuels ou séparés pour les transactions intragroupe.
   - Si l’instrument de couverture est désigné, la documentation et l’efficacité doivent être établies conformément au modèle de couverture retenu.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un élément monétaire intragroupe libellé en devise.<br>- Les écarts de change sur cet élément ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un élément monétaire intragroupe libellé en devise.
   - Les écarts de change sur cet élément ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Ici, le dividende est supposé déjà comptabilisé en créance/dette intragroupe, donc il s’agit d’un élément reconnu et monétaire. IFRS 9 permet, en consolidation, de désigner comme élément couvert le risque de change d’un élément monétaire intragroupe si les écarts de change qui en résultent ne sont pas totalement éliminés en consolidation. Cette logique correspond à une couverture d’un poste reconnu, donc à une couverture de juste valeur dans ce cas.

**Implications pratiques**: La documentation de couverture doit viser la créance de dividende reconnue comme poste couvert en risque de change dans les comptes consolidés.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits posés, le dividende n’est plus une transaction future hautement probable : il a déjà été comptabilisé en créance à recevoir. Or IFRS 9 réserve ce type de désignation, pour les transactions intragroupe, aux transactions prévisionnelles hautement probables dont le risque de change affectera le résultat consolidé. Cette condition n’est pas celle d’une créance déjà reconnue.

**Implications pratiques**: Une fois le dividende reconnu en créance, ce modèle n’est pas le véhicule approprié pour la couverture du risque de change de ce poste.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur l’exposition de change d’un dividende intragroupe devenu créance à recevoir, donc sur un poste monétaire intragroupe distinct. IFRIC 16 réserve la couverture d’investissement net au risque de change attaché au net d’actifs d’une activité à l’étranger. Ce n’est pas, dans cette situation, la nature du poste couvert décrit.

**Implications pratiques**: Il ne faut pas assimiler la créance de dividende à l’investissement net dans l’activité étrangère pour la désignation de couverture.

**Référence**:
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity