print("vous avez ici un code qui donne la premiere forme canonique d'une fonction")
print("indications:"
      " et = &,"
      " ou = |,"
      " not A = ~A,")
fonction_logique = input("entrer la fonction logique:")
def first_canonical_form(fonction_logique):
    variables = set()
    for char in fonction_logique:
        if char.isalpha():
            variables.add(char)

    variables = sorted(list(variables))
    num_vars = len(variables)
    num_combinations = 2 ** num_vars

    minterms = []
    for i in range(num_combinations):
        assignment = bin(i)[2:].zfill(num_vars)
        eval_dict = {variables[j]: bool(int(assignment[j])) for j in range(num_vars)}
        if eval(fonction_logique, eval_dict):
            minterms.append(assignment)

    terms = []
    for minterm in minterms:
        term = ""
        for i, var in enumerate(variables):
            if minterm[i] == "0":
                term += f"~{var}&"
            else:
                term += f"{var}&"
        terms.append(term[:-1])

    canonical_form = " | ".join(terms)
    return canonical_form

# Exemple d'utilisation
forme_canonique = first_canonical_form(fonction_logique)
print("Première forme canonique de la fonction logique : ", forme_canonique)
input()
