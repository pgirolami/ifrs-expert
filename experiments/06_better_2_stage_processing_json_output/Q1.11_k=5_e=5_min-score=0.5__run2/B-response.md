{
  "assumptions_fr": [
    "Un dividende intragroupe déclaré et comptabilisé en créance/dette est traité comme un élément monétaire intragroupe.",
    "L’analyse est limitée à la comptabilité de couverture du risque de change selon IFRS 9 dans les états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais sous conditions.\nUne fois la créance de dividende intragroupe enregistrée, l’approche pertinente est celle de l’élément monétaire intragroupe; en consolidation, IFRS 9 ne l’admet que si le risque de change génère des écarts non entièrement éliminés et si la désignation, la documentation et l’efficacité de la couverture respectent 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Selon l’hypothèse retenue, le dividende déclaré déjà comptabilisé est une créance/dette intragroupe, donc un élément monétaire intragroupe et non une transaction future.\nDans ce timing précis, IFRS 9 6.3.6 ouvre une exception en consolidation pour le risque de change de tels postes s’il crée des écarts non entièrement éliminés; la couverture reste alors soumise à la documentation et aux tests d’efficacité de 6.4.1.",
      "conditions_fr": [
        "La créance/dette de dividende doit générer des écarts de change qui ne sont pas entièrement éliminés en consolidation.",
        "La relation de couverture doit être formellement désignée et documentée à l’origine.",
        "Les critères d’efficacité de la couverture d’IFRS 9 6.4.1 doivent être satisfaits."
      ],
      "practical_implication_fr": "Le dividende enregistré peut être traité comme poste couvert de change en consolidation, mais seulement dans le cadre étroit de l’exception applicable aux éléments monétaires intragroupe.",
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
      "label_fr": "Exclusion générale des éléments intragroupe en consolidation",
      "applicability": "non",
      "reasoning_fr": "Le contexte vise un dividende intragroupe déjà enregistré dans des comptes consolidés; la règle générale de 6.3.5 exclut en principe les éléments intragroupe au profit des seules contreparties externes.\nMais, compte tenu de l’hypothèse d’un élément monétaire intragroupe, cette règle n’est pas l’approche opérante ici car l’exception spécifique de 6.3.6 prend le relais.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas fonder la conclusion finale sur la seule règle d’exclusion générale, car le cas décrit relève potentiellement de son exception spécifique.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d’une transaction intragroupe prévisionnelle",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction intragroupe encore prévisionnelle et hautement probable, donc un stade antérieur à celui décrit dans la question.\nOr, l’hypothèse retenue est qu’une créance de dividende est déjà comptabilisée; on ne peut donc pas requalifier ce fait en forecast transaction pour fonder la réponse.",
      "conditions_fr": [],
      "practical_implication_fr": "Après comptabilisation de la créance de dividende, il ne faut pas documenter la relation comme une cash flow hedge d’une transaction prévisionnelle intragroupe.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le bon angle temporel ici est le poste monétaire intragroupe déjà comptabilisé; l’approche « transaction intragroupe prévisionnelle » n’est plus la bonne.",
    "En consolidation, il faut démontrer que les écarts de change sur la créance/dette de dividende ne sont pas entièrement éliminés.",
    "La désignation formelle, la documentation initiale, l’identification du risque couvert et l’analyse de l’efficacité doivent être établies conformément à IFRS 9 6.4.1."
  ]
}
