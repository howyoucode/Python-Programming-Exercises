# Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.

data = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

unique_values = {}
for key, value in data.items():
    if value not in unique_values.values():
        unique_values[key] = value


print(unique_values)
