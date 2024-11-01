# Formula to check a valid triangle 
# a + b > c
# a + c > b
# b + c > a

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("It's an Equilateral Triangle: All three sides are equal.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It's an Isosceles Triangle: Exactly two sides are equal.")
    else:
        print("It's a Scalene Triangle: All three sides are different.")
else:
    print("The entered lengths do not form a valid triangle.")
