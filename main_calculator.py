from datetime import datetime
import json

# Global variables
history = []

def load_operations():
    """Load the operation history from a JSON file."""
    global history
    try:
        with open("save.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        return []

def save_history():
    """Save the operation history to a JSON file."""
    with open("save.json", "w") as file:
        json.dump(history, file, indent=4)

def get_time():
    """Return the current date and time as a formatted string."""
    now_time = datetime.now()
    now_date_time = now_time.strftime("%d/%m/%Y | %H:%M:%S")
    return now_date_time

def mute_integer(variable):
    """Convert the variable to an integer if it is an integer, otherwise return a rounded float."""
    if variable == int(variable):
        return int(variable)
    else:
        return float("{:.3f}".format(variable))  # Return a float rounded to 3 decimal places

def ask_number(script):
    """Prompt the user to enter a number and handle errors."""
    while True:
        try:
            number = float(input(script).replace(",", "."))  # Accept comma as decimal separator
            number = mute_integer(number)
            return number
        except ValueError:
            print("Error: Please enter a valid number.")

def show_result(operator, a, b, result):
    """Display the result of the operation and add it to the history."""
    if result is not None:
        result = mute_integer(result)
    if operator == "sqr":
        print(f"The result of sqrt({a}) is: {result}")
        history.append({"time": get_time(), "operation": f"sqrt({a}) = {result}"})
    else:
        print(f"The result of {a} {operator} {b} is: {result}")
        history.append({"time": get_time(), "operation": f"{a} {operator} {b} = {result}"})

def ask_operator():
    """Prompt the user to choose an operation from the available options."""
    print("")
    print("═══════════════════════════════════════════════════════")
    print("                   ══ WELCOME ══")
    print("                     Calculator")
    print("═══════════════════════════════════════════════════════")
    print("Please choose an operation from the following options:")
    print("  +  : Addition")
    print("  -  : Subtraction")
    print("  *  : Multiplication")
    print("  /  : Division")
    print("  // : Integer Division")
    print("  %  : Modulo")
    print("  ** : Exponentiation")
    print("  sqr: Square Root")
    print("  H  : History Menu")
    print("═══════════════════════════════════════════════════════")

    operator = input("Enter the desired operation: ").strip()
    while operator not in ["+", "-", "*", "/", "//", "%", "**", "sqr", "H", "D"]:
        print("Error: Invalid operator.")
        operator = input("Please enter a valid operation: ").strip()
    return operator

def operating(a, b, operator):
    """Perform the requested operation between a and b."""
    if b == 0 and operator in ["/", "//", "%"]:  # Handle division by zero error
        print("Error: Division by zero is not allowed.")
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
                print("Error: The square root of a negative number is not defined in real numbers.")
                return None
            return a ** 0.5

def delete_history():
    """Clear the operation history."""
    history.clear()
    print("History cleared.")

def delete_index_history():
    """Delete a specific operation from the history by index."""
    index_delete = int(input("Enter the index of the operation you want to delete: "))
    if index_delete < 1 or index_delete > len(history):
        print("Invalid index.")
        return
    history.pop(index_delete - 1)

def display_history():
    """Display the operation history."""
    if not history:
        print("═══════════════════════════════════════════════════════")
        print("                   ══ HISTORY ══")
        print("                 No history available.")
        print("═══════════════════════════════════════════════════════")
        print("                  Press ctrl + c to exit                  ")
    else:
        print("═══════════════════════════════════════════════════════")
        print("                   ══ HISTORY ══")
        print("═══════════════════════════════════════════════════════")
        print("Would you like to perform one of the following actions?")
        print("  A  : Display History")
        print("  E  : Delete an Operation")
        print("  D  : Clear All History")
        print("Ctrl+C : Return to Home")
        print("═══════════════════════════════════════════════════════")
        history_option = input("Your choice: ").strip().upper()

        # match case for clarity
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
                print("                   ══ HISTORY ══")
                print("                 No history available.")
                print("═══════════════════════════════════════════════════════")
            case _:
                pass  # Unrecognized option

def display_history_2():
    """Display the operation history in a formatted manner."""
    print("═══════════════════════════════════════════════════════")
    print("                   ══ HISTORY ══")
    print(f"No.| Date      | Time    | Operations")
    for i, op in enumerate(history, start=1):
        print(f"{i}. {op['time']} | {op['operation']}")
    print("═══════════════════════════════════════════════════════")

def calculator():
    """Main function to execute the calculator."""
    while True:
        operator = ask_operator()

        if operator == "H":
            display_history()
            continuer = input("Would you like to perform another operation? (yes/no): ").strip().lower()
            if continuer == 'yes':
                continue
            else:
                print("Thank you for using the calculator.")
                break

        if operator == "sqr":
            a = ask_number("Enter the number: ")
            result = operating(a, 0, operator)
            show_result(operator, a, None, result)
        else:
            a = ask_number("Enter the first number: ")
            b = ask_number("Enter the second number: ")
            result = operating(a, b, operator)
            show_result(operator, a, b, result)

        while True:
            second_operation = input("Would you like to perform a second operation with the previous result? (yes/no): ").strip().lower()
            if second_operation == 'yes':
                second_operator = ask_operator()  # Choose a second operator
                if second_operator == "sqr":
                    # Perform the square root
                    second_result = operating(result, 0, second_operator)
                    show_result(second_operator, result, 0, second_result)
                    result = second_result
                elif second_operator == "H":
                    display_history()
                else:
                    c = ask_number("Enter an additional number: ")
                    # Perform the second operation
                    second_result = operating(result, c, second_operator)
                    if second_result is not None:
                        show_result(second_operator, result, c, second_result)
                        result = second_result  # Reuse the last result for the next operation
            elif second_operation == 'no':
                break  # Exit the loop to stop performing a second operation

        # Ask the user if they want to continue
        continuer = input("Would you like to perform another operation? (yes (y) or no (n)): ").strip().lower()
        if continuer not in ['yes', 'y']:
            print("Thank you for using the calculator.")
            break

# Main function
def main():
    load_operations()
    calculator()
    save_history()

if __name__ == "__main__":
    main()
