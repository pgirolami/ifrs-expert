{
  "assumptions_fr": [
    "La question vise la comptabilité de couverture du risque de change, dans des états financiers consolidés, pour une exposition née entre entités du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement via l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe en consolidation. Une créance de dividende déjà comptabilisée relève de cette logique seulement si elle génère des écarts de change non entièrement éliminés en consolidation; ce n’est ni une transaction future, ni une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la distribution a déjà été reconnue comme une créance : l’exposition est donc un poste existant entre sociétés du groupe, et non une transaction future.\nIFRS 9 prévoit une exception en consolidation pour le risque de change d’un élément monétaire intragroupe lorsqu’il crée des gains ou pertes de change non totalement éliminés.\nLa désignation peut donc être admise pour cette créance de dividende seulement si ce risque de change subsiste effectivement au niveau consolidé.",
      "conditions_fr": [
        "La créance de dividende constitue un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
        "Le risque de change sur cette créance génère des gains ou pertes non entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Vérifier les monnaies fonctionnelles des deux entités et démontrer que les écarts de change remontent bien dans le résultat consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.6",
          "excerpt": "if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Ici, la distribution intragroupe a déjà été reconnue sous forme de créance dans les comptes consolidés.\nL’exposition n’est donc plus une transaction intragroupe future hautement probable, mais un poste monétaire existant.\nLe modèle de cash flow hedge des transactions intragroupe prévues ne correspond pas à ce fait précis.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette relation comme une couverture de transaction future dès lors que la créance existe déjà.",
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
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe, et non sur un montant de net assets d’une activité étrangère.\nIFRIC 16 limite ce modèle aux couvertures d’un investissement net dans une activité étrangère.\nCette approche ne s’applique donc pas à la créance de dividende décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas assimiler la créance de dividende à un investissement net couvert au sens d’IFRIC 16.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La voie pertinente est l’exception d’IFRS 9 pour les éléments monétaires intragroupe, pas le modèle des transactions intragroupe prévues.",
    "Le point décisif est la persistance d’un risque de change non entièrement éliminé en consolidation.",
    "Si la couverture est retenue, la désignation et la documentation doivent être établies conformément à IFRS 9 6.4.1."
  ]
}
