def add(x, y): #fonction add
    return x + y
def subtract(x, y): #fonction subtarct
    return x - y
def multiply(x, y): #fonction multiply
    return x * y
def divide(x, y): #fonction divide
    return x / y

print("what operation.") #print menu choice fonction
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ") #choice fonction
    if choice in ('1', '2', '3', '4'):

        try:
            num1 = float(input("Enter first number: ")) #ask nombre 1
            num2 = float(input("Enter second number: ")) #ask nombre 2
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))  #execution fonction add and print result

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2)) #execution fonction subtract and print result

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2)) #execution fonction multiply and print result

        elif choice == '4':
            if num2==0:
                try:
                    num2 = float(input("Enter second number (if it's a divide the num need to be different of 0): ")) #divide with 0 and ask nomber 2 different
                except ValueError:
                    print("Invalid input. Please enter a number diffent of 0.")
            print(num1, "/", num2, "=", divide(num1, num2)) #execution fonction divide and print result

        next_calculation = input("Let's do next calculation? (yes/no): ") #ask calcul again, if yes execution of the boucle
        if next_calculation == "no": 
          break #if no quit program
    else:
        print("Invalid Input")