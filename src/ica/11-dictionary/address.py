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

address_book = [betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'}]

print(address_book)

address_book.append({'Name': 'Jane Doe',
                     'Phone': '555-1234',
                     'Street': '123 Main St',
                     'City': 'Minneapolis',
                     'State': 'MN',
                     'Email': 'jane.d@email.com'})

address_book.append({'Name': 'John Smith',
                     'Phone': '555-5678',
                     'Street': '456 Oak Ave',
                     'City': 'Chicago',
                     'State': 'IL',
                     'Email': 'john.s@email.com'})


def filter_by_city(city_name: str, book: list):
    return [person for person in book if person['City'] == city_name]