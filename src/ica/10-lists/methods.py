# src/ica/10-lists/methods.py

def end_points(num_list):
    """
    Takes a list of numbers and returns a tuple containing the minimum and maximum values.
    Returns (None, None) if the list is empty.
    """
    if not num_list:
        return None, None
    return min(num_list), max(num_list)

# --- Test Cases ---
if __name__ == '__main__':
    print("--- Testing end_points ---")
    numbers = [10, 2, 99, -5, 42, 17]
    print(f"List: {numbers}")

    result_tuple = end_points(numbers)
    print(f"Result stored as a single tuple: {result_tuple}")
    print(f"Min value: {result_tuple[0]}, Max value: {result_tuple[1]}")

    print("-" * 20)

    min_val, max_val = end_points(numbers)
    print(f"Result unpacked into two variables:")
    print(f"Min value: {min_val}, Max value: {max_val}")