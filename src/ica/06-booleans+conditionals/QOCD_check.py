def has_QOCD(input_string):
  """
  Checks if the input string contains 'Q', 'O', 'C', or 'D'.
  :param input_string: The string to check.
  :return: True if any of the specified characters are present, False otherwise.
  """
  return 'Q' in input_string or 'O' in input_string or 'C' in input_string or 'D' in input_string

if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")