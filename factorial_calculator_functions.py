def get_non_negative_integer() -> int:
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
        except ValueError:
            pass
        print("Invalid input. Please enter a non-negative integer.")


def calculate_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if name == "main":
    number = get_non_negative_integer()
    print(f"The factorial of {number} is: {calculate_factorial(number)}")