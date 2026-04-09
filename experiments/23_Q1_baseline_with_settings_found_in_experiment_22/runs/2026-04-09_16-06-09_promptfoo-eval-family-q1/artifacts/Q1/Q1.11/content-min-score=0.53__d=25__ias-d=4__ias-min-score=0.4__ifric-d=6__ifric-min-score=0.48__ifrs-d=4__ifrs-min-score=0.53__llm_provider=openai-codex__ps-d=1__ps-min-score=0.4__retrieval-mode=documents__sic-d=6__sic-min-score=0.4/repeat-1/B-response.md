# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ias39`
   - `ifrs9`
   - `ifric16`
   - `ias21`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ias29`
   - `ifrs12`
   - `sic7`

## Hypothèses
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe, une fois comptabilisé, crée une créance/dette monétaire libellée en devise entre entités du groupe.
   - L’exposition visée est le risque de change sur cette créance/dette après sa comptabilisation, et non un hedge de net investment.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement dans le cas étroit où la créance/dette intragroupe constitue un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation, typiquement entre entités ayant des monnaies fonctionnelles différentes. À défaut, le hedge accounting en comptes consolidés n’est pas disponible.

## Points Opérationnels

   - Vérifier au moment de la comptabilisation du dividende si la créance/dette est bien un poste monétaire intragroupe en devise entre entités à monnaies fonctionnelles différentes.
   - En consolidation, documenter la couverture uniquement sur le risque de change qui n’est pas totalement éliminé ; sinon la désignation échoue.
   - L’instrument de couverture doit être externe à l’entité présentant les comptes consolidés.
   - Si les conditions de hedge accounting ne sont pas remplies, appliquer IAS 21 et comptabiliser les écarts de change en résultat.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un poste monétaire intragroupe libellé en devise.<br>- Le risque de change génère des écarts de change non totalement éliminés en consolidation.<br>- La relation de couverture est documentée et qualifie au sens des critères IFRS applicables. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |
| 4. Comptabilisation du change sans hedge accounting | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un poste monétaire intragroupe libellé en devise.
   - Le risque de change génère des écarts de change non totalement éliminés en consolidation.
   - La relation de couverture est documentée et qualifie au sens des critères IFRS applicables.

**Raisonnment**:
En comptes consolidés, un élément intragroupe ne peut en principe pas être un élément couvert. Toutefois, il existe une exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il génère des gains/pertes de change non totalement éliminés en consolidation. Une créance de dividende enregistrée peut entrer dans cette exception si elle est monétaire et entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: Possible en consolidation uniquement dans le cas d’exception sur le risque de change d’un poste monétaire intragroupe ; sinon non.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 86(a)
    >fair value hedge: a hedge of the exposure to changes in fair value

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, l’exposition naît après comptabilisation d’une créance de dividende intragroupe existante. Le texte fourni traite l’exception intragroupe en consolidation pour un poste monétaire intragroupe au titre du risque de change, sans viser ici un flux futur hautement probable de dividende intragroupe. La question porte donc sur une créance enregistrée, pas sur une transaction future de dividende.

**Implications pratiques**: Cette voie n’est pas la base appropriée pour la créance de dividende déjà comptabilisée dans le cas posé.

**Référence**:
 - 86(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 80
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende intragroupe une fois enregistrée. Or la couverture d’un investissement net concerne le risque de change sur les net assets d’une activité étrangère, pas une créance de dividende intercompany distincte. Les extraits fournis d’IFRIC 16 cadrent cette couverture sur l’investissement net dans l’activité étrangère.

**Implications pratiques**: Ne pas documenter la créance de dividende enregistrée comme hedge de net investment.

**Référence**:
 - 2
    >The item being hedged ... may be an amount of net assets
 - 11
    >the hedged item can be an amount of net assets
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation

### 4. Comptabilisation du change sans hedge accounting
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de qualification en hedge accounting, IAS 21 s’applique au poste monétaire en devise. Les écarts de change sur les postes monétaires sont comptabilisés en résultat, sauf cas spécifiques tels que les éléments faisant partie d’un investissement net. C’est le traitement de repli si les conditions de l’exception intragroupe ne sont pas réunies.

**Implications pratiques**: En pratique, les écarts de change sur la créance/dette de dividende iront en résultat si aucun hedge accounting qualifiant n’est mis en place.

**Référence**:
 - 28
    >Exchange differences ... shall be recognised in profit or loss
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment
 - 5
    >This Standard does not apply to hedge accounting for foreign currency items