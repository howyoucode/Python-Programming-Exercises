# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.

data = {'a': 1, 'b': 2, 'c': 3}

reversed_dict = {value: key for key, value in data.items()}
print(reversed_dict)