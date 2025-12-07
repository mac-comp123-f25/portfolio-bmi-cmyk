import math
from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def scale_down(pic):
    """
    Takes a picture and returns a new one that is half the size.
    """
    old_w = pic.getWidth()
    old_h = pic.getHeight()

    # Calculate new dimensions, using ceiling to handle odd sizes
    new_w = math.ceil(old_w / 2)
    new_h = math.ceil(old_h / 2)

    new_pic = Picture(new_w, new_h)

    # Loop over the new, smaller picture's coordinates
    for (nx, ny) in new_pic:
        # Map the new coordinates back to the original picture's coordinates
        source_x = nx * 2
        source_y = ny * 2

        # Get the color from the source and set it in the new picture
        color = pic.getColor(source_x, source_y)
        new_pic.setColor(nx, ny, color)

    return new_pic


def scale_up(pic):
    """
    Takes a picture and returns a new one that is twice the size.
    """
    old_w = pic.getWidth()
    old_h = pic.getHeight()

    new_w = old_w * 2
    new_h = old_h * 2

    new_pic = Picture(new_w, new_h)

    # Loop over the original, smaller picture's coordinates
    for (sx, sy) in pic:
        color = pic.getColor(sx, sy)

        # Map one source pixel to a 2x2 block in the new, larger picture
        new_pic.setColor(sx * 2, sy * 2, color)
        new_pic.setColor(sx * 2 + 1, sy * 2, color)
        new_pic.setColor(sx * 2, sy * 2 + 1, color)
        new_pic.setColor(sx * 2 + 1, sy * 2 + 1, color)

    return new_pic


def main():
    """
    Main function to test scaling functions.
    """
    original = Picture("../SampleImages/stateFairCorn.jpg")
    original.show()
    original.setTitle("Original")

    # Test scale_down
    half_size = scale_down(original)
    half_size.show()
    half_size.setTitle("Half Size")

    # Test scale_up
    double_size = scale_up(original)
    double_size.show()
    double_size.setTitle("Double Size")

    keep_windows_open()


if __name__ == "__main__":
    main()