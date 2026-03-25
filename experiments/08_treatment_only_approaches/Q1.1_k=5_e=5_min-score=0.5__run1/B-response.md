{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà généré une créance et une dette monétaires comptabilisées.",
    "La créance et la dette sont exposées à un risque de change parce que les entités concernées ont des monnaies fonctionnelles différentes.",
    "Les écarts de change qui en résultent ne sont pas totalement éliminés en consolidation, de sorte que l'élément monétaire intragroupe peut être un élément couvert dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les faits décrits, la voie la plus directement applicable est la couverture de juste valeur du risque de change sur la créance/dette intragroupe en consolidation. La couverture de flux de trésorerie et la couverture d'investissement net restent possibles seulement si la documentation vise bien cet objet de couverture spécifique."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà créé une créance/dette monétaire comptabilisée.\nSous les hypothèses données, IFRS 9 permet précisément qu'un risque de change sur un élément monétaire intragroupe soit un élément couvert en consolidation lorsqu'il affecte le résultat consolidé, ce qui correspond au modèle de couverture de juste valeur d'un actif ou passif comptabilisé.",
      "conditions_fr": [
        "L'élément couvert est bien la créance ou la dette monétaire intragroupe exposée au change.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation est formellement désignée et documentée dès l'origine.",
        "La documentation identifie l'instrument de couverture, l'élément couvert, le risque de change couvert et le test d'efficacité."
      ],
      "practical_implication_fr": "C'est le modèle le plus naturel pour documenter en consolidation la partie change de la créance de dividende déjà comptabilisée.",
      "references": [
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
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte IFRS 9 admet le modèle de couverture de flux de trésorerie pour un actif ou passif comptabilisé lorsqu'il s'agit de couvrir une variabilité de flux attribuable à un risque particulier.\nDans cette situation, ce traitement n'est recevable que si la documentation vise la variabilité des flux de règlement en monnaie fonctionnelle liée au change, et non la seule réévaluation comptable de la créance intragroupe.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux de règlement due au change sur l'actif ou passif comptabilisé.",
        "Cette variabilité doit pouvoir affecter le résultat consolidé.",
        "L'exception de l'élément monétaire intragroupe en consolidation doit être satisfaite.",
        "Les exigences de désignation, documentation et efficacité de IFRS 9 doivent être respectées."
      ],
      "practical_implication_fr": "Ce modèle est envisageable, mais il demande une justification documentaire plus ciblée sur les flux de règlement que sur la juste valeur du poste.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the documentation shall include identification of the hedging instrument, the hedged item, the nature of the risk being hedged"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce modèle ne s'applique pas à la créance de dividende en tant que telle; IFRIC 16 vise un risque de change sur un investissement net dans une activité étrangère, c'est-à-dire un montant de net assets inclus dans les comptes consolidés.\nDans cette situation, il n'est donc possible que si le groupe choisit de documenter un risque de change sur un investissement net qualifiant, distinct de la créance intragroupe déjà comptabilisée.",
      "conditions_fr": [
        "Il existe une activité étrangère dont les net assets sont inclus dans les comptes consolidés.",
        "L'élément couvert est un montant de net assets égal ou inférieur à la valeur comptable de cet investissement net, et non la créance de dividende elle-même.",
        "La relation respecte les exigences de désignation, documentation et efficacité de IFRS 9.",
        "Pour un même risque sur les mêmes net assets, une seule relation de couverture peut qualifier dans les comptes consolidés."
      ],
      "practical_implication_fr": "Si cette voie est retenue, la part efficace est portée en OCI avec les écarts de conversion et reclassée lors de la cession de l'activité étrangère.",
      "references": [
        {
          "section": "2",
          "excerpt": "will apply only when the net assets of that foreign operation are included in the financial statements"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        },
        {
          "section": "14",
          "excerpt": "The hedging instrument(s) may be held by any entity or entities within the group"
        },
        {
          "section": "3",
          "excerpt": "the gain or loss on the hedging instrument that is determined to be an effective hedge of the net investment is recognised in other comprehensive income"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le choix du modèle doit être figé à l'origine de la relation et documenté formellement dès l'inception.",
    "Pour la créance de dividende déjà comptabilisée, la couverture de juste valeur est la voie la plus directement alignée avec les faits décrits.",
    "La couverture de flux de trésorerie exige de démontrer que c'est bien la variabilité des flux de règlement en monnaie fonctionnelle qui est couverte.",
    "La couverture d'investissement net suppose de changer d'objet de couverture: on ne couvre plus la créance, mais un investissement net qualifiant dans une activité étrangère.",
    "En couverture d'investissement net, le groupe doit éviter une double qualification de couverture sur les mêmes net assets et le même risque dans les comptes consolidés."
  ]
}
