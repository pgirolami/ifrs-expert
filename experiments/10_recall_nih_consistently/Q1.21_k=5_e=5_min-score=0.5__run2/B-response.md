{
  "assumptions_fr": [
    "La créance de dividendes est un poste monétaire intragroupe comptabilisé, libellé en devise étrangère.",
    "La question est analysée dans le contexte des états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, IFRS 9 prévoit une exception permettant de désigner le risque de change d’un poste monétaire intragroupe comme élément couvert lorsque les écarts de change ne sont pas entièrement éliminés. La situation décrite correspond à cette exception."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un poste monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, la créance de dividendes est supposée être un poste monétaire intragroupe déjà comptabilisé en devise.\nIFRS 9 interdit en principe les éléments intragroupe comme éléments couverts en consolidation, mais crée une exception explicite pour le seul risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés.\nComme la question indique précisément une exposition de change dans les comptes consolidés, cette exception est la bonne base de désignation.",
      "conditions_fr": [
        "La désignation ne peut viser que le risque de change.",
        "Les écarts de change sur ce poste ne doivent pas être entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Le receivable intragroupe peut être désigné comme élément couvert, mais uniquement au titre de son risque de change dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction intragroupe future et hautement probable.\nOr, ici, le dividende a déjà donné lieu à une créance comptabilisée ; l’exposition porte donc sur un poste monétaire existant et non sur un flux futur encore prévu.\nLe modèle de cash flow hedge d’une transaction intragroupe prévue ne correspond pas à ce fait précis.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette situation comme couverture d’une transaction intragroupe future hautement probable.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... or a highly probable forecast transaction"
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
      "reasoning_fr": "Cette approche concerne le risque de change attaché à un investissement net dans une activité étrangère, c’est-à-dire à un montant d’actifs nets de la foreign operation.\nLa question vise au contraire une créance de dividendes intragroupe déjà comptabilisée ; rien dans les faits fournis n’indique qu’elle constitue l’investissement net lui-même.\nLe modèle de net investment hedge n’est donc pas le traitement pertinent pour cette exposition.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette créance de dividendes ne doit pas être traitée comme élément couvert d’une couverture d’investissement net.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "7",
          "excerpt": "hedges the foreign currency risk arising from its net investments in foreign operations"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation pertinente est celle du seul risque de change du poste monétaire intragroupe déjà reconnu.",
    "Le point de contrôle décisif est que les écarts de change sur cette créance subsistent en consolidation et ne sont pas entièrement éliminés.",
    "Pour ce fait précis, les modèles de cash flow hedge et de net investment hedge doivent être écartés."
  ]
}
