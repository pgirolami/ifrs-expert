{
  "assumptions_fr": [
    "Le dividende intragroupe donne naissance à une créance et à une dette monétaires libellées en devise au sein du groupe.",
    "La question vise l’application de la comptabilité de couverture d’IFRS 9 dans des comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en principe via une couverture de juste valeur, si la créance de dividende est un élément monétaire intragroupe en devise et si ses écarts de change ne sont pas intégralement éliminés en consolidation. La couverture de flux de trésorerie et la couverture d’un investissement net ne correspondent pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés en consolidation. Ici, le dividende a déjà donné lieu à une créance à recevoir reconnue; le modèle de couverture de juste valeur est donc celui qui correspond le mieux à un actif reconnu exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe libellé dans une devise autre que la monnaie fonctionnelle de l’une des entités concernées.",
        "Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation de couverture au niveau consolidé doit viser la créance monétaire intragroupe et mesurer l’inefficacité sur le risque de change couvert.",
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
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits portent sur un dividende intragroupe déjà déclaré, ayant donné lieu à la comptabilisation d’une créance à recevoir. Le contexte IFRS 9 vise, pour les transactions intragroupe en consolidation, les transactions hautement probables futures; ici, l’exposition n’est plus celle d’une transaction future mais celle d’un poste monétaire déjà reconnu.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne devrait pas être retenu pour une créance de dividende déjà comptabilisée dans la situation décrite.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
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
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche ne vise que le risque de change sur un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets de l’opération étrangère. Une créance de dividende intragroupe à recevoir est un poste de règlement intragroupe, distinct d’un investissement net.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter la créance de dividende comme instrument couvert d’une couverture d’investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "2",
          "excerpt": "The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que la créance de dividende est bien un poste monétaire en devise entre entités ayant des monnaies fonctionnelles différentes.",
    "Confirmer que les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas intégralement éliminés en consolidation.",
    "Documenter la relation de couverture au niveau consolidé en identifiant la créance, le risque de change couvert, l’instrument de couverture et la mesure de l’inefficacité."
  ]
}
