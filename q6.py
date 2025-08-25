def find_first_negative(lst):
    """
    Finds the first negative number in a list using a while loop.
    - Returns the first negative number if found.
    - If no negative numbers are present, returns the string "No negatives".

    Parameters:
        lst (list): The list of numbers to search.

    Returns:
        int or str: The first negative number if found, otherwise "No negatives".
    """
    # Check if input is a list
    if not isinstance(lst, list):
        print("Warning: The input is not a list.")
        return "No negatives"

    # Initialize index for while loop
    i = 0

    # Iterate using a while loop up to the end of the list
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:  # Ensure element is numeric
            return lst[i]  # Found first negative, return it immediately
        i += 1  # Move to the next element

    # No negative number found in the entire list
    return "No negatives"


# ===========================
# Example test cases for Task 2
# ===========================

# Test 1: List with negatives present
test_list1 = [3, 5, -1, 7, -2, 8]
result1 = find_first_negative(test_list1)
print(f"Test 1 Output: {result1}")  # Output: -1

# Test 2: List with no negatives
test_list2 = [2, 10, 7, 0]
result2 = find_first_negative(test_list2)
print(f"Test 2 Output: {result2}")  # Output: "No negatives"
