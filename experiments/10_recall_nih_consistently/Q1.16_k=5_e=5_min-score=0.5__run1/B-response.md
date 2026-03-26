{
  "assumptions_fr": [
    "La créance de dividende est supposée être un actif monétaire reconnu, libellé en devise étrangère.",
    "La question est analysée au niveau des états financiers consolidés selon IFRS 9, IFRIC 16 n’étant pertinente que si l’exposition était qualifiée d’investissement net dans une activité étrangère."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidé, le risque de change d’une créance monétaire intragroupe peut être désigné comme élément couvert si les écarts de change correspondants ne sont pas totalement éliminés en consolidation. Dans les faits décrits, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est supposée être un actif monétaire intragroupe déjà comptabilisé en devise.\nIFRS 9 admet, en consolidé, la désignation du risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation.\nLe modèle cohérent est la couverture de juste valeur, car l’exposition porte sur la valeur de la créance reconnue affectée par le change.",
      "conditions_fr": [
        "Les écarts de change sur la créance intragroupe ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation de couverture peut viser la créance reconnue et le risque de change qui affecte son évaluation en consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans les faits décrits, la créance de dividende est déjà comptabilisée et son montant nominal est fixé dans la devise de la créance.\nL’exposition identifiée tient à la conversion en monnaie fonctionnelle d’un actif monétaire reconnu, et non à une variabilité de flux futurs au sens du cash flow hedge.\nCe modèle ne correspond donc pas à cette situation précise.",
      "conditions_fr": [],
      "practical_implication_fr": "Documenter la relation comme une couverture de flux de trésorerie serait difficilement cohérent avec la nature d’une créance de dividende déjà reconnue.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Une créance de dividende intragroupe n’est pas, dans les faits décrits, un montant de net assets d’une activité étrangère mais un élément monétaire séparé.\nIFRIC 16 réserve ce modèle aux couvertures d’investissement net dans une activité étrangère et précise qu’il ne doit pas être appliqué par analogie.\nCe traitement ne s’applique donc pas à la créance de dividende visée par la question.",
      "conditions_fr": [],
      "practical_implication_fr": "La relation ne doit pas être documentée comme une couverture d’investissement net si l’objet couvert est la créance de dividende elle-même.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie dès l’origine de la relation de couverture, avec identification de l’instrument de couverture, de la créance couverte, du risque de change couvert et de la méthode d’évaluation de l’efficacité.",
    "Le point décisif en consolidé est de démontrer que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés en consolidation.",
    "La présente conclusion vise uniquement une créance de dividende déjà reconnue; elle ne traite pas un dividende intragroupe encore non comptabilisé."
  ]
}
