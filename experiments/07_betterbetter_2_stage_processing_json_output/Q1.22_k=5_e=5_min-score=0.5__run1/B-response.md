{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un élément monétaire libellé dans une devise différente de la monnaie fonctionnelle d’au moins une entité concernée.",
    "Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans ce schéma, l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe en comptes consolidés peut s’appliquer, malgré l’exclusion générale des intragroupes. La couverture peut donc être documentée sur cette composante de risque, sous réserve de la documentation et des tests d’efficacité de l’article 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà reconnu en créance dans les comptes consolidés : au stade de reconnaissance visé par la question, il s’agit donc d’un actif reconnu. Malgré la règle générale d’exclusion des intragroupes en consolidation, l’hypothèse posée reprend précisément l’exception de l’élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. IFRS 9 permet en outre de désigner une composante de risque d’un actif reconnu ; la voie de la couverture de juste valeur est donc permise dans cette situation, avec la documentation et les tests d’efficacité requis.",
      "conditions_fr": [
        "Documenter dès l’inception la relation de couverture, l’instrument, la créance couverte, le risque de change et le hedge ratio.",
        "Démontrer l’existence d’une relation économique et que le risque de crédit ne domine pas les variations de valeur."
      ],
      "practical_implication_fr": "Il faut mettre en place une documentation de hedge accounting centrée sur la créance de dividende déjà comptabilisée et suivre l’inefficacité sur la durée de la couverture.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "An entity may designate an item in its entirety or a component of an item as the hedged item"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk"
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
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui",
      "reasoning_fr": "La question vise aussi une créance de dividende déjà reconnue ; or IFRS 9 admet une cash flow hedge sur un actif ou passif reconnu pour une variabilité de flux attribuable à un risque particulier. Sous les hypothèses données, le risque de change de cet élément monétaire intragroupe est éligible en consolidation car il n’est pas entièrement éliminé et il affecte le résultat consolidé. La documentation d’une couverture de flux de trésorerie sur cette composante de change est donc également permise à ce stade, sous les conditions ordinaires de 6.4.1.",
      "conditions_fr": [
        "Documenter à l’inception que le risque couvert est la variabilité des flux de règlement en monnaie fonctionnelle liée au change.",
        "Appliquer les tests d’efficacité, y compris la relation économique et un hedge ratio cohérent avec la gestion du risque."
      ],
      "practical_implication_fr": "Il faut modéliser et suivre la variabilité des flux de règlement de la créance en monnaie fonctionnelle jusqu’à son encaissement ou extinction.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est l’exception de l’élément monétaire intragroupe : sans impact résiduel en résultat consolidé, la couverture ne tiendrait pas.",
    "La documentation doit être établie à l’inception de la relation de couverture et identifier précisément la créance de dividende, la composante de change et le hedge ratio.",
    "Le choix entre juste valeur et flux de trésorerie doit rester cohérent avec le risque effectivement désigné sur la créance déjà comptabilisée."
  ]
}
