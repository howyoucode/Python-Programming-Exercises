# Flatten the following nested dictionary into a single-level dictionary:
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

d = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

flat = {}
for k1, v1 in d.items():
    for k2, v2 in v1.items():
        flat[f"{k1}_{k2}"] = v2

print(flat)