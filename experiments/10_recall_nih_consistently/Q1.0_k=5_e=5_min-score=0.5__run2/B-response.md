{
  "assumptions_fr": [
    "On suppose que le dividende intragroupe crée, dans les comptes consolidés, une créance ou dette intercompagnie libellée en devise.",
    "On suppose que la question porte sur l’application de la comptabilité de couverture selon IFRS 9 dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement via une couverture de juste valeur de la composante change de la créance intragroupe déjà comptabilisée, si ce poste monétaire crée en consolidation une exposition de change non totalement éliminée. La couverture de flux de trésorerie n’est pas l’approche adaptée dans cette situation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans votre cas, il existe déjà une créance à recevoir: on est donc sur un actif reconnu, ce qui correspond à l’approche de couverture de juste valeur. En consolidé, la règle générale exclut l’intragroupe, mais une exception existe pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. La couverture viserait donc le risque de change de la créance/dette intragroupe, et non le dividende intragroupe en tant que tel.",
      "conditions_fr": [
        "La créance ou dette née du dividende doit constituer un poste monétaire intragroupe exposé au change.",
        "Les écarts de change correspondants ne doivent pas être intégralement éliminés en consolidation, typiquement parce que les entités ont des monnaies fonctionnelles différentes."
      ],
      "practical_implication_fr": "Si ces conditions sont remplies, la documentation de couverture doit désigner dès l’origine le poste monétaire intragroupe, le risque de change couvert et l’instrument de couverture.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans votre situation, le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance à recevoir. L’approche identifiée ici pour la couverture de flux vise les transactions intragroupe hautement probables; or vous n’êtes plus sur une transaction future mais sur un poste déjà reconnu. Le contexte fourni ne permet donc pas de retenir cette voie pour ce cas précis.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter ce cas en cash flow hedge sur la base du contexte fourni; l’analyse doit se concentrer sur le poste monétaire reconnu.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "B6.3.5",
          "excerpt": "This is usually the case for royalty payments, interest payments or management charges between members of the same group, unless there is a related external transaction."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord si la créance de dividende est bien un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
    "En consolidé, le point clé n’est pas le dividende intragroupe lui-même mais l’existence d’un risque de change résiduel non entièrement éliminé sur la créance/dette intercompagnie.",
    "Si la couverture est retenue, la désignation et la documentation doivent être formalisées à l’origine de la relation de couverture.",
    "Une fois la créance comptabilisée, l’approche à analyser est celle de la couverture de juste valeur, pas celle d’une transaction intragroupe future."
  ]
}
