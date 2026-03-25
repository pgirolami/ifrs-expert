{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette monétaire intragroupe comptabilisée.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que cette créance/dette génère des écarts de change qui ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans ce cas précis, l'exception IFRS 9 relative au risque de change d'un élément monétaire intragroupe en comptes consolidés est pertinente. La relation reste toutefois à formaliser selon les exigences ordinaires de désignation, documentation et efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d'un élément monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Selon les hypothèses, le dividende intragroupe a déjà créé une créance/dette monétaire comptabilisée entre entités de monnaies fonctionnelles différentes.\nIFRS 9 6.3.6 vise précisément le risque de change d'un élément monétaire intragroupe en comptes consolidés lorsque les écarts de change ne sont pas totalement éliminés à la consolidation, ce qui est supposé ici.\nCette approche s'applique donc à la situation décrite, sous réserve des exigences normales de documentation et d'efficacité prévues par 6.4.1.",
      "conditions_fr": [
        "Établir la désignation et la documentation formelles à l'origine de la relation de couverture.",
        "Identifier l'instrument de couverture, l'élément couvert, le risque de change et le hedge ratio.",
        "Démontrer la relation économique et que le risque de crédit ne domine pas."
      ],
      "practical_implication_fr": "La couverture doit être documentée sur la créance/dette de dividende comptabilisée comme élément couvert en change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_exclusion",
      "label_fr": "Exclusion générale des intragroupe",
      "applicability": "non",
      "reasoning_fr": "Cette approche exprime la règle générale selon laquelle, en consolidation, seuls des éléments avec des parties externes peuvent en principe être désignés comme éléments couverts.\nOr, la question porte sur une créance/dette monétaire intragroupe déjà comptabilisée et, selon les hypothèses, ses écarts de change ne sont pas totalement éliminés en consolidation.\nComme IFRS 9 6.3.6 prévoit expressément une exception pour ce cas, l'exclusion générale n'est pas l'approche applicable ici.",
      "conditions_fr": [],
      "practical_implication_fr": "On ne peut pas conclure à l'interdiction de la couverture en se fondant uniquement sur la règle générale d'exclusion des intragroupe.",
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
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d'une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette approche concerne une transaction intragroupe future hautement probable, donc un stade antérieur à la comptabilisation d'une créance ou d'une dette.\nOr la question et les hypothèses placent l'analyse après enregistrement de la créance de dividende correspondante ; le fait pattern n'est plus celui d'une transaction future.\nPour cette raison de timing, cette approche n'est pas applicable à la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "S'il y a hedge accounting, il doit porter sur la créance/dette reconnue, non sur le dividende comme transaction future.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le bon objet couvert est la créance/dette de dividende déjà comptabilisée ; la voie de la transaction intragroupe future n'est plus pertinente à ce stade.",
    "Aucune documentation rétroactive : la désignation et la documentation doivent être en place à l'origine de la relation de couverture.",
    "Il faut conserver la démonstration que les écarts de change sur cette créance/dette ne sont pas totalement éliminés en consolidation du fait des monnaies fonctionnelles différentes."
  ]
}
