{
  "assumptions_fr": [
    "L’analyse est menée au regard d’IFRS 9, en comptes consolidés.",
    "L’exposition visée est un risque de change intragroupe entre entités du groupe ayant des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais pas du seul fait qu’une exposition de change distincte est identifiée. En consolidation, une créance sur dividendes intragroupe n’est éligible que si elle entre dans l’exception visant le risque de change d’un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation; sinon, la règle générale d’exclusion des éléments intragroupe s’applique."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance sur dividendes est, dans la situation décrite, une créance reconnue; le modèle de juste valeur peut donc viser son risque de change. Mais au niveau consolidé, un élément intragroupe est en principe exclu, sauf si la créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
      "conditions_fr": [
        "la créance sur dividendes constitue un élément monétaire intragroupe",
        "les écarts de change correspondants ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "Il faut démontrer que les écarts de change sur la créance subsistent au résultat consolidé malgré les éliminations intragroupe.",
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
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 admet une couverture de flux de trésorerie sur un actif ou passif reconnu; ce modèle peut donc être envisagé si le risque géré est la variabilité, en monnaie fonctionnelle, des flux de règlement de la créance sur dividendes. Ici encore, l’éligibilité au niveau consolidé dépend de l’exception applicable aux éléments monétaires intragroupe dont le risque de change affecte encore le résultat consolidé.",
      "conditions_fr": [
        "la créance sur dividendes constitue un élément monétaire intragroupe",
        "les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés"
      ],
      "practical_implication_fr": "La documentation doit viser les flux de règlement de la créance, avec la même vérification préalable des effets de change en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "1054",
          "excerpt": "the relevant period or periods during which the foreign currency risk of the hedged transaction affects profit or loss is when it affects consolidated profit or loss."
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "La question porte sur une créance intragroupe sur dividendes, c’est-à-dire sur un élément monétaire distinct, et non sur un montant de net assets d’une activité étrangère. Le modèle de couverture d’investissement net vise exclusivement le risque de change attaché à l’investissement net dans une activité étrangère; il ne correspond donc pas à cette exposition.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette créance ne doit pas être documentée comme une couverture d’investissement net.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "hedge of a net investment in a foreign operation"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation."
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Commencer par qualifier la créance sur dividendes comme élément monétaire intragroupe et identifier les monnaies fonctionnelles des entités concernées.",
    "Tester ensuite si les écarts de change sur cette créance sont encore présents en résultat consolidé après éliminations; sans cet effet résiduel, il n’y a pas d’éligibilité au niveau consolidé.",
    "Si l’éligibilité est confirmée, choisir et documenter le modèle retenu entre couverture de juste valeur et couverture de flux de trésorerie; ne pas utiliser le modèle d’investissement net."
  ]
}
