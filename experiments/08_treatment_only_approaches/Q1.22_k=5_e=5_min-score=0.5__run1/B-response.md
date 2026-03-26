{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe est libellée en devise et constitue un élément monétaire entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "La désignation de couverture satisfait par ailleurs aux critères d’éligibilité, de documentation et d’efficacité d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, l’interdiction générale visant les éléments intragroupe est écartée pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change affectent le résultat consolidé. Pour une créance de dividende déjà reconnue, la couverture de juste valeur est la voie la plus directe; une couverture de flux peut aussi être documentée si l’objectif vise bien la variabilité des flux."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif monétaire reconnu en devise; sous l’hypothèse que ses écarts de change ne sont pas totalement éliminés, l’exception d’IFRS 9 6.3.6 permet de la traiter comme élément couvert en consolidation.\nLa couverture de juste valeur est la lecture la plus directe, car elle vise la variation de valeur d’un actif reconnu attribuable au risque de change et affectant le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe reconnu et libellé en devise.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "Le risque désigné est la composante de change de cet élément monétaire.",
        "La relation de couverture est formellement documentée dès l’origine et respecte les critères d’efficacité et de hedge ratio."
      ],
      "practical_implication_fr": "Il est permis de documenter la créance de dividende comme élément couvert de juste valeur au titre du seul risque de change en comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la même créance reconnue peut aussi être analysée comme une exposition à la variabilité des flux de règlement en monnaie fonctionnelle, due au change, pouvant affecter le résultat consolidé.\nCette voie reste toutefois conditionnelle: il faut démontrer que l’objectif de gestion vise bien la variabilité des flux, et satisfaire à l’exception de 6.3.6 ainsi qu’aux critères de documentation et d’efficacité de 6.4.1.",
      "conditions_fr": [
        "La créance reconnue expose le groupe à une variabilité des flux de règlement en monnaie fonctionnelle liée au change.",
        "Les écarts de change affectent le résultat consolidé.",
        "La désignation repose sur l’exception applicable au risque de change d’un élément monétaire intragroupe en consolidation.",
        "La documentation IFRS 9 identifie l’instrument de couverture, l’élément couvert, le risque couvert et le hedge ratio."
      ],
      "practical_implication_fr": "La documentation doit montrer que l’objet couvert est la variabilité des flux de règlement en monnaie fonctionnelle, et pas seulement la réévaluation du poste.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif est de démontrer, en consolidation, que les écarts de change sur la créance/dette de dividende intragroupe ne sont pas totalement éliminés et affectent le résultat consolidé.",
    "La documentation doit viser uniquement la composante de risque de change de l’élément monétaire intragroupe, pas le dividende intragroupe en tant que tel de manière générale.",
    "La relation de couverture doit être désignée dès l’origine avec l’instrument de couverture, l’élément couvert, la nature du risque, le hedge ratio et l’analyse des sources d’inefficacité.",
    "Pour une créance déjà comptabilisée, la couverture de juste valeur est en pratique l’option la plus directement alignée avec les textes fournis; la couverture de flux exige une justification plus explicite de la variabilité des flux en monnaie fonctionnelle."
  ]
}
