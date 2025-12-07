from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def draw_something():
    """
    Draws a simple smiley-face on a blank picture and returns the picture.
    """
    # Create a blank picture of size 200x200 with a light blue background
    canvas = Picture(200, 200, "lightblue")

    # Draw the head (a yellow filled circle)
    # Bounding box for the head: (25, 25) to (175, 175)
    canvas.drawOval(25, 25, 175, 175, outlineColor="black", fillColor="yellow")

    # Draw the left eye (a black filled circle)
    canvas.drawOval(60, 60, 80, 80, fillColor="black")

    # Draw the right eye
    canvas.drawOval(120, 60, 140, 80, fillColor="black")

    # Draw the smile (as an arc)
    # Bounding box for the smile: (50, 50) to (150, 150)
    # Starts at 225 degrees and ends at 315 degrees
    canvas.drawArc(50, 50, 150, 150, startAngle=225, endAngle=90, style="arc", outlineColor="black", width=3)

    return canvas


def main():
    """
    Tests the draw_something function.
    """
    print("Drawing a smiley face...")
    my_drawing = draw_something()
    my_drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()