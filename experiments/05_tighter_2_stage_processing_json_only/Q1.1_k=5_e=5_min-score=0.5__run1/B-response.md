{
  "assumptions": [
    "La créance de dividende intragroupe est un élément monétaire libellé dans une devise différente de la monnaie fonctionnelle d'au moins une entité.",
    "La question vise les comptes consolidés et les écarts de change correspondants peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement dans le cadre de l'exception IFRS 9 sur le risque de change d'un élément monétaire intragroupe et avec une documentation de couverture complète à l'origine. En revanche, la couverture d'investissement net ne vise pas la créance de dividende en tant que telle."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose une règle générale d'externalité en consolidation, puis prévoit une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés. Une créance de dividende reconnue peut donc être désignée, limitée à sa composante change, dans une couverture de juste valeur. Il faut en plus satisfaire aux exigences formelles de désignation, documentation et efficacité.",
      "conditions_fr": [
        "la créance de dividende est un actif monétaire reconnu",
        "les contreparties ont des monnaies fonctionnelles différentes",
        "les écarts de change ne sont pas totalement éliminés en consolidation",
        "seule la composante risque de change est désignée",
        "les exigences IFRS 9 de désignation, documentation et efficacité sont respectées"
      ],
      "practical_implication_fr": "Possible si vous documentez dès l'origine la créance comme élément couvert pour sa seule composante change.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "IFRS 9 6.3.7(a)",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "IFRS 9 6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet une couverture de flux de trésorerie d'un risque particulier affectant les flux d'un actif reconnu. Combinée avec l'exception sur les éléments monétaires intragroupe en devise, cette voie peut être retenue si la variabilité de change affecte le résultat consolidé. La désignation reste cantonnée au risque de change et doit être formalisée et testée selon IFRS 9.",
      "conditions_fr": [
        "l'élément intragroupe entre dans l'exception relative au risque de change des éléments monétaires intragroupe",
        "le risque de change affecte le résultat consolidé",
        "seule la composante risque de change est désignée",
        "les exigences IFRS 9 de désignation, documentation et efficacité sont respectées"
      ],
      "practical_implication_fr": "Possible si la documentation vise la variabilité des flux en devise rattachée à la créance et son effet en résultat consolidé.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "IFRS 9 6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "IFRS 9 6.4.1(b)-(c)",
          "excerpt": "at the inception ... there is formal designation and documentation ... the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 encadre uniquement la couverture du risque de change d'un investissement net dans une activité à l'étranger. La créance de dividende intragroupe n'est pas, en tant que telle, un montant de net assets désigné comme investissement net. Ce modèle ne convient donc pas à la créance, sauf si l'objet couvert devient l'investissement net lui-même.",
      "conditions_fr": [
        "ce modèle ne devient pertinent que si l'élément couvert est les actifs nets d'une activité à l'étranger et non la créance de dividende"
      ],
      "practical_implication_fr": "À écarter pour la créance elle-même; à envisager seulement si la stratégie porte sur l'investissement net dans l'entité étrangère.",
      "references": [
        {
          "section": "IFRIC 16 8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "IFRIC 16 10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        },
        {
          "section": "IFRIC 16 11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "no_hedge_accounting",
      "label_fr": "Absence de comptabilité de couverture en consolidation",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La règle IFRS 9 en consolidation est que les éléments couverts doivent en principe être avec une partie externe. Si la créance ne remplit pas l'exception spécifique des éléments monétaires intragroupe en devise, ou si les écarts n'affectent pas le résultat consolidé, aucune comptabilité de couverture n'est disponible. Le même résultat s'impose en cas d'absence de documentation initiale ou de non-respect des critères d'efficacité.",
      "conditions_fr": [
        "l'élément n'est pas un élément monétaire intragroupe éligible",
        "ou le risque de change n'affecte pas le résultat consolidé",
        "ou les critères IFRS 9 de documentation et d'efficacité ne sont pas satisfaits"
      ],
      "practical_implication_fr": "À retenir par défaut si l'exception intragroupe change ou les critères formels IFRS 9 ne sont pas remplis.",
      "references": [
        {
          "section": "IFRS 9 6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "IFRS 9 6.4.1(b)-(c)",
          "excerpt": "at the inception ... there is formal designation and documentation ... the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La base technique principale vient d'IFRS 9: règle générale d'externalité, puis exception limitée au risque de change des éléments monétaires intragroupe.",
    "La documentation doit être mise en place à l'origine de la relation de couverture et identifier l'instrument de couverture, l'élément couvert, le risque couvert et la méthode d'évaluation de l'efficacité.",
    "Il faut démontrer que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés en consolidation et qu'ils affectent le résultat consolidé.",
    "La désignation doit être limitée à la composante risque de change; le modèle d'investissement net ne doit pas être utilisé pour la créance de dividende elle-même.",
    "En pratique, le choix est donc entre une documentation de juste valeur, une documentation de flux de trésorerie, ou l'absence de comptabilité de couverture si les conditions IFRS 9 ne sont pas remplies."
  ]
}
