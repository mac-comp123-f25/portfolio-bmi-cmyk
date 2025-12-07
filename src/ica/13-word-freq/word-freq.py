import string

def compute_frequencies(filename):
    """
    Reads a text file, cleans the words, and computes the frequency of each word.

    The function performs the following steps:
    1. Reads the entire content of the file.
    2. Splits the content into a list of words.
    3. Cleans each word by converting it to lowercase and removing leading/trailing punctuation.
    4. Builds a dictionary where keys are the cleaned words and values are their frequencies.

    Args:
        filename (str): The path to the text file.

    Returns:
        dict: A dictionary mapping each unique word to its frequency count.
    """
    # Step 1: Define Function and Read File
    try:
        with open(filename, 'r', encoding='utf-8') as file_in:
            full_text = file_in.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}

    # Step 2: Split to Words and Remove Punctuation
    words = full_text.split()
    cleaned_words = []
    for word in words:
        # Convert to lowercase and strip punctuation from both ends
        clean_word = word.lower().strip(string.punctuation)
        # Add the word to our list only if it's not an empty string
        if clean_word:
            cleaned_words.append(clean_word)

    # Step 3: Build the Frequency Dictionary
    freq_dict = {}
    for word in cleaned_words:
        if word in freq_dict:
            # If the word is already a key, increment its count
            freq_dict[word] += 1
        else:
            # If the word is not yet a key, add it with a count of 1
            freq_dict[word] = 1

    return freq_dict


def print_frequencies(freq_dict, top_n=20):
    """
    (Optional Function)
    Prints the word frequencies in a sorted, readable format.
    The list is sorted from most frequent to least frequent.

    Args:
        freq_dict (dict): A dictionary of word frequencies.
        top_n (int): The number of top results to print.
    """
    if not freq_dict:
        print("The frequency dictionary is empty.")
        return

    # 1. Convert the dictionary to a list of (frequency, word) tuples
    freq_list = []
    for word, freq in freq_dict.items():
        freq_list.append((freq, word))

    # 2. Sort the list in descending order based on frequency
    freq_list.sort(reverse=True)

    print(f"\n--- Top {top_n} Most Frequent Words ---")
    # 3. Print the results using ljust for alignment
    # Set a width for the word column for nice alignment
    column_width = 15
    print(f"{'Word'.ljust(column_width)}| Count")
    print(f"{'-' * column_width}|{'-' * 6}")

    for freq, word in freq_list[:top_n]:
        print(f"{word.ljust(column_width)}| {freq}")


# --- Main execution block to demonstrate the functions ---
if __name__ == '__main__':
    # Test with a small file first
    test_filename = "../TextFiles/alice.txt"
    print(f"Computing word frequencies for: {test_filename}")

    # Get the frequency dictionary
    word_counts = compute_frequencies(test_filename)

    # Print a few sample word counts to verify
    if word_counts:
        print("\n--- Sample Frequencies ---")
        print(f"'alice': {word_counts.get('alice', 0)}")
        print(f"'rabbit': {word_counts.get('rabbit', 0)}")
        print(f"'the': {word_counts.get('the', 0)}")

        # Use the optional function to print the sorted list
        print_frequencies(word_counts, top_n=25)