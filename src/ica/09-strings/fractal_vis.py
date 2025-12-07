# This script utilizes the provided 'l_system' and 'turtle_drawing' modules
# located in the 'fractal' sub-folder to generate and draw L-system fractals.

from fractal.l_system import create_l_system
from fractal.turtle_drawing import draw_l_system
import turtle


def setup_turtle(start_pos=(-350, 0), start_heading=0):
    """
    Sets up the turtle environment for drawing.
    Returns the turtle and screen objects.
    """
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)  # 0 is the fastest speed
    t.hideturtle()
    screen.tracer(0, 0)  # Turn off screen updates for max speed

    # Set initial position and heading
    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()

    return t, screen


def draw_koch():
    """Draws the Koch curve (example from textbook)."""
    t, screen = setup_turtle()
    instructions = create_l_system("F", {"F": "F+F-F-F+F"}, 3)
    draw_l_system(t, instructions, 90, 5)
    screen.update()


# --- NEW FRACTAL IMPLEMENTATIONS ---

def draw_sierpinski_arrowhead():
    """
    Draws the Sierpinski arrowhead curve.

    L-System details:
    - Variables: A, B
    - Axiom: A
    - Rules: (A → B-A-B), (B → A+B+A)
    - Angle: 60°
    - Note: For drawing, both A and B are interpreted as "draw forward".
    """
    t, screen = setup_turtle(start_pos=(-350, -300))
    rules = {"A": "B-A-B", "B": "A+B+A"}
    instructions = create_l_system("A", rules, 6)

    # The draw_l_system function likely only draws on 'F' or 'G'.
    # We replace 'A' and 'B' with 'F' to make them drawing commands.
    draw_instructions = instructions.replace('A', 'F').replace('B', 'F')

    draw_l_system(t, draw_instructions, 60, 5)
    screen.update()


def draw_dragon_curve():
    """
    Draws the Heighway Dragon Curve.

    L-System details:
    - Variables: X, Y, F
    - Axiom: FX
    - Rules: (X → X+YF+), (Y → -FX-Y)
    - Angle: 90°
    - Note: Only 'F' is interpreted as "draw forward". X and Y control the
      recursion but are not drawn.
    """
    t, screen = setup_turtle(start_pos=(100, 100), start_heading=180)
    rules = {"X": "X+YF+", "Y": "-FX-Y"}
    instructions = create_l_system("FX", rules, 10)

    # No replacement needed as 'F' is the drawing command.
    draw_l_system(t, instructions, 90, 5)
    screen.update()


def draw_hilbert_curve():
    """
    Draws the Hilbert Curve, a space-filling curve.

    L-System details:
    - Variables: A, B, F
    - Axiom: A
    - Rules: (A → -BF+AFA+FB-), (B → +AF-BFB-FA+)
    - Angle: 90°
    - Note: Only 'F' is interpreted as "draw forward".
    """
    t, screen = setup_turtle(start_pos=(-180, -180))
    rules = {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}
    instructions = create_l_system("A", rules, 5)

    # We replace 'A' and 'B' with empty strings to remove them, leaving only F, +, -
    # This step is optional if draw_l_system ignores non-command characters.
    draw_instructions = instructions.replace('A', '').replace('B', '')

    draw_l_system(t, draw_instructions, 90, 8)
    screen.update()


# --- Main execution block ---
if __name__ == '__main__':
    # To see a fractal, uncomment ONE of the function calls below.

    # draw_koch()
    # draw_sierpinski_arrowhead()
    draw_dragon_curve()
    # draw_hilbert_curve()

    # Keep the window open until it is manually closed.
    turtle.done()