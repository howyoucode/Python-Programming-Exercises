# Access the value of the City key in the nested dictionary from the previous question.

person = {
    'Name': 'John',
    'Age': 30,
    'Address': {
        'Street': '123 Elm St',
        'City': 'Boston'
    }
}


print(person['Address']['City'])