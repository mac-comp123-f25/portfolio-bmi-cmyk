def write_to_n(number, filename):
    """
    Opens a file for writing and writes the numbers from 1 to `number`,
    one per line.

    Args:
        number (int): The upper limit of the numbers to write.
        filename (str): The name of the file to create/overwrite.
    """
    # Open the file in 'w' (write) mode. This will create the file if it
    # doesn't exist, or erase its contents if it does.
    out_file = open(filename, 'w')

    for i in range(1, number + 1):
        # Convert the number to a string and add a newline character
        line_to_write = str(i) + '\n'
        out_file.write(line_to_write)

    # Closing the file is essential to ensure all data is written from the buffer
    # to the disk.
    out_file.close()


# Example usage
if __name__ == '__main__':
    output_filename = "../TextFiles/output_numbers.txt"
    write_to_n(10, output_filename)
    print(f"Wrote numbers 1 through 10 to '{output_filename}'.")
    print("Check the file to see the result.")