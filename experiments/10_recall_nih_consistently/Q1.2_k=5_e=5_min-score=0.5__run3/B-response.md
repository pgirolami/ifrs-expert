{
  "assumptions_fr": [
    "La créance de dividende intragroupe est, dans les comptes consolidés, un actif monétaire libellé en devise étrangère.",
    "La question porte sur les modèles IFRS pouvant viser l’exposition de change reflétée dans les comptes consolidés sur ce poste."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans les faits fournis, l’écart de change sur la créance va par défaut en résultat consolidé. Une documentation de couverture n’est envisageable de manière ciblée que via une couverture de juste valeur de la créance en devise; la couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas naturellement à une créance de dividende déjà comptabilisée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fx_profit_or_loss",
      "label_fr": "Écart de change en résultat",
      "applicability": "oui",
      "reasoning_fr": "Le dividende a déjà été comptabilisé en créance et, selon les hypothèses, cette créance reste un actif monétaire en devise dans les comptes consolidés. Dans ce cas, le traitement de base est la comptabilisation des écarts de change en résultat, sauf si une exception de comptabilité de couverture s’applique. Ce n’est pas une documentation de couverture, mais c’est bien le traitement applicable au cas.",
      "conditions_fr": [],
      "practical_implication_fr": "À défaut de couverture qualifiante, la partie change de la créance impacte le résultat consolidé.",
      "references": [
        {
          "section": "5.7.2",
          "excerpt": "shall be recognised in profit or loss"
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
      "applicability": "non",
      "reasoning_fr": "Ici, le dividende n’est plus seulement un flux futur attendu : il a déjà été constaté en créance. En outre, l’extrait fourni sur l’exception de cash flow hedge vise un poste monétaire désigné comme instrument de couverture, alors qu’ici la créance de dividende est le poste exposé au change. Sur ces faits, cette voie ne correspond pas au cas décrit.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie ne permet pas, sur les faits fournis, de documenter la partie change de la créance déjà comptabilisée.",
      "references": [
        {
          "section": "B5.7.2",
          "excerpt": "An exception is a monetary item that is designated as a hedging instrument in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est supposée être un actif financier monétaire déjà reconnu en consolidation et exposé au change. Parmi les traitements proposés, la couverture de juste valeur est celle qui s’aligne le mieux avec un risque de change porté par un actif déjà comptabilisé. Elle n’est pertinente que si la documentation vise précisément ce risque sur cette créance reconnue.",
      "conditions_fr": [
        "la créance de dividende reste reconnue en consolidation comme actif monétaire exposé au change",
        "la documentation porte spécifiquement sur le risque de change de cette créance jusqu’à son règlement"
      ],
      "practical_implication_fr": "C’est la piste de documentation la plus cohérente, dans les faits fournis, pour couvrir le change sur la créance.",
      "references": [
        {
          "section": "5.7.3",
          "excerpt": "hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        },
        {
          "section": "5.7.2",
          "excerpt": "not part of a hedging relationship"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite uniquement du risque de change sur un investissement net dans une activité étrangère, c’est-à-dire sur un montant de net assets. Le poste décrit ici est une créance de dividende intragroupe, pas l’investissement net lui-même. Sur ces faits, cette documentation ne couvre donc pas ce dividende dans les comptes consolidés.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette documentation viserait un net investment d’activité étrangère, pas la créance de dividende elle-même.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ est de confirmer que la créance de dividende subsiste effectivement en consolidation comme poste monétaire en devise.",
    "Sans relation de couverture qualifiante, les écarts de change sur cette créance vont en résultat consolidé.",
    "Dans les faits fournis, la couverture de juste valeur est la seule piste de documentation directement alignée avec une créance déjà reconnue.",
    "La couverture de flux de trésorerie conviendrait plutôt à un dividende encore futur; ici le dividende est déjà comptabilisé en créance.",
    "La couverture d’investissement net ne documente pas le dividende lui-même mais un montant de net assets d’une activité étrangère."
  ]
}
