def crop_picture(source_pic, crop_x, crop_y, crop_width, crop_height):
    """
    Crops a rectangular region from a source picture and returns it as a new picture.
    """
    # Create a new, blank picture with the dimensions of the crop area
    new_pic = Picture(crop_width, crop_height)

    # Loop over the pixels of the NEW (target) picture
    for (nx, ny) in new_pic:
        # Calculate the corresponding pixel coordinates in the SOURCE picture
        source_x = crop_x + nx
        source_y = crop_y + ny

        # Get the color from the source picture at the calculated coordinates
        color = source_pic.getColor(source_x, source_y)

        # Set the color in the new picture at its coordinates
        new_pic.setColor(nx, ny, color)

    return new_pic


def main():
    """
    Main function to test the crop_picture function.
    """
    dam = Picture("../SampleImages/hooverDam.jpg")
    dam.show()
    dam.setTitle("Original Dam")

    # Perform cropping as specified in the prompt
    dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
    dam_crop2 = crop_picture(dam, 100, 150, 100, 150)

    # Show the results
    dam_crop1.show()
    dam_crop1.setTitle("Crop 1")
    dam_crop2.show()
    dam_crop2.setTitle("Crop 2")

    keep_windows_open()


if __name__ == "__main__":
    main()