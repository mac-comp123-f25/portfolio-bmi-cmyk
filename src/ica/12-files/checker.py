def select_words(s, fn):
    """
    Opens a file and returns a list of all words (one per line) that
    contain the given substring 's'.

    Args:
        s (str): The substring to search for.
        fn (str): The filename of the word list.

    Returns:
        list: A list of words containing the substring.
    """
    matching_words = []
    file_in = open(fn, 'r')

    for line in file_in:
        # Remove the newline character from the end of the line
        word = line.strip()
        if s in word:
            matching_words.append(word)

    file_in.close()
    return matching_words


# Test cases as requested in the activity description.
if __name__ == '__main__':
    # Test 1: "ii" on the short file
    ii_short = select_words("ii", "../TextFiles/shortcross.txt")
    print(f"Found {len(ii_short)} words with 'ii' in shortcross.txt. (Expected: 2)")
    print(f"Words: {ii_short}\n")

    # Test 2: "ii" on the full file
    ii_full = select_words("ii", "../TextFiles/crosswords.txt")
    print(f"Found {len(ii_full)} words with 'ii' in crosswords.txt. (Expected: 38)\n")

    # Test 3: "quo" on the short file
    quo_short = select_words("quo", "../TextFiles/shortcross.txt")
    print(f"Found {len(quo_short)} words with 'quo' in shortcross.txt. (Expected: 0)")
    print(f"Words: {quo_short}\n")

    # Test 4: "quo" on the full file
    quo_full = select_words("quo", "../TextFiles/crosswords.txt")
    print(f"Found {len(quo_full)} words with 'quo' in crosswords.txt. (Expected: 65)")