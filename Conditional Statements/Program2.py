age = int(input("Enter your age: "))
if age < 18:
    result = "minor"
elif age < 60:
    result = "adult"
else:
    result = "senior"

print(f"The age category you entered is {result}.")