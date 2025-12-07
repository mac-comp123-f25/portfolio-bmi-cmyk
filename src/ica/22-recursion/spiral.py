import turtle


def spiral_in(turt, side_len):
    """
    Draws a rectangular spiral recursively, from the outside in.
    """
    # Base Case: If the side length is too small, stop drawing.
    if side_len <= 5:
        return  # Do nothing further.
    else:
        # Recursive Step: Draw one side of the spiral.
        turt.forward(side_len)
        turt.right(90)
        # Call the function again with a smaller side length.
        spiral_in(turt, side_len - 5)


def check_spiral_in(start_len):
    """
    Sets up the turtle and screen to test the spiral_in function.
    """
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(-start_len / 2, start_len / 2)  # Center the spiral
    t.pendown()

    spiral_in(t, start_len)

    screen.exitonclick()


# --- Test Call ---
if __name__ == "__main__":
    check_spiral_in(200)
