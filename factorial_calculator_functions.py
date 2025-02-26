"""
factorial_calculator_functions.py

This script calculates the factorial of a non-negative integer.
It consists of two functions:
1. get_non_negative_integer() - Handles user input and validation.
2. calculate_factorial(n) - Calculates the factorial of a given non-negative integer.
"""

def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a valid non-negative integer.

    This function repeatedly asks the user for a valid integer input. If the input is not valid (negative number or non-integer),
    it will keep prompting the user until a valid non-negative integer is entered.

    Returns:
        int: The validated non-negative integer input by the user.

    Example:
        >>> get_non_negative_integer()
        Enter a non-negative integer: 5
        5
    """
    while True:
        try:
            user_input = input("Enter a non-negative integer: ")
            number = int(user_input)
            if number < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                return number
        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer. Please enter a non-negative integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given non-negative integer.

    This function uses an iterative approach to calculate the factorial of n.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the number n.

    Example:
        >>> calculate_factorial(5)
        120
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    # Main program execution
    number = get_non_negative_integer()  # Get valid non-negative integer input
    result = calculate_factorial(number)  # Calculate the factorial
    print(f"The factorial of {number} is: {result}")  # Display the result
