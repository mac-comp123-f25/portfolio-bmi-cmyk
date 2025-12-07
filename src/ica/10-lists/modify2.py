def remove_all(value, a_list):
    """
    Removes all occurrences of 'value' from 'a_list' in-place.
    Uses a while loop to handle the changing size of the list during iteration.
    """
    while value in a_list:
        a_list.remove(value)

# --- Test Case ---
if __name__ == '__main__':
    print("--- Testing remove_all ---")
    test_list = [1, 5, 2, 5, 3, 5, 4, 5]
    print(f"Original list: {test_list}")
    remove_all(5, test_list)
    print(f"List after removing all 5s: {test_list}") # Expected: [1, 2, 3, 4]