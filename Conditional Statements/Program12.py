temperature = float(input("Enter the temperature in Celsius: "))

if temperature >= 30:
    print("It's hot.")
elif 15 <= temperature < 30:
    print("It's moderate.")
else:
    print("It's cold.")