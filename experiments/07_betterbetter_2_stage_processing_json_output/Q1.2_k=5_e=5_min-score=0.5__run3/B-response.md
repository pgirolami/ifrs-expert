{
  "assumptions_fr": [
    "On suppose que la créance de dividende intragroupe est un élément monétaire déjà comptabilisé, libellé en devise, et que la question vise la présentation dans les comptes consolidés.",
    "On suppose qu’il s’agit d’identifier, en principe, les voies de documentation de couverture envisageables, sans conclure d’avance que tous les critères détaillés de qualification sont déjà démontrés dans le dossier."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans ce contexte, deux voies de documentation répondent au risque de change porté par la créance déjà reconnue : la couverture de juste valeur et la couverture de flux de trésorerie.\nLa couverture d’investissement net ne répond pas au fait décrit, car elle vise un investissement net dans une activité étrangère, non la créance de dividende."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Le fait décrit est une créance intragroupe déjà comptabilisée et libellée en devise; au stade actuel, le risque de change porte donc sur un élément monétaire reconnu.\nLe contexte indique que les écarts de change sur les éléments monétaires vont en résultat, ce qui rend pertinente une documentation de couverture visant la variation de valeur liée au change dans les comptes consolidés.\nSous les hypothèses retenues, cette voie répond directement à la question, sous réserve des conditions normales de désignation, documentation et suivi d’efficacité.",
      "conditions_fr": [
        "désigner formellement la relation de couverture au niveau consolidé",
        "identifier un instrument de couverture éligible et documenter la composante change couverte",
        "mettre en place le suivi d’efficacité requis par IFRS 9"
      ],
      "practical_implication_fr": "Il faut documenter la composante change de la créance reconnue et suivre en consolidation les variations de l’item couvert et de l’instrument de couverture.",
      "references": [
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        },
        {
          "section": "5.7.3",
          "excerpt": "A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "Selon l’hypothèse posée, la créance de dividende en devise est déjà reconnue mais son règlement futur laisse subsister une variabilité de flux en monnaie fonctionnelle liée au change.\nCette approche répond donc aussi à la question « de quelles manières » dans les comptes consolidés, car elle vise la partie change des encaissements futurs associés à la créance déjà comptabilisée.\nElle reste à documenter et à piloter au niveau consolidé avec un instrument éligible et une démonstration d’efficacité cohérente.",
      "conditions_fr": [
        "décrire dans la documentation de couverture que le risque couvert est la variabilité de change des flux de règlement de la créance",
        "désigner un instrument de couverture éligible au niveau consolidé",
        "assurer un suivi d’efficacité jusqu’au règlement de la créance"
      ],
      "practical_implication_fr": "Opérationnellement, le groupe documente le risque de change sur les flux de règlement de la créance et suit l’efficacité de la couverture jusqu’à l’encaissement.",
      "references": [
        {
          "section": "6.1.1",
          "excerpt": "manage exposures arising from particular risks that could affect profit or loss"
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
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Le contexte IFRIC 16 limite cette documentation aux couvertures du risque de change d’un investissement net dans une activité étrangère, avec comme élément couvert un montant de net assets.\nOr la question porte sur un dividende intragroupe déjà comptabilisé en créance; sous les hypothèses retenues, il s’agit d’un poste monétaire distinct et non de l’investissement net lui-même.\nCette piste ne répond donc pas au fait décrit sans changer l’objet couvert et, partant, le cas de départ.",
      "conditions_fr": [],
      "practical_implication_fr": "Poursuivre cette piste reviendrait à documenter un autre risque et un autre élément couvert que la créance de dividende visée par la question.",
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
    "Le choix opérationnel se fait ici entre une documentation de juste valeur et une documentation de flux de trésorerie sur la créance déjà comptabilisée.",
    "La documentation doit être établie au niveau des comptes consolidés et identifier explicitement la composante change, l’instrument de couverture et le suivi d’efficacité.",
    "La piste « investissement net » doit être écartée pour ce fait précis, car elle vise les net assets d’une activité étrangère et non la créance de dividende déjà reconnue."
  ]
}
