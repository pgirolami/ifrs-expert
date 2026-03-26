{
  "assumptions_fr": [
    "La question est analysée dans le cadre des états financiers consolidés.",
    "Le dividende a été déclaré et a créé une créance/dette intragroupe monétaire libellée en devise."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance/dette de dividende constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, le modèle pertinent est celui de la couverture du risque de change d’un poste monétaire intragroupe; les deux autres traitements ne correspondent pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, l’exposition visée est une créance/dette intragroupe déjà comptabilisée au titre d’un dividende déclaré. IFRS 9 prévoit précisément une exception pour le risque de change d’un poste monétaire intragroupe en consolidation, mais seulement si ce poste crée des gains ou pertes de change qui ne sont pas totalement éliminés en consolidation.",
      "conditions_fr": [
        "la créance/dette de dividende génère des écarts de change qui ne sont pas totalement éliminés en consolidation",
        "cela suppose en pratique une exposition entre entités du groupe ayant des monnaies fonctionnelles différentes"
      ],
      "practical_implication_fr": "La documentation peut viser la créance/dette de dividende comme élément couvert pour son risque de change en consolidation, si la condition d’écarts non totalement éliminés est satisfaite.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.3.6",
          "excerpt": "if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_intragroup_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits portent sur un dividende déjà déclaré ayant créé une créance/dette comptabilisée. Ce n’est donc plus une transaction intragroupe future hautement probable, qui est le champ visé par ce modèle de cash flow hedge.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne doit pas être retenu pour documenter la couverture de cette exposition déjà reconnue.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable."
        },
        {
          "section": "B6.3.5",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "L’exposition décrite est une créance/dette de dividende intragroupe, et non un montant de net assets d’une activité étrangère. Le modèle de couverture d’investissement net vise le risque de change attaché à l’investissement net dans l’activité étrangère, pas un poste monétaire intragroupe né d’un dividende déclaré.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette exposition comme une couverture d’investissement net.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance/dette de dividende est bien un poste monétaire intragroupe créant des écarts de change non totalement éliminés en consolidation.",
    "Si cette condition est remplie, documenter la relation comme couverture du risque de change d’un poste monétaire intragroupe, et non comme couverture de flux de trésorerie d’une transaction future.",
    "La désignation et la documentation formelles de la relation de couverture doivent être établies à l’origine de la relation.",
    "Ne pas utiliser le modèle de couverture d’investissement net pour cette créance de dividende."
  ]
}
