# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I have a question in relation to the accounting for a profit participating loan liability. For instance, a limited recourse loan where principal is payable on maturity but the interest on such loan is linked to profits i.e. based on a priority of payments if there is any residual profits that is the interest expense on the loan for the period.

Now, per my understanding I believe this amounts to the case for an embedded derivative i.e. the host contract being principal payments and interest being paid only if there is residual profit left per the waterfall priority of payments. Thus, the loan liability should be held at fair value through profit or loss.

I have come across many opinions for it to be accounted on an amortised cost basis at EIR, however, given the payments of interest are variable and based on if there is residual profit left, would it be accounted for at FVTPL or amortised cost.

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - L’instrument est un passif financier entrant dans le champ d’IFRS 9 et la question porte sur sa comptabilisation ultérieure.
   - Aucune désignation irrévocable à la juste valeur par résultat lors de la comptabilisation initiale n’est mentionnée dans les faits décrits.
   - La rémunération variable est liée aux profits résiduels de l’emprunteur/émetteur tels que décrits dans la question.

## Recommandation

**OUI**

Dans les faits décrits, le traitement recommandé est le coût amorti. IFRS 9 pose le coût amorti comme règle générale pour les passifs financiers, et la clause d’intérêt liée aux profits résiduels ne conduit pas ici, sur la base du texte fourni, à une séparation obligatoire d’un dérivé incorporé; la JVPR ne serait envisageable que par désignation initiale.

## Points Opérationnels

   - Déterminer à l’origine les flux contractuels estimés du prêt, y compris la composante de rémunération variable attendue, pour calculer le taux d’intérêt effectif.
   - À chaque clôture, réviser les estimations de paiements d’intérêt liés aux profits résiduels et comptabiliser l’ajustement du coût amorti en résultat selon B5.4.6.
   - Ne retenir la JVPR que si une désignation irrévocable à l’origine est démontrée; la variabilité liée aux profits, à elle seule, ne suffit pas ici.
   - La conclusion clé du cas présenté est que l’analyse de dérivé incorporé échoue déjà sur la définition du dérivé fournie par IFRS 9.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI | - (non spécifiées) |
| 2. Juste valeur par résultat | OUI SOUS CONDITIONS | - Désignation irrévocable à la JVPR dès la comptabilisation initiale. |
| 3. Dérivé incorporé séparé | NON | - (non spécifiées) |

### 1. Coût amorti
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le prêt est d’abord un passif financier, et IFRS 9 prévoit le coût amorti comme règle générale pour les passifs financiers. Le fait que l’intérêt soit variable et dépende des profits résiduels n’impose pas en soi la JVPR; les flux contractuels estimés peuvent être révisés et l’ajustement du coût amorti est alors comptabilisé en résultat.

**Implications pratiques**: Comptabiliser la dette au coût amorti et réviser les flux contractuels estimés via le taux d’intérêt effectif d’origine, avec effet en résultat.

**Référence**:
 - 4.2.1
    >An entity shall classify all financial liabilities as subsequently measured at amortised cost, except for:
 - 5.7.2
    >shall be recognised in profit or loss when the financial liability is derecognised and through the amortisation process.
 - B5.4.6
    >it shall adjust the ... amortised cost of the financial liability ... to reflect actual and revised estimated contractual cash flows.

### 2. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Désignation irrévocable à la JVPR dès la comptabilisation initiale.

**Raisonnment**:
Dans les faits fournis, rien n’indique une obligation de mesurer ce passif à la JVPR du seul fait de l’intérêt indexé sur les profits. En revanche, ce traitement pourrait s’appliquer si l’entité avait irrévocablement désigné l’instrument à la JVPR lors de la comptabilisation initiale; à défaut, ce n’est pas le traitement de base ici.

**Implications pratiques**: Si cette désignation initiale existe, la dette entière est mesurée à la JVPR plutôt qu’au coût amorti.

**Référence**:
 - 4.2.2
    >may, at initial recognition, irrevocably designate a financial liability as measured at fair value through profit or loss
 - B4.3.9
    >this Standard permits the entire instrument to be designated as at fair value through profit or loss.

### 3. Dérivé incorporé séparé
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Sur les faits décrits, la clause de rendement dépend des profits résiduels de l’emprunteur/émetteur, donc d’une variable non financière spécifique à une partie au contrat. Or le texte fourni exige qu’un instrument séparé avec les mêmes termes réponde à la définition d’un dérivé; cette condition n’est pas satisfaite ici, donc la séparation d’un dérivé incorporé ne s’impose pas.

**Implications pratiques**: Ne pas scinder la clause de participation aux profits comme dérivé incorporé sur la base des faits fournis; traiter la dette comme un passif financier unique.

**Référence**:
 - 4.3.1
    >provided in the case of a non-financial variable that the variable is not specific to a party to the contract.
 - 4.3.3
    >a separate instrument with the same terms as the embedded derivative would meet the definition of a derivative
 - 4.3.4
    >If an embedded derivative is separated, the host contract shall be accounted for in accordance with the appropriate Standards.
