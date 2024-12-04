# Merge the following two dictionaries and print the result:

dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 

merged = dict1.update(dict2)
        # OR
merged = dict1 | dict2
print(merged)