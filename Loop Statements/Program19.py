# Use a for loop to print the square of each number from 1 to 10

num_range = int(input("Enter the range"))
for num in range(1, num_range +1):
    square = num ** 2
    print(f"The square of {num} is {square}")