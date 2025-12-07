# src/ica/10-lists/comper.py

def times_n(n, num_list):
    """
    Returns a new list where each number from the original list is multiplied by n.
    Uses a list comprehension.
    """
    return [num * n for num in num_list]

def remove_all_comprehension(value, a_list):
    """
    Returns a new list with all occurrences of 'value' removed.
    This version creates a new list and does not modify the original.
    Uses a list comprehension with a conditional.
    """
    return [item for item in a_list if item != value]

# --- Test Cases ---
if __name__ == '__main__':
    print("--- Testing times_n ---")
    my_nums = [1, 2, 3, 4, 5]
    factor = 10
    print(f"Original list: {my_nums}, Factor: {factor}")
    print(f"New list: {times_n(factor, my_nums)}") # Expected: [10, 20, 30, 40, 50]

    print("\n--- Testing remove_all_comprehension ---")
    original_list = [1, 5, 2, 5, 3, 5, 4, 5]
    value_to_remove = 5
    print(f"Original list: {original_list}")
    new_list = remove_all_comprehension(value_to_remove, original_list)
    print(f"New list after removing all {value_to_remove}s: {new_list}") # Expected: [1, 2, 3, 4]
    print(f"Original list remains unchanged: {original_list}")
    