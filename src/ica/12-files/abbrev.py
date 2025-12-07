def print_abbrev(filename):
    """
    Opens a file, reads it line by line, and prints the first 20 characters
    of each line.

    Args:
        filename (str): The path to the text file.
    """
    file_in = open(filename, 'r')
    for line in file_in:
        # Slice the line to get the first 20 characters
        abbreviated_line = line[:20]
        print(abbreviated_line)
    file_in.close()

if __name__ == '__main__':
    print("--- Abbreviated alice.txt ---")
    print_abbrev("../TextFiles/alice.txt")