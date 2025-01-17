def mute_integer(variable):
            if variable== int(variable): 
                variable= int(variable)
                return variable
            else:
                 return variable
            
def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            number= float(input(script).replace(",", "."))  # On accepte les entiers et les décimaux et remplace la virgule par un point
            number = mute_integer(number)
            return number

        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

history=[]
index=1

"""def delete_history():
     history.clear
     print("Historique effacé.")"""

def ask_operator():
            operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr,H): ").strip()
            while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr","H"]:  # Vérification de l'opérateur valide
                print("Erreur: opérateur non valide.")
                operator = input("Entrez l'opération (+, -, *, **, /, //, %, sqr, H): ").strip()
            return operator
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
    
    while True:
        operator = ask_operator()
        if "H" in operator:
                if not history:
                    print("Aucun historique disponible.")
                else:
                    print("Historique:")
                    for i, op in enumerate(history, start=1):
                        print(f"{i}. {op}")
                continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
                if continuer != 'oui':
                    print("Merci d'avoir utilisé la calculatrice.")
                continue

        # Demander les entrées
        a = ask_number("Entrez le premier nombre: ")

        # Si l'opération est une racine carrée, ne pas demander de deuxième nombre
        if operator == "sqr":
            result = operating(a, 0, operator)
        else:
            b = ask_number("Entrez le second nombre: ")
            result = operating(a, b, operator)

        # Effectuer l'opération et afficher le résultat
        if result is not None:
          result = mute_integer(result)
        if operator == "sqr":
                print(f"Le résultat de sqrt({a}) est : {result}")
                history.append(f"{operator} {a}  = {result}")
                
        else:
                print(f"Le résultat de {a} {operator} {b} est : {result}")
                history.append(f"{a} {operator} {b} = {result}")
                
        # Demander à l'utilisateur s'il souhaite continuer
        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui ou o pour continuer) : ").strip().lower()
        if continuer not in ['oui', 'o']:
            print("Merci d'avoir utilisé la calculatrice.")
            break

# Lancer la calculatrice
calculator()