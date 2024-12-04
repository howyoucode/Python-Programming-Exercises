# Iterate through all the keys in the outermost level of the nested dictionary and print them.

person = {
    'Name': 'John',
    'Age': 30,
    'Address': {
        'Street': '123 Elm St',
        'City': 'Boston'
    },
    'Phone': '123-456-7890'
}

for key in person:
    print(key)