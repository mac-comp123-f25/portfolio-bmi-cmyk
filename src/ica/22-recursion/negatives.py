def count_negatives(num_list):
    """
    Counts the number of negative numbers in a list using recursion.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int: The count of negative numbers in the list.
    """
    # Base Case: If the list is empty, there are no negative numbers.
    if not num_list:
        return 0
    else:
        # Recursive Step: Process the rest of the list recursively.
        count_in_rest = count_negatives(num_list[1:])

        # Check the first element of the current list.
        first_num = num_list[0]
        if first_num < 0:
            # If the first number is negative, add 1 to the count from the rest.
            return 1 + count_in_rest
        else:
            # Otherwise, the count is just the count from the rest of the list.
            return count_in_rest


# --- Test Cases ---
if __name__ == "__main__":
    list1 = [1, -2, 3, -4, 5]
    print(f"List: {list1}, Negative count: {count_negatives(list1)}")  # Expected: 2

    list2 = [1, 2, 3, 4, 5]
    print(f"List: {list2}, Negative count: {count_negatives(list2)}")  # Expected: 0

    list3 = [-1, -2, -3]
    print(f"List: {list3}, Negative count: {count_negatives(list3)}")  # Expected: 3

    list4 = []
    print(f"List: {list4}, Negative count: {count_negatives(list4)}")  # Expected: 0