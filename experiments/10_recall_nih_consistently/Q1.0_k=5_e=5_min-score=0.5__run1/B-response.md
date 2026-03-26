{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture selon IFRS 9 dans les comptes consolidés.",
    "Le dividende intragroupe et la créance correspondante sont libellés dans une devise différente de la devise fonctionnelle de l'entité qui porte la créance, ce qui crée un risque de change intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, une documentation de couverture peut être mise en place en consolidation sur le risque de change d'une créance de dividende intragroupe déjà comptabilisée, mais seulement si cette créance constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. En revanche, ce n'est pas une couverture d'investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d'un poste monétaire intragroupe, par exemple une créance/dette, lorsque les écarts de change ne sont pas totalement éliminés. Ici, la question vise une créance de dividende déjà comptabilisée, donc un actif reconnu, ce qui correspond directement au modèle de couverture de juste valeur d'un actif reconnu exposé au change.",
      "conditions_fr": [
        "la créance de dividende constitue un poste monétaire intragroupe",
        "les entités concernées ont des monnaies fonctionnelles différentes",
        "les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation peut viser la créance de dividende reconnue comme élément couvert au niveau consolidé sur son risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "reasoning_fr": "Le texte IFRS 9 admet aussi une couverture de flux de trésorerie sur un actif ou passif reconnu, dès lors que le risque couvert est une variabilité de flux pouvant affecter le résultat. Dans cette situation, si la créance de dividende intragroupe en devise crée une variabilité du montant encaissé en monnaie fonctionnelle et que les écarts de change ne sont pas totalement éliminés en consolidation, ce modèle peut aussi être soutenu.",
      "conditions_fr": [
        "la créance de dividende constitue un poste monétaire intragroupe",
        "les entités concernées ont des monnaies fonctionnelles différentes",
        "les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit alors viser la variabilité des flux en monnaie fonctionnelle jusqu'au règlement de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe comptabilisée, et non sur les net assets d'une foreign operation. IFRIC 16 limite explicitement ce modèle aux hedges of net investments in foreign operations et interdit de l'appliquer par analogie à d'autres relations de couverture.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette exposition ne doit pas être documentée comme une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La base technique en consolidation est l'exception IFRS 9 sur le risque de change d'un poste monétaire intragroupe, pas la simple existence d'un flux intragroupe.",
    "La documentation doit être formalisée à l'origine de la relation de couverture et identifier l'instrument de couverture, la créance de dividende, le risque de change couvert et la manière d'apprécier l'efficacité.",
    "Il faut démontrer que la créance de dividende génère bien des écarts de change qui subsistent en consolidation entre entités ayant des monnaies fonctionnelles différentes.",
    "La piste 'couverture d'investissement net' doit être écartée pour cette situation."
  ]
}
