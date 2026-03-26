{
  "assumptions_fr": [
    "La question porte sur les états financiers consolidés.",
    "La créance est exposée à un risque de change du fait des fluctuations de cours."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance de dividendes constitue en consolidation un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Dans ce cas, la voie pertinente est le fair value hedge; le net investment hedge n’est pas adapté et IAS 39 n’est possible que si cette méthode a été élue."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, l’exposition décrite porte sur une créance déjà reconnue et sensible au change dans les comptes consolidés. IFRS 9 exclut en principe les éléments intragroupe en consolidation, mais admet une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés; dans ce cas, un fair value hedge est cohérent avec le risque porté par l’actif reconnu.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
        "Le risque documenté doit être le risque de change qui affecte le résultat consolidé."
      ],
      "practical_implication_fr": "Documenter en consolidation une relation de couverture visant le seul risque de change de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "applicability": "non",
      "reasoning_fr": "Sur les faits donnés, le sujet est une créance déjà comptabilisée qui crée une sensibilité de change dans les comptes consolidés. Le modèle de cash flow hedge vise une exposition à la variabilité des flux de trésorerie; ici, l’exposition décrite correspond d’abord à un risque de valeur d’un actif reconnu, et non à une transaction future intragroupe hautement probable.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas retenir ce modèle comme base principale de documentation pour cette créance existante.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "B6.3.5",
          "excerpt": "the foreign currency risk of a forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "La question vise une créance de dividendes intragroupe apparaissant en consolidation, pas des net assets d’une foreign operation. Or IFRIC 16 réserve ce modèle au risque de change lié à une net investment in a foreign operation; la créance n’est donc pas le bon objet de couverture sous ce modèle.",
      "conditions_fr": [],
      "practical_implication_fr": "Écarter la documentation en hedge of a net investment pour cette exposition.",
      "references": [
        {
          "section": "7",
          "excerpt": "hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "ias_39_hedge",
      "label_fr": "Hedge accounting selon IAS 39",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le contexte prévoit qu’une entité peut continuer à appliquer IAS 39 au lieu du chapitre 6 d’IFRS 9. Cette voie n’est donc ouverte dans cette situation que si le groupe a effectivement fait cette élection de méthode comptable; sinon l’analyse doit rester sous IFRS 9.",
      "conditions_fr": [
        "Le groupe doit avoir choisi, comme méthode comptable, de continuer à appliquer IAS 39 pour le hedge accounting."
      ],
      "practical_implication_fr": "Vérifier d’abord l’élection de méthode comptable avant de préparer la documentation.",
      "references": [
        {
          "section": "1",
          "excerpt": "an entity may choose as its accounting policy to continue to apply the hedge accounting requirements in IAS 39"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier dès l’origine que l’exposition de change sur la créance n’est pas totalement éliminée en consolidation et qu’elle affecte le résultat consolidé.",
    "Si la couverture est retenue, privilégier une documentation de fair value hedge visant explicitement le risque de change de la créance.",
    "Formaliser la désignation et la documentation de la relation de couverture à l’inception.",
    "Contrôler la méthode comptable du groupe: IFRS 9 par défaut, IAS 39 uniquement en cas d’élection existante."
  ]
}
