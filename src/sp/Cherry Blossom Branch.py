"""
This script draws a recursive cherry blossom branch. Users can adjust the size and color.

@author: Bridgette Mi (bmi@macalester.edu)
"""

import turtle
import random


def setup_screen():
    """Sets up the turtle screen and turtle object."""
    screen = turtle.Screen()
    screen.title("Recursive Cherry Blossom")
    screen.bgcolor("#0a043c")  # A dark blue background

    t = turtle.Turtle()
    t.speed(0)  # Set speed to fastest
    t.hideturtle()
    t.left(90)
    t.up()
    t.setpos(0, -screen.window_height() / 2 + 50)
    t.down()

    return t, screen


def get_user_input():
    """Gets size and color preferences from the user."""
    size = turtle.numinput(
        "Branch Size",
        "Enter the main branch length (60-120):",
        default=90, minval=60, maxval=120
    )

    color_theme = turtle.textinput(
        "Color Theme",
        "Choose a color theme: 'pink', 'white', or 'purple'"
    ).lower()

    return size, color_theme


def select_palette(theme):
    """Returns a color palette based on the user's theme choice."""
    if theme == "white":
        return ["#ffffff", "#f0f0f0", "#e0e0e0", "#fffafa"]
    elif theme == "purple":
        return ["#d1b3ff", "#c49dff", "#b787ff", "#a970ff"]
    else:  # Default to pink
        return ["#ffc0cb", "#ffb6c1", "#ffb3ba", "#ffa6b2"]


def draw_blossom(t, size):
    """Draws a single, simple five-petal blossom."""
    original_color = t.color()
    t.color(random.choice(current_palette))

    t.begin_fill()
    for _ in range(5):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)
        t.right(72)  # 360 / 5 petals = 72 degrees
    t.end_fill()

    t.color(original_color[0], original_color[1])  # Restore original pen color


def draw_branch(t, branch_length):
    """
    Recursively draws a branch and its sub-branches.
    This is the core recursive function for the tree.
    """
    if branch_length < 10:
        # Base Case: If the branch is too short, draw a blossom and stop.
        if random.random() > 0.5:  # 50% chance to draw a blossom at the end
            draw_blossom(t, 5)
        return

    # Draw the main part of the branch
    t.pensize(branch_length / 10)
    t.forward(branch_length)

    # Store current state
    position = t.pos()
    heading = t.heading()

    # --- Recursive Step 1: Create the right sub-branch ---
    angle_right = random.randint(15, 30)
    length_reduction = random.uniform(0.65, 0.8)

    t.right(angle_right)
    draw_branch(t, branch_length * length_reduction)

    # Return to the stored state to draw the next branch
    t.up()
    t.setpos(position)
    t.setheading(heading)
    t.down()

    # --- Recursive Step 2: Create the left sub-branch ---
    angle_left = random.randint(15, 30)
    length_reduction = random.uniform(0.65, 0.8)

    t.left(angle_left)
    draw_branch(t, branch_length * length_reduction)

    # --- Backtrack ---
    t.up()
    t.setpos(position)
    t.setheading(heading)
    t.down()
    t.pensize(branch_length / 10)
    t.backward(branch_length)


# --- Main Execution ---
if __name__ == "__main__":
    turtle.tracer(0)
    main_branch_length, theme_choice = get_user_input()
    artist, window = setup_screen()
    current_palette = select_palette(theme_choice)
    artist.color("#5c4033")
    draw_branch(artist, main_branch_length)

    turtle.update()  # Update the screen to show the final drawing
    window.mainloop()  # Keep the window open