import random
from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def get_rand_bg():
    """
    Creates and returns a picture of 100x100 pixels with a random
    color background.
    """
    # Generate random values for the red, green, and blue channels (0-255)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    random_color = (r, g, b)

    # Create a blank 100x100 picture
    bg_picture = Picture(100, 100)

    # Set all pixels to the generated random color
    bg_picture.setAllPixels(random_color)

    return bg_picture


def main():
    """
    Tests the get_rand_bg function.
    """
    print("Creating a picture with a random background color...")
    random_pic = get_rand_bg()
    random_pic.show()

    keep_windows_open()


if __name__ == "__main__":
    main()