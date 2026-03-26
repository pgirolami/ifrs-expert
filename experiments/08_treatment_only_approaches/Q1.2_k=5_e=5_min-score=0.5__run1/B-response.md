{
  "assumptions_fr": [
    "Sous l'hypothèse que la créance de dividende intragroupe, libellée en devise, crée bien une exposition de change dans les comptes consolidés.",
    "La question porte sur les modèles de comptabilité de couverture IFRS 9 à envisager pour cette exposition, sans préjuger du respect effectif de tous les critères formels de désignation, documentation et efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, une documentation de couverture peut être envisagée en comptes consolidés principalement via une couverture de juste valeur, et éventuellement via une couverture de flux de trésorerie si la documentation vise les flux futurs de règlement. En revanche, la couverture d'un investissement net ne correspond pas au fait décrit d'une créance de dividende intragroupe."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Sous l'hypothèse retenue, la créance de dividende est déjà comptabilisée et sa composante change affecte le résultat consolidé.\nLes extraits IFRS 9 renvoient explicitement au traitement des éléments couverts et des gains/pertes de change sur actifs monétaires.\nDans ce cadre, documenter une couverture de juste valeur de la composante change de la créance est cohérent avec la situation, sous réserve des critères IFRS 9 applicables.",
      "conditions_fr": [
        "La créance en dividende doit rester un élément reconnu exposé au change dans les comptes consolidés.",
        "La relation de couverture doit être formellement documentée et satisfaire aux exigences IFRS 9 de désignation et d'efficacité."
      ],
      "practical_implication_fr": "La documentation doit viser la composante change de la créance reconnue au bilan consolidé.",
      "references": [
        {
          "section": "5.7.3",
          "excerpt": "A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        },
        {
          "section": "5.7.2",
          "excerpt": "A gain or loss on a financial asset that is measured at amortised cost ... shall be recognised in profit or loss"
        },
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Sous l'hypothèse retenue, le règlement futur de la créance en devise expose encore le groupe à une variabilité de flux en monnaie fonctionnelle.\nL'objectif de la comptabilité de couverture est de refléter les activités de gestion du risque; les extraits fournis n'excluent donc pas une documentation visant cette variabilité.\nCette voie reste toutefois conditionnelle, car les critères détaillés de désignation et d'efficacité ne figurent pas dans les extraits fournis.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux de règlement futurs du dividende en devise dans les comptes consolidés.",
        "Les exigences IFRS 9 de documentation et d'efficacité doivent être satisfaites."
      ],
      "practical_implication_fr": "La documentation doit être centrée sur les flux futurs de règlement du dividende en devise au niveau consolidé.",
      "references": [
        {
          "section": "6.1.1",
          "excerpt": "The objective of hedge accounting is to represent, in the financial statements, the effect of an entity’s risk management activities"
        },
        {
          "section": "5.7.3",
          "excerpt": "A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        },
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Les textes fournis sur cette méthode visent uniquement le risque de change lié à un investissement net dans une opération étrangère.\nL'élément couvert y est un montant de net assets, égal ou inférieur à la valeur comptable de ces net assets, et non une créance de dividende intragroupe.\nDans les faits décrits, cette documentation ne correspond donc pas à l'exposition à couvrir.",
      "conditions_fr": [
        "Il faudrait que l'exposition porte sur des net assets d'une opération étrangère, et non sur un dividende intragroupe comptabilisé en créance."
      ],
      "practical_implication_fr": "Cette piste ne permet pas de documenter la partie change de la créance de dividende décrite.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Valider d'abord, au niveau consolidé, que la créance de dividende en devise laisse bien subsister une exposition de change; l'analyse ci-dessus repose sur cette hypothèse.",
    "Si une documentation est retenue, elle doit être alignée sur le risque effectivement géré: valeur de la créance reconnue pour la couverture de juste valeur, ou flux futurs de règlement pour la couverture de flux de trésorerie.",
    "La couverture d'investissement net doit être écartée pour ce cas, car les extraits fournis la réservent aux net investments dans des opérations étrangères.",
    "Les extraits fournis renvoient aux exigences détaillées de désignation et d'efficacité IFRS 9; leur respect reste indispensable avant mise en place."
  ]
}
