# Create a nested dictionary to represent the following data:
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  


person = {
    'Name': 'John',
    'Age': 30,
    'Address': {
        'Street': '123 Elm St',
        'City': 'Boston'
    }
}

print(person)

        # OR 

data = [('name', 'John'), ('age', 30), ('Address', {'Street': '123 Elm St', 'City': 'Boston'})]
dictionary = {}
for key, value in data:
    dictionary[key] = value

        # OR

dictionary = dict(data)
print(dictionary)