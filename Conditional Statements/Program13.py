operators = ["+", "-", "/", "*"]
choose_operator = input("Select the operator (+, -, *, /): ")

if choose_operator in operators:
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))
    
    if choose_operator == "+":
        result = num1 + num2
    elif choose_operator == "-":
        result = num1 - num2
    elif choose_operator == "*":
        result = num1 * num2
    elif choose_operator == "/":
        if num2 != 0: 
            result = num1 / num2
        else:
            result = "Undefined (cannot divide by zero)"
    
    print("Result:", result)
else:
    print("Not a valid option.")
