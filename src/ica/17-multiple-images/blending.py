def simple_blend(pic1, pic2):
    """
    Blends two pictures of the same size with a 50/50 mix.
    """
    # Assume pictures are the same size
    width = pic1.getWidth()
    height = pic1.getHeight()
    new_pic = Picture(width, height)

    for (x, y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        # Calculate the average of each channel
        avg_r = (r1 + r2) // 2
        avg_g = (g1 + g2) // 2
        avg_b = (b1 + b2) // 2

        new_pic.setColor(x, y, (avg_r, avg_g, avg_b))

    return new_pic


def blend2(pic1, pic2):
    """
    Blends two pictures of potentially different sizes. The resulting picture
    has dimensions equal to the smaller of the two inputs.
    """
    # Determine the dimensions of the new picture
    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(new_width, new_height)

    for (x, y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        avg_r = (r1 + r2) // 2
        avg_g = (g1 + g2) // 2
        avg_b = (b1 + b2) // 2

        new_pic.setColor(x, y, (avg_r, avg_g, avg_b))

    return new_pic


def weighted_blend(pic1, pic2, wgt1):
    """
    Blends two pictures using a weighted average.
    """
    wgt2 = 1.0 - wgt1

    new_width = min(pic1.getWidth(), pic2.getWidth())
    new_height = min(pic1.getHeight(), pic2.getHeight())
    new_pic = Picture(new_width, new_height)

    for (x, y) in new_pic:
        (r1, g1, b1) = pic1.getColor(x, y)
        (r2, g2, b2) = pic2.getColor(x, y)

        # Calculate the weighted average for each channel
        avg_r = int(r1 * wgt1 + r2 * wgt2)
        avg_g = int(g1 * wgt1 + g2 * wgt2)
        avg_b = int(b1 * wgt1 + b2 * wgt2)

        new_pic.setColor(x, y, (avg_r, avg_g, avg_b))

    return new_pic


def main():
    # Test simple_blend
    p1 = Picture("../SampleImages/daylilies.jpg")
    p2 = Picture("../SampleImages/wildColumbine.jpg")
    p3 = simple_blend(p1, p2)
    p3.show()
    p3.setTitle("Simple Blend (Same Size)")

    # Test blend2 and weighted_blend
    p4 = Picture("../SampleImages/muirWoods.jpg")
    p5 = Picture("../SampleImages/peony.jpg")
    p8 = weighted_blend(p4, p5, 0.25)
    p9 = weighted_blend(p4, p5, 0.5)
    p10 = weighted_blend(p4, p5, 0.75)

    p8.show()
    p8.setTitle("Weighted Blend (0.25)")
    p9.show()
    p9.setTitle("Weighted Blend (0.50)")
    p10.show()
    p10.setTitle("Weighted Blend (0.75)")

    keep_windows_open()


if __name__ == "__main__":
    main()