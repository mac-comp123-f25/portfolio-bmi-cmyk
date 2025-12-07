income = {}
print(f"1. Empty income dictionary: {income}")

years = {
    "Alice": 1995,
    "Bob": 1992,
    "Susan": 1968
}
print(f"2. Initial years dictionary: {years}")

years2 = years.copy()
print(f"3. Copied dictionary years2: {years2}")

susan_birth_year = years["Susan"]
print(f"4. Susan's birth year is: {susan_birth_year}")

years["Henry"] = 2004
print(f"5. 'years' after adding Henry: {years}")
print(f"   'years2' remains unchanged: {years2}")

del years2["Susan"]
print(f"6. 'years2' after deleting Susan: {years2}")
print(f"   'years' remains unchanged: {years}")