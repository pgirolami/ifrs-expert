{
  "assumptions_fr": [
    "L’analyse est faite dans les états financiers consolidés du groupe.",
    "La créance de dividende intragroupe est un poste monétaire exposé à un risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation le risque de change d’une créance de dividende intragroupe peut être documenté dans une relation de couverture si ce poste monétaire génère des écarts de change non entièrement éliminés. Le cadrage le plus direct est la couverture de juste valeur ; la couverture d’investissement net ne correspond pas au fait décrit."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé en créance à recevoir, donc il s’agit d’un actif reconnu. IFRS 9 prévoit expressément qu’en consolidation le risque de change d’un poste monétaire intragroupe peut être un élément couvert si les écarts de change ne sont pas totalement éliminés. Dans ce cas, une documentation formelle de la relation de couverture est possible.",
      "conditions_fr": [
        "Les écarts de change sur la créance intragroupe ne doivent pas être entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La créance de dividende peut être désignée comme élément couvert au titre du risque de change en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait générateur n’est plus une transaction intragroupe future : la créance de dividende est déjà reconnue. Néanmoins, le modèle de cash flow hedge vise aussi un actif reconnu ; il peut donc être envisagé seulement si le risque désigné est bien la variabilité des flux liée au change sur cette créance et si cette variabilité affecte le résultat consolidé. Ce n’est pas le cadrage le plus immédiat du cas.",
      "conditions_fr": [
        "L’exposition couverte doit être formulée comme la variabilité des flux liée au change sur la créance déjà reconnue, et non comme une transaction intragroupe encore future.",
        "Le risque de change doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit viser la variabilité des flux en monnaie fonctionnelle sur la créance reconnue.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Le fait décrit porte sur une créance de dividende intragroupe déjà comptabilisée, pas sur un montant de net assets d’une activité étrangère. IFRIC 16 réserve ce modèle au risque de change sur l’investissement net lui-même entre la monnaie fonctionnelle de l’activité étrangère et celle du parent. Ce traitement ne correspond donc pas à cette créance intragroupe.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter la créance de dividende sous le modèle de couverture d’investissement net.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie dès l’inception de la relation de couverture, avec identification de l’instrument, de la créance couverte, du risque de change et du hedge ratio.",
    "En consolidation, il faut vérifier et documenter que les écarts de change sur la créance de dividende intragroupe ne sont pas entièrement éliminés et qu’ils affectent le résultat consolidé.",
    "Pour ce fait précis, la couverture de juste valeur est le cadrage le plus naturel ; une couverture de flux de trésorerie exige une justification plus ciblée sur la variabilité des flux de la créance reconnue."
  ]
}
