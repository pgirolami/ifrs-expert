{
  "assumptions_fr": [
    "La créance ou dette de dividendes intragroupe est un élément monétaire reconnu entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change identifiés ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au niveau consolidé, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Sous les hypothèses données, l’exposition est donc éligible, sous réserve de la désignation, de la documentation et des tests d’efficacité exigés par IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance sur dividendes est supposée être un actif monétaire intragroupe reconnu.\nMême si la règle générale vise des éléments externes au groupe, le paragraphe 6.3.6 autorise, en consolidation, le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat.\nLe modèle de couverture de juste valeur est donc applicable ici pour un actif reconnu exposé au change, sous réserve des critères de désignation et d’efficacité du paragraphe 6.4.1.",
      "conditions_fr": [
        "La créance sur dividendes est bien un élément monétaire intragroupe reconnu.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux exigences d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "La créance intragroupe peut être désignée comme élément couvert au niveau consolidé dans une relation de couverture de juste valeur du risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi une couverture de flux de trésorerie pour un actif reconnu lorsque la variabilité de ses flux liée à un risque particulier peut affecter le résultat.\nL’exception du paragraphe 6.3.6 rend l’exposition intragroupe éligible au niveau consolidé si les écarts de change sur l’élément monétaire subsistent après consolidation.\nCe traitement peut donc être retenu ici, à condition que le risque de change soit désigné et que les exigences de documentation et d’efficacité du paragraphe 6.4.1 soient respectées.",
      "conditions_fr": [
        "Le risque désigné porte sur la variabilité des flux en devise de la créance reconnue.",
        "Les écarts de change sur la créance intragroupe affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux exigences d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "L’exposition de change liée aux flux de règlement de la créance peut être documentée en couverture de flux de trésorerie au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu que la créance de dividendes intragroupe constitue bien un élément monétaire et que ses écarts de change subsistent en consolidation.",
    "Documenter dès l’inception l’instrument de couverture, l’élément couvert, le risque de change visé et le hedge ratio conformément au paragraphe 6.4.1.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit être aligné sur l’objectif de gestion du risque retenu pour cette créance sur dividendes."
  ]
}
