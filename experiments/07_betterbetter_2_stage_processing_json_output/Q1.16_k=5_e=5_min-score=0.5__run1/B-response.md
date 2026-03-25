{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un item monétaire déjà comptabilisé, libellé dans une devise autre que la monnaie fonctionnelle de son détenteur.",
    "Les écarts de change liés à cette créance ne sont pas intégralement éliminés en consolidation et affectent donc le résultat consolidé.",
    "L'entité peut satisfaire aux exigences IFRS 9 de désignation, de documentation formelle et d'efficacité de la couverture."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, IFRS 9 admet par exception le risque de change d’un item monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés. Sous les hypothèses données, une documentation de couverture est donc possible."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance intragroupe",
      "applicability": "oui",
      "reasoning_fr": "La question porte sur une créance de dividendes intragroupe déjà reconnue ; selon les hypothèses, elle constitue un item monétaire exposé à un risque de change qui affecte le résultat consolidé.\nIFRS 9 permet précisément, en consolidation, de désigner le risque de change d’un item monétaire intragroupe comme élément couvert ; une documentation en couverture de juste valeur est donc cohérente avec ce stade de reconnaissance, sous réserve de la documentation IFRS 9 à l’inception de la relation.",
      "conditions_fr": [],
      "practical_implication_fr": "L'entité peut documenter au niveau consolidé une relation de couverture de juste valeur sur le risque de change de la créance de dividendes intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie des flux de règlement en devise",
      "applicability": "oui",
      "reasoning_fr": "Le fait pattern vise la même créance intragroupe déjà comptabilisée ; l’exposition de change se matérialise aussi dans les flux futurs de règlement en monnaie fonctionnelle, qui, selon les hypothèses, affectent le résultat consolidé.\nComme IFRS 9 autorise un cash flow hedge sur un actif reconnu et admet par exception l’item monétaire intragroupe en consolidation, cette documentation est également recevable dans cette situation si la relation est formalisée conformément à IFRS 9 dès son inception.",
      "conditions_fr": [],
      "practical_implication_fr": "L'entité peut aussi structurer la documentation autour de la variabilité des flux de règlement en devise de la créance reconnue.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability ... and could affect profit or loss"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La base IFRS centrale est l’exception de consolidation pour le risque de change d’un item monétaire intragroupe ; sans effet résiduel en résultat consolidé, la désignation échoue.",
    "La documentation doit être mise en place à l’inception de la relation de couverture, avec identification de la créance, du risque de change couvert, de l’instrument de couverture et du test d’efficacité.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit rester aligné avec le risque effectivement documenté sur cette créance déjà comptabilisée."
  ]
}
