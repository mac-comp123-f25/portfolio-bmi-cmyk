def copy_pic_into(small_pic, big_pic, start_x, start_y):
    """
    Copies the small_pic into the big_pic, with the top-left corner
    of small_pic positioned at (start_x, start_y) in big_pic.
    """
    # Loop over each pixel in the source (small) picture
    for (x, y) in small_pic:
        # Get the color from the source pixel
        color = small_pic.getColor(x, y)

        # Calculate the corresponding target position in the big picture
        target_x = start_x + x
        target_y = start_y + y

        # Set the color at the target position
        big_pic.setColor(target_x, target_y, color)


def main():
    """
    Main function to test the copy_pic_into function.
    """
    # Load the source and target images
    green_turtle = Picture("../SampleImages/greenTurtle.jpg")
    scene = Picture("../SampleImages/bearLake.jpg")

    # Perform the copy operations as specified in the prompt
    copy_pic_into(green_turtle, scene, 25, 25)
    copy_pic_into(green_turtle, scene, 200, 200)
    copy_pic_into(green_turtle, scene, 400, 200)

    # Show the final result
    scene.show()
    scene.setTitle("Turtles in Bear Lake")

    keep_windows_open()


if __name__ == "__main__":
    main()