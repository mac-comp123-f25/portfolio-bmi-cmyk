def times_n(n, num_list):
  """
  Uses a list comprehension to build a new list that has multiplied
  each of the original numbers in the list by n. Returns the new list.
  """
  return [num * n for num in num_list]

def remove_all_comp(value, a_list):
  """
  Creates a new list that does the same thing as the remove_all
  function from before, but uses a list comprehension.
  """
  return [item for item in a_list if item != value]

# --- Test Calls ---
print("--- Testing times_n ---")
numbers = [1, 2, 3, 4]
factor = 10
print(f"Original list: {numbers}, Factor: {factor}")
print(f"New list: {times_n(factor, numbers)}") # Expected: [10, 20, 30, 40]

print("\n--- Testing remove_all_comp ---")
data = [1, 5, 2, 5, 3, 5, 4, 5]
val_to_remove = 5
print(f"Original list: {data}, Value to remove: {val_to_remove}")
new_data = remove_all_comp(val_to_remove, data)
print(f"New list: {new_data}") # Expected: [1, 2, 3, 4]
print(f"Original list is unchanged: {data}")