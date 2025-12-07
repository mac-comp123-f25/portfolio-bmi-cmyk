import turtle
import random


def draw_fractal_tree(turt, branch_len, angle):
    """
    Draws a fractal tree recursively.

    MODIFICATION:
    This version adds randomness to the branch length reduction and turn angles
    to create a more natural-looking, asymmetrical tree. The original function
    had fixed subtractions and angles.
    """
    # Base Case: If the branch length is too short, stop.
    if branch_len < 5:
        return
    else:
        # Draw the main branch
        turt.forward(branch_len)

        # --- Left Branch ---
        # Introduce randomness to the angle and length
        left_angle = angle + random.randint(-10, 10)
        turt.left(left_angle)
        new_len_left = branch_len - random.randint(10, 20)
        draw_fractal_tree(turt, new_len_left, angle)

        # --- Right Branch ---
        turt.right(left_angle * 2)  # Turn back past center for the right branch
        new_len_right = branch_len - random.randint(10, 20)
        draw_fractal_tree(turt, new_len_right, angle)

        # Return to original orientation and position
        turt.left(left_angle)
        turt.backward(branch_len)


def check_draw_fractal_tree(start_len):
    """
    Sets up the turtle and screen for drawing the fractal tree.
    """
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.left(90)  # Point the turtle upwards
    t.penup()
    t.backward(start_len * 1.5)  # Move to the bottom of the screen
    t.pendown()
    t.pencolor("green")

    draw_fractal_tree(t, start_len, 20)

    screen.exitonclick()


# --- Test Call ---
if __name__ == "__main__":
    check_draw_fractal_tree(75)