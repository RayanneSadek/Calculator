import time

operators_list = { "+": "l'addition", "-": "la soustraction", "*" : "la multiplication", "/": "la division"}
historique = {}

def obtenir_heure_locale():
    local_time = time.localtime()
    return (local_time.tm_hour, local_time.tm_min, local_time.tm_sec, local_time.tm_mday, local_time.tm_mon, local_time.tm_year)
def insert_number_1():
    while True:
        try:
            input_user_1 = input("Veuillez entrer le premier nombre: ")
            if input_user_1 == "":
                print("Vous n'avez pas entré le premier nombre")
                continue
            else:
                input_number = input_user_1.replace(',','.')
                num1 = float(input_number)
            
            if num1 ==int(num1):
                return int(num1)
            else:
                return num1

        except ValueError:
            print ('Erreur de frappe')
            insert_number_1()
            continue

def insert_number_2():
    while True :
        try:
            input_user_2 =  input("Veuillez entrer le second nombre: ")
            input_number = input_user_2.replace(',','.')
            if input_user_2== "":
                print("Vous n'avez pas entré le second nombre: ")
                insert_number_2
                continue
            num2 = float(input_number)
            
            if num2 ==int(num2):
                return int(num2)
            else:
                return num2

        except ValueError:
            print ('Erreur de frappe')
            continue

def operators_choice():
        while True:
            operator = input("Quel type d'opération (+, -, * ou /) :")
            
            if operator == "":
                print("Vous n'avez pas indiqué quel type d'opération vous désirez.")
                continue
            
            elif operator not in operators_list:
                print("Opérateur non valide.")
                continue


            else:
                print(f"Vous avez choisi {operators_list[operator]}, le résultat est :")
                return operator
            
def calc(operator, num1, num2): 

     match operator:
        
        case "+" :
                result = num1 + num2
                if result == int(result):
                        result = int(result)
                        string = (f"{num1} {operator} {num2} = {result}")
                else:
                    string = (f"{num1} {operator} {num2} = {result:.3f}")
                print(string)
        
        case "-" :
                    result = num1 - num2
                    if result == int(result):
                        result = int(result)
                        string = (f"{num1} {operator} {num2} = {result}")
                    else:
                        string = (f"{num1} {operator} {num2} = {result:.3f}")
                    print(string)
        case "*":
                    result = num1 * num2
                    if result == int(result):
                        result = int(result)
                        string = (f"{num1} {operator} {num2} = {result}")
                    else:
                        string = (f"{num1} {operator} {num2} = {result:.3f}")
                    print(string)
        case "/" :
                    if num2 == 0:
                       print("Division par 0 impossible")
                       main()

                    result = num1 / num2
                    
                    if result == int(result):
                        result = int(result)
                    
                    string = (f"{num1} {operator} {num2} = {result:.2f}")
                    print(string)

def  choice():           
        choice = input("Une nouvelle opération: Entre O. Pour quitter: Entre n'importe quoi").upper()
        if choice == "O":
                    main()
        else:
            print("Au revoir")

def main():
    print("")
    print("═════════════════════════════════════")
    print("---------  Calculatrice  ------------")
    print("═════════════════════════════════════")
    num1 = insert_number_1()
    num2 = insert_number_2()
    operator = operators_choice()
    calc(operator, num1, num2)
    choice()


           
      
main()










