{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un élément monétaire comptabilisé, libellé dans une monnaie différente de la monnaie fonctionnelle d’au moins une entité du groupe concernée.",
    "L’analyse est effectuée au niveau des comptes consolidés.",
    "Les écarts de change liés à cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans les comptes consolidés, car IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il n’est pas totalement éliminé en consolidation.\nLa seule composante de change peut être désignée; la couverture devra toutefois satisfaire aux critères de désignation, documentation et efficacité de 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, la règle générale exclut les éléments intragroupe, mais 6.3.6 ouvre une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés.\nIci, la créance de dividende répond à cette logique selon les hypothèses; la seule composante de change est désignable comme composante de risque au titre de 6.3.7, sous réserve de 6.4.1.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
        "La composante de change est séparément identifiable et fiable à mesurer.",
        "La relation de couverture est formellement désignée et documentée dès l’origine."
      ],
      "practical_implication_fr": "La couverture viserait la variation de valeur de la créance intragroupe attribuable au seul risque de change dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi de viser la variabilité des flux de règlement en monnaie fonctionnelle d’une créance déjà comptabilisée, si cette variabilité provient du seul change.\nCette voie n’est recevable ici que parce que l’exception de 6.3.6 est satisfaite en consolidation et si la relation est documentée comme couverture de cash flows sur la seule composante de change conformément à 6.3.7 et 6.4.1.",
      "conditions_fr": [
        "La couverture porte sur la variabilité des flux de règlement attribuable au change.",
        "Les flux couverts peuvent affecter le résultat consolidé.",
        "Les écarts de change sur l’élément monétaire intragroupe ne sont pas totalement éliminés en consolidation.",
        "La documentation et les tests d’efficacité respectent 6.4.1."
      ],
      "practical_implication_fr": "La couverture viserait la variabilité en monnaie fonctionnelle des encaissements attendus au règlement de la créance de dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord, en consolidation, que les écarts de change sur la créance/dividende intragroupe ne sont pas totalement éliminés; sinon l’exception de 6.3.6 ne joue pas.",
    "La désignation doit viser uniquement la composante de change, qui doit être séparément identifiable et fiable à mesurer.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit être cohérent avec l’objectif de gestion du risque et être documenté dès l’inception."
  ]
}
