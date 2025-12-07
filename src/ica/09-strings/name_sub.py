import string

def count_words(word, text):
  """
  Counts how many times a word appears in a text as a whole word,
  ignoring capitalization and surrounding punctuation.
  """
  count = 0
  target_word = word.lower()
  word_list = text.split()

  for w in word_list:
    # Clean the word by removing surrounding punctuation and converting to lowercase
    cleaned_word = w.strip(string.punctuation).lower()
    if cleaned_word == target_word:
      count += 1
  return count

# Example Usage:
print(count_words('ban', 'ban is banana')) # Should be 1
print(count_words('The', 'The quick brown fox jumps over the lazy dog.')) # Should be 2
print(count_words('Go', 'Go, Dogs, Go!')) # Should be 3