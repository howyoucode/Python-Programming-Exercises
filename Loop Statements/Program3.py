# Write a program to calculate the sum of all numbers between 1 and 100.

#While Loop
i = 0
sum_of_num = 0
while i <= 100:
    sum_of_num += i
    i += 1

print(sum_of_num)

#For loop
total_sum = 0
for number in range(1, 101):
    total_sum += number
print("The sum of all numbers between 1 and 100 is:", total_sum)