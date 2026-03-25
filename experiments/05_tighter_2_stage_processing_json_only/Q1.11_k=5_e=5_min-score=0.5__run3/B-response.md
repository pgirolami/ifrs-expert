{
  "assumptions": [
    "Le dividende intragroupe déclaré a déjà été comptabilisé en créance/dette intragroupe ; l'exposition analysée est donc un poste monétaire reconnu et non une transaction future.",
    "La créance/dette est libellée dans une devise générant des écarts de change dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : dans les comptes consolidés, le risque de change d'un poste monétaire intragroupe peut être désigné comme élément couvert si les écarts de change ne sont pas totalement éliminés en consolidation. Il faut ensuite satisfaire aux exigences de désignation, de documentation et d'efficacité d'IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose une exception explicite pour le risque de change d'un poste monétaire intragroupe dans les comptes consolidés. Une créance de dividende déjà comptabilisée relève de cette logique si elle est un poste monétaire reconnu et si les écarts de change ne sont pas totalement éliminés à la consolidation. La relation doit aussi respecter la documentation initiale et les tests d'efficacité.",
      "conditions_fr": [
        "La créance/dette de dividende est un poste monétaire intragroupe reconnu.",
        "Les entités du groupe concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux critères d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "La couverture est possible en consolidé pour la créance de dividende seulement si le risque de change subsiste après consolidation.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "IFRS 9 6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_item_prohibition",
      "label_fr": "Interdiction générale des éléments intragroupe",
      "applicability": "non",
      "reasoning_fr": "La règle générale d'IFRS 9 est restrictive : en hedge accounting, les éléments couverts doivent en principe être exposés vis-à-vis d'une partie externe au reporting entity. Pris isolément, un dividende intragroupe ne remplit donc pas cette règle dans les comptes consolidés. Cette approche cède toutefois devant l'exception spécifique des postes monétaires intragroupe.",
      "conditions_fr": [],
      "practical_implication_fr": "Si l'exception de l'article 6.3.6 ne s'applique pas, la désignation est exclue en consolidé.",
      "references": [
        {
          "section": "IFRS 9 6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d'une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette voie vise une transaction intragroupe encore future, hautement probable, et dont le risque de change affectera le résultat consolidé. Or l'hypothèse posée est qu'une créance de dividende est déjà enregistrée ; l'exposition n'est donc plus une transaction future mais un poste monétaire reconnu. Cette approche n'est donc pas la bonne base technique ici.",
      "conditions_fr": [
        "La transaction doit être encore non comptabilisée et hautement probable.",
        "La transaction doit être libellée dans une devise autre que la monnaie fonctionnelle de l'entité qui y entre.",
        "Le risque de change doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Une fois le dividende constaté en créance/dette, il faut sortir de la logique de transaction future et analyser le poste monétaire reconnu.",
      "references": [
        {
          "section": "IFRS 9 6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "IFRS 9 B6.3.5",
          "excerpt": "the intragroup transaction cannot qualify as a hedged item ... unless there is a related external transaction"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite d'une autre catégorie : la couverture du risque de change sur un investissement net dans une activité à l'étranger. L'élément couvert y est un montant de net assets de l'activité étrangère, non une créance de dividende intragroupe déjà comptabilisée. Ce cadre ne répond donc pas à la question posée.",
      "conditions_fr": [
        "L'élément couvert devrait être un montant de net assets d'une activité étrangère, et non une créance intragroupe."
      ],
      "practical_implication_fr": "Ne pas documenter cette situation comme hedge de net investment ; le cadre pertinent reste celui du poste monétaire intragroupe.",
      "references": [
        {
          "section": "IFRIC 16 11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de bascule est le timing : avant comptabilisation du dividende, l'analyse relève d'une transaction future ; après comptabilisation, elle relève d'un poste monétaire reconnu.",
    "Il faut vérifier concrètement si les monnaies fonctionnelles diffèrent et si les écarts de change sur la créance/dette ne sont pas totalement éliminés en consolidation.",
    "La documentation à l'origine doit identifier l'instrument de couverture, la créance/dette couverte, le risque de change visé, le hedge ratio et les sources d'inefficacité.",
    "Si l'exposition au change n'affecte pas effectivement les comptes consolidés, la désignation comme élément couvert en consolidé ne tient pas."
  ]
}
