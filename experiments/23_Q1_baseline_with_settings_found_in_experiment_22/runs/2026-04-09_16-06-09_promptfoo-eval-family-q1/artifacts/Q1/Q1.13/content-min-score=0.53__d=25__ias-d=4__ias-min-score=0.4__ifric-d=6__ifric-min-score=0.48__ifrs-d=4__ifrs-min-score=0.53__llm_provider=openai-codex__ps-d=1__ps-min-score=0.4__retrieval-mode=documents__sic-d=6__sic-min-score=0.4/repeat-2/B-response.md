# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Dans les comptes consolidés, des dividendes intragroupe ont été décidés et une créance à recevoir a été comptabilisée. Dans ce contexte, la composante de risque de change associée à cette créance peut-elle être intégrée dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs9`
   - `ifrs19`
   - `ifrs17`
   - `ifric17`
   - `ifrs12`
   - `ifric2`
   - `ias24`
   - `ias37`
   - `ifric16`
   - `sic7`
   - `sic25`
   - `ias23`
   - `ias26`
   - `ps1`
   - `ifric19`
   - `ifric21`
   - `sic29`

## Hypothèses
   - La créance issue du dividende intragroupe décidé est un élément monétaire comptabilisé.
   - La question est analysée dans le cadre des comptes consolidés et du modèle de comptabilité de couverture d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais uniquement si la créance de dividende intragroupe constitue un élément monétaire intragroupe exposé à un risque de change qui n’est pas entièrement éliminé en consolidation. Dans cette situation, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’un investissement net.

## Points Opérationnels

   - Vérifier si les deux entités concernées ont des devises fonctionnelles différentes, car c’est ce point qui fonde la non-élimination complète du risque de change en consolidation.
   - La désignation doit être formellement documentée dès l’origine de la relation de couverture, avec identification du poste couvert, du risque de change couvert et du test d’efficacité.
   - Si la créance de dividende est éliminée sans laisser d’exposition de change en résultat consolidé, aucune relation de couverture ne peut être justifiée sur ce poste.
   - Le traitement doit être apprécié au niveau des comptes consolidés, et non uniquement dans les comptes individuels des entités du groupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes de change non entièrement éliminés en consolidation, notamment entre entités ayant des devises fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes de change non entièrement éliminés en consolidation, notamment entre entités ayant des devises fonctionnelles différentes.

**Raisonnment**:
Dans les comptes consolidés, un poste intragroupe n’est en principe pas éligible, sauf exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés en consolidation. Une créance de dividende comptabilisée entre entités de devises fonctionnelles différentes peut entrer dans cette exception. Comme il s’agit d’un actif reconnu exposé aux variations de change, le modèle de couverture de juste valeur est celui qui correspond à cette situation.

**Implications pratiques**: La relation documentée peut viser la composante de risque de change de la créance si l’exception intragroupe d’IFRS 9 est satisfaite.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le fait générateur décrit est une créance de dividende déjà comptabilisée. Le sujet porte donc sur un actif monétaire reconnu dont l’exposition se matérialise par des écarts de change sur sa valeur comptable, et non sur une transaction future hautement probable ou sur une variabilité de flux futurs au sens pertinent pour ce cas. Dans ce contexte précis, IFRS 9 oriente davantage vers la couverture de juste valeur.

**Implications pratiques**: La documentation de couverture ne devrait pas retenir ce traitement pour la créance de dividende déjà reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise la composante de change d’une créance de dividende intragroupe comptabilisée, et non le risque de change attaché à un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 traitent ce modèle comme une catégorie distincte liée aux net assets d’une opération étrangère. Ce n’est pas le fait générateur décrit ici.

**Implications pratiques**: Ce modèle ne doit pas être utilisé pour couvrir la créance de dividende intragroupe elle-même.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.