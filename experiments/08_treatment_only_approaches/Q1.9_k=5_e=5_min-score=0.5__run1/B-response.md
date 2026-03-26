{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et est comptabilisé comme une créance/dette monétaire intragroupe.",
    "La créance/dette est libellée dans une devise qui génère des écarts de change non entièrement éliminés en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes.",
    "Les exigences normales d'IFRS 9 en matière de désignation, de documentation et d'efficacité de la couverture sont respectées."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation, parce qu'IFRS 9 prévoit une exception pour le risque de change d'un poste monétaire intragroupe en consolidation. La désignation reste toutefois subordonnée au fait que les écarts de change ne soient pas entièrement éliminés et que la relation de couverture soit correctement documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est déjà un actif reconnu et prend la forme d'un poste monétaire intragroupe. La règle générale d'exclusion des éléments intragroupe en consolidation est écartée par l'exception d'IFRS 9 pour le risque de change d'un poste monétaire intragroupe ; la composante de change peut donc être désignée en couverture de juste valeur si elle affecte le résultat consolidé.",
      "conditions_fr": [
        "La créance/dette de dividende doit constituer un poste monétaire intragroupe reconnu.",
        "Les écarts de change doivent ne pas être entièrement éliminés en consolidation.",
        "La composante de risque de change doit être séparément identifiable et mesurable de façon fiable.",
        "La désignation, la documentation initiale et les tests d'efficacité doivent être conformes à IFRS 9."
      ],
      "practical_implication_fr": "Le groupe peut désigner le seul risque de change de la créance de dividende reconnue comme élément couvert en juste valeur dans les comptes consolidés.",
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
      "reasoning_fr": "Dans cette même situation, l'exception d'IFRS 9 pour les postes monétaires intragroupe permet aussi de viser le seul risque de change de la créance reconnue. Le traitement en couverture de flux de trésorerie n'est recevable que si le risque désigné est formulé comme une variabilité des flux de règlement en monnaie fonctionnelle qui affectera le résultat consolidé, avec documentation et efficacité démontrées.",
      "conditions_fr": [
        "La créance/dette de dividende doit être un poste monétaire intragroupe reconnu au moment de la désignation.",
        "Le risque de change désigné doit affecter le résultat consolidé et ne pas être entièrement éliminé en consolidation.",
        "La composante de risque doit être séparément identifiable et mesurable de façon fiable.",
        "La relation doit satisfaire aux exigences de documentation initiale et d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "Le groupe peut structurer la couverture sur la variabilité des flux de règlement en monnaie fonctionnelle de la créance de dividende reconnue.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
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
    "Le point clé en consolidation est de démontrer que les écarts de change sur la créance/dette de dividende ne sont pas totalement éliminés.",
    "La désignation doit viser uniquement la composante de risque de change, et non l'élément intragroupe dans son ensemble.",
    "La documentation de couverture doit être en place dès l'origine de la relation de couverture.",
    "Le fait que le dividende soit déjà reconnu en créance/dette oriente l'analyse vers un actif ou passif reconnu, et non vers une simple transaction intragroupe future."
  ]
}
