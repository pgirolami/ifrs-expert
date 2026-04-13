# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Reformulation**:
>Eligibility of intragroup dividend receivables for foreign exchange risk hedge accounting designation in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`)
   - IFRS (`ifrs9`, `ifrs12`, `ifrs19`, `ifrs7`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`)
   - IFRS (`ifrs9`, `ifrs12`, `ifrs19`, `ifrs7`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - La question porte sur des dividendes intragroupe à recevoir entre entités du même groupe, dans les comptes consolidés
   - La créance de dividende intragroupe est un élément monétaire libellé dans une devise autre que la fonctionnelle de l'entité qui la comptabilise

## Recommandation

**OUI SOUS CONDITIONS**

La désignation directe du risque de change sur une créance de dividende intragroupe en tant que tel n'est pas permise en raison de l'exigence de transaction avec une partie externe (IFRS 9 §6.3.5). Toutefois, l'exposition au risque de change peut être couverte dans le cadre d'une couverture de l'investissement net dans l'opération étrangère, sous réserve que les conditions spécifiques soient remplies.

## Points Opérationnels

   - Documenter soigneusement la relation de couverture en precisant que l'élément couvert est le risque de change attaché à l'investissement net, et non la créance de dividende en tant que telle
   - S'assurer que l'exposition au risque de change n'est pas déjà couverte par une autre entité du groupe (IFRIC 16 §13)
   - Vérifier que la créance de dividende n'a pas été eliminée lors de la consolidation avant d'être prise en compte dans l'investissement net


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de change classique | NON | - (non spécifiées) |
| 2. Couverture de l'investissement net dans une operation etrangere | OUI SOUS CONDITIONS | - Le dividende intragroupe doit être un élément monétaire faisant partie de l'investissement net de l'entité dans l'operation etrangere (IAS 21 §32)<br>- Le risque de change couvert doit être celui existant entre la devise fonctionnelle de l'operation etrangere et celle de la société mère (IFRIC 16 §10)<br>- Le risque de change doit affecter le resultat consolidé (IAS 21 §32 in fine)<br>- L'exposition au risque de change ne peut être couverte qu'une seule fois dans les comptes consolidés (IFRIC 16 §13) |

### 1. Couverture de change classique

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
En vertu d'IFRS 9 §6.3.5, seuls les actifs, passifs, engagements ferme ou transactions forecast avec une partie externe à l'entité rapportante peuvent être désignés comme éléments couverts. Une créance de dividende intragroupe est une transaction entre entités du même groupe ; elle ne répond pas à cette condition d'externalité.

**Implications pratiques**: Le risque de change sur la créance de dividende intragroupe ne peut pas être désigné directement comme élément couvert dans une relation de couverture en comptes consolidés.

**Référence**:
 - ifrs9 6.3.5

    >**For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.** Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 2. Couverture de l'investissement net dans une operation etrangere

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende intragroupe doit être un élément monétaire faisant partie de l'investissement net de l'entité dans l'operation etrangere (IAS 21 §32)
   - Le risque de change couvert doit être celui existant entre la devise fonctionnelle de l'operation etrangere et celle de la société mère (IFRIC 16 §10)
   - Le risque de change doit affecter le resultat consolidé (IAS 21 §32 in fine)
   - L'exposition au risque de change ne peut être couverte qu'une seule fois dans les comptes consolidés (IFRIC 16 §13)

**Raisonnement**:
IAS 21 §32 crée une exception pour le risque de change des éléments monétaires intragroupe faisant partie de l'investissement net dans une operation etrangere. IFRIC 16 §9(a)(i) confirme que le risque de change entre la devise fonctionnelle de l'operation etrangere et celle de la societe mère peut être désigné comme risque couvert. Le dividende à recevoir fait partie intégrante de la position d'investissement net.

**Implications pratiques**: Le risque de change afférent à la créance de dividende intragroupe peut être inclus dans une relation de couverture de l'investissement net, sous réserve de respecter les conditions de documentation et d'efficacité requises par IFRS 9.

**Référence**:
 - ias21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 9(a)(i)

    >whether the parent entity may designate as a hedged risk only the foreign exchange differences arising from a difference between the functional currencies of the parent entity and its foreign operation
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.