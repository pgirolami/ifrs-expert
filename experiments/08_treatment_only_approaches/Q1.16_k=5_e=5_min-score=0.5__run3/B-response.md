{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré, de sorte qu’une créance et une dette intragroupe reconnues existent.",
    "Cette créance/dette est un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation au niveau consolidé, car IFRS 9 permet par exception de désigner le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. La documentation doit toutefois satisfaire dès l’origine aux exigences formelles et d’efficacité d’IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividendes intragroupe est un actif monétaire reconnu.\nSous les hypothèses données, IFRS 9 6.3.6 autorise en consolidation la désignation du risque de change sur un élément monétaire intragroupe dont les écarts ne sont pas totalement éliminés.\nLe modèle de couverture de juste valeur est donc utilisable si l’entité documente que le risque couvert est la variation de valeur de cette créance attribuable au change et respectent les critères de 6.4.1.",
      "conditions_fr": [
        "La créance intragroupe est reconnue et constitue un élément monétaire.",
        "Les entités concernées ont des monnaies fonctionnelles différentes et les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée à l’origine, avec test d’efficacité conforme à IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "L’entité peut documenter au niveau consolidé une couverture du risque de change de la créance par un instrument de couverture éligible.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Dans cette situation, IFRS 9 6.5.2(b) permet aussi qu’un actif reconnu soit l’élément couvert d’un cash flow hedge.\nCompte tenu de l’exception de 6.3.6, le caractère intragroupe n’empêche pas la désignation au niveau consolidé si le risque de change affecte bien le résultat consolidé.\nCette voie n’est applicable que si l’entité documente que le risque couvert est la variabilité des flux de trésorerie en monnaie fonctionnelle jusqu’au règlement et satisfait aux critères de 6.4.1.",
      "conditions_fr": [
        "La créance intragroupe expose le groupe à une variabilité de flux de trésorerie en monnaie fonctionnelle liée au change jusqu’au règlement.",
        "Le risque de change sur l’élément monétaire intragroupe affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation.",
        "La désignation, la stratégie de couverture et l’évaluation de l’efficacité sont documentées dès l’origine conformément à IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "L’entité peut retenir une documentation de cash flow hedge si elle aligne clairement le risque couvert sur la variabilité des flux liée au change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La conclusion vaut au niveau consolidé et repose sur l’exception d’IFRS 9 6.3.6 ; sans écarts de change non totalement éliminés, l’élément intragroupe ne serait pas éligible.",
    "La documentation doit être établie dès l’origine et identifier l’instrument de couverture, la créance couverte, le risque de change couvert et la méthode d’évaluation de l’efficacité.",
    "IFRIC 16 ne doit pas être appliquée par analogie ici : son champ vise les couvertures de net investments in foreign operations, pas une créance de dividendes intragroupe.",
    "Le choix entre fair value hedge et cash flow hedge doit être cohérent avec l’objectif de gestion du risque effectivement documenté pour cette créance."
  ]
}
