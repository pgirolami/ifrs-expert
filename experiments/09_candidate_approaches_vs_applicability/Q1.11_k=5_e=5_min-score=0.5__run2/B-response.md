{
  "assumptions_fr": [
    "Le dividende déclaré a créé une créance/dette intragroupe monétaire qui reste en cours pendant la période de couverture.",
    "Cette créance/dette est libellée dans une monnaie générant des écarts de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "La question vise les états financiers consolidés du groupe, et non les comptes individuels ou séparés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous les hypothèses retenues, la créance/dette de dividende intragroupe relève de l’exception IFRS 9 sur les postes monétaires intragroupe en consolidation et peut être désignée comme élément couvert. Le modèle pertinent ici est le fair value hedge, pas le cash flow hedge."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Dans les comptes consolidés, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe. Ici, le dividende déclaré a déjà créé une créance/dette intragroupe comptabilisée; sous les hypothèses retenues, ses écarts de change ne sont pas totalement éliminés en consolidation. Cela correspond à un actif/passif reconnu exposé à un risque pouvant affecter le résultat.",
      "conditions_fr": [],
      "practical_implication_fr": "Documenter la relation comme fair value hedge du risque de change sur la créance/dette de dividende intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, le dividende n’est plus une transaction intragroupe future hautement probable: une créance/dette a déjà été comptabilisée. Or, dans le contexte fourni, la voie cash flow hedge en consolidation est présentée pour des transactions intragroupe futures hautement probables. Le cas présent relève donc du poste monétaire intragroupe déjà reconnu, et non d’un cash flow hedge.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette exposition comme cash flow hedge dans ce cas; retenir le fair value hedge si la couverture est mise en place.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation de couverture doit être établie à l’inception et identifier l’instrument de couverture, la créance/dette de dividende intragroupe, le risque de change couvert et le hedge ratio.",
    "Vérifier et conserver la preuve que les écarts de change sur le poste monétaire intragroupe ne sont pas totalement éliminés en consolidation, ce qui suppose des monnaies fonctionnelles différentes.",
    "Suivre l’efficacité de la relation de couverture, y compris la relation économique et l’absence de domination du risque de crédit."
  ]
}
