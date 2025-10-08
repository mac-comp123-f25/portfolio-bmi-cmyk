def name_subst(name, text):
  """
  Replaces the special string "ZZZ" in a piece of text with a given name.
  """
  return text.replace("ZZZ", name)

# Example Usage:
sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
print(sallie)

print(name_subst("Fred", "Jamie and ZZZ flew over the trees."))
