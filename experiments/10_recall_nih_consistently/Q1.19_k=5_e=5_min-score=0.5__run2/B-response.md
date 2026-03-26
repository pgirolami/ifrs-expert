{
  "assumptions_fr": [
    "La question porte sur des états financiers consolidés.",
    "La créance de dividende intragroupe constitue un élément monétaire exposé au risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement si la créance intragroupe génère des écarts de change non intégralement éliminés en consolidation. Dans les faits décrits, la voie pertinente est la couverture de juste valeur du risque de change sur la créance déjà comptabilisée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été reconnu en créance à recevoir : il s’agit donc d’un actif reconnu, et non d’une transaction future.\nLe contexte prévoit expressément qu’en consolidation le risque de change d’un élément monétaire intragroupe peut être un élément couvert; appliqué à une créance reconnue, cela s’aligne avec le modèle de couverture de juste valeur.",
      "conditions_fr": [
        "la créance intragroupe doit générer des écarts de change qui ne sont pas intégralement éliminés en consolidation, typiquement entre entités ayant des monnaies fonctionnelles différentes"
      ],
      "practical_implication_fr": "La relation peut être documentée au niveau consolidé sur la créance reconnue et le risque de change correspondant.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Le contexte rattache explicitement l’intragroupe en consolidation, pour ce modèle, aux transactions intragroupe hautement probables.\nOr, dans la situation décrite, le dividende n’est plus au stade prévisionnel : il a déjà été reconnu en créance à recevoir. Le risque porte donc sur un solde monétaire existant, pas sur une transaction future.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n’est pas la plus appropriée une fois le dividende déjà comptabilisé en créance intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Une créance de dividende intragroupe n’est pas un montant de net assets d’une activité à l’étranger, mais un solde intragroupe distinct déjà comptabilisé.\nLe modèle de couverture d’investissement net vise le risque de change sur les actifs nets de l’activité étrangère, non sur une créance de dividende intragroupe.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne répond pas au risque décrit, qui porte sur une créance intragroupe et non sur l’investissement net.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu si la créance de dividende crée bien des écarts de change non intégralement éliminés en consolidation.",
    "La documentation formelle doit être établie à l’inception de la relation de couverture et identifier l’instrument, la créance couverte, le risque de change et le hedge ratio.",
    "Le fait que le dividende soit déjà reconnu oriente l’analyse vers un solde monétaire existant, et non vers une transaction intragroupe hautement probable.",
    "La désignation doit être portée au niveau des comptes consolidés, car c’est à ce niveau que l’exception sur l’élément monétaire intragroupe est appréciée."
  ]
}
