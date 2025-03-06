"""
factorial_calculator_functions.py

This program calculates the factorial of a given non-negative integer.
It consists of two functions:
1. get_non_negative_integer() - Handles user input and validation.
2. calculate_factorial(n) - Computes the factorial of the given number.

Notable Observations:
- *Function Decomposition:* The program is divided into two functions: get_non_negative_integer for input handling and calculate_factorial for the factorial calculation. This promotes modularity and code organization.
- *Iterative Calculation:* The calculate_factorial function uses a loop to iteratively multiply numbers, which is the core logic of calculating a factorial.
- *Base Case:* The factorial function handles the base case of 0! (factorial of 0) by returning 1.
"""

def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a valid non-negative integer.

    Returns:
        int: The validated non-negative integer input by the user.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))  # User input
            if num < 0:
                print("Error: Please enter a non-negative integer.")  # Check negative input
            else:
                return num  # Return the validated integer
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")  # Check non-integer input

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    
    Args:
        n (int): Non-negative integer.
    
    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1 
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial  # Return the calculated factorial

if _name_ == "_main_":
    # Main Program Flow
    number = get_non_negative_integer()
    result = calculate_factorial(number)  # Compute factorial
    print(f"The factorial of {number} is: {result}")  # Display the result