# Iterate through the dictionary student and print all key-value pairs in the format key: value.

student = {
    'name': 'Ali Hassan',
    'age': 20,
    'grade': 'A+',
    'city': 'Faisalabad'
}

for key, value in student.items():
    print(f'{key} : {value}.')