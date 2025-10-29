def percent_to_letter(percentage):
  """
  Converts a numeric percentage to a letter grade.
  :param percentage: The numeric score.
  :return: A string representing the letter grade ('A', 'B', 'C', 'D', 'F').
  """
  if percentage >= 90:
    return 'A'
  elif percentage >= 80:
    return 'B'
  elif percentage >= 70:
    return 'C'
  elif percentage >= 60:
    return 'D'
  else:
    return 'F'

if __name__ == "__main__":
  assert percent_to_letter(95.5) == 'A'
  assert percent_to_letter(90) == 'A'
  assert percent_to_letter(89.9) == 'B'
  assert percent_to_letter(80) == 'B'
  assert percent_to_letter(75) == 'C'
  assert percent_to_letter(60) == 'D'
  assert percent_to_letter(59) == 'F'
  assert percent_to_letter(0) == 'F'
  assert percent_to_letter(-10) == 'F'
  print("All tests passed!")