import itertools
# le nombres de variables vient ici selon votre choix
variables = input("mettre vos variables ici:")
#entrer votre fonction entre les guillemets
print("indications:"
      " et = &,"
      " ou = |,"
      " not A = ~A,")
expression = input("entrer votre fonction:")
def table_de_verite(variables, expression):
    # Créer une liste de tuples avec toutes les combinaisons possibles de valeurs booléennes pour les variables
    combinations = list(itertools.product([0, 1], repeat=len(variables)))
    
    # En-tête de la table de vérité
    header = ' | '.join(variables) + ' | ' + expression
    print(header)
    print('-' * len(header))
    
    # Pour chaque combinaison de valeurs booléennes, évaluer l'expression et afficher le résultat
    for combo in combinations:
        # Créer un dictionnaire pour mapper les valeurs booléennes aux variables
        variable_map = dict(zip(variables, combo))
        # Évaluer l'expression en remplaçant les variables par leurs valeurs dans la combinaison actuelle
        result = eval(expression, variable_map)
        # Afficher la combinaison de valeurs booléennes suivie du résultat de l'expression
        print(' | '.join(str(val) for val in combo) + ' | ' + str(int(result)))
#resultat final
table_de_verite(variables, expression)

