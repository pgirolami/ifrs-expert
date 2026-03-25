{
  "assumptions": [
    "Le dividende intragroupe déclaré a créé une créance/dette intragroupe comptabilisée constituant un élément monétaire.",
    "Le solde est libellé dans une devise générant des écarts de change pertinents au niveau de la consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En comptes consolidés, IFRS 9 admet par exception la couverture du risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. La relation doit être désignée et documentée dès l’origine et satisfaire aux critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture du risque de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose comme règle générale que les éléments couverts doivent être avec une partie externe, mais le paragraphe 6.3.6 prévoit une exception pour le risque de change d’un élément monétaire intragroupe en consolidation. Une créance de dividende déjà enregistrée peut entrer dans cette exception si les écarts de change correspondants ne sont pas totalement éliminés en consolidation et si la relation respecte la documentation et l’efficacité exigées par 6.4.1.",
      "conditions_fr": [
        "La créance/dette de dividende enregistrée est un élément monétaire intragroupe reconnu.",
        "Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée à l’origine.",
        "Les critères d’efficacité et le hedge ratio de l’IFRS 9 6.4.1 sont respectés."
      ],
      "practical_implication_fr": "Le traitement est envisageable, mais il faut démontrer l’exposition de change résiduelle en consolidation et documenter la relation dès l’inception.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "IFRS 9 6.4.1(b)-(c)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation ... and ... the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Ce modèle vise une transaction encore future et hautement probable, dont le risque de change affectera le résultat consolidé. Une créance de dividende déjà comptabilisée n’est plus une transaction prévue ; ce fondement ne correspond donc pas à la situation décrite.",
      "conditions_fr": [
        "La transaction doit encore être prévue et hautement probable.",
        "Le risque de change doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Une fois la créance de dividende reconnue, il ne faut pas documenter la relation comme une couverture de transaction intragroupe prévue.",
      "references": [
        {
          "section": "IFRS 9 6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item ... and the foreign currency risk will affect consolidated profit or loss"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite d’un objet couvert différent : un montant de net assets d’une activité étrangère inclus dans les comptes consolidés. Une créance de dividende intragroupe comptabilisée est un poste monétaire distinct ; elle ne se confond pas avec l’investissement net couvert par ce modèle.",
      "conditions_fr": [
        "L’élément couvert doit être un montant de net assets d’une activité étrangère inclus dans les comptes consolidés.",
        "Les exigences de désignation, documentation et efficacité d’IFRS 9 doivent être respectées."
      ],
      "practical_implication_fr": "Ce modèle ne doit pas être utilisé pour une créance de dividende intragroupe isolée.",
      "references": [
        {
          "section": "IFRIC 16.11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "IFRIC 16.14",
          "excerpt": "A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu que la créance/dette de dividende est bien un élément monétaire intragroupe exposé à des écarts de change non totalement éliminés en consolidation.",
    "Documenter à l’inception l’instrument de couverture, le poste couvert, le risque de change visé, la stratégie de gestion et la méthode d’évaluation de l’efficacité.",
    "Ne pas utiliser le modèle de couverture de transaction intragroupe prévue si la créance de dividende est déjà comptabilisée.",
    "Ne pas confondre cette situation avec une couverture d’investissement net, qui vise les net assets d’une activité étrangère et non une créance intragroupe isolée."
  ]
}
