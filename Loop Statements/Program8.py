# Use a for loop to print numbers from 10 down to 1.

# First Method
number  = int(input("Enter a number: "))
for i in range(1, number + 1):
    print(number)
    number -= 1

# Second Method
for i in range(number, 0, -1):
    print(i)
