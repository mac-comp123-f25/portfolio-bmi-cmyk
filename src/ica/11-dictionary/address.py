def filter_by_city(city_name, address_book_list):
    """
    Creates a new list containing only those dictionaries from an address book
    where the city entry matches the input city name.

    Args:
        city_name (str): The city to filter by.
        address_book_list (list): A list of dictionaries, where each dictionary is a contact.

    Returns:
        list: A new list containing only the matching contacts.
    """
    # Using a list comprehension for a concise solution
    return [person for person in address_book_list if person['City'] == city_name]

# --- Provided Data ---
betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

# Original address book with two new entries added
address_book = [
    betsy_info,
    tom_info,
    {'Name': 'Susan Fox',
     'Phone': 'x6553',
     'Street': '1600 Grand Avenue',
     'City': 'Saint Paul',
     'State': 'MN',
     'Email': 'fox@macalester.edu'},
    # Added Entry 1 (not in Saint Paul)
    {'Name': 'Peter Parker',
     'Phone': '555-1234',
     'Street': '20 Ingram Street',
     'City': 'New York',
     'State': 'NY',
     'Email': 'spidey@dailybugle.com'},
    # Added Entry 2 (in a different city)
    {'Name': 'Diana Prince',
     'Phone': '555-9876',
     'Street': '1 Museum Drive',
     'City': 'Washington D.C.',
     'State': 'DC',
     'Email': 'wwonder@argus.gov'}
]

# --- Main execution and testing ---
if __name__ == '__main__':
    # Print the original (now expanded) value of address_book
    print("--- Full Address Book ---")
    for entry in address_book:
        print(entry)
    print("\n" + "="*40 + "\n")

    # Use the function to filter by "Saint Paul"
    saint_paul_residents = filter_by_city('Saint Paul', address_book)
    print("--- Residents of Saint Paul ---")
    for person in saint_paul_residents:
        print(person)
    print("\n" + "="*40 + "\n")

    # Use the function to filter by "New York"
    new_york_residents = filter_by_city('New York', address_book)
    print("--- Residents of New York ---")
    for person in new_york_residents:
        print(person)