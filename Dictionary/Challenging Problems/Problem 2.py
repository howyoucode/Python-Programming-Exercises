# Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.

n = int(input("Enter a number: "))
cube = {num: num**3 for num in range(1, n+1)}

print(cube)