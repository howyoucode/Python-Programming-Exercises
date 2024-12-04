# Delete the Address key from the nested dictionary.

person = {
    'Name': 'John',
    'Age': 30,
    'Address': {
        'Street': '123 Elm St',
        'City': 'Boston'
    },
    'Phone': '123-456-7890'
}

del person['Address']

print(person)