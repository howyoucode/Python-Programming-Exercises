# Use a loop to print numbers in reverse order within a given range.

# First Method
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for number in range(start, end + 1):
    print(end)
    end -= 1

# Second Method
for i in range(end, start -1, -1):
    print(i)
