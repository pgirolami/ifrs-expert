{
  "assumptions_fr": [
    "La question porte sur des états financiers consolidés.",
    "La créance est un élément monétaire intragroupe libellé en devise étrangère.",
    "L’enjeu est la comptabilité de couverture du risque de change selon les IFRS."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, le risque de change d’un élément monétaire intragroupe peut être désigné comme élément couvert s’il génère des écarts de change non intégralement éliminés. Au vu des faits décrits, cela correspond au modèle de couverture de juste valeur, et non à une couverture de flux de trésorerie ni à une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la distribution a déjà été reconnue sous forme de créance, donc l’exposition porte sur un actif comptabilisé. IFRS 9 prévoit, en consolidation, une exception permettant au risque de change d’un élément monétaire intragroupe de qualifier comme élément couvert si les écarts de change ne sont pas totalement éliminés. Le modèle de couverture de juste valeur est celui qui correspond le mieux à cette créance reconnue.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
        "L’exposition doit entraîner des gains ou pertes de change non intégralement éliminés en consolidation."
      ],
      "practical_implication_fr": "La relation doit être documentée comme une couverture de juste valeur du risque de change de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Ici, le fait générateur est une créance de dividende déjà comptabilisée, et non une transaction intragroupe future hautement probable. Les extraits fournis rattachent explicitement l’exception intragroupe en cash flow hedge aux transactions prévues, alors que la question vise la réévaluation de change d’une créance existante. Ce traitement ne correspond donc pas aux faits décrits.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne doit pas être retenu pour cette créance de dividende déjà reconnue.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "B6.3.5",
          "excerpt": "a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, l’élément visé est une créance de dividende intragroupe, pas un montant de net assets d’une activité à l’étranger. IFRIC 16 limite ce modèle aux couvertures du risque de change découlant d’un investissement net dans une activité étrangère. Il ne s’applique donc pas à cette créance reconnue en consolidation.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette créance ne doit pas être documentée comme élément couvert dans une couverture d’investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier à la date de désignation que les sociétés concernées ont des monnaies fonctionnelles différentes et que l’écart de change n’est pas intégralement éliminé en consolidation.",
    "Documenter dès l’origine la relation de couverture, l’élément couvert, le risque de change couvert et l’instrument de couverture.",
    "Limiter l’analyse à la créance déjà reconnue : si les faits portent en réalité sur un dividende seulement prévu, la conclusion peut changer."
  ]
}
