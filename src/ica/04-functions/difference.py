def smallest_diff(x, y, z):
    """
    This function takes three numbers and returns the smallest difference
    between any two of them.
    """

    print('smallest_diff inputs:', x, y, z)

    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)

    print('Calculated diffs:', diff1, diff2, diff3, ' | return value:', min_diff)
    return min_diff

print("--- Calling with (3, 9, 5) ---")
smallest_diff(3, 9, 5)

print("\n--- Calling with (32, 43, 90) ---")
smallest_diff(32, 43, 90)