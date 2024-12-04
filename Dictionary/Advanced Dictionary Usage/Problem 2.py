# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].

data = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
dictionary = dict(data)


            # OR 

data = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]

dictionary = {}
for key, value in data:
    dictionary[key] = value

print(dictionary)