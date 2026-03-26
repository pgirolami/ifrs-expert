{
  "assumptions_fr": [
    "Le dividende a déjà été comptabilisé comme créance/dette intragroupe ; il est donc analysé comme un poste monétaire intragroupe et non comme une transaction prévue.",
    "L'analyse est limitée aux états financiers consolidés en IFRS 9, dans le cadre de la comptabilité de couverture."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui sous conditions. En consolidation, un dividende intragroupe comptabilisé à recevoir n'est éligible que via l'exception visant le risque de change d'un poste monétaire intragroupe. La relation peut être documentée si les écarts de change ne sont pas totalement éliminés en consolidation et si les exigences de désignation, documentation et efficacité d'IFRS 9 sont respectées."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe comptabilisé à recevoir est traité, selon l'hypothèse donnée, comme un poste monétaire intragroupe reconnu.\nEn consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais le paragraphe 6.3.6 permet la couverture du risque de change d'un poste monétaire intragroupe si les écarts de change ne sont pas totalement éliminés.\nComme il s'agit d'un actif reconnu exposé à un risque particulier pouvant affecter le résultat, la documentation doit relever d'une couverture de juste valeur, sous réserve du respect du paragraphe 6.4.1.",
      "conditions_fr": [
        "Le dividende doit être comptabilisé comme une créance/dette intragroupe reconnue, donc comme un poste monétaire intragroupe.",
        "Le risque de change doit générer des gains ou pertes qui ne sont pas totalement éliminés en consolidation, en pratique entre entités à monnaies fonctionnelles différentes.",
        "La relation doit satisfaire aux exigences de désignation formelle, de documentation initiale et d'efficacité prévues par IFRS 9."
      ],
      "practical_implication_fr": "La relation se documente comme une couverture de juste valeur du seul risque de change de la créance de dividende intragroupe, et non comme une couverture générale d'un flux intragroupe.",
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier à l'inception que la créance de dividende est bien un poste monétaire intragroupe libellé dans une devise créant une exposition de change résiduelle en consolidation.",
    "Documenter explicitement que le risque couvert est le seul risque de change et démontrer pourquoi les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Préparer la documentation IFRS 9 dès l'origine : instrument de couverture, élément couvert, risque couvert, ratio de couverture et méthode d'évaluation de l'efficacité.",
    "Si aucun écart de change ne subsiste en consolidation, le traitement ne s'applique pas dans cette situation."
  ]
}
