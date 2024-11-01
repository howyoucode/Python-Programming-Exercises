# Print the multiplication table of a given number

number = int(input("Enter a number to print a table: "))
i =1
while i <= 10:
    print(number, "x", i, "=", i*number)
    i += 1