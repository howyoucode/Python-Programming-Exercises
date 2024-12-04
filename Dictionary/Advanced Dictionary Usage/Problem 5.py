# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}

def identical(dict1, dict2):
    return dict1 == dict2

print(identical(dict1, dict2))