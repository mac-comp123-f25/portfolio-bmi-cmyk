from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def main():
    """
    Main script to perform basic image manipulation.
    """
    # Create a Picture object from the file
    image_path = "../SampleImages/mightyMidway.jpg"
    original_pic = Picture(image_path)
    original_pic.show()

    # Get dimensions and calculate the number of pixels
    width = original_pic.getWidth()
    height = original_pic.getHeight()
    num_pixels = width * height
    print(f"The image '{image_path}' has {num_pixels} pixels.")

    # Make a copy of the image
    pic_copy = original_pic.copy()

    # Define the red color
    red_color = (255, 0, 0)

    # Change the pixels in each corner to be red
    # Top-left corner
    pic_copy.setColor(0, 0, red_color)
    # Top-right corner
    pic_copy.setColor(width - 1, 0, red_color)
    # Bottom-left corner
    pic_copy.setColor(0, height - 1, red_color)
    # Bottom-right corner
    pic_copy.setColor(width - 1, height - 1, red_color)

    # Save the resulting picture to a new file
    output_filename = "mightyMidway-redCorners.jpg"
    pic_copy.save(output_filename)
    print(f"Modified image saved as '{output_filename}'.")

    # Use the explore method on the new picture
    print("Opening explorer for the modified image. Zoom in on corners to see changes.")
    pic_copy.explore()

    # Keep the image windows open until manually closed
    keep_windows_open()


if __name__ == "__main__":
    main()