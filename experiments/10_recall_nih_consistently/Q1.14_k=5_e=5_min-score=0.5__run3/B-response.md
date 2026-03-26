{
  "assumptions_fr": [
    "On suppose que la créance de dividende intragroupe comptabilisée est un élément monétaire libellé en devise étrangère.",
    "On suppose que la question est posée au niveau des états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement via l’exception IFRS 9 relative à un élément monétaire intragroupe. La documentation de couverture est possible seulement si cette créance de dividende en devise crée des écarts de change qui ne sont pas totalement éliminés en consolidation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée peut relever de l’exception visant un élément monétaire intragroupe. Mais l’exception ne joue que si cette créance expose le groupe à des écarts de change non totalement éliminés en consolidation; à défaut, la règle générale sur les positions intragroupe empêche la désignation.",
      "conditions_fr": [
        "La créance de dividende et la dette intragroupe correspondante concernent des entités du groupe dont les monnaies fonctionnelles diffèrent.",
        "Les écarts de change sur cet élément monétaire ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation peut viser la créance de dividende intragroupe comme élément monétaire existant, si l’exposition de change subsiste au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        },
        {
          "section": "6.3.6",
          "excerpt": "that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette voie ne correspond pas aux faits décrits, car l’exposition provient d’une créance de dividende déjà comptabilisée et non d’une transaction intragroupe encore future. Le modèle visé ici suppose une transaction intragroupe hautement probable; ce n’est plus le cas une fois le dividende reconnu en créance.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette relation comme une couverture de transaction prévue intragroupe.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Cette approche ne vise pas une créance de dividende intragroupe isolée, mais l’exposition de change attachée à un investissement net dans une activité étrangère. Les textes fournis rattachent l’élément couvert aux net assets de l’activité étrangère; ce n’est pas la nature de l’exposition décrite dans la question.",
      "conditions_fr": [],
      "practical_implication_fr": "Le modèle de couverture d’investissement net ne doit pas être utilisé pour une créance de dividende intragroupe déjà comptabilisée.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Qualifier d’abord l’exposition comme une créance de dividende intragroupe existante, et non comme une transaction future.",
    "Vérifier et documenter que les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation, ce qui suppose en pratique des monnaies fonctionnelles différentes.",
    "Si cette condition est remplie, formaliser dès l’origine la désignation, l’instrument de couverture, le risque de change couvert et la méthode d’évaluation de l’efficacité."
  ]
}
