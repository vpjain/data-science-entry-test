def update_dictionary(dct, key, value):
    """
    Updates the dictionary `dct` with the specified key-value pair.
    - If the key already exists in the dictionary, print the original value and update it.
    - If the key is new, add the key-value pair.
    - Return the updated dictionary.

    Parameters:
        dct (dict): The dictionary to update.
        key: The key to be added or updated.
        value: The value to assign to the key.

    Returns:
        dict: The updated dictionary.
    """
    # Check if dct is a dictionary
    if not isinstance(dct, dict):
        print("Warning: The first argument is not a dictionary.")
        return dct

    # If the key already exists, print its original value
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")

    # Update the value for the key (or add it if not present)
    dct[key] = value

    return dct


# ===========================
# Example test cases for Task 2
# ===========================

# Test 1: Add a new key-value pair to an empty dictionary
test_dict1 = {}
result1 = update_dictionary(test_dict1, "name", "Alice")
print(f"Test 1 Output: {result1}")  # Output: {'name': 'Alice'}

# Test 2: Update an existing key in the dictionary
test_dict2 = {"age": 25}
result2 = update_dictionary(test_dict2, "age", 26)
print(f"Test 2 Output: {result2}")  # Output: {'age': 26}
