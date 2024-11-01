min_value = 10
max_value = 50

number = float(input(f"Enter a number to check if it's between {min_value} and {max_value}: "))

if min_value <= number <= max_value:
    print(f"The number {number} is within the range.")
else:
    print(f"The number {number} is outside the range.")
