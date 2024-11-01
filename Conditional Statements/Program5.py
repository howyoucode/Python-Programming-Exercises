grade_percentage = float(input("Enter the percentage of your grade: "))
if grade_percentage >= 90:
    result = "A"
elif grade_percentage >= 80:
    result = "B"
elif grade_percentage >= 70:
    result = "C"    
elif grade_percentage >= 60:
    result = "D"
else:
    result = "F"  

print(f"You got {result} grade.")