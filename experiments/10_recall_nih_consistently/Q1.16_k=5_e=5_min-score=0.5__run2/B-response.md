{
  "assumptions_fr": [
    "La créance de dividende est libellée dans une monnaie différente de la monnaie fonctionnelle pertinente.",
    "La question porte sur les états financiers consolidés et sur l’application de la comptabilité de couverture selon les IFRS."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance de dividende constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. La base IFRS pertinente est alors l’exception visant le risque de change d’un élément monétaire intragroupe, et non une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La situation décrite vise une créance intragroupe déjà constatée, exposée au change au niveau consolidé. IFRS 9 admet par exception que le risque de change d’un élément monétaire intragroupe soit désigné en couverture en consolidé si les écarts de change correspondants ne sont pas totalement éliminés, notamment entre entités ayant des monnaies fonctionnelles différentes.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les gains ou pertes de change sur cette créance ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit être établie au niveau consolidé sur le risque de change résiduel attaché à la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est un actif reconnu, et la définition de la couverture de juste valeur vise l’exposition aux variations de valeur d’un actif reconnu attribuables à un risque pouvant affecter le résultat. Dans cette situation, cette voie peut convenir pour le risque de change de la créance, mais seulement si l’élément intragroupe est d’abord éligible en consolidé au titre de l’exception de l’article 6.3.6.",
      "conditions_fr": [
        "La créance expose le résultat consolidé à des écarts de change.",
        "L’éligibilité de l’élément monétaire intragroupe en consolidation est démontrée."
      ],
      "practical_implication_fr": "Si cette voie est retenue, la documentation doit viser la variation de valeur de la créance attribuable au change.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Les faits décrivent une créance de dividende déjà comptabilisée, et non une transaction intragroupe future hautement probable. Dans le contexte fourni, la logique de cash flow hedge est surtout illustrée pour la variabilité de flux futurs ou pour des transactions intragroupe prévisionnelles ; ici, l’enjeu principal est la réévaluation de change d’une créance existante.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n’est pas la base la plus adaptée pour documenter la situation telle qu’elle est décrite.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "B6.3.5",
          "excerpt": "a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Une créance de dividende intragroupe n’est pas, dans les faits décrits, un montant de net assets d’une activité étrangère mais une créance intercompany distincte. IFRIC 16 réserve ce modèle au risque de change provenant d’un investissement net dans une activité étrangère, ce qui ne correspond pas à la créance de dividende ici.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation ne doit pas être structurée comme une couverture d’investissement net sur ces faits.",
      "references": [
        {
          "section": "8",
          "excerpt": "applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation et la documentation doivent être formelles dès l’origine de la relation de couverture.",
    "Il faut démontrer en consolidé que les écarts de change sur la créance ne sont pas totalement éliminés.",
    "La documentation doit identifier la créance de dividende, l’instrument de couverture, le risque de change couvert et la méthode d’appréciation de l’efficacité.",
    "Si la créance est éliminée sans effet résiduel de change dans le résultat consolidé, la documentation de couverture ne sera pas recevable sur ces faits."
  ]
}
