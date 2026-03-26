{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un élément monétaire intragroupe libellé en devise étrangère.",
    "L’analyse est effectuée dans le cadre des états financiers consolidés et du modèle de comptabilité de couverture d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe n’est en principe pas éligible comme élément couvert. Toutefois, pour une créance intragroupe monétaire en devise, la désignation est possible si le risque de change génère des écarts non entièrement éliminés en consolidation et si les critères d’IFRS 9 sur la documentation et l’efficacité sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est supposée être une créance monétaire en devise reconnue en consolidation. La règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les gains ou pertes de change ne sont pas entièrement éliminés en consolidation. La désignation est donc possible ici seulement si cette exposition de change affecte encore le résultat consolidé et si la relation de couverture remplit les critères formels d’IFRS 9.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe libellé en devise étrangère.",
        "Les gains ou pertes de change correspondants ne doivent pas être entièrement éliminés en consolidation.",
        "La relation de couverture doit être formellement désignée et documentée dès l’origine.",
        "Les exigences d’éligibilité et d’efficacité de la couverture doivent être satisfaites."
      ],
      "practical_implication_fr": "La couverture est envisageable en consolidation, mais seulement après démonstration d’un risque de change résiduel au niveau consolidé et mise en place d’une documentation IFRS 9 complète.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que la créance de dividende intragroupe reste un élément monétaire en devise au niveau consolidé au moment de la désignation.",
    "Documenter dès l’origine le risque de change couvert, l’instrument de couverture, le ratio de couverture et le test d’efficacité.",
    "Démontrer que les écarts de change liés à cette créance ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé."
  ]
}
