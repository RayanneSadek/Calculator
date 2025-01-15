def ask_number(scritp):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            return float(input(scritp))  # On accepte les entiers et les décimaux
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

def operating(a, b, operator):
    """ Effectue l'opération demandée entre a et b. """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("Erreur: division par zéro impossible.")
            return None
        return a / b
    elif operator == "//":
        if b==0:
            print("Erreur division par zero impossible ")
            return None
        return a // b
    elif operator == "%":
        if b == 0:
             print("Erreur division par zero impossible ")
             return None
        return a % b

    else:
        print("Erreur: opération inconnue.")
        return None

def calculator():
    """ Fonction principale pour exécuter la calculatrice. """
    print("Bienvenue dans la calculatrice !")
    operation_history =[]
    
    while True:
        # Demander les entrées
        a = ask_number ("Entrez le premier nombre: ")
        b = ask_number("Entrez le second nombre: ")
        
        operator = input("Entrez l'opération (+, -, *, /, //, %): ").strip()
        
        # Effectuer l'opération et afficher le résultat
        result = operating(a, b, operator)
        
        if result is not None:
            print(f"Le résultat de {a} {operator} {b} est : {result}")
            operation_history.append(f"{a} {operator} {b} = {result}")
        
        # Demander à l'utilisateur s'il souhaite continuer
        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
        if continuer != 'oui':
            print("Merci d'avoir utilisé la calculatrice.")
            break
    #affichage de l'historique
    print("\naffichage de l'historique des opérations")
    if operation_history:
        for operation in operation_history:
            print(operation)

# Lancer la calculatrice
calculator()
