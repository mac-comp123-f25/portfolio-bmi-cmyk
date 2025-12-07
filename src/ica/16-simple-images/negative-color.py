def negative(pic):
    """
    Takes an input picture and creates and returns a new picture
    that is the color negative of the input.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        # Calculate the negative of each color channel
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        new_pic.setColor(x, y, (new_r, new_g, new_b))

    return new_pic


def main():
    """
    Main function to test the negative function.
    """
    # Load an image
    image_path = "../SampleImages/mightyMidway.jpg"
    original_pic = Picture(image_path)
    original_pic.show()
    original_pic.setTitle("Original")

    # Create and show the negative version
    negative_pic = negative(original_pic)
    negative_pic.show()
    negative_pic.setTitle("Negative")

    keep_windows_open()


if __name__ == "__main__":
    main()