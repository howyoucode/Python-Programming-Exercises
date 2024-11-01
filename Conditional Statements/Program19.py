user_input = input("Enter a string: ")
if user_input.isupper():
    print("Its a uppercase.")
elif user_input.islower():
    print("Its a lowercase.")
else:
    print("Mix")

#By Manual
is_upper = False
is_lower = False

for char in user_input:
    if 'A' <= char <= 'Z':
        is_upper = True
    elif 'a' <= char <= 'z':
        is_lower = True

if is_upper and is_lower:
    print("The string is a mix of uppercase and lowercase letters.")
elif is_upper:
    print("The string is uppercase.")
elif is_lower:
    print("The string is lowercase.")
else:
    print("The string contains no letters.")
