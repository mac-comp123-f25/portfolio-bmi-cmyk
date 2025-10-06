def sum_digits(code_words):
  """
  Takes a list of strings and returns the sum of two-digit numbers
  extracted from each string. The number is formed by combining the
  first and last digit found in the string.
  """
  total_sum = 0
  for code in code_words:
    digits = []
    for char in code:
      if char.isdigit():
        digits.append(char)

    if digits:
      first_digit = digits[0]
      last_digit = digits[-1]
      two_digit_number_str = first_digit + last_digit
      total_sum += int(two_digit_number_str)

  return total_sum

# Example Usage:
print(sum_digits(['jaw2n5btf9w', 'xxgg7x']))
print(sum_digits(['comp123', '1600grand', 'spring24']))