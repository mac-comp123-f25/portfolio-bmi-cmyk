from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def change_red(picture, factor):
    """Increases or decreases the red value of each pixel by a factor."""
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        new_red = red * factor
        picture.setColor(x, y, (new_red, grn, blu))


def change_blue(picture, factor):
    """Increases or decreases the blue value of each pixel by a factor."""
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        new_blue = blu * factor
        picture.setColor(x, y, (red, grn, new_blue))


def remove_blue(picture):
    """Sets the blue value of every pixel in the picture to 0."""
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, grn, 0))


def fix_green(picture, green_value):
    """Sets the green value of every pixel to the specified green_value."""
    for (x, y) in picture:
        (red, grn, blu) = picture.getColor(x, y)
        picture.setColor(x, y, (red, green_value, blu))


def main():
    # --- Test change_red ---
    pic1 = Picture("../SampleImages/raspberries.jpg")
    pic1.show()
    change_red(pic1, 1.5)  # Increase red
    pic1.show()

    # --- Test change_blue ---
    pic2 = Picture("../SampleImages/butterfly.jpg")
    pic2.show()
    change_blue(pic2, 0.5)  # Decrease blue
    pic2.show()

    # --- Test remove_blue ---
    pic3 = Picture("../SampleImages/bryceCanyon.jpg")
    pic3.show()
    remove_blue(pic3)
    pic3.show()

    # --- Test fix_green ---
    pic4 = Picture("../SampleImages/stateFairCorn.jpg")
    pic4.show()
    fix_green(pic4, 255)  # Set all green values to max
    pic4.show()

    keep_windows_open()


if __name__ == "__main__":
    main()