{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un élément monétaire comptabilisé, libellé en devise étrangère.",
    "L'exposition de change identifiée génère des écarts de change non totalement éliminés en consolidation et susceptibles d'affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 admet expressément le risque de change d'un élément monétaire intragroupe lorsqu'il crée des écarts de change non totalement éliminés, ce qui est précisément supposé ici. La relation retenue doit ensuite satisfaire aux exigences de désignation, documentation et efficacité du paragraphe 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change de la créance",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce cas, la créance sur dividendes est supposée déjà comptabilisée comme actif monétaire intragroupe en devise. Malgré la règle générale d'exclusion des éléments intragroupe, le paragraphe 6.3.6 admet au niveau consolidé le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés, ce qui correspond aux hypothèses. Comme l'item est déjà reconnu, une couverture de juste valeur du risque de change est cohérente avec le paragraphe 6.5.2(a), sous réserve des critères de 6.4.1.",
      "conditions_fr": [
        "Documenter formellement la relation de couverture dès son origine au niveau consolidé.",
        "Démontrer une relation économique entre l'instrument de couverture et le risque de change de la créance.",
        "Retenir un hedge ratio cohérent avec la gestion du risque effectivement pratiquée."
      ],
      "practical_implication_fr": "Il faut désigner la créance intragroupe comme item couvert en consolidation et mettre en place un suivi périodique de l'efficacité.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation ... and the entity will assess whether the hedging relationship meets the hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie des flux de règlement en devise",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les faits portent sur une créance intragroupe déjà comptabilisée, et le paragraphe 6.5.2(b) vise aussi la variabilité des flux de trésorerie d'un actif reconnu. Si les flux de règlement en devise de cette créance exposent le groupe à des écarts de change non totalement éliminés, l'exception du paragraphe 6.3.6 permet la désignation au niveau consolidé dans le cadre exact des hypothèses. Cette voie reste conditionnée à la documentation, au test de relation économique et au hedge ratio exigés par 6.4.1.",
      "conditions_fr": [
        "Documenter formellement la relation de couverture dès son origine au niveau consolidé.",
        "Montrer que la variabilité des flux de règlement en devise est bien l'exposition couverte.",
        "Démontrer la relation économique et un hedge ratio aligné sur la stratégie de gestion du risque."
      ],
      "practical_implication_fr": "Il faut structurer la couverture autour des flux de règlement en devise de la créance et en suivre l'efficacité au niveau consolidé.",
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
          "excerpt": "the hedge ratio ... is the same as that resulting from the quantity of the hedged item ... and the quantity of the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "L'analyse se place après comptabilisation de la créance : il s'agit donc d'un item reconnu, non d'une transaction future à reformuler.",
    "Au niveau consolidé, la base d'éligibilité est l'exception du paragraphe 6.3.6 pour les éléments monétaires intragroupe en devise.",
    "Le choix entre juste valeur et flux de trésorerie doit refléter la stratégie de gestion du risque effectivement documentée et testée selon le paragraphe 6.4.1."
  ]
}
