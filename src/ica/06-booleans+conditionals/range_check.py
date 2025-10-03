def range_limit(num):
  """
  Limits a number to the range [1, 10].
  :param num: The number to limit.
  :return: The number if it's in the range, 1 if it's less than 1, or 10 if it's greater than 10.
  """
  if num < 1:
    return 1
  elif num > 10:
    return 10
  else:
    return num

if __name__ == "__main__":
  assert range_limit(8) == 8
  assert range_limit(-1) == 1
  assert range_limit(50) == 10
  print("All tests passed!")