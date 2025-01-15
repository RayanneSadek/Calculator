operators_list = { "+": "l'addition", "-": "la soustraction", "*" : "la multiplication", "/": "la division"}

def insert_number_1():
    try:
        input_user_1 = input("Veuillez entrer le premier nombre: ")
        input_number = input_user_1.replace(',','.')
        number1 = float(input_number)

        return number1,input_number

    except ValueError:
        print ('Erreur de frappe')
        insert_number_1()

def insert_number_2():
    try:
        number2=float(input("Renseigne le second nombre: "))
        return number2

    except ValueError:
        print ('Erreur de frappe')
        insert_number_2()

def operators_choice():
        operator = input("Quel type d'opération (+, -, * ou /) :")

        if operator in operators_list:
                print(f"Vous avez choisi {operators_list[operator]}, le résultat est :")
                return operator

        else:
            print("Opérateur non valide.")
            operators_choice()

def calculator(operator, num1, num2):
   
    if operator == "+":
            print(num1+num2)
        
    else:
       print("fuck")

def calc(operator, num1, num2):
        number,  number_str = insert_number_1()
        match operator:
        
            case "+" :
                    print(f"{number_str}")
            case "-" :
                        print(num1 - num2)
            case "*" :
                        print(num1 * num2)
            case "/" :
                        print(num1 / num2)


def main():
    print("")
    print("═════════════════════════════════════")
    print("------------- Calculatrice ----------")
    print("═════════════════════════════════════")
    num1 = insert_number_1()
    num2 = insert_number_2()
    operator = operators_choice()
    calc(input_number, operator, num1, num2)



main()