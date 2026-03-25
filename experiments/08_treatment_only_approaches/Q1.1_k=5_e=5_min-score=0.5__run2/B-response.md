{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe constituent un élément monétaire en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation, de sorte que cet élément peut être qualifié d’élément couvert dans les comptes consolidés.",
    "Un instrument de couverture éligible existe et les exigences de désignation formelle, de documentation et d’efficacité sont respectées."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans cette situation, une documentation de couverture sur la partie change est possible en comptes consolidés. La couverture de juste valeur est la voie la plus directe pour une créance déjà comptabilisée; la couverture de flux de trésorerie reste envisageable si la documentation vise explicitement la variabilité du montant de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Oui dans cette situation. La créance de dividende est déjà reconnue et, selon les hypothèses, son risque de change sur élément monétaire intragroupe n’est pas totalement éliminé en consolidation; elle peut donc être désignée comme élément couvert. La documentation peut viser uniquement la composante change, ce qui correspond bien à une couverture de l’exposition à la variation de valeur de cette créance affectant le résultat consolidé.",
      "conditions_fr": [
        "Limiter l’élément couvert à la composante risque de change de la créance intragroupe.",
        "Documenter dès l’origine l’instrument de couverture, l’élément couvert, le risque couvert et l’appréciation de l’efficacité.",
        "Confirmer que les écarts de change sur cette créance affectent bien le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation cherche une compensation en résultat consolidé entre la variation de change de la créance et celle de l’instrument de couverture.",
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
      "reasoning_fr": "Possible dans cette situation si la documentation retient comme risque couvert la variabilité, due au change, du montant en monnaie fonctionnelle qui sera réglé sur la créance de dividende. Bien que la créance soit déjà comptabilisée, IFRS 9 permet aussi une couverture de flux de trésorerie sur un actif reconnu, et l’exception relative aux éléments monétaires intragroupe permet ici la désignation en consolidation selon les hypothèses posées.",
      "conditions_fr": [
        "Définir l’exposition couverte comme la variabilité des flux de règlement liée au change de la créance reconnue.",
        "Mettre en place la désignation et la documentation formelles à l’origine de la relation de couverture.",
        "S’assurer que cette variabilité de change est susceptible d’affecter le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation cible le montant en monnaie fonctionnelle qui sera effectivement encaissé ou réglé à l’extinction de la créance de dividende.",
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
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie à l’origine de la relation de couverture et isoler explicitement la seule composante change de la créance de dividende.",
    "En consolidation, le point déterminant est l’exception IFRS 9 pour l’élément monétaire intragroupe: seule la partie dont les écarts de change ne sont pas totalement éliminés peut être couverte.",
    "Pour une créance déjà reconnue, la couverture de juste valeur est généralement le cadrage le plus direct; la couverture de flux de trésorerie exige que l’objectif documenté porte sur la variabilité du règlement."
  ]
}
