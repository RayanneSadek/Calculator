def ask_number(script):
    """ Demande à l'utilisateur d'entrer un nombre et gère les erreurs. """
    while True:
        try:
            input_user = input(script).strip()

            if input_user == "":# Gestion des absences d'entrées
                print("Vous n'avez pas entré le nombre demandé")
                      
                continue
            
            input_number = input_user.replace(',','.') #Remplace les , par des . pour la conformité
            number = float(input_number)#transformation de la string en float
            
            if number  ==int(number): # Suppression du .0 en cas d'entiers
                return int(number)
            else:
                return number
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide.")

def operating(a, b, operator):
    """Effectue l'opération demandée entre a et b."""
    match operator:
        case "+":
            result = a + b
            if result == int(result): # Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "-":
            result = a - b
            if result == int(result):# Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "*":
            result = a * b
            if result == int(result):# Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "/":
            if b == 0:
                print("Erreur: division par zéro impossible.")
                return None
            result = a / b
            if result == int(result):# Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "//":
            if b == 0:# Gestion de la division par 0
                print("Erreur division par zero impossible ")
            result = a // b
            if result == int(result):# Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "%":
            if b == 0:
                print("Erreur division par zero impossible ")
            result = a % b
            if result == int(result):# Mute en entier quand le résultat n'est pas un décimal
                result = int(result)
                string = (f"{a} {operator} {b} = {result}")
            else:
                string = (f"{a} {operator} {b} = {result:.3f}")
            print(string)
        case "":
            print("vide")
        case _:
            print("Erreur: opération inconnue.")#Gestion des erreurs d'entrées de décimal
  

def calculator():
        """ Fonction principale pour exécuter la calculatrice. """
        print("")
        print("═══════════════════════════════════════════════════════")
        print("                   ══ BIENVENUE ══")
        print("                     Calculatrice")
        print("═══════════════════════════════════════════════════════")

    
        while True:
            # Demander les entrées
            a = ask_number ("Entrez le premier nombre: ")
            b = ask_number("Entrez le second nombre: ")
            
            operator = input("Entrez l'opération (+, -, *, /, //, %): ").strip()
            
            # Effectuer l'opération et afficher le résultat
            result = operating(a, b, operator)
            


             # Demander à l'utilisateur s'il souhaite continuer
            continuer = input("Souhaitez-vous effectuer une autre opération ? (oui/non) : ").strip().lower()
            if continuer != 'oui':
                print("Merci d'avoir utilisé la calculatrice.")
                break

# Lancer la calculatrice
calculator()