number = int(input("Enter a number to check its Even or Odd: "))
if (number % 2) == 0:
    print(number, "Its Even.")
elif (number % 3) == 0:
    print(number, "Its Oddd.")
else:
    print("Enter a valid number.")