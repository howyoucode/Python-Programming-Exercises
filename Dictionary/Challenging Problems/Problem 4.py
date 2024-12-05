# Write a Python program to split a dictionary into two based on whether the values are odd or even.

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

odd_dict = {}
even_dict = {}

for key, value in d.items():
    if value % 2 == 0:
        even_dict[key] = value
    else:
        odd_dict[key] = value

print("Odd Dictionary:", odd_dict)
print("Even Dictionary:", even_dict)
