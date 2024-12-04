# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

data = {'z': 1, 'a': 2, 'c': 3}
data = {key: data[key] for key in sorted(data)}
print(data)

