def find_and_replace(lst, find_val, replace_val):
    """
    Searches for all occurrences of `find_val` in the input list `lst`
    and replaces them with `replace_val`.

    Parameters:
        lst (list): The list to be modified.
        find_val: The value to search for in the list.
        replace_val: The value that replaces each occurrence of find_val.

    Returns:
        list: The modified list with replacements.
              If `lst` is not a list, returns an empty list.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        print("Warning: The first argument is not a list. Returning an empty list.")
        return []

    # Iterate through the list and replace occurrences of find_val with replace_val
    # List comprehension creates a new list with the replacements
    modified_list = [replace_val if item == find_val else item for item in lst]

    return modified_list

# ===========================
# Example test cases for Task 2
# ===========================

# Test 1: Replace 2 with 5 in a list of integers
test_list1 = [1, 2, 3, 4, 2, 2]
result1 = find_and_replace(test_list1, 2, 5)
print(f"Test 1 Output: {result1}")  # Output: [1, 5, 3, 4, 5, 5]

# Test 2: Replace "apple" with "orange" in a list of strings
test_list2 = ["apple", "banana", "apple"]
result2 = find_and_replace(test_list2, "apple", "orange")
print(f"Test 2 Output: {result2}")  # Output: ['orange', 'banana', 'orange']
