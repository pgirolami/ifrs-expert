{
  "assumptions_fr": [
    "La question porte sur des états financiers consolidés.",
    "La créance ou transaction liée au dividende crée une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, un élément intragroupe est en principe exclu comme élément couvert, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas entièrement éliminés et affectent le résultat consolidé. La couverture d’un investissement net n’est pas adaptée à une simple créance de dividende."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est traitée comme un actif reconnu exposé au change. En consolidation, la règle générale exclut les éléments intragroupe, mais l’exception d’IFRS 9 permet de couvrir le risque de change d’un élément monétaire intragroupe si les gains ou pertes de change ne sont pas entièrement éliminés et affectent le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende doit être un élément monétaire intragroupe exposé au risque de change.",
        "Les écarts de change sur cette créance doivent ne pas être entièrement éliminés en consolidation et affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Possible si la relation vise le risque de change sur la créance monétaire et son effet en résultat consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le contexte IFRS 9 admet un cash flow hedge d’un actif ou passif reconnu, et l’exception de 6.3.6 vise précisément le risque de change d’un élément monétaire intragroupe. Ici, cette voie n’est ouverte que si la variabilité liée au change sur la créance de dividende affecte le résultat consolidé et n’est pas entièrement neutralisée en consolidation.",
      "conditions_fr": [
        "La créance de dividende doit être un élément monétaire intragroupe dont le règlement est exposé au change.",
        "Le risque de change associé doit affecter le résultat consolidé et ne pas être entièrement éliminé en consolidation."
      ],
      "practical_implication_fr": "Possible si la relation documente la variabilité en monnaie fonctionnelle du règlement de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise le risque de change d’un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets, et non une créance de dividende intragroupe. Dans les faits décrits, l’exposition couverte est une créance monétaire spécifique, pas l’investissement net lui-même.",
      "conditions_fr": [],
      "practical_implication_fr": "À écarter pour une simple créance de dividende intragroupe.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, le point clé est de qualifier la créance de dividende comme élément monétaire intragroupe.",
    "Il faut vérifier et documenter que les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.",
    "Si ces conditions sont remplies, la désignation peut relever d’une couverture de juste valeur ou de flux de trésorerie; la couverture d’un investissement net ne convient pas à ces faits."
  ]
}
