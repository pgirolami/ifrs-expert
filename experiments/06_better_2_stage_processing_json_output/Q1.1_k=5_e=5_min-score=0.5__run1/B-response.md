{
  "assumptions_fr": [
    "Le dividende intragroupe ou la créance correspondante est libellé dans une devise générant une exposition de change au niveau du groupe.",
    "La demande vise les voies de comptabilité de couverture possibles en comptes consolidés, sous réserve du respect des exigences IFRS 9 de désignation, de documentation et d'efficacité."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans ce cas précis, la voie applicable est la couverture de juste valeur du risque de change sur la créance intragroupe déjà reconnue, via l'exception IFRS 9 pour un élément monétaire intragroupe en consolidation. La voie \"transaction hautement probable\" est trop tardive et la couverture d'investissement net ne vise pas la créance de dividende elle-même."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur d'un élément monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le fait posé est un dividende intragroupe déjà comptabilisé en créance ; avec l'hypothèse d'une exposition de change au niveau du groupe, on est bien au stade d'un élément monétaire intragroupe déjà reconnu.\nDans ce timing, l'exception IFRS 9 pour le risque de change d'un élément monétaire intragroupe en consolidation peut être utilisée, sous réserve de la désignation et de la documentation formelles ainsi que des critères d'efficacité.",
      "conditions_fr": [
        "La créance doit rester un élément monétaire intragroupe dont le risque de change affecte le résultat consolidé.",
        "La relation de couverture doit être formellement désignée et documentée dès l'inception de la relation.",
        "Le hedge ratio et l'efficacité doivent respecter les critères IFRS 9."
      ],
      "practical_implication_fr": "La documentation doit viser la créance intragroupe déjà reconnue comme élément couvert pour son seul risque de change en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
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
      "label_fr": "Couverture de flux de trésorerie d'une transaction intragroupe hautement probable",
      "applicability": "non",
      "reasoning_fr": "La question précise que le dividende intragroupe a déjà été comptabilisé en créance ; le stade de la transaction future hautement probable est donc dépassé.\nOr cette exception vise une transaction intragroupe encore future et hautement probable ; l'appliquer ici supposerait revenir à un stade antérieur, ce qui contredit le timing donné.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n'est plus ouverte pour la créance déjà reconnue ; elle n'aurait été envisageable qu'avant la comptabilisation du dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... or a highly probable forecast transaction"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Le modèle de couverture d'investissement net vise le risque de change attaché à une participation nette dans une activité étrangère, et non la créance de dividende intragroupe déjà constatée.\nDans les faits donnés et sous les hypothèses retenues, l'objet à couvrir est la créance née du dividende ; utiliser cette approche exigerait de reformuler l'exposition couverte, ce qui sort du cas posé.",
      "conditions_fr": [],
      "practical_implication_fr": "Une documentation de net investment hedge serait une documentation distincte portant sur l'investissement net, pas sur la créance de dividende déjà comptabilisée.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "no_hedge_accounting",
      "label_fr": "Aucune comptabilité de couverture qualifiante en consolidation",
      "applicability": "non",
      "reasoning_fr": "La règle générale IFRS 9 exclut les éléments intragroupe comme éléments couverts en consolidation, mais le contexte fourni retient précisément une exposition de change au niveau du groupe sur une créance intragroupe déjà reconnue.\nCe fait correspond à l'exception spécifique des éléments monétaires intragroupe ; la conclusion \"aucune couverture admissible\" ne tient donc pas dans cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "En l'espèce, l'analyse ne s'arrête pas à l'interdiction générale, car l'exception change sur élément monétaire intragroupe doit être examinée.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Comme la créance est déjà comptabilisée, la piste \"transaction intragroupe hautement probable\" n'est plus disponible pour cet objet de couverture.",
    "La documentation consolidée doit expliquer pourquoi le risque de change sur la créance intragroupe subsiste au niveau du groupe et n'est pas entièrement éliminé en consolidation.",
    "La relation doit identifier l'instrument de couverture, l'élément couvert, le risque de change couvert, le hedge ratio et la méthode d'appréciation de l'efficacité.",
    "Une éventuelle stratégie de couverture d'investissement net doit être documentée séparément et ne remplace pas la couverture de la créance de dividende déjà reconnue."
  ]
}
