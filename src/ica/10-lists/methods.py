def end_points(numbers):
  """
  Takes a list of numbers as input and returns both the minimum
  and maximum values from the list as a tuple.
  """
  if not numbers: # Handle empty list case
    return (None, None)
  return (min(numbers), max(numbers))

# --- Test Calls ---
num_list = [10, -5, 100, 0, 50]
print(f"Original list: {num_list}")

# Test call 1: Store the returned tuple in a single variable
endpoints_tuple = end_points(num_list)
print(f"Endpoints stored as a single tuple: {endpoints_tuple}")
print(f"Min: {endpoints_tuple[0]}, Max: {endpoints_tuple[1]}")


# Test call 2: Unpack the returned tuple into two separate variables
min_val, max_val = end_points(num_list)
print(f"\nEndpoints stored in separate variables:")
print(f"Min value: {min_val}, Max value: {max_val}")