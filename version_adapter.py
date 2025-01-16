def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            return float(input(script).replace(",", "."))  # On accepte les entiers et les décimaux et remplace la virgule par un point
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

def operating(a, b, operator):
    """ Effectue l'opération demandée entre a et b. """
    # Vérification de la division par zéro, pour toutes les opérations concernées
    if b == 0 and operator in ["/", "//", "%"]:  # factorisation de la gestion de l'erreur division par zéro
        print("Erreur: division par zéro impossible.")
        return None
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "**":  # puissance
            return a ** b
        case "/":
            return a / b
        case "//":
            return a // b
        case "%":
            return a % b
        case "sqr":
            if a < 0:
                print("Erreur: la racine carrée d'un nombre négatif n'est pas définie dans les réels.")
                return None
            return a ** 0.5  # Utilisation de l'exponentiation pour la racine carrée

def calculator():
    """ Fonction principale pour exécuter la calculatrice. """
    print("Bienvenue dans la calculatrice !")
    operation_history = []

    while True:
        # Demander les entrées
        a = ask_number("Entrez le premier nombre: ")
        operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr): ").strip()

        while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr"]:  # Vérification de l'opérateur valide
            print("Erreur: opérateur non valide.")
            operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr ): ").strip()

        # Si l'opération est une racine carrée, ne pas demander de deuxième nombre
        if operator == "sqr":
            result = operating(a, 0, operator)
        else:
            b = ask_number("Entrez le second nombre: ")
            result = operating(a, b, operator)

        # Effectuer l'opération et afficher le résultat
        if result is not None:
             if result == int(result):  # Convertir en entier quand le résultat n'est pas un décimal
                result = int(result)
        if operator == "sqr":
                print(f"Le résultat de sqrt({a}) est : {result}")
                operation_history.append(f"sqrt({a}) = {result}")

        else:
                print(f"Le résultat de {a} {operator} {b} est : {result}")
                operation_history.append(f"{a} {operator} {b} = {result}")

        # Affichage de l'historique des opérations
        print("\nHistorique des opérations :")
        if operation_history:
            for operation in operation_history:
                print(operation)

        # Demander à l'utilisateur s'il souhaite continuer
        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui ou o pour continuer) : ").strip().lower()
        if continuer not in ['oui', 'o']:
            print("Merci d'avoir utilisé la calculatrice.")
            break

# Lancer la calculatrice
calculator()
