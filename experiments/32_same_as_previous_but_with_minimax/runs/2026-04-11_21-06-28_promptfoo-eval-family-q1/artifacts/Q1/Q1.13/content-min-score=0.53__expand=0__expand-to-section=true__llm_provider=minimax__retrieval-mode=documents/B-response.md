# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Dans les comptes consolidés, des dividendes intragroupe ont été décidés et une créance à recevoir a été comptabilisée. Dans ce contexte, la composante de risque de change associée à cette créance peut-elle être intégrée dans une relation de couverture documentée ?

**Reformulation**:
>Whether foreign exchange risk on intragroup dividend receivable can be designated as hedged item in consolidated financial statements under IFRS 9 hedge accounting requirements

## Documentation
**Consultée**
   - IAS (`ias24`, `ias37`, `ias23`, `ias26`)
   - IFRIC (`ifric17`, `ifric2`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs17`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic7`, `sic25`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias24`, `ias37`, `ias23`, `ias26`)
   - IFRIC (`ifric17`, `ifric2`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs17`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic7`, `sic25`, `sic29`)

## Hypothèses
   - Il s'agit des comptes consolidés du groupe (pas des comptes individuels des entités)
   - La créance dividendes est intragroupe (créance d'une société mère sur sa filiale)
   - La créance est libellée dans une devise étrangère (sinon il n'y aurait pas de risque de change à couvrir)

## Recommandation

**OUI SOUS CONDITIONS**

Le risque de change d'une créance intragroupe peut être désigné comme élément hedgé dans les comptes consolidés, mais uniquement si les différences de change ne sont pas éliminées totalement lors de la consolidation en vertu d'IAS 21, ce qui suppose que les entités du groupe ont des devises fonctionnelles différentes.

## Points Opérationnels

   - Vérifier que les devises fonctionnelles de la société mère et de sa filiale sont bien différentes avant de tenter de désigner le risque de change
   - Documenter la relation de couverture conformément aux exigences d'IFRS 9 (désignation formelle, efficacité démontrée)
   - En présence de devises fonctionnelles identiques, le risque de change est éliminé en consolidation et ne peut faire l'objet d'une couverture
   - Les dividendes intragroupe étant des transactions avec une partie interne, la désignation comme élément hedgé n'est possible que par l'exception du paragraphe 6.3.6


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Exclusion générale des éléments intragroupe de la comptabilité de couverture | NON | - (non spécifiées) |
| 2. Exception pour le risque de change des éléments monétaires intragroupe | OUI SOUS CONDITIONS | - La créance dividendes doit être un élément monétaire intragroupe<br>- Les différences de change associées doivent ne pas être éliminées totalement lors de la consolidation (IAS 21)<br>- Les devises fonctionnelles de la société mère et de la filiale doivent être différentes |
| 3. Couverture d'un investissement net dans une opération étrangère | NON | - (non spécifiées) |

### 1. Exclusion générale des éléments intragroupe de la comptabilité de couverture

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le paragraphe 6.3.5 d'IFRS 9 pose comme principe que seuls les éléments avec une partie externe au groupe peuvent être désignés comme élément hedgé dans les comptes consolidés. Une créance dividendes intragroupe ne satisfies pas cette condition de base.

**Implications pratiques**: L'approche 1 constitue le principe général applicable, mais elle est supplantée par l'exception de l'approche 2.

**Référence**:
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items

### 2. Exception pour le risque de change des éléments monétaires intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance dividendes doit être un élément monétaire intragroupe
   - Les différences de change associées doivent ne pas être éliminées totalement lors de la consolidation (IAS 21)
   - Les devises fonctionnelles de la société mère et de la filiale doivent être différentes

**Raisonnement**:
Le paragraphe 6.3.6 d'IFRS 9 prévoit une exception permettant de désigner le risque de change d'un élément monétaire intragroupe comme élément hedgé si les gains ou pertes de change ne sont pas éliminés totalement lors de la consolidation selon IAS 21. Cela suppose que la créance dividendes est entre deux entités ayant des devises fonctionnelles différentes.

**Implications pratiques**: Si les conditions sont réunies, une relation de couverture documentée peut être établie pour le risque de change sur la créance intragroupe dans les comptes consolidés.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation

### 3. Couverture d'un investissement net dans une opération étrangère

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRIC 16 traite de la couverture du risque de change lié à l'investissement net dans une opération étrangère (filiale). La créance dividendes n'est pas un investissement net; elle est une créance courant sur des distributions decided et ne relève pas de ce dispositif.

**Implications pratiques**: Cette approche ne s'applique pas aux créances dividendes intragroupe.

**Référence**:
 - IFRIC 16 2

    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation will apply only when the net assets of that foreign operation are included in the financial statements