def weighted_scale(pic, w1, w2, w3):
    """
    Takes a picture and three weights (w1, w2, w3) as input.
    Returns a new picture where each pixel is a grayscale value
    calculated using a weighted average of the original RGB channels.
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        # Calculate the weighted luminance
        lumin = (r * w1) + (g * w2) + (b * w3)
        # Set all channels to the new luminance value
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic


def main():
    """
    Main function to test the weighted_scale function.
    """
    # Load an image
    image_path = "../SampleImages/antiqueTractors.jpg"
    original_pic = Picture(image_path)
    original_pic.show()
    original_pic.setTitle("Original")

    # Test with weights emphasizing red
    red_weighted = weighted_scale(original_pic, 0.7, 0.15, 0.15)
    red_weighted.show()
    red_weighted.setTitle("Red Weighted (0.7, 0.15, 0.15)")

    # Test with weights emphasizing green
    green_weighted = weighted_scale(original_pic, 0.1, 0.8, 0.1)
    green_weighted.show()
    green_weighted.setTitle("Green Weighted (0.1, 0.8, 0.1)")

    # Keep windows open until closed by the user
    keep_windows_open()


if __name__ == "__main__":
    main()