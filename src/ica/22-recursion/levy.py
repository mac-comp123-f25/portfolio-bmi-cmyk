import turtle
import math


def calc_next_size(current_size):
    """
    Helper function to calculate the size of the next segment in the Levy C Curve.
    """
    return current_size / math.sqrt(2.0)


def draw_levy(turt, size, reps):
    """
    Draws a Levy C Curve fractal recursively.
    """
    # Base Case: If repetitions are 1, just draw a straight line.
    if reps == 1:
        turt.forward(size)
    else:
        # Recursive Step: Replace the line with two smaller Levy curves
        # forming an isosceles right triangle.

        # 1. Compute the new size
        new_size = calc_next_size(size)

        # 2. Turn left
        turt.left(45)

        # 3. Recursively draw the first segment
        draw_levy(turt, new_size, reps - 1)

        # 4. Turn right
        turt.right(90)

        # 5. Recursively draw the second segment
        draw_levy(turt, new_size, reps - 1)

        # 6. Turn left to return to the original orientation
        turt.left(45)


def check_draw_levy(size, reps):
    """
    Sets up the turtle and screen for drawing the Levy C Curve.
    """
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    draw_levy(t, size, reps)

    screen.exitonclick()


# --- Test Call ---
if __name__ == "__main__":
    # This will draw the fractal for 10 repetitions.
    check_draw_levy(300, 10)