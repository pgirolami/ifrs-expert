{
  "assumptions_fr": [
    "La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle pertinente, de sorte qu’il existe une exposition de change dans les comptes consolidés.",
    "La demande porte sur les modèles possibles de documentation de couverture dans les comptes consolidés, et non sur une validation détaillée de toute l’éligibilité ou de l’efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, la voie pertinente est la couverture de juste valeur si la créance de dividende en devise demeure bien une exposition reconnue au change en consolidation.\nLa couverture d’investissement net ne vise pas, sur les faits donnés, une créance de dividende mais un montant de net assets d’une opération étrangère."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende a été comptabilisé en créance ; sur l’hypothèse retenue, cette créance en devise crée une exposition de change dans les comptes consolidés.\nComme les écarts de change des actifs monétaires vont en résultat et qu’un actif couvert suit les règles de comptabilité de couverture, une documentation de couverture de juste valeur peut être appliquée si la créance est bien l’exposition conservée en consolidation.",
      "conditions_fr": [
        "La créance de dividende doit rester une exposition reconnue au change dans les comptes consolidés.",
        "La relation de couverture doit être formellement désignée et suivie comme relation de couverture IFRS 9."
      ],
      "practical_implication_fr": "L’objectif est de compenser en résultat consolidé la partie change de la créance par celle de l’instrument de couverture.",
      "references": [
        {
          "section": "B3.1.2",
          "excerpt": "Unconditional receivables and payables are recognised as assets or liabilities"
        },
        {
          "section": "B5.7.2",
          "excerpt": "foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss"
        },
        {
          "section": "5.7.3",
          "excerpt": "hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, l’objet visé est la partie change d’une créance de dividende intragroupe, et non un montant de net assets d’une opération étrangère.\nOr IFRIC 16 limite ce modèle aux couvertures d’un investissement net ; sur les faits donnés, ce traitement ne s’applique donc pas à ce dividende.",
      "conditions_fr": [
        "L’objet couvert devrait être un montant de net assets d’une opération étrangère, ce qui n’est pas le cas ici."
      ],
      "practical_implication_fr": "Non pertinent ici : ce modèle viserait une exposition d’investissement net avec comptabilisation en OCI puis reclassement à la cession.",
      "references": [
        {
          "section": "8",
          "excerpt": "applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "hedged item can be an amount of net assets equal to or less than the carrying amount"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance de dividende en devise subsiste comme exposition de change dans les comptes consolidés.",
    "Si la couverture de juste valeur est retenue, documenter dès l’origine la relation entre la créance reconnue et l’instrument de couverture.",
    "Suivre séparément les effets de change en résultat consolidé pour démontrer l’effet de compensation recherché.",
    "Ne pas utiliser une documentation de couverture d’investissement net pour cette créance de dividende, sauf si l’objet couvert est en réalité un montant de net assets d’une opération étrangère."
  ]
}
