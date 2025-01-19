from datetime import datetime
import json

history = []
index=1

def load_operations():
    global history
    try:
        with open("save.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        return []

def save_history():
    """Sauvegarde l'historique dans le fichier save.json"""
    with open("save.json", "w") as file:
        json.dump(history, file, indent=4)

def get_time():
    """Retourne l'heure et la date actuelles sous forme de chaîne formatée"""
    now_time = datetime.now()
    now_date_time = now_time.strftime("%d/%m/%Y | %H:%M:%S")
    return now_date_time

def mute_integer(variable):
    """Si la variable est un entier, renvoie-la en tant qu'entier."""
    if variable == int(variable):
        return int(variable)
    else:
        return float("{:.3f}".format(variable))  # Renvoie un float arrondi

def ask_number(script):
    """Demande à l'utilisateur d'entrer un nombre et gère les erreurs"""
    while True:
        try:
            number = float(input(script).replace(",", "."))  # Accepte la virgule comme séparateur décimal
            number = mute_integer(number)
            return number
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

def show_result(operator, a, b, result):
    """Affiche le résultat de l'opération et l'ajoute à l'historique"""
    if result is not None:
        result = mute_integer(result)
    if operator == "sqr":
        print(f"Le résultat de sqrt({a}) est : {result}")
        history.append({"time": get_time(), "operation": f"sqrt({a}) = {result}"})
    else:
        print(f"Le résultat de {a} {operator} {b} est : {result}")
        history.append({"time": get_time(), "operation": f"{a} {operator} {b} = {result}"})

def ask_operator():
    """Demande à l'utilisateur de choisir une opération parmi les options disponibles"""
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
    print("  H  : Menu Historique")
    print("═══════════════════════════════════════════════════════")
    
    operator = input("Entrez l'opération souhaitée : ").strip()
    while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr", "H", "D"]:
        print("Erreur : opérateur non valide.")
        operator = input("Veuillez entrer une opération valide : ").strip()
    return operator

def operating(a, b, operator):
    """Effectue l'opération demandée entre a et b"""
    if b == 0 and operator in ["/", "//", "%"]:  # Gestion de l'erreur division par zéro
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

def delete_history():
    """Efface l'historique des opérations"""
    history.clear()
    print("Historique effacé.")

def delete_index_history():
    """efface l'index de l'historique"""
    index_delete=int(input("Entrez l'index de l'opération que vous souhaitez effacer: "))
    if index_delete<1 or index_delete>len(history):
        print("Index invalide.")
        return
    history.pop(index_delete-1)

def display_history():
    """Affiche l'historique des opérations"""
    if not history:
                print("═══════════════════════════════════════════════════════")
                print("                   ══ HISTORIQUE ══")
                print("                 Aucun historique disponible.")
                print("═══════════════════════════════════════════════════════")
                print("                  ctrl +c pour sortir                  ")
    else:
                print("═══════════════════════════════════════════════════════")
                print("                   ══ HISTORIQUE ══")
                print("═══════════════════════════════════════════════════════")
                print("Voulez-vous effectuer l'une des opérations suivantes ?")
                print("  A  : Afficher l'historique")
                print("  E  : Effacer une opération")
                print("  D  : Effacer tout l'historique")
                print("Ctrl+C : Retourner à l'accueil")
                print("═══════════════════════════════════════════════════════")
                history_option = input("Votre choix : ").strip().upper()
               
                # match case pour plus de clarté
                match history_option:
                    case "A":
                        display_history_2()
                    case "E":
                        display_history_2() 
                        delete_index_history()
                        print("═══════════════════════════════════════════════════════")
                    case "D":
                            delete_history()
                            print("═══════════════════════════════════════════════════════")
                            print("                   ══ HISTORIQUE ══")
                            print("                 Aucun historique disponible.")
                            print("═══════════════════════════════════════════════════════")
                    case _:
                        pass  # Option non reconnue
def display_history_2():
                        print("═══════════════════════════════════════════════════════")
                        print("                   ══ HISTORIQUE ══")
                        print(f"N°| Date      | Heure    | Opérations")
                        for i, op in enumerate(history, start=1):
                            print(f"{i}. {op['time']} | {op['operation']}")
                        print("═══════════════════════════════════════════════════════") 

def calculator():
    """Fonction principale pour exécuter la calculatrice"""
    while True:
        operator = ask_operator()

        if operator == "H":
            display_history()
            continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
            if continuer == 'oui':
                continue
            else:
                print("Merci d'avoir utilisé la calculatrice.")
                break

        if operator == "sqr":
            a = ask_number("Entrez le nombre: ")
            result = operating(a, 0, operator)
            show_result(operator, a, None, result)
        else:
            a = ask_number("Entrez le premier nombre: ")
            b = ask_number("Entrez le second nombre: ")
            result = operating(a, b, operator)
            show_result(operator, a, b, result)

        while True:
            second_operation = input("Souhaitez-vous effectuer une deuxième opération avec le résultat précédent ? (oui/non): ").strip().lower()
            if second_operation == 'oui':
                second_operator = ask_operator()  # Choisir un second opérateur
                if second_operator == "sqr":
                    # Effectuer la racine carrée
                    second_result = operating(result, 0, second_operator)
                    show_result(second_operator, result, 0, second_result)
                    result = second_result
                elif second_operator == "H":
                        display_history() 
                       
                else:
                    c = ask_number("Entrez un nombre supplémentaire: ")
                    # Effectuer la deuxième opération
                    second_result = operating(result, c, second_operator)
                    if second_result is not None:
                        show_result(second_operator, result, c, second_result)
                        result = second_result  # Réutiliser le dernier résultat pour la prochaine opération
            elif second_operation == 'non':
                break  # Sortir de la boucle pour ne plus faire de deuxième opération

        # Demander à l'utilisateur s'il souhaite continuer
        continuer = input("Souhaitez-vous effectuer une autre opération ? (oui (o) ou non(n)) : ").strip().lower()
        if continuer not in ['oui', 'o']:
            print("Merci d'avoir utilisé la calculatrice.")
            break

# Fonction principale
def main():
    load_operations()
    calculator()
    save_history()


if __name__ == "__main__":
    main()