{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe sont libellées dans une devise qui crée une exposition de change au sein du groupe.",
    "La demande vise les voies IFRS de documentation de couverture pertinentes en consolidation pour cette exposition déjà comptabilisée, y compris les issues alternatives prévues par les textes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Pour une créance de dividende intragroupe déjà comptabilisée, la seule voie IFRS potentielle en consolidation est l'exception relative au risque de change d'un élément monétaire intragroupe, sous conditions. À défaut, il n'y a pas de hedge accounting en consolidation; la couverture de transaction future est trop tardive et la couverture d'investissement net correspond à un autre fait pattern."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d'un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait pattern porte sur un dividende intragroupe déjà comptabilisé en créance, donc sur un poste intragroupe existant et non sur une transaction future.\nIFRS 9 pose une exception en consolidation pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés à la consolidation.\nSous les hypothèses données, cette voie est ouverte seulement si la créance/payable constitue bien un élément monétaire, si l'exposition de change subsiste en résultat consolidé et si la documentation de couverture remplit les critères de l'IFRS 9.",
      "conditions_fr": [
        "la créance et la dette de dividende constituent un élément monétaire intragroupe",
        "les écarts de change sur cet élément ne sont pas totalement éliminés en consolidation",
        "la relation de couverture est désignée et documentée formellement à son inception, de manière prospective",
        "les critères d'éligibilité et d'efficacité de l'IFRS 9 sont satisfaits"
      ],
      "practical_implication_fr": "C'est la seule voie de hedge accounting directement alignée avec une créance de dividende intragroupe déjà reconnue.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "no_hedge_accounting",
      "label_fr": "Pas de couverture pour un intragroupe ordinaire",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende est déjà comptabilisé en créance intragroupe et, en consolidation, la règle générale d'IFRS 9 réserve les éléments couverts aux expositions avec une contrepartie externe.\nCette conclusion devient la bonne dans cette situation si la créance ne remplit pas l'exception spécifique du paragraphe 6.3.6 pour les éléments monétaires intragroupe.\nAutrement dit, si l'effet de change ne subsiste pas au niveau consolidé, aucune documentation de couverture ne peut être appliquée sur ce dividende intragroupe.",
      "conditions_fr": [
        "la créance de dividende ne satisfait pas l'exception de change applicable aux éléments monétaires intragroupe en consolidation",
        "aucune autre relation de couverture qualifiante n'est documentée sur un item différent"
      ],
      "practical_implication_fr": "Si l'exception change n'est pas remplie, la partie change reste sans hedge accounting en comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d'une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Le contexte dit qu'un dividende intragroupe a déjà été comptabilisé en créance; le stade n'est donc plus celui d'une transaction future hautement probable.\nOr IFRS 9 n'ouvre cette voie en consolidation que pour une transaction intragroupe future, hautement probable, en devise, dont le risque de change affectera le résultat consolidé.\nCette approche aurait pu être analysée avant la comptabilisation du dividende, mais pas pour la créance déjà reconnue décrite dans la question.",
      "conditions_fr": [],
      "practical_implication_fr": "À ce stade, cette documentation n'est pas disponible pour la créance déjà comptabilisée.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... or a highly probable forecast transaction"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net à l'étranger",
      "applicability": "non",
      "reasoning_fr": "Le fait pattern vise un dividende intragroupe comptabilisé en créance, pas un montant de net assets d'une activité étrangère inclus dans les comptes consolidés.\nIFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change d'un investissement net dans une activité étrangère, avec comptabilisation en OCI puis reclassement à la cession.\nSans fait indiquant que la créance de dividende représente cet investissement net, cette voie ne s'applique pas à la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter la créance de dividende comme net investment hedge sauf exposition distincte sur des net assets d'une activité étrangère.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "14",
          "excerpt": "A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment in a foreign operation."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ est le stade comptable: la créance existe déjà, donc l'analyse porte d'abord sur l'exception 'élément monétaire intragroupe', pas sur une transaction future.",
    "En consolidation, il faut tester si les écarts de change sur la créance et la dette de dividende ne sont pas totalement éliminés, typiquement en présence de devises fonctionnelles différentes.",
    "Toute relation de couverture retenue doit être documentée prospectivement avec désignation formelle, risque couvert, instrument, hedge ratio et modalités d'évaluation de l'efficacité.",
    "Si l'item économique visé est en réalité un investissement net dans une activité étrangère, il faut constituer une documentation distincte de net investment hedge et non une couverture de la créance de dividende elle-même."
  ]
}
