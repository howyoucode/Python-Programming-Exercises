# Create a program that simulates a countdown timer starting from a given number down to zero.

import time  # Importing time module for sleep function

countdown_start = int(input("Enter a number to start the countdown: "))

for i in range(countdown_start, -1, -1):
    print(i)
    time.sleep(1)

print("Countdown complete!")
