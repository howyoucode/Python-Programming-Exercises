# Create a program to calculate the sum of the digits of an inputted integer.

number = int(input("Enter an integer: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10 
    sum_of_digits += digit
    number //= 10
print("Sum of the digits:", sum_of_digits)