def rotate_left(oldPic):
    """
    Rotates a picture 90 degrees to the left.
    """
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h, w)
    for x in range(w):
        for y in range(h):
            old_color = oldPic.getColor(x, y)
            newX = y
            newY = w - x - 1
            new_pic.setColor(newX, newY, old_color)

    return new_pic


def rotate_right(oldPic):
    """
    Rotates a picture 90 degrees to the right.
    """
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    # The new picture will have swapped dimensions
    new_pic = Picture(h, w)

    # Loop over the original picture's coordinates
    for x in range(w):
        for y in range(h):
            old_color = oldPic.getColor(x, y)

            # Calculate the new coordinates for a right rotation
            newX = h - y - 1
            newY = x

            new_pic.setColor(newX, newY, old_color)

    return new_pic


def main():
    """
    Main function to test rotation functions.
    """
    arches = Picture("../SampleImages/arches.jpg")
    arches.show()
    arches.setTitle("Original")

    # Test rotate_left
    left_rotated = rotate_left(arches)
    left_rotated.show()
    left_rotated.setTitle("Rotated Left")

    # Test rotate_right
    right_rotated = rotate_right(arches)
    right_rotated.show()
    right_rotated.setTitle("Rotated Right")

    keep_windows_open()


if __name__ == '__main__':
    main()