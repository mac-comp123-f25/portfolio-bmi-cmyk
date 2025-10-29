import turtle
def do_move(turt, move):
    """
    Moves the turtle based on a command string.
    :param turt: The turtle object to move.
    :param move: A string command ('f', 'b', 'l', 'r').
    """
    if move is None:  # Handles the case where the user clicks "Cancel"
        return

    move = move.lower()  # Make the input case-insensitive
    if move == 'f':
        turt.forward(15)
    elif move == 'b':
        turt.backward(15)
    elif move == 'r':
        turt.right(90)
    elif move == 'l':
        turt.left(90)
    else:
        # This message will now appear in the console, not interfering with the window.
        print("Warning: Invalid move. Please use 'f', 'b', 'l', or 'r'.")


def tele_turtle(n):
    """
    Creates a turtle and a window, then prompts the user for n moves using GUI pop-ups.
    :param n: The maximum number of moves to perform.
    """
    win = turtle.Screen()
    win.title("Tele-Operated Turtle")
    tele_t = turtle.Turtle()

    for i in range(n):
        # Use turtle's own textinput for a GUI-friendly prompt
        prompt_title = "Turtle Control"
        prompt_text = f"Move {i + 1}/{n}: Enter next move (f, b, r, l)"
        move = win.textinput(prompt_title, prompt_text)

        # If the user clicks cancel, the loop will break
        if move is None:
            break

        do_move(tele_t, move)

    print("All moves are done. Click the window to exit.")
    win.exitonclick()


if __name__ == "__main__":
    tele_turtle(10)  # will ask the user to enter 10 commands