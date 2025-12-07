def color_shuffle(pic):
    """
    Takes a picture and returns a new picture with color channels shuffled:
    Red becomes Green, Green becomes Blue, and Blue becomes Red.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        # Shuffle the channels: new color is (b, r, g)
        new_pic.setColor(x, y, (b, r, g))

    return new_pic


def main():
    """
    Main function to test the color_shuffle function as shown in the prompt.
    """
    # Load the original image
    mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
    mushrooms0.show()
    mushrooms0.setTitle("mushrooms0")

    # Apply the shuffle once
    mushrooms1 = color_shuffle(mushrooms0)
    mushrooms1.show()
    mushrooms1.setTitle("mushrooms1")

    # Apply the shuffle a second time
    mushrooms2 = color_shuffle(mushrooms1)
    mushrooms2.show()
    mushrooms2.setTitle("mushrooms2")

    keep_windows_open()


if __name__ == "__main__":
    main()