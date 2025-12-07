def up_to_period(filename):
    """
    Reads a file and returns all text from the beginning up to and including
    the first period.

    Args:
        filename (str): The path to the text file.

    Returns:
        str: The text up to the first period.
    """
    file_in = open(filename, 'r')
    full_text = file_in.read()
    file_in.close()

    accumulator = ""
    for char in full_text:
        accumulator += char
        if char == '.':
            break  # Exit the loop once the period is found and added
    return accumulator

# Sample call as requested in the activity description.
if __name__ == '__main__':
    excerpt = up_to_period('../TextFiles/mockingbird.txt')
    print(excerpt)