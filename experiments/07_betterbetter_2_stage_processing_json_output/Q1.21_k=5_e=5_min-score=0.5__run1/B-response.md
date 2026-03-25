{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un poste monétaire intragroupe comptabilisé, libellé dans une devise générant des écarts de change dans les états financiers consolidés.",
    "L'exposition de change mentionnée en consolidation signifie que les écarts de change correspondants ne sont pas intégralement éliminés à la consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Même si les éléments intragroupe sont en principe exclus comme éléments couverts en consolidation, IFRS 9 prévoit une exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Avec les hypothèses données, la créance de dividendes relève de cette exception, sous réserve des critères généraux de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d'un poste monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le fait décrit est une créance de dividendes intragroupe déjà comptabilisée, donc un poste monétaire intragroupe reconnu. Selon les hypothèses retenues, cette créance crée des écarts de change non intégralement éliminés en consolidation et pouvant affecter le résultat consolidé ; l'exception d'IFRS 9.6.3.6 s'applique donc malgré la règle générale d'exclusion des éléments intragroupe. La désignation reste à mettre en œuvre au bon moment avec la documentation et les tests d'efficacité exigés par IFRS 9.6.4.1.",
      "conditions_fr": [
        "Documenter formellement dès l'inception la relation de couverture, l'instrument de couverture, l'élément couvert et le risque de change couvert.",
        "Utiliser un instrument de couverture éligible.",
        "Démontrer la relation économique, l'absence de domination du risque de crédit et un hedge ratio conforme à la gestion du risque."
      ],
      "practical_implication_fr": "Le groupe peut viser une désignation du seul risque de change de cette créance intragroupe dans les comptes consolidés et appliquer la comptabilité de couverture si la relation est correctement formalisée et efficace.",
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
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation pertinente porte sur le risque de change de la créance intragroupe, non sur l'ensemble du poste pour d'autres risques.",
    "L'analyse doit être faite au niveau des comptes consolidés, en vérifiant que les écarts de change liés à cette créance affectent bien le résultat consolidé.",
    "La relation de couverture doit être documentée dès l'inception et faire l'objet d'un suivi continu des critères d'efficacité IFRS 9."
  ]
}
