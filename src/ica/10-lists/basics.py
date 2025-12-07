# src/ica/10-lists/basics.py

def every_other(a_list):
    """
    Returns a new list containing every other value from the original list.
    Uses list slicing for an efficient solution.
    """
    return a_list[::2]

def sum_positive(num_list):
    """
    Returns the sum of only the positive numbers in a list.
    """
    total_sum = 0
    for number in num_list:
        if number > 0:
            total_sum += number
    return total_sum

# --- Test Cases ---
if __name__ == '__main__':
    print("--- Testing every_other ---")
    my_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Original: {my_list1}")
    print(f"Every other: {every_other(my_list1)}")  # Expected: [1, 3, 5, 7]

    my_list2 = ['a', 'b', 'c', 'd', 'e']
    print(f"Original: {my_list2}")
    print(f"Every other: {every_other(my_list2)}")  # Expected: ['a', 'c', 'e']

    print("\n--- Testing sum_positive ---")
    num_list1 = [1, -2, 3, 4, -5, 6]
    print(f"List: {num_list1}")
    print(f"Sum of positives: {sum_positive(num_list1)}")  # Expected: 1 + 3 + 4 + 6 = 14

    num_list2 = [-1, -2, -3]
    print(f"List: {num_list2}")
    print(f"Sum of positives: {sum_positive(num_list2)}")  # Expected: 0