{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un solde monétaire comptabilisé, exposé au change dans les comptes consolidés.",
    "L'analyse est limitée aux modèles de comptabilité de couverture potentiellement mobilisables en consolidation au titre d'IFRS 9 et d'IFRIC 16.",
    "L'objectif est d'identifier les traitements envisageables sur ces faits, sans conclure au-delà des faits fournis."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Sur les faits donnés, la couverture de juste valeur est la voie la plus directement adaptée à une créance de dividende déjà comptabilisée en devise.\nUne couverture de flux peut être envisagée si la documentation vise les flux de règlement futurs; la couverture d'investissement net ne vise pas la créance elle-même."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l'élément visé est une créance de dividende déjà comptabilisée et exposée au change en consolidation.\nLes extraits fournis rattachent les écarts de change des actifs monétaires au résultat et prévoient un traitement spécifique des éléments couverts; cela correspond directement à une couverture de juste valeur de la partie change, sous réserve d'une désignation et d'une efficacité documentées.",
      "conditions_fr": [
        "La créance en devise doit être désignée comme élément couvert pour son risque de change.",
        "Un instrument de couverture éligible doit compenser cette exposition au niveau consolidé.",
        "La relation de couverture doit être documentée et démontrer son efficacité."
      ],
      "practical_implication_fr": "C'est le modèle le plus directement aligné avec une créance déjà reconnue.",
      "references": [
        {
          "section": "5.7.3",
          "excerpt": "A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        },
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende donnera lieu à un encaissement en devise; la partie change peut donc être analysée comme une variabilité des flux de règlement en consolidation.\nCependant, les extraits fournis ne donnent pas ici de règle détaillée sur l'éligibilité d'une créance déjà comptabilisée à ce modèle; son application reste donc conditionnelle à une documentation centrée sur les flux futurs de règlement.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux de règlement en devise du dividende.",
        "L'exposition couverte doit encore affecter les flux futurs au niveau consolidé.",
        "La relation de couverture doit être désignée et suivie comme couverture de flux."
      ],
      "practical_implication_fr": "Modèle possible, mais moins immédiatement naturel qu'une couverture de juste valeur pour une créance déjà constatée.",
      "references": [
        {
          "section": "6.1.1",
          "excerpt": "manage exposures arising from particular risks that could affect profit or loss"
        },
        {
          "section": "B5.7.2",
          "excerpt": "An exception is a monetary item that is designated as a hedging instrument in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, l'élément visé est la créance de dividende intragroupe et non un montant de net assets d'une opération étrangère.\nIFRIC 16 réserve la couverture d'investissement net au risque de change sur l'investissement net dans une opération étrangère; elle ne vise donc pas, sur ces faits, la seule créance de dividende.",
      "conditions_fr": [
        "Il faudrait que l'élément couvert soit un montant de net assets d'une opération étrangère.",
        "Le risque couvert devrait être celui entre la monnaie fonctionnelle de l'opération étrangère et celle du parent."
      ],
      "practical_implication_fr": "Ce modèle ne documente pas la partie change de la créance de dividende elle-même.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie au niveau consolidé en identifiant explicitement la seule composante change couverte.",
    "Pour une créance déjà comptabilisée, la couverture de juste valeur est l'option la plus lisible au regard des extraits fournis.",
    "La couverture d'investissement net doit être écartée si l'objectif est de couvrir la créance de dividende elle-même et non l'investissement net dans l'opération étrangère."
  ]
}
