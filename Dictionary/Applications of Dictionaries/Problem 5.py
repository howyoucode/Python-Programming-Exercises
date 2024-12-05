# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def get_val(data, key):
    return data[key] if key in data else "Key not found"

data = {'a': 10, 'b': 15, 'c': 7}

print(get_val(data, 'b'))  # Output: 15
print(get_val(data, 'd'))  # Output: Key not found

