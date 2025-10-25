def calculatrice():
    print("Mini Calculatrice")
    print("Opérations disponibles : +  -  *  /")
    a = float(input("Entrez le premier nombre : "))
    operateur = input("Entrez l'opération (+, -, *, /) : ")
    b = float(input("Entrez le deuxième nombre : "))

    if operateur == "+":
        resultat = a + b
    elif operateur == "-":
        resultat = a - b
    elif operateur == "*":
        resultat = a * b
    elif operateur == "/":
        if b != 0:
            resultat = a / b
        else:
            return "Erreur : division par zéro"
    else:
        return "Opérateur non valide"
    return f"Résultat : {resultat}"

print(calculatrice())
