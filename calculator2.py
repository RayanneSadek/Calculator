def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            return float(input(script))  # On accepte les entiers et les décimaux
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")
def operating(a, b, operator): # fonction qui gère les opérations et les erreurs
    """ Effectue l'opération demandée entre a et b. """
    # Vérification de la division par zéro, pour toutes les opérations concernées
    if b == 0 and operator in ["/", "//", "%"]:      # factorisation de la gestion de l'erreur division par ZERO
        print("Erreur: division par zéro impossible.")
        return None
    

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator =="**":# puissance
        return a ** b
    elif operator == "/":
        return a / b
    elif operator == "//":
        return a // b
    elif operator == "%":
        return a % b
    elif operator == "sqr":
        if a < 0:
            print("Erreur: la racine carrée d'un nombre négatif n'est pas définie dans les réels.")
            return None
        return a ** 1/2  # Utilisation de l'exponentiation pour la racine carré

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
        operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr): ").strip()
    
        while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr"]:# Vérification de l'opérateur valide
            print("Erreur: opérateur non valide.")
            operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr ): ").strip()
        if operator == "sqr":
            result = operating(a, 0, operator)
        else:
            b = ask_number("Entrez le second nombre: ")
            result = operating(a, b, operator)    
       # b = ask_number("Entrez le second nombre: ")
        
       
        
        # Effectuer l'opération et afficher le résultat
        #result = operating(a, b, operator)
        
        if result is not None:
            print(f"Le résultat de {a} {operator} {b if operator != 'sqr' else ''} est : {result}")
            operation_history.append(f"{a} {operator} {b if operator != 'sqr' else ''} = {result}")
        #affichage de l'historique
        print("\naffichage de l'historique des opérations")
        if operation_history:
            for operation in operation_history:
                print(operation)
        # Demander à l'utilisateur s'il souhaite continuer
        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui ou o pourcontinuer ou n'importe qu'elle autre lettre)  : ").strip().lower()
        if continuer != 'oui' and continuer!="o":
            print("Merci d'avoir utilisé la calculatrice.")
            break
    

# Lancer la calculatrice
calculator()
