# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-il possible, au niveau consolidé, de qualifier de manière formelle une couverture du risque de change sur des dividendes intragroupe ayant fait l’objet d’une comptabilisation en créance à recevoir ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question porte sur des états financiers consolidés établis selon les IFRS.
   - La créance de dividende intragroupe est libellée en devise et crée une exposition de change.
   - L’enjeu est la désignation formelle en comptabilité de couverture, et non une simple couverture économique.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, cela peut être formellement qualifié principalement comme couverture de juste valeur du risque de change de la créance intragroupe, mais seulement si l’élément est un poste monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation. À défaut, le dérivé reste comptabilisé à la juste valeur par résultat sans relation de couverture formelle.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si la créance de dividende constitue bien un poste monétaire intragroupe générant des écarts de change non totalement éliminés.
   - La documentation de couverture doit être formalisée dès l’origine de la relation et préciser l’instrument, l’élément couvert, le risque couvert et le test d’efficacité.
   - Si le dividende n’est pas encore comptabilisé mais seulement prévu, l’analyse basculerait vers les règles des transactions intragroupe hautement probables, distinctes du cas posé ici.
   - En l’absence de qualification formelle, le dérivé sera maintenu à la juste valeur par résultat au niveau consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un poste monétaire.<br>- Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.<br>- La relation doit satisfaire aux exigences formelles de désignation, documentation et efficacité de couverture. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Dérivé à la juste valeur par résultat | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un poste monétaire.
   - Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.
   - La relation doit satisfaire aux exigences formelles de désignation, documentation et efficacité de couverture.

**Raisonnment**:
Ici, le dividende a déjà été comptabilisé en créance à recevoir, donc il s’agit d’un actif reconnu. IFRS 9 permet qu’un poste monétaire intragroupe soit un élément couvert en consolidation pour son risque de change si les écarts de change ne sont pas pleinement éliminés, ce qui cadre avec une couverture de juste valeur d’un actif reconnu.

**Implications pratiques**: C’est l’approche la plus pertinente pour une créance de dividende déjà reconnue au bilan consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.4.1
    >at the inception ... there is formal designation and documentation of the hedging relationship

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, l’exposition porte sur un dividende intragroupe déjà comptabilisé en créance à recevoir, et non sur une transaction future hautement probable. Le texte IFRS vise explicitement, pour l’exception intragroupe en consolidation, les transactions intragroupe prévues hautement probables, pas un dividende déjà reconnu en créance.

**Implications pratiques**: Cette voie n’est pas la bonne qualification pour un dividende déjà acté et comptabilisé en créance.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - B6.3.5
    >forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe ne correspond pas à un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net vise le risque de change sur les actifs nets d’une opération étrangère inclus dans les états financiers, pas l’encaissement d’un dividende intragroupe reconnu en créance.

**Implications pratiques**: Cette qualification ne convient pas au risque de change d’une créance de dividende intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 1
    >The item being hedged ... may be an amount of net assets
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations

### 4. Dérivé à la juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Si la relation de couverture formelle n’est pas désignée ou ne remplit pas les critères IFRS 9, le dérivé reste comptabilisé séparément à la juste valeur, avec variations en résultat. C’est donc le traitement de repli applicable en consolidation dans cette situation.

**Implications pratiques**: À défaut de couverture comptable qualifiée, la volatilité du dérivé passe en résultat.

**Référence**:
 - 4.2.1
    >derivatives that are liabilities, shall be subsequently measured at fair value
 - B3.1.1
    >an entity recognises all of its contractual rights and obligations under derivatives