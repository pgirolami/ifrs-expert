{
  "assumptions_fr": [
    "La question vise des comptes consolidés d’une entité non qualifiée d’entité d’investissement.",
    "Le dividende intragroupe est libellé dans une devise créant une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "La mise en distribution du dividende a créé une créance et une dette intragroupe comptabilisées, constituant un poste monétaire."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement selon l’approche de couverture de juste valeur du risque de change du poste monétaire intragroupe déjà comptabilisé. En consolidation, cela n’est possible que si les écarts de change ne sont pas intégralement éliminés et si les critères d’IFRS 9.6.4.1 sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe a déjà donné naissance à une créance/dette reconnue, donc à un actif/passif comptabilisé. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés; avec des monnaies fonctionnelles différentes, cette condition est cohérente avec les hypothèses.\nLa relation doit en plus satisfaire aux exigences de désignation, de documentation et d’efficacité d’IFRS 9.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe est un poste monétaire entre entités ayant des monnaies fonctionnelles différentes.",
        "Le risque de change sur ce poste génère des écarts non intégralement éliminés en consolidation.",
        "La relation respecte les critères de désignation formelle, de documentation et d’efficacité d’IFRS 9.6.4.1."
      ],
      "practical_implication_fr": "La documentation doit viser une couverture de juste valeur du seul risque de change de la créance/dette de dividende intragroupe.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Cette approche ne correspond pas aux faits retenus, car le dividende a déjà été déclaré et a créé une créance/dette intragroupe comptabilisée. Le modèle de cash flow hedge vise la variabilité de flux de trésorerie ou une transaction future hautement probable; l’exception intragroupe visée par IFRS 9 concerne précisément une transaction intragroupe prévisionnelle.\nIci, l’analyse pertinente en consolidation porte donc sur le poste monétaire déjà reconnu, non sur un dividende encore prévisionnel.",
      "conditions_fr": [
        "Non applicable dès lors que le dividende a déjà donné lieu à une créance/dette comptabilisée."
      ],
      "practical_implication_fr": "Il ne faut pas documenter ce dividende déjà reconnu comme une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Qualifier l’élément couvert comme une créance/dette de dividende intragroupe déjà comptabilisée, et non comme une transaction prévisionnelle.",
    "Limiter le risque couvert au risque de change qui subsiste en consolidation du fait des monnaies fonctionnelles différentes.",
    "Documenter dès l’origine l’instrument de couverture, l’élément couvert, le risque couvert, le hedge ratio et les sources attendues d’inefficacité."
  ]
}
