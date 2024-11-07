number = int(input("Enter a number to check a prime number: "))

if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0 or number % 13 ==0:
    print("Its not a prime number.")
else:
    print("prime number.")

#By loop
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number:")
            break
    else:
        print("Prime number")
else:
    print("Prime number.")
