# Command Line Calculator

A feature-rich calculator application with operation history tracking, built in Python.

## Features

- Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
- Advanced operations: Integer Division, Modulo, Exponentiation, Square Root
- Comprehensive operation history with timestamps
- Ability to perform sequential calculations using previous results
- History management (view, delete specific entries, clear all)
- Persistent storage of calculation history across sessions
- Input validation and error handling

## How to Use

### Requirements
- Python 3.6 or higher (for match-case support)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/command-line-calculator.git
   cd command-line-calculator
   ```

2. Run the calculator:
   ```
   python calculator.py
   ```

### Available Operations

| Symbol | Operation |
|--------|-----------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Integer Division |
| % | Modulo |
| ** | Exponentiation |
| sqr | Square Root |
| H | History Menu |

### Using the Calculator

1. Start the application and select an operation from the menu
2. Enter the required numbers (one number for square root, two for other operations)
3. View the result
4. Choose to:
   - Perform additional operations with the result
   - Start a new calculation
   - Exit the program

### Managing History

Access the history menu by entering 'H' at the operation selection prompt.

From the History menu, you can:
- **A**: Display all past operations with timestamps
- **E**: Delete a specific operation by index
- **D**: Clear the entire history
- **Ctrl+C**: Return to the main menu

## Features in Detail

### Input Validation
- Handles both decimal point formats (dot and comma)
- Validates numeric input and provides error messages
- Prevents division by zero errors

### Number Formatting
- Automatically converts whole numbers to integers (e.g., 5.0 → 5)
- Limits decimal places to three for cleaner output

### Error Handling
- Prevents division by zero
- Handles square root of negative numbers
- Validates user input

### History Management
- Timestamps each operation
- Saves history to a JSON file (save.json)
- Loads history when the application starts

## Examples

```
═══════════════════════════════════════════════════════
                   ══ BIENVENUE ══
                     Calculatrice
═══════════════════════════════════════════════════════
Veuillez choisir une opération parmi les suivantes :
  +  : Addition
  -  : Soustraction
  *  : Multiplication
  /  : Division
  // : Division entière
  %  : Modulo
  ** : Puissance
  sqr: Racine carrée
  H  : Menu Historique
═══════════════════════════════════════════════════════
```

## Implementation Details

The calculator is implemented with the following architecture:
- Function-based modular design for readability and maintainability
- JSON-based persistent storage for calculation history
- Timestamp tracking for all operations
- Match-case statements for clean selection logic
- Recursive operation capability for chained calculations

## License

[MIT License](LICENSE)

## Contributing

Feel free to submit pull requests, create issues, or suggest enhancements!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
