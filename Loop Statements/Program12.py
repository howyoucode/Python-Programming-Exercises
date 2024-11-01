# Print all prime numbers between 1 and 50.

limit = int(input("Enter the limit: "))

for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")