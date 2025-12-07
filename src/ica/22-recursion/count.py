def countdown(n):
    """
    Prints numbers from n down to 1, then prints "Blast Off!".
    Uses recursion.

    Args:
        n (int): A non-negative integer to start the countdown from.
    """
    # Base Case: If n is 0, we have reached the end of the countdown.
    if n <= 0:
        print("Blast Off!")
    # Recursive Step: If n > 0, print the current number and
    # then call the function for the next number down.
    else:
        print(n)
        countdown(n - 1)


# --- Test Cases ---
if __name__ == "__main__":
    print("--- Countdown from 5 ---")
    countdown(5)
    # Expected Output:
    # 5
    # 4
    # 3
    # 2
    # 1
    # Blast Off!

    print("\n--- Countdown from 3 ---")
    countdown(3)
    # Expected Output:
    # 3
    # 2
    # 1
    # Blast Off!

    print("\n--- Countdown from 0 ---")
    countdown(0)
    # Expected Output:
    # Blast Off!