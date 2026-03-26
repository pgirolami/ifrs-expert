{
  "assumptions_fr": [
    "La créance de dividende intragroupe et la dette correspondante ne sont pas réglées et créent une exposition de change parce qu’au moins une monnaie fonctionnelle diffère de la devise du dividende.",
    "La question porte sur la comptabilité de couverture selon IFRS 9 dans les comptes consolidés pour une créance intragroupe déjà comptabilisée."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous réserve que la créance/dette de dividende soit un poste monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation. Dans ce cas, une documentation de couverture en comptes consolidés est envisageable, avec un modèle cohérent avec l’exposition réellement documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée est un actif reconnu, ce qui correspond au modèle de couverture de juste valeur pour un risque de change sur un poste existant. En consolidation, l’intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés.",
      "conditions_fr": [
        "La créance et la dette de dividende constituent un poste monétaire intragroupe non réglé",
        "Les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "Ce modèle est utilisable si la documentation désigne la créance de dividende comme élément couvert de change au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Ce modèle peut s’envisager ici si l’exposition couverte est définie comme la variabilité, en monnaie fonctionnelle, du flux d’encaissement futur jusqu’au règlement de la créance de dividende. Il est toutefois moins naturel qu’une couverture de juste valeur pour une créance déjà reconnue et, en consolidation, il faut aussi que le poste monétaire intragroupe génère des écarts de change non entièrement éliminés.",
      "conditions_fr": [
        "La documentation vise la variabilité du flux d’encaissement du dividende jusqu’au règlement",
        "Les écarts de change sur le poste monétaire intragroupe ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "Ne retenir ce modèle que si le dossier de couverture cible bien le flux d’encaissement futur, et non uniquement la réévaluation comptable de la créance.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que le risque de change sur la créance/dette de dividende subsiste réellement au niveau consolidé; sinon l’exception intragroupe ne s’applique pas.",
    "La documentation doit être formalisée dès l’initiation de la relation de couverture et identifier l’instrument de couverture, l’élément couvert, le risque de change et l’évaluation de l’efficacité.",
    "Pour une créance de dividende déjà comptabilisée, la couverture de juste valeur sera en pratique souvent le modèle le plus direct; la couverture de flux exige de cadrer explicitement l’exposition comme un flux futur jusqu’au règlement."
  ]
}
