def string_reverse(s):
    """
    Reverses the provided string `s`.
    - s must be a string.
    - Returns the reversed string.
    - Returns an empty string if `s` is not a string.

    Parameters:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    # Check if the input is a string
    if not isinstance(s, str):
        print("Warning: Input is not a string. Returning empty string.")
        return ""
    # Use string slicing to reverse the string efficiently
    reversed_s = s[::-1]
    return reversed_s


# ===========================
# Example test cases for Task 2
# ===========================

# Test 1: Reverse a typical sentence
test_str1 = "Hello World"
result1 = string_reverse(test_str1)
print(f"Test 1 Output: '{result1}'")  # Output: 'dlroW olleH'

# Test 2: Reverse a short word
test_str2 = "Python"
result2 = string_reverse(test_str2)
print(f"Test 2 Output: '{result2}'")  # Output: 'nohtyP'
