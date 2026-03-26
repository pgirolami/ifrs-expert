{
  "assumptions_fr": [
    "La question porte sur les états financiers consolidés du groupe.",
    "La créance de dividendes intragroupe est un poste monétaire comptabilisé qui crée une exposition au risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : en consolidé, le risque de change d’un poste monétaire intragroupe peut être désigné comme élément couvert par exception à la règle générale d’exclusion des transactions intragroupe. Il faut que ce risque génère des écarts de change non intégralement éliminés en consolidation ; dans les faits décrits, les modèles pertinents sont la couverture de juste valeur ou de flux de trésorerie, pas la couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividendes est décrite comme une créance intragroupe déjà comptabilisée ; elle entre donc, par nature, dans la catégorie des actifs reconnus.\nEn consolidé, l’exception de l’IFRS 9 permet de désigner le risque de change d’un poste monétaire intragroupe si les écarts de change ne sont pas entièrement éliminés. Dans ce cas, une couverture de juste valeur est compatible avec un actif reconnu exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance doit constituer un poste monétaire intragroupe.",
        "Le risque de change doit générer des gains ou pertes de change non intégralement éliminés en consolidation."
      ],
      "practical_implication_fr": "Le groupe peut désigner le risque de change de la créance de dividendes en couverture de juste valeur si l’exposition résiduelle apparaît bien en résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "La même exception d’éligibilité en consolidé vaut pour le risque de change du poste monétaire intragroupe, sous réserve que l’exposition affecte le résultat consolidé.\nDans cette situation, si le groupe vise la variabilité du flux encaissé en monnaie fonctionnelle au dénouement de la créance de dividendes, le modèle de couverture de flux de trésorerie peut aussi correspondre à un actif reconnu.",
      "conditions_fr": [
        "La créance doit constituer un poste monétaire intragroupe.",
        "Le risque de change doit affecter le résultat consolidé parce qu’il n’est pas entièrement éliminé en consolidation.",
        "La relation de couverture doit viser la variabilité du flux encaissé liée au change lors du règlement de la créance."
      ],
      "practical_implication_fr": "Ce modèle est envisageable si le groupe documente la couverture comme une protection du montant encaissé en monnaie fonctionnelle au règlement du dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits portent sur une créance de dividendes intragroupe, pas sur le risque de change attaché à un investissement net dans une activité à l’étranger.\nOr ce modèle vise un montant de net assets d’une foreign operation. En l’état, la créance de dividendes ne correspond donc pas à l’élément couvert de cette relation de couverture.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe ne devrait pas fonder la désignation de cette créance sur le modèle de couverture d’investissement net.",
      "references": [
        {
          "section": "6.5.13",
          "excerpt": "Hedges of a net investment in a foreign operation"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que les entités concernées ont des monnaies fonctionnelles différentes et que les écarts de change sur la créance/payable intragroupe ne sont pas intégralement éliminés en consolidation.",
    "Limiter la désignation au risque de change de la créance de dividendes ; la règle générale IFRS exclut sinon les éléments intragroupe en consolidé.",
    "Choisir un seul modèle de couverture cohérent avec l’objectif de gestion du risque au démarrage de la relation et le documenter dès l’inception."
  ]
}
