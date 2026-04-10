# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Documentation consultée**
   - `ifrs9`
   - `ifrs17`
   - `sic25`
   - `ias21`
   - `ifric17`
   - `ifrs19`
   - `ifrs7`
   - `ias7`
   - `ias37`
   - `ifric16`
   - `ifric2`
   - `ias26`
   - `ifric19`
   - `ps1`
   - `sic7`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise générant un risque de change au niveau des comptes consolidés.
   - La question porte sur les états financiers consolidés établis en IFRS.
   - La créance est déjà reconnue en comptabilité consolidée ; il ne s’agit donc pas d’un dividende seulement prévu ou non encore comptabilisé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende intragroupe constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, la documentation de couverture peut être envisagée sur ce risque de change ; le modèle pertinent n’est pas la couverture de flux de trésorerie ni la couverture d’investissement net sur ces faits.

## Points Opérationnels

   - Le point décisif est de qualifier la créance de dividende comme poste monétaire intragroupe et de vérifier que son écart de change n’est pas totalement éliminé en consolidation.
   - La documentation de couverture doit être mise en place sur la composante de risque de change de ce poste reconnu, et non sur un dividende simplement anticipé.
   - Si les effets de change sur ce poste sont comptabilisés en résultat consolidé, cela soutient l’éligibilité de la composante couverte dans le cadre IFRS 9.
   - La couverture d’investissement net ne doit pas être utilisée comme substitut pour un dividende intragroupe déclaré et comptabilisé en créance.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire reconnu.<br>- Le risque de change doit affecter le résultat consolidé et ne pas être totalement éliminé en consolidation.<br>- La relation de couverture doit être documentée conformément aux exigences de la comptabilité de couverture IFRS 9. |
| 3. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 4. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, la créance de dividende reconnue crée d’abord une problématique de change relevant d’IAS 21. Pour un poste monétaire, les écarts de change sont en principe comptabilisés en résultat ; et, pour un poste monétaire intragroupe, ils ne sont pas totalement éliminés en consolidation lorsqu’il existe un engagement de conversion entre monnaies différentes.

**Implications pratiques**: En l’absence de relation de couverture qualifiée, les écarts de change sur la créance suivront le traitement IAS 21, en principe en résultat.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire reconnu.
   - Le risque de change doit affecter le résultat consolidé et ne pas être totalement éliminé en consolidation.
   - La relation de couverture doit être documentée conformément aux exigences de la comptabilité de couverture IFRS 9.

**Raisonnment**:
Cette approche peut s’appliquer si la créance de dividende est un poste monétaire intragroupe reconnu et si son risque de change subsiste dans les comptes consolidés. IFRS 9 permet qu’un passif ou actif reconnu soit un élément couvert, et prévoit expressément qu’un poste monétaire intragroupe en devise peut être un élément couvert en consolidation lorsque les écarts de change ne sont pas totalement éliminés.

**Implications pratiques**: Si ces conditions sont remplies, une documentation de couverture sur la composante de change est envisageable dans un schéma de hedge accounting.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items ... shall be recognised

### 3. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Sur les faits décrits, le dividende est déjà reconnu en créance dans les comptes consolidés. Or le modèle de cash flow hedge vise notamment une transaction future prévue et hautement probable ; ici, le sujet n’est plus un flux futur prévu mais un poste monétaire déjà comptabilisé exposé au change.

**Implications pratiques**: La problématique décrite doit être analysée comme celle d’un poste monétaire existant, non comme celle d’un flux futur à couvrir.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 27
    >IFRS 9 requires that exchange differences on monetary items that qualify as hedging instruments in a cash flow hedge are recognised initially in other comprehensive income

### 4. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change lié à un investissement net dans une activité à l’étranger, pas celui d’une créance de dividende intragroupe reconnue. La créance de dividende constitue un poste distinct du net investment ; les extraits fournis circonscrivent ce modèle à l’exposition sur les actifs nets de l’activité étrangère.

**Implications pratiques**: Il ne faut pas assimiler la créance de dividende au risque de change d’un investissement net dans une entité étrangère.

**Référence**:
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation