{
  "assumptions_fr": [
    "La question est analysée dans le contexte des états financiers consolidés.",
    "Le montant à recevoir intragroupe crée bien une exposition au risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe n’est en principe pas éligible. Toutefois, si la créance de dividende constitue un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation et affecte le résultat consolidé, une couverture peut être documentée ; la couverture d’un investissement net n’est pas adaptée ici."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La règle générale exclut les éléments intragroupe en consolidation. Mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe ; une créance de dividende comptabilisée peut entrer dans ce cadre si les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, une couverture de juste valeur peut être documentée pour une créance déjà reconnue.",
      "conditions_fr": [
        "la créance de dividende est un élément monétaire intragroupe",
        "elle est exposée à un risque de change entre entités ayant des monnaies fonctionnelles différentes",
        "les gains ou pertes de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé"
      ],
      "practical_implication_fr": "Possible pour la créance déjà comptabilisée, sous réserve de démontrer l’exception intragroupe sur le risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 admet une couverture de flux de trésorerie pour la variabilité des flux d’un actif ou passif comptabilisé. Ici, ce modèle n’est envisageable que si l’encaissement futur de la créance de dividende reste exposé à un risque de change qui subsiste en consolidation et affecte le résultat consolidé. Sans l’exception applicable aux éléments monétaires intragroupe, la créance resterait inéligible.",
      "conditions_fr": [
        "la créance de dividende est un élément monétaire intragroupe",
        "la variabilité de l’encaissement en monnaie fonctionnelle provient du risque de change",
        "les effets de change affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "Envisageable si l’objectif est de couvrir la variabilité du règlement en monnaie fonctionnelle sur la créance intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Ce modèle vise uniquement le risque de change provenant d’un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets de cette activité. Une créance de dividende intragroupe comptabilisée ne correspond pas, dans les faits décrits, à un tel investissement net. Cette voie ne répond donc pas à l’exposition visée par la question.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas retenir ce modèle pour couvrir une créance de dividende intragroupe.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance de dividende est un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
    "Documenter en consolidation que les écarts de change sur cette créance ne sont pas totalement éliminés et qu’ils affectent le résultat consolidé.",
    "Rédiger dès l’inception la documentation de couverture exigée : instrument de couverture, créance couverte, risque de change visé et ratio de couverture.",
    "Écarter le modèle de couverture d’investissement net, qui ne correspond pas à une simple créance de dividende intragroupe."
  ]
}
