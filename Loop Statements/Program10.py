# Use a loop to count the number of digits in an integer.

digit = int(input("Enter the number: "))
count = 0
for i in  str(abs(digit)):
    count += 1

print("Number of digits:", count)