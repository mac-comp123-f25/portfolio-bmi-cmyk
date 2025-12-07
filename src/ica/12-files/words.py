def i_words(filename):
    """
    Reads a file, splits it into words, and returns a new list containing
    only the words that have the letter 'i' in them.

    Args:
        filename (str): The path to the text file.

    Returns:
        list: A list of words containing the letter 'i'.
    """
    file_in = open(filename, 'r')
    full_text = file_in.read()
    file_in.close()

    all_words = full_text.split()

    # Use a list comprehension to create the new list
    words_with_i = [word for word in all_words if 'i' in word or 'I' in word]

    return words_with_i

if __name__ == '__main__':
    i_word_list = i_words('../TextFiles/alice.txt')
    print(f"Found {len(i_word_list)} words with 'i' in alice.txt.")
    print("First 10 words are:", i_word_list[:10])