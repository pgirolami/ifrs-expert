{
  "assumptions_fr": [
    "L’analyse est conduite au niveau des états financiers consolidés.",
    "La créance de dividende intragroupe déjà comptabilisée est un élément monétaire exposé au risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en principe, car IFRS 9 prévoit une exception pour le risque de change sur un élément monétaire intragroupe en consolidation. Dans ce cas précis, la documentation reste toutefois subordonnée au fait que les écarts de change ne soient pas totalement éliminés en consolidation et que les critères de désignation, de documentation et d’efficacité soient remplis."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les faits visent une créance de dividende intragroupe déjà comptabilisée ; sous l’hypothèse qu’il s’agit d’un élément monétaire exposé au change, l’exception d’IFRS 9 6.3.6 peut s’appliquer en consolidation.\nAu stade actuel de reconnaissance, une couverture de juste valeur d’un actif reconnu est cohérente avec 6.5.2(a), sous réserve que les écarts de change affectent le résultat consolidé et que la désignation, la documentation initiale et l’efficacité exigées par 6.4.1 soient respectées.",
      "conditions_fr": [
        "Le risque de change sur la créance intragroupe doit générer des gains ou pertes non totalement éliminés en consolidation.",
        "La relation de couverture doit être formellement désignée et documentée à l’origine de la relation.",
        "La relation doit satisfaire aux exigences d’efficacité, y compris la relation économique et un hedge ratio approprié."
      ],
      "practical_implication_fr": "Il faut documenter la créance reconnue comme élément couvert, le risque de change visé et le dispositif de test d’efficacité pour les variations futures.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture de flux de trésorerie de la créance monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les faits portent aussi sur une créance intragroupe déjà reconnue ; il n’est donc pas nécessaire de reformuler le cas en transaction future pour analyser cette voie.\nSous les hypothèses retenues, 6.5.2(b) admet une couverture de flux de trésorerie d’un actif reconnu si la variabilité des flux de règlement en monnaie fonctionnelle due au change peut affecter le résultat consolidé, et 6.3.6 permet cette désignation en intragroupe si l’exposition n’est pas totalement éliminée en consolidation.",
      "conditions_fr": [
        "Le risque de change sur la créance intragroupe doit générer des gains ou pertes non totalement éliminés en consolidation.",
        "La variabilité des flux de règlement en monnaie fonctionnelle de la créance doit être l’exposition effectivement désignée.",
        "La relation de couverture doit être formellement désignée, documentée à l’origine et satisfaire aux tests d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "Il faut documenter la variabilité des flux de règlement restants de la créance reconnue et suivre l’efficacité de la couverture jusqu’au dénouement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1(c)",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être mise en place à l’origine de la relation de couverture ; elle ne couvre pas rétroactivement les écarts de change déjà constatés avant la désignation.",
    "Le point clé, en consolidation, est de démontrer que le risque de change sur la créance de dividende intragroupe produit des effets en résultat consolidé qui ne sont pas totalement éliminés.",
    "Le choix entre juste valeur et flux de trésorerie doit être aligné sur le risque effectivement documenté sur la créance déjà comptabilisée et sur la manière dont l’efficacité sera mesurée."
  ]
}
