{
  "assumptions_fr": [
    "Le dividende déclaré a déjà été comptabilisé en créance/dette intragroupe ; l’exposition doit donc être analysée comme un élément monétaire comptabilisé et non comme une transaction future.",
    "La question vise la comptabilité de couverture en comptes consolidés selon IFRS 9 pour des entités du groupe exposées à un risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en comptes consolidés, mais par l’exception IFRS 9 applicable aux éléments monétaires intragroupe déjà comptabilisés. La qualification suppose encore que les écarts de change ne soient pas entièrement éliminés en consolidation et que la relation de couverture soit formellement documentée et efficace."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Selon l’hypothèse retenue, le dividende a déjà été déclaré et comptabilisé en créance intragroupe ; il faut donc l’analyser comme un élément monétaire reconnu.\nEn comptes consolidés, IFRS 9 prévoit précisément une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation.\nLa qualification formelle reste subordonnée à la désignation et à la documentation de la relation de couverture à son inception, ainsi qu’aux critères d’efficacité.",
      "conditions_fr": [
        "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur la créance/dette intragroupe ne sont pas entièrement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée dès son inception, avec identification de l’instrument de couverture, de l’élément couvert et du risque de change couvert.",
        "Les critères d’efficacité de la couverture prévus par IFRS 9 sont satisfaits."
      ],
      "practical_implication_fr": "En pratique, la documentation doit viser la créance/dette de dividende comme élément monétaire intragroupe couvert au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_item_exclusion",
      "label_fr": "Exclusion générale des éléments intragroupe",
      "applicability": "non",
      "reasoning_fr": "Cette approche exprime bien la règle générale applicable en consolidation : les éléments couverts doivent en principe concerner des tiers externes.\nMais, dans les faits posés et sous les hypothèses retenues, la créance de dividende est déjà un élément monétaire intragroupe reconnu, situation visée par l’exception spécifique d’IFRS 9.6.3.6.\nPris isolément, le raisonnement d’exclusion générale ne gouverne donc pas ce cas exact.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas s’arrêter à l’exclusion générale sans tester l’exception propre aux éléments monétaires intragroupe.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette voie concerne un stade antérieur : une transaction intragroupe future hautement probable.\nOr, selon l’hypothèse retenue, le dividende a déjà été déclaré et comptabilisé en créance à recevoir ; il ne s’agit plus d’une forecast transaction.\nL’appliquer supposerait revenir à un stade de reconnaissance antérieur, ce qui serait incompatible avec les faits.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce cadre n’est pertinent que tant que le dividende n’est pas encore comptabilisé et reste au stade de transaction future.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Le modèle IFRIC 16 vise la couverture du risque de change d’un investissement net dans une activité à l’étranger, c’est-à-dire des net assets de l’opération étrangère.\nLa question porte ici sur un dividende intragroupe déjà comptabilisé en créance à recevoir, et non sur une couverture d’investissement net.\nL’utiliser imposerait de reformuler l’exposition couverte, ce qui contredirait le fact pattern retenu.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle doit être réservé aux couvertures de net investment, pas aux créances de dividendes intragroupe.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "14",
          "excerpt": "A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé de timing est que le dividende est déjà comptabilisé : l’analyse pertinente est celle d’une créance/dette monétaire intragroupe, non d’une transaction future.",
    "Au niveau consolidé, la qualification dépend d’abord de l’existence d’un risque de change qui n’est pas entièrement éliminé en consolidation sur cette créance/dette intragroupe.",
    "La formalisation exige une documentation de couverture à l’inception de la relation, incluant le risque couvert, l’instrument, l’élément couvert et le hedge ratio.",
    "Le modèle de couverture d’un investissement net ne doit pas être utilisé pour requalifier une exposition de dividende intragroupe déjà reconnue."
  ]
}
