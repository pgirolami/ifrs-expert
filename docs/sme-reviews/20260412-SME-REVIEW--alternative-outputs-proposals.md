# Alternative Proposals for Output

During the [2026-04-12 SME Review](./20260412-SME-REVIEW.md), the output was deemed as too verbose. Below are some alternatives to discuss with SME.

# 0. Original answer
># Analyse d'une question comptable
>
>**Date**: 2026-04-10
>
>## Question
>
>**Utilisateur**:
>>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
>
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>## Documentation
>**Consultée**
>   - IAS (`ias32`)
>   - IFRIC (`ifric16`)
>   - IFRS (`ifrs9`)
>
>**Retenue pour l'analyse**
>   - IAS (`ias32`)
>   - IFRIC (`ifric16`)
>   - IFRS (`ifrs9`)
>
>## Hypothèses
>   - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée avant la date de clôture.
>   - La créance intragroupe est un poste monétaire libellé dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
>   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
>
>## Recommandation
>
>**OUI SOUS CONDITIONS**
>
>Oui, mais seulement si la créance intragroupe sur dividende constitue un poste monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.
>
>## Points Opérationnels
>
>   - Le point clé est le niveau de reporting: en consolidation, les éléments intragroupe sont en principe exclus, sauf l'exception IFRS 9 sur les postes monétaires intragroupe en devise.
>   - Le timing est déterminant: dès lors qu'une créance sur dividende est comptabilisée, l'analyse porte sur un poste reconnu et non sur une transaction future hautement probable.
>   - Il faut vérifier concrètement que les écarts de change sur cette créance affectent bien le résultat consolidé, faute de quoi la désignation ne tient pas.
>   - La documentation de couverture doit être rédigée au niveau du groupe consolidé et cibler uniquement le risque de change admissible.
>
>
>## Approches évaluées
>
>| Approche | Applicabilité | Conditions |
>| --- | --- | --- |
>| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance sur dividende est un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Le risque de change sur cette créance génère des gains ou pertes non totalement éliminés en consolidation. |
>| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
>| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |
>
>### 1. Couverture de juste valeur
>
>**Applicabilité**: OUI SOUS CONDITIONS
>
>**Conditions**:
>   - La créance sur dividende est un poste monétaire intragroupe.
>   - Les entités concernées ont des monnaies fonctionnelles différentes.
>   - Le risque de change sur cette créance génère des gains ou pertes non totalement éliminés en consolidation.
>
>**Raisonnement**:
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item. En comptes consolidés, un élément intragroupe n'est admissible que par exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>**Implications pratiques**: La documentation doit viser spécifiquement le risque de change du poste monétaire intragroupe reconnu en consolidation.
>
>**Référence**:
> - ifrs9 6.3.1
>
>    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
>(a)a single item; or
>(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
>A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
> - ifrs9 6.3.5
>
>    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
> - ifrs9 6.3.6
>
>    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
>
>### 2. Couverture de flux de trésorerie
>
>**Applicabilité**: NON
>
>**Conditions**:
>   - (conditions non spécifiées)
>
>**Raisonnement**:
>Cette approche vise notamment une transaction future prévue et hautement probable. Or, dans votre cas, la question porte sur des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée; il ne s'agit donc plus d'une transaction future non encore reconnue. Le fait générateur décrit vous place sur un poste reconnu, pas sur un flux futur à couvrir.
>
>**Implications pratiques**: La désignation en couverture de flux de trésorerie n'est pas adaptée une fois la créance sur dividende déjà constatée.
>
>**Référence**:
> - ifrs9 6.3.1
>
>    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
>(a)a single item; or
>(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
>A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
> - ifrs9 6.3.3
>
>    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.
>
>### 3. Couverture d'un investissement net dans une activité à l'étranger
>
>**Applicabilité**: NON
>
>**Conditions**:
>   - (conditions non spécifiées)
>
>**Raisonnement**:
>Votre question vise le risque de change attaché à une créance de dividende intragroupe comptabilisée, non l'exposition de change sur un investissement net dans une activité à l'étranger. IFRIC 16 encadre un modèle distinct, centré sur la différence de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la mère. Ce n'est pas la nature de l'exposition décrite ici.
>
>**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d'investissement net.
>
>**Référence**:
> - ifric16 10
>
>    >**Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
> - ifric16 12
>
>    >**The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation** and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.
>
>

# 1. Only the Recommendation
>**Oui, mais** seulement si la créance intragroupe sur dividende constitue un poste monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.

# 2. Primary Accounting Issue + Recommendation
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>**Réponse**: Oui, mais seulement si la créance intragroupe sur dividende constitue un poste monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.

# 3. Primary Accounting Issue + Recommendation + Reasoning
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>**Réponse**: Oui, mais seulement si la créance intragroupe sur dividende constitue un poste monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.
>
>**Raisonnement**:
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item. En comptes consolidés, un élément intragroupe n'est admissible que par exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.

# 4. Primary Accounting Issue + Reasoning only
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item. En comptes consolidés, un élément intragroupe n'est admissible que par exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.


# 5. Primary Accounting Issue + Reasoning only + References
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item. En comptes consolidés, un élément intragroupe n'est admissible que par exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>**Références**:
> - [IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)
> - [IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)
> - [IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)

# 6. Primary Accounting Issue + Reasoning only + References & citations
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item. En comptes consolidés, un élément intragroupe n'est admissible que par exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>**Références**:
> - [IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)
>
>    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
>(a)a single item; or
>(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
>A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
> - [IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)
>
>    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
> - [IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)
>
>    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

# 7. Primary Accounting Issue + Reasoning only + References inside response
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
>
>Dans votre situation, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). En comptes consolidés, un élément intragroupe n'est admissible que par exception ([IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)) pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation ([IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)). Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.

# 8. Primary Accounting Issue + Reasoning only with Hypothesis + References inside response
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
> Dans cette réponse, on considère que
>  - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée avant la date de clôture.
>   - La créance intragroupe est un poste monétaire libellé dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
>   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
>
>Ainsi, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). En comptes consolidés, un élément intragroupe n'est admissible que par exception ([IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)) pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation ([IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)). Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.

# 9. Primary Accounting Issue + Reasoning only with Hypothesis + References inside response
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
> Pour cette réponse, on considère que
>  - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée avant la date de clôture.
>   - La créance intragroupe est un poste monétaire libellé dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
>   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
>
>Ainsi, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). En comptes consolidés, un élément intragroupe n'est admissible que par exception ([IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)) pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation ([IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)). Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>L'approche par couverture de flux de trésorerie vise notamment une transaction future prévue et hautement probable ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). Or, dans votre cas, la question porte sur des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée; il ne s'agit donc plus d'une transaction future non encore reconnue. Le fait générateur décrit vous place sur un poste reconnu, pas sur un flux futur à couvrir.
>
>Votre question vise le risque de change attaché à une créance de dividende intragroupe comptabilisée, non l'exposition de change sur un investissement net dans une activité à l'étranger. IFRIC 16 encadre un modèle distinct, centré sur la différence de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la mère. Ce n'est pas la nature de l'exposition décrite ici ([IFRIC 16 10](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_10), [IFRIC 16 12](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_12))
. La couverture d'un investissement net dans une activité à l'étranger ne s'applique donc pas.



