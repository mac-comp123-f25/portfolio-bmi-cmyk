def red_channel(pic):
    """
    Takes a picture and returns a new picture containing only the red channel.
    Green and blue channels are set to 0.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))
    return new_pic


def green_channel(pic):
    """
    Takes a picture and returns a new picture containing only the green channel.
    Red and blue channels are set to 0.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))
    return new_pic


def blue_channel(pic):
    """
    Takes a picture and returns a new picture containing only the blue channel.
    Red and green channels are set to 0.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, 0, b))
    return new_pic


def main():
    """
    Main function to test the channel separation functions.
    """
    # Load the original image
    astilbe = Picture("../SampleImages/astilbe.jpg")
    astilbe.show()
    astilbe.setTitle("astilbe")

    # Create and show the red channel version
    astilbe_red = red_channel(astilbe)
    astilbe_red.show()
    astilbe_red.setTitle("astilbe_red")

    # Create and show the green channel version
    astilbe_green = green_channel(astilbe)
    astilbe_green.show()
    astilbe_green.setTitle("astilbe_green")

    # Create and show the blue channel version
    astilbe_blue = blue_channel(astilbe)
    astilbe_blue.show()
    astilbe_blue.setTitle("astilbe_blue")

    keep_windows_open()


if __name__ == "__main__":
    main()