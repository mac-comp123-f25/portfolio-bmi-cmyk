def change_start(value, a_list):
    """
    Modifies the input list by changing the value at index 0.
    This function does not return anything as it modifies the list directly.
    """
    if len(a_list) > 0:
        a_list[0] = value

# --- Test Case ---
if __name__ == '__main__':
    print("--- Testing change_start ---")
    t_list = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f"Original list: {t_list}")
    change_start('X', t_list)
    print(f"Modified list: {t_list}")
    # Expected Output: ['X', 'b', 'c', 'd', 'e', 'f']