def every_other(a_list):
  """
  Takes a list as an input and returns a new list that contains
  every other value from the original input list.
  """
  # Using list slicing with a step of 2 is the most concise way.
  return a_list[::2]

def sum_positive(numbers):
  """
  Takes a list of numbers as an input and returns the sum of the
  positive numbers.
  """
  total = 0  # Accumulator variable
  for num in numbers:
    if num > 0:
      total += num
  return total

# --- Test Calls ---
print("--- Testing every_other ---")
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original list: {my_list}")
print(f"Every other: {every_other(my_list)}") # Expected: [1, 3, 5, 7]

print("\n--- Testing sum_positive ---")
num_list = [1, -2, 3, -4, 5, 0]
print(f"Number list: {num_list}")
print(f"Sum of positives: {sum_positive(num_list)}") # Expected: 1 + 3 + 5 = 9

# modify.py

def change_start(value, a_list):
  """
  Modifies the input list by changing the value in the zero
  position to be the input value. Does not return a new list.
  """
  if len(a_list) > 0: # Good practice to avoid errors on empty lists
    a_list[0] = value

# --- Test Call ---
t_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"Original list: {t_list}")

change_start('X', t_list)

print(f"Modified list: {t_list}") # Expected: ['X', 'b', 'c', 'd', 'e', 'f']

# modify2.py

def remove_all(value, a_list):
  """
  Removes all occurrences of 'value' from 'a_list' without
  changing the order of the other values. Modifies the list in-place.
  """
  # As long as the value is still in the list, keep removing it.
  while value in a_list:
    a_list.remove(value)

# --- Test Call ---
data = [1, 5, 2, 5, 3, 5, 4, 5]
print(f"Original list: {data}")

remove_all(5, data)

print(f"List after removing all 5s: {data}") # Expected: [1, 2, 3, 4]