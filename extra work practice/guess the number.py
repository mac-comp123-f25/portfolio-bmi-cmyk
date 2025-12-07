import random


def guess_the_number_game():
    """
    A simple "guess the number" game.
    """

    # 1. Game Setup
    print("========================================")
    print("  Welcome to the Guess the Number Game! ")
    print("========================================")
    print("I'm thinking of a number between 1 and 100.")

    # The computer generates a random integer between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    # 2. Main Game Loop
    while True:
        # Get user input
        try:
            guess_str = input("\nPlease enter your guess: ")
            # Try to convert the user's input string into an integer
            user_guess = int(guess_str)
        except ValueError:
            # If the user enters something that is not a valid number,
            # print an error and continue to the next loop iteration.
            print("That's not a valid number! Please enter an integer.")
            continue

        # Increment the attempt counter
        attempts += 1

        # 3. Check the guess
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            # The guess is correct!
            print(f"\n🎉 Congratulations, you guessed it! The number was {secret_number}.")
            print(f"It took you {attempts} guesses.")
            break  # Exit the loop, the game is over

    print("\nThanks for playing!")


# --- Program Entry Point ---
# This ensures the game runs only when the script is executed directly
if __name__ == "__main__":
    guess_the_number_game()