# 9. Primary Accounting Issue + Reasoning only with Hypothesis + References inside response + unapplicable alternative approaches + Citations
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
> Pour cette réponse, on considère que
>  - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée avant la date de clôture.
>   - La créance intragroupe est un poste monétaire libellé dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
>   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
>
>Ainsi, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). En comptes consolidés, un élément intragroupe n'est admissible que par exception ([IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)) pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation ([IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)). Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>L'approche par couverture de flux de trésorerie vise notamment une transaction future prévue et hautement probable ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). Or, dans votre cas, la question porte sur des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée; il ne s'agit donc plus d'une transaction future non encore reconnue. Le fait générateur décrit vous place sur un poste reconnu, pas sur un flux futur à couvrir.
>
>Votre question vise le risque de change attaché à une créance de dividende intragroupe comptabilisée, non l'exposition de change sur un investissement net dans une activité à l'étranger. IFRIC 16 encadre un modèle distinct, centré sur la différence de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la mère. Ce n'est pas la nature de l'exposition décrite ici ([IFRIC 16 10](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_10), [IFRIC 16 12](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_12))
. La couverture d'un investissement net dans une activité à l'étranger ne s'applique donc pas.
>
>**Citations**:
> - [IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)
>
>    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
>(a)a single item; or
>(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
>A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
> - [IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)
>
>    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
> - [IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)
>
>    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
>
> - [IFRIC 16 10](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_10)
>
>    >**Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
> - [IFRIC 16 12](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_12)
>
>    >**The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation** and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.



# 10. Primary Accounting Issue + Hypothesis + Recommendation + Reasoning + References inside response + unapplicable alternative approaches + Citations
>**Reformulation**:
>>Dans les états financiers consolidés, quel modèle de comptabilité de couverture IFRS pouvons-nous appliquer au risque de change découlant d’une créance intragroupe liée à un dividende ?
>
> Pour cette réponse, on considère que
>  - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée avant la date de clôture.
>   - La créance intragroupe est un poste monétaire libellé dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
>   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
>
>**Oui**, mais seulement si la créance intragroupe sur dividende constitue un poste monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.
>
>En effet, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant en principe servir de hedged item ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). En comptes consolidés, un élément intragroupe n'est admissible que par exception ([IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)) pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation ([IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)). Si cette condition est remplie, une documentation de couverture peut être envisagée sur ce risque.
>
>L'approche par couverture de flux de trésorerie vise notamment une transaction future prévue et hautement probable ([IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)). Or, dans votre cas, la question porte sur des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée; il ne s'agit donc plus d'une transaction future non encore reconnue. Le fait générateur décrit vous place sur un poste reconnu, pas sur un flux futur à couvrir.
>
>Votre question vise le risque de change attaché à une créance de dividende intragroupe comptabilisée, non l'exposition de change sur un investissement net dans une activité à l'étranger. IFRIC 16 encadre un modèle distinct, centré sur la différence de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la mère. Ce n'est pas la nature de l'exposition décrite ici ([IFRIC 16 10](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_10), [IFRIC 16 12](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_12))
. La couverture d'un investissement net dans une activité à l'étranger ne s'applique donc pas.
>
>**Citations**:
> - [IFRS 9 6.3.1](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.1)
>
>    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
>(a)a single item; or
>(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
>A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
> - [IFRS 9 6.3.5](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.5)
>
>    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
> - [IFRS 9 6.3.6](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/#IFRS09_6.3.6)
>
>    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
>
> - [IFRIC 16 10](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_10)
>
>    >**Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
> - [IFRIC 16 12](https://www.ifrs.org/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16/#IFRIC16_12)
>
>    >**The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation** and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.
