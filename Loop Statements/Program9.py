# Write a program to print the first 10 Fibonacci numbers

limit = int(input("Enter the limit: "))

i = 1
a = 0
b = 1
while i <= limit:
    print(a)
    c = a + b 
    a = b
    b = c
    i += 1