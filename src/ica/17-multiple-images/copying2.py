import random
from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def copy_pic_into_random(small_pic, big_pic):
    """
    Copies the small_pic into the big_pic at a random valid position.
    """
    # Calculate the maximum possible starting coordinates that will keep
    # the small picture entirely within the big picture's bounds.
    max_x = big_pic.getWidth() - small_pic.getWidth()
    max_y = big_pic.getHeight() - small_pic.getHeight()

    # Choose a random starting position within the valid range
    start_x = random.randrange(0, max_x + 1)
    start_y = random.randrange(0, max_y + 1)

    print(f"Copying to random position: ({start_x}, {start_y})")

    # Loop and copy pixels, same as the previous activity
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        target_x = start_x + x
        target_y = start_y + y
        big_pic.setColor(target_x, target_y, color)


def main():
    """
    Main function to test the random copying.
    """
    green_turtle = Picture("../SampleImages/greenTurtle.jpg")
    scene = Picture("../SampleImages/bearLake.jpg")

    # Copy the turtle to a random position multiple times
    copy_pic_into_random(green_turtle, scene)
    copy_pic_into_random(green_turtle, scene)
    copy_pic_into_random(green_turtle, scene)

    scene.show()
    scene.setTitle("Random Turtles")

    keep_windows_open()


if __name__ == "__main__":
    main()