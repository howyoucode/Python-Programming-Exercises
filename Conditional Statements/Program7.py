num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 == num2:
    if num1 > num3:
        print(f"{num1} and {num2} are equal and larger than {num3}.")
    else:
        print(f"{num3} is the largest number.")
elif num1 == num3:
    if num1 > num2:
        print(f"{num1} and {num3} are equal and larger than {num2}.")
    else:
        print(f"{num2} is the largest number.")
elif num2 == num3:
    if num2 > num1:
        print(f"{num2} and {num3} are equal and larger than {num1}.")
    else:
        print(f"{num1} is the largest number.")
else:
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the largest number.")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the largest number.")
    else:
        print(f"{num3} is the largest number.")