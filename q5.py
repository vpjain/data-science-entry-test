def check_divisibility(num, divisor):
    """
    Checks if a number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric (int or float).
    - Returns True if num is divisible by divisor, False otherwise.

    Parameters:
        num (int, float): The number to be divided.
        divisor (int, float): The number to divide by.

    Returns:
        bool: True if divisible, False otherwise.
              Also returns False if inputs are not numeric or divisor is zero.
    """
    # Ensure both inputs are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Warning: Both num and divisor must be numeric.")
        return False
    # Avoid ZeroDivisionError by checking for divisor equal to zero
    if divisor == 0:
        print("Warning: Division by zero is not allowed.")
        return False

    # Modulo operator checks if num is evenly divisible by divisor
    is_divisible = (num % divisor == 0)
    return is_divisible


# ===========================
# Example test cases for Task 2
# ===========================

# Test 1: 10 divisible by 2
result1 = check_divisibility(10, 2)
print(f"Test 1 Output (10, 2): {result1}")  # Output: True

# Test 2: 7 divisible by 3
result2 = check_divisibility(7, 3)
print(f"Test 2 Output (7, 3): {result2}")   # Output: False
