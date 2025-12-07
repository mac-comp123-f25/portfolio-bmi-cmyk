def middle_value(a, b, c):
  """
  Finds the middle value among three numbers using nested if statements.
  :param a: First number.
  :param b: Second number.
  :param c: Third number.
  :return: The middle value.
  """
  if a <= b <= c or c <= b <= a:
    return b
  elif b <= a <= c or c <= a <= b:
    return a
  else:
    return c

if __name__ == "__main__":
  assert middle_value(5, 2, 77) == 5
  assert middle_value(-10, 50, 57) == 50
  assert middle_value(-1, -6, -3) == -3
  assert middle_value(1, 1, 1) == 1
  assert middle_value(10, 20, 10) == 10
  print("All tests passed!")