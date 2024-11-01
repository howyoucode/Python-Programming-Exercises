# Find the factorial of a number using a while loop.

number = int(input("Enter the number: "))
i = 1
factorial = 1
while i <= number:
    factorial *= number
    number -= 1

print(factorial)