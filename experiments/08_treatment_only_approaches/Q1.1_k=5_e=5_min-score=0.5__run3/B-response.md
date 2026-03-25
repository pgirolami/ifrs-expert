{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe est un élément monétaire en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
    "La relation de couverture est envisagée dans les comptes consolidés et peut satisfaire aux exigences de désignation, de documentation et d'efficacité d'IFRS 9.6.4.1."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Malgré la règle générale d'exclusion des postes intragroupe en consolidation, l'exception d'IFRS 9.6.3.6 permet ici de couvrir la composante change du dividende intragroupe comptabilisé en créance/dette.\nDans cette situation, les deux documentations possibles sont la couverture de juste valeur et la couverture de flux de trésorerie, sous la documentation IFRS 9 requise dès l'origine."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "La règle générale exclut les éléments intragroupe comme éléments couverts en consolidation, mais IFRS 9.6.3.6 crée une exception pour le risque de change d'un élément monétaire intragroupe dont les écarts ne sont pas totalement éliminés; c'est précisément l'hypothèse de votre dividende comptabilisé en créance.\nComme la créance de dividende est déjà un actif reconnu, le modèle d'IFRS 9.6.5.2(a) est adapté pour documenter l'exposition aux variations de valeur imputables au change qui affectent le résultat consolidé.",
      "conditions_fr": [
        "Le dividende doit rester un élément monétaire en devise dans les comptes consolidés.",
        "La désignation doit viser la composante risque de change du poste intragroupe.",
        "La documentation initiale doit identifier l'instrument, l'élément couvert, le hedge ratio et le test d'efficacité."
      ],
      "practical_implication_fr": "La documentation vise la réévaluation en change du poste intragroupe déjà comptabilisé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
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
      "applicability": "oui",
      "reasoning_fr": "Dans votre situation, la créance de dividende intragroupe entraîne aussi un encaissement/paiement futur en devise dont la contre-valeur dans la monnaie fonctionnelle consolidée varie jusqu'au règlement.\nLa même exception d'IFRS 9.6.3.6 rend ce risque de change intragroupe éligible en consolidation, et IFRS 9.6.5.2(b) permet d'utiliser le modèle de cash flow hedge pour la variabilité des flux liés à un actif ou passif reconnu.",
      "conditions_fr": [
        "Le règlement futur du dividende doit encore exposer le groupe à un risque de change.",
        "La désignation doit porter sur la variabilité des flux en monnaie fonctionnelle due au change.",
        "La documentation initiale et les tests d'efficacité d'IFRS 9.6.4.1 doivent être formalisés au niveau consolidé."
      ],
      "practical_implication_fr": "La documentation vise la variabilité de la contre-valeur en monnaie fonctionnelle au règlement du dividende.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu que la créance et la dette de dividende constituent bien un poste monétaire en devise entre entités à monnaies fonctionnelles différentes.",
    "La base IFRS en consolidation repose sur l'exception d'IFRS 9.6.3.6 à la règle générale d'exclusion des transactions intragroupe.",
    "Documenter dès l'origine l'élément couvert, l'instrument de couverture, le risque de change désigné, le hedge ratio et la méthode d'évaluation de l'efficacité.",
    "Le choix entre juste valeur et flux de trésorerie dépend de l'objectif documenté: couvrir la réévaluation du poste reconnu ou la variabilité du règlement en monnaie fonctionnelle."
  ]
}
