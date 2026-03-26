{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a fait naître une créance et une dette intragroupe déjà comptabilisées.",
    "L'effet de change potentiel existe parce que les entités du groupe concernées ont des monnaies fonctionnelles différentes et que l'analyse porte sur les comptes consolidés.",
    "L'analyse est faite au regard des règles de comptabilité de couverture d'IFRS 9 et, si pertinent, d'IFRIC 16."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en comptes consolidés, si la créance/dette de dividende est un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la seule composante de change peut être désignée comme risque couvert; la voie la plus directe est l'exception d'IFRS 9 sur les postes monétaires intragroupe."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe déclaré a créé une créance/dette reconnue, ce qui correspond au point de départ d'une couverture de juste valeur d'un actif ou passif comptabilisé. En consolidation, cela n'est toutefois recevable que si l'on entre dans l'exception d'IFRS 9 pour le risque de change d'un poste monétaire intragroupe qui génère des écarts non totalement éliminés.",
      "conditions_fr": [
        "La créance ou dette de dividende doit constituer un poste monétaire intragroupe.",
        "Les écarts de change sur ce poste doivent ne pas être totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La relation serait documentée sur la variation de valeur du poste comptabilisé attribuable au seul risque de change.",
      "references": [
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette approche peut aussi être envisagée si l'exposition est formulée comme la variabilité, en monnaie fonctionnelle, du règlement futur du dividende intragroupe. Dans les faits décrits, elle ne devient possible en consolidation que parce que le poste est intragroupe et que seule l'exception de l'article 6.3.6 permet de dépasser la règle générale d'exclusion des éléments intragroupe.",
      "conditions_fr": [
        "Le risque documenté doit porter sur la variabilité du règlement en devise du dividende qui affecte le résultat consolidé.",
        "Le poste doit relever de l'exception applicable aux postes monétaires intragroupe en consolidation."
      ],
      "practical_implication_fr": "Il faut démontrer que l'exposition couverte est bien la variabilité du montant de règlement liée au change, et non simplement l'existence d'un solde intragroupe.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture de composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question vise précisément la seule composante de change; IFRS 9 autorise la désignation d'un composant de risque plutôt que de l'élément entier. Pour le dividende intragroupe en devise, cette composante est pertinente si elle est séparément identifiable et mesurable de façon fiable, sous réserve que l'élément de base soit lui-même admissible en consolidation.",
      "conditions_fr": [
        "La composante de change doit être séparément identifiable.",
        "La composante de change doit être mesurable de façon fiable.",
        "Le poste sous-jacent doit être admissible en consolidation au titre de l'exception sur les postes monétaires intragroupe."
      ],
      "practical_implication_fr": "La documentation peut viser uniquement le risque de change, sans couvrir l'intégralité de la créance ou de la dette de dividende.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "B6.3.8",
          "excerpt": "separately identifiable ... and reliably measurable"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "C'est l'approche la plus directement applicable aux faits. La règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 prévoit expressément une exception pour le risque de change d'un poste monétaire intragroupe lorsqu'il crée des gains ou pertes de change non totalement éliminés; c'est précisément l'hypothèse posée.",
      "conditions_fr": [
        "Le dividende comptabilisé à recevoir/à payer doit être un poste monétaire intragroupe.",
        "Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "Si ces deux conditions sont remplies, le poste peut être désigné comme élément couvert pour son seul risque de change dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_5",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Les textes sur la couverture d'un investissement net visent un montant de net assets d'une activité à l'étranger et non une créance/dette de dividende déclarée entre entités du groupe. Dans la situation décrite, l'exposition est celle d'un poste monétaire intragroupe ponctuel, pas celle d'un investissement net dans une activité étrangère.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas qualifier ce dividende intragroupe de couverture d'investissement net sur la base des faits fournis.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        },
        {
          "section": "8",
          "excerpt": "applies only to hedges of net investments in foreign operations"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Confirmer juridiquement et comptablement que le dividende déclaré a bien créé une créance/dette monétaire intragroupe.",
    "Vérifier que les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation; sinon, l'exception d'IFRS 9 ne joue pas.",
    "Documenter dès l'origine l'élément couvert, l'instrument de couverture, la seule composante de change visée et la manière d'apprécier l'efficacité.",
    "La base technique la plus solide, au vu des faits fournis, est la désignation du risque de change d'un poste monétaire intragroupe, plutôt qu'une couverture d'investissement net."
  ]
}
