# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La créance/dette de dividende intragroupe est un élément monétaire comptabilisé, libellé en devise étrangère.
   - Cet élément reste comptabilisé dans les comptes consolidés, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, une documentation de couverture est permise si la créance de dividende intragroupe constitue, dans les comptes consolidés, un élément monétaire intragroupe générant des écarts de change non totalement éliminés. Dans ce cas, IFRS 9 admet qu’un tel risque de change intragroupe soit désigné comme élément couvert.

## Points Opérationnels

   - Le point décisif est que la créance de dividende soit déjà reconnue et conserve, en consolidé, un risque de change non totalement éliminé.
   - La documentation doit être établie dès l’inception de la relation de couverture et identifier clairement l’élément couvert, le risque de change et la méthode d’efficacité.
   - Si cette condition d’exposition résiduelle en consolidé n’est pas remplie, la documentation de couverture n’est pas recevable et IAS 21 s’applique seul.
   - La couverture d’investissement net n’est pas adaptée à une créance de dividende intragroupe de règlement ; il faut raisonner sur fair value hedge ou cash flow hedge selon la relation documentée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende intragroupe doit être un élément monétaire reconnu en devise.<br>- Le risque de change doit affecter le résultat consolidé car il n’est pas totalement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La relation doit viser la variabilité des flux de règlement liée au change sur l’élément monétaire reconnu.<br>- Le risque de change sur l’élément intragroupe doit affecter le résultat consolidé et ne pas être totalement éliminé. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |
| 4. Comptabilisation du change sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende intragroupe doit être un élément monétaire reconnu en devise.
   - Le risque de change doit affecter le résultat consolidé car il n’est pas totalement éliminé en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu et le risque visé est une composante spécifique de change. IFRS 9 admet qu’un élément monétaire intragroupe en devise puisse être un élément couvert en consolidé si les écarts de change ne sont pas totalement éliminés ; une couverture de juste valeur est donc permise sous cette condition.

**Implications pratiques**: Une désignation formelle est possible en consolidé si la documentation identifie le risque de change porté par la créance reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.7
    >only changes ... attributable to a specific risk or risks (risk component)

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La relation doit viser la variabilité des flux de règlement liée au change sur l’élément monétaire reconnu.
   - Le risque de change sur l’élément intragroupe doit affecter le résultat consolidé et ne pas être totalement éliminé.

**Raisonnment**:
Cette approche est aussi permise dans ce cas si l’entité documente la variabilité en monnaie fonctionnelle des flux de règlement du dividende reconnue en résultat consolidé. Les textes IFRS 9 et IAS 21 montrent qu’un risque de change sur un élément monétaire peut faire l’objet d’une relation de cash flow hedge, y compris pour un élément intragroupe admis par l’exception de consolidation.

**Implications pratiques**: Si la relation est documentée en cash flow hedge, la mécanique de comptabilisation suit le modèle IFRS 9/IAS 21 des couvertures de flux de trésorerie.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 27
    >exchange differences on monetary items that qualify as hedging instruments in a cash flow hedge

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le sujet porte sur une créance de dividende intragroupe reconnue, donc sur un poste de règlement identifié, et non sur une exposition de net investment dans une activité étrangère. Les textes sur le net investment hedge visent le risque de change lié aux net assets d’une opération étrangère ; ce n’est pas la situation décrite.

**Implications pratiques**: Cette voie n’est pas la bonne base de documentation pour un dividende intragroupe comptabilisé en créance.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Comptabilisation du change sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture documentée, IAS 21 s’applique directement. Dans cette situation, la créance/dette de dividende intragroupe étant supposée monétaire et en devise, les écarts de change sont comptabilisés en résultat tant qu’aucune comptabilité de couverture IFRS 9 n’est mise en place.

**Implications pratiques**: Sans hedge accounting, les écarts de change sur la créance/dette reconnue vont en résultat consolidé.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items ... shall be recognised in profit or loss
 - 6.3.6
    >foreign exchange rate gains or losses that are not fully eliminated on consolidation