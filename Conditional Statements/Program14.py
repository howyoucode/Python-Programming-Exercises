year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("It's a leap century year.")
    else:
        print("It's a century year, but not a leap year.")
else:
    print("It's not a century year.")
