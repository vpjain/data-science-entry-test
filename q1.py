def swap(x, y):
    """
    Swaps the values of x and y if both are numeric (int or float).
    - If either x or y is not numeric, return -1.
    - If both are numeric, print their swapped values.

    Args:
        x: The first value to swap (should be int or float).
        y: The second value to swap (should be int or float).

    Returns:
        None if swap is successful and values are printed.
        -1 if either x or y is not numeric.
    """
    # Check if both x and y are either int or float (numeric types)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        # Return -1 if either value is not numeric
        return -1

    # Swap x and y using tuple unpacking (idiomatic Python)
    x, y = y, x

    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")

# ===========================
# Example test cases for swap
# ===========================

# Scenario 1: Non-numeric input
result1 = swap("Apple", 10)  # Expected to return -1
if result1 == -1:
    print("Either x or y is not numeric. Function returned -1.")

# Scenario 2: Both numeric inputs
result2 = swap(9, 17)        # Expected to print "Swapped values: x = 17, y = 9"
if result2 == -1:
    print("Either x or y is not numeric. Function returned -1.")
