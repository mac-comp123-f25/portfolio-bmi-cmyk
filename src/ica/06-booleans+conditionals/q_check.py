def has_q(input_string):
  """
  Checks if the input string contains a lowercase 'q'.
  :param input_string: The string to check.
  :return: True if 'q' is in the string, False otherwise.
  """
  return 'q' in input_string

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")