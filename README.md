# Python Calculator

This project is a basic command-line calculator that allows users to input two numbers and perform an arithmetic operation on them. It supports addition, subtraction, multiplication, and division. The user can continue using the result of the previous operation as the first number for the next calculation or start a new calculation.

## Features
- Supports basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Continuously performs calculations using the result from the previous calculation.
- Prompts the user to start a new calculation or continue with the current result.

## How It Works
1. The program first prompts the user to enter the first number.
2. The user is then asked to select one of the four arithmetic operations (`+`, `-`, `*`, `/`).
3. The program prompts the user to input a second number and then performs the selected operation.
4. After showing the result, the program allows the user to either continue calculating with the result or start a new calculation.

### Functions:
1. **`input_num()`**: 
   - Prompts the user to input the first number, select an operation, and input the next number.
   - Returns a list containing these three values.

2. **`calculate(first_number, picked_operation, next_number)`**: 
   - Takes the three inputs: the first number, the picked operation, and the next number.
   - Performs the corresponding arithmetic operation and prints the result.
   - Returns the result of the calculation.

3. **`total_value()`**: 
   - Uses `input_num()` to get user input, calls `calculate()` to compute the result, and asks the user if they want to continue using the result in further calculations.

4. **Main Loop**:
   - A `while` loop that runs indefinitely, allowing the user to continue performing calculations until they choose to start a new one.

## Prerequisites

- Python 3.10 or higher is required because the program uses the `match-case` statement, introduced in Python 3.10.

## Usage

1. Clone this repository to your local machine.
2. Run the program in a terminal:
   ```bash
   python calculator.py

