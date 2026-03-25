{
  "assumptions_fr": [
    "La question vise les états financiers consolidés IFRS, et non les états financiers individuels ou séparés.",
    "Un dividende intragroupe déclaré et comptabilisé en créance/dette est analysé, pour ce test, comme un élément monétaire intragroupe reconnu."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement via l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe en consolidation. Il faut que les écarts de change sur la créance/dette de dividende ne soient pas totalement éliminés en consolidation, et que la désignation, la documentation initiale et les critères d’efficacité soient satisfaits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce cas, on est en consolidation IFRS et, selon l’hypothèse donnée, le dividende intragroupe déjà comptabilisé à recevoir est testé comme un élément monétaire intragroupe reconnu. IFRS 9 6.3.6 prévoit précisément une exception permettant de désigner le risque de change d’un tel élément, mais seulement si les gains ou pertes de change ne sont pas totalement éliminés en consolidation. La relation peut donc être documentée à ce stade, sous réserve aussi de la désignation/documentation initiale et des critères d’efficacité de 6.4.1.",
      "conditions_fr": [
        "la créance/dette de dividende expose le groupe à des écarts de change non totalement éliminés en consolidation",
        "les entités concernées ont des monnaies fonctionnelles différentes de sorte que ces écarts subsistent en consolidation",
        "la désignation formelle, la documentation initiale et les critères d’efficacité d’IFRS 9 sont respectés"
      ],
      "practical_implication_fr": "Si ces conditions sont remplies, la créance de dividende peut être désignée comme élément couvert du risque de change en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.3.6",
          "excerpt": "foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "external_item_restriction",
      "label_fr": "Règle générale des éléments externes",
      "applicability": "non",
      "reasoning_fr": "Cette voie ne permet pas, dans ce cas précis, de documenter la couverture car la question porte sur des dividendes intragroupe en consolidation. Or IFRS 9 6.3.5 réserve en principe les éléments couverts aux actifs, passifs, engagements fermes ou transactions prévues avec une partie externe à l’entité de reporting. Le fait pattern ne satisfait donc pas cette règle générale, sauf à passer par l’exception spécifique de 6.3.6.",
      "conditions_fr": [],
      "practical_implication_fr": "Par défaut, un dividende intragroupe ne peut pas être désigné comme élément couvert dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.5",
          "excerpt": "transactions between entities in the same group only in the individual or separate financial statements ... and not in the consolidated financial statements of the group"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction intragroupe future, hautement probable, dont le risque de change affectera le résultat consolidé. Ici, selon la question et l’hypothèse, le dividende est déjà comptabilisé à recevoir : on est au stade d’un élément reconnu, non d’une transaction future. Elle n’est donc pas applicable sans revenir à un stade antérieur différent du fait pattern posé.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette piste est pertinente avant comptabilisation d’un dividende, pas après reconnaissance d’une créance de dividende.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "B6.3.5",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Le modèle d’IFRIC 16 concerne la couverture du risque de change attaché à un investissement net dans une activité étrangère, c’est-à-dire un montant de net assets de l’activité étrangère. La question posée vise au contraire une créance de dividende intragroupe déjà comptabilisée en consolidation. Cette approche supposerait donc un objet couvert différent et n’est pas applicable à ce cas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas assimiler une créance de dividende intragroupe à un investissement net couvert selon IFRIC 16.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif, au stade où le dividende est déjà comptabilisé, est le test de non-élimination totale des écarts de change en consolidation.",
    "La présence de monnaies fonctionnelles différentes entre les entités concernées est l’indice fourni par le contexte pour expliquer pourquoi des écarts de change peuvent subsister en consolidation.",
    "La documentation doit être établie dès l’origine de la relation de couverture et identifier l’instrument de couverture, la créance de dividende couverte, le risque de change visé et l’évaluation de l’efficacité.",
    "Il ne faut pas requalifier le cas en transaction intragroupe future ni en couverture d’investissement net : ces modèles répondent à un autre stade ou à un autre objet couvert."
  ]
}
