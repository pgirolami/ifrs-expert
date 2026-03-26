{
  "assumptions_fr": [
    "La créance de dividende intragroupe est libellée en devise et génère une exposition de change dans les comptes consolidés.",
    "La question porte uniquement sur les modèles de comptabilité de couverture à apprécier dans les comptes consolidés pour cette exposition de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, la voie pertinente est la couverture de flux de trésorerie, si l'exposition de change subsiste bien en consolidation et est documentée au niveau consolidé. La couverture d'investissement net ne vise pas la créance de dividende elle-même mais un montant de net assets d'une opération étrangère."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende a déjà été comptabilisé en créance et, selon l'hypothèse retenue, cette créance en devise crée une exposition de change dans les comptes consolidés.\nComme cette exposition peut affecter le résultat consolidé, une documentation de couverture de flux de trésorerie peut être utilisée pour la partie change de cette créance, à condition qu'elle soit formalisée et suivie au niveau consolidé.",
      "conditions_fr": [
        "La créance de dividende en devise expose encore le groupe au risque de change au moment de la désignation.",
        "La relation de couverture est désignée et documentée dans les comptes consolidés."
      ],
      "practical_implication_fr": "Il faut documenter au niveau consolidé le risque de change visé, l'instrument de couverture et le suivi de la relation de couverture.",
      "references": [
        {
          "section": "6.1.1",
          "excerpt": "manage exposures arising from particular risks that could affect profit or loss"
        },
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Dans les faits décrits, l'élément visé est une créance de dividende intragroupe déjà comptabilisée, donc un poste monétaire distinct.\nOr IFRIC 16 limite ce modèle à la couverture du risque de change d'un investissement net dans une opération étrangère, c'est-à-dire d'un montant de net assets. Cette documentation ne convient donc pas à la créance de dividende elle-même dans les comptes consolidés.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter la partie change de cette créance comme une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter la relation de couverture au niveau des comptes consolidés, et non seulement dans les comptes sociaux.",
    "Vérifier avant désignation que la créance de dividende en devise crée encore une exposition de change dans le périmètre consolidé.",
    "Retenir la couverture de flux de trésorerie pour la partie change de la créance si ces conditions sont remplies.",
    "Écarter la couverture d'investissement net pour cette créance, car ce modèle vise les net assets d'une opération étrangère."
  ]
}
