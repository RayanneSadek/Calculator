from datetime import datetime

# Get the positive time
def get_time():
    now_time = datetime.now()
    now_date_time = now_time.strftime("%d/%m/%Y | %H:%M:%S")
    return now_date_time

def mute_integer(variable):
    if variable == int(variable): 
        variable = int(variable)
        return variable
    else:
        return variable

def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            number = float(input(script).replace(",", "."))  # On accepte les entiers et les décimaux et remplace la virgule par un point
            number = mute_integer(number)
            return number
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

# Print the result and record in the history file
def show_result(operator, a, b, result):
    if result is not None:
        result = mute_integer(result)
    if operator == "sqr":
        print(f"Le résultat de sqrt({a}) est : {result}")
        history.append({"time": get_time(), "operation": f"sqrt({a}) = {result}"})
    else:
        print(f"Le résultat de {a} {operator} {b} est : {result}")
        history.append({"time": get_time(), "operation": f"{a} {operator} {b} = {result}"})

history = []
index = 1

def delete_history():
    """ Efface l'historique des opérations. """
    history.clear()
    print("Historique effacé.")

def ask_operator():
    """ Menu visuel pour choisir une opération. """
    print("")
    print("═══════════════════════════════════════════════════════")
    print("                   ══ BIENVENUE ══")
    print("                     Calculatrice")
    print("═══════════════════════════════════════════════════════")
    print("Veuillez choisir une opération parmi les suivantes :")
    print("  +  : Addition")
    print("  -  : Soustraction")
    print("  *  : Multiplication")
    print("  /  : Division")
    print("  // : Division entière")
    print("  %  : Modulo")
    print("  ** : Puissance")
    print("  sqr: Racine carrée")
    print("  H  : Historique")
    print("  D  : Effacer l'historique")
    print("═══════════════════════════════════════════════════════")
    
    operator = input("Entrez l'opération souhaitée : ").strip()
    while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr", "H", "D"]:
        print("Erreur : opérateur non valide.")
        operator = input("Veuillez entrer une opération valide : ").strip()
    return operator

def operating(a, b, operator):
    """ Effectue l'opération demandée entre a et b. """
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
        case "**":
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
            return a ** 0.5

def calculator():
    """ Fonction principale pour exécuter la calculatrice. """
    while True:
        operator = ask_operator()
        
        if operator == "H":
            if not history:
                print("═══════════════════════════════════════════════════════")
                print("                   ══ HISTORIQUE ══")
                print("                 Aucun historique disponible.")
                print("═══════════════════════════════════════════════════════")
            else:
                print("═══════════════════════════════════════════════════════")
                print("                   ══ HISTORIQUE ══")
                for i, op in enumerate(history, start=1):
                    print(f"{i}. {op['time']} | {op['operation']}")
                print("═══════════════════════════════════════════════════════")
            continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
            if continuer == 'oui':
                continue
            else:
                print("Merci d'avoir utilisé la calculatrice.")
                break

        if operator == "D":
            delete_history()
            continue

        a = ask_number("Entrez le premier nombre: ")

        if operator == "sqr":
            result = operating(a, 0, operator)
            show_result(operator, a, None, result)
        else:
            b = ask_number("Entrez le second nombre: ")
            result = operating(a, b, operator)
            show_result(operator, a, b, result)

        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui (o) ou non(n)) : ").strip().lower()
        if continuer not in ['oui', 'o']:
            print("Merci d'avoir utilisé la calculatrice.")
            break

# fonction main
def main():
    calculator()

if __name__ == "__main__":
    main()
