# Python Programming Exercises

This repository contains a set of Python exercises divided into two many categories: **Conditional Statements** and **Loops** and many more. Each section is designed to reinforce key concepts in Python programming, ranging from basic control flow to more complex looping structures.

## Table of Contents
1. [Conditional Statements](#conditional-statements)
2. [Loops](#loops)
3. [Functons](#Functions)
4. [Dictionary](#Dictionary).

---

## Conditional Statements

This section includes 20 exercises that involve using conditional statements in Python to solve different types of problems. Each exercise helps build an understanding of decision-making in programming.

1. **Positive, Negative, or Zero Check:** Write a program to check if a given number is positive, negative, or zero.
2. **Age Classification:** Determine if a user is a minor, adult, or senior citizen based on age input.
3. **Leap Year Checker:** Check if a given year is a leap year.
4. **Even or Odd Checker:** Determine if an integer is even or odd.
5. **Grade Conversion:** Convert a percentage score into a letter grade (A, B, C, D, F).
6. **Largest of Two Numbers:** Find the largest of two numbers.
7. **Largest of Three Numbers:** Find the largest of three numbers.
8. **Palindrome Check:** Check if a given string is a palindrome.
9. **Triangle Validity Checker:** Determine if three given side lengths form a valid triangle.
10. **Vowel or Consonant:** Identify if a character is a vowel or consonant.
11. **Multiple of 3 and 5:** Check if a number is a multiple of both 3 and 5.
12. **Temperature Categorization:** Classify temperature in Celsius as freezing, moderate, or hot.
13. **Basic Calculator:** Perform a basic arithmetic operation based on user input.
14. **Century Year Check:** Determine if a year is a century year.
15. **Range Check:** Check if a number is within a specified range.
16. **Triangle Type Classification:** Classify a triangle as equilateral, isosceles, or scalene.
17. **Divisibility Check:** Check if a number is divisible by 2, 3, or both.
18. **Pass or Fail:** Determine if a user’s score is a pass or fail (50 or above).
19. **String Case Check:** Identify if a string is uppercase, lowercase, or a mix.
20. **Prime Number Check:** Check if a given number is prime.

---

## Loops

The following 20 exercises provide practice with different types of loops in Python, helping to strengthen skills in iteration and control flow.

1. **Print 1 to 20:** Print numbers from 1 to 20 using a for loop.
2. **Even Numbers (1-50):** Use a while loop to print even numbers from 1 to 50.
3. **Sum of Numbers (1-100):** Calculate the sum of all numbers from 1 to 100.
4. **Multiplication Table:** Print the multiplication table of a given number.
5. **Odd Numbers (1-100):** Print all odd numbers from 1 to 100.
6. **String Character Printer:** Use a for loop to print each character of a string.
7. **Factorial Calculator:** Find the factorial of a number using a while loop.
8. **Countdown from 10:** Print numbers from 10 down to 1.
9. **Fibonacci Series:** Print the first 10 Fibonacci numbers.
10. **Digit Counter:** Use a loop to count the number of digits in an integer.
11. **Number Reversal:** Print the reverse of a given number.
12. **Prime Numbers (1-50):** Print all prime numbers between 1 and 50.
13. **Pyramid Pattern:** Use nested loops to print a pyramid pattern of * characters.
14. **Loop Break Example:** Write a program that breaks out of a loop when a specific condition is met.
15. **Sum of Even and Odd Numbers:** Calculate the sum of even and odd numbers up to a given number.
16. **Digit Sum Calculator:** Calculate the sum of the digits of an inputted integer.
17. **Number Guessing Game:** Keep asking for a number until the correct number is guessed.
18. **Reverse Order Printer:** Print numbers in reverse order within a given range.
19. **Squares (1-10):** Print the square of each number from 1 to 10.
20. **Countdown Timer:** Simulate a countdown timer starting from a given number down to zero.

## Functions
# Basic Function Questions

1. Write a function to calculate the area of a circle given its radius.
2. Create a function that takes two numbers and returns their sum.
3. Write a function to find the factorial of a number using recursion.
4. Write a function that takes a string and returns it reversed.
5. Create a function to check if a given number is prime.
6. Write a function to count the vowels in a given string.

Intermediate Function Questions

1. Create a function that takes a list of numbers and returns the largest number.
2. Write a function to find the nth Fibonacci number using recursion.
3. Write a function to check whether a string is a palindrome.
4. Create a function that takes a list of integers and returns the sum of all even numbers.
5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
6. Create a function that accepts a dictionary and returns the key with the highest value.

Advanced Function Questions

1. Write a function that calculates the power of a number without using the ** operator.
2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
3. Write a function to flatten a nested list.
4. Create a function to check if two strings are anagrams.
5. Write a function that takes a list and removes all duplicate elements.
6. Create a function that takes a string and counts the frequency of each character.

# Real-world Scenarios

1. Write a function that takes a list of employee salaries and calculates the average salary.
2. Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.

---

## Dictionary  

### **Basic Operations**  
1. Create a dictionary `student` with keys: `name`, `age`, and `grade`. Assign them appropriate values.  
2. Access the value of the key `grade` in the `student` dictionary.  
3. Add a new key `city` to the `student` dictionary and set its value to `"New York"`.  
4. Update the value of the `age` key in the `student` dictionary to `20`.  
5. Remove the key `city` from the `student` dictionary.  

---

### **Iterating through Dictionaries**  
6. Iterate through the dictionary `student` and print all keys.  
7. Iterate through the dictionary `student` and print all values.  
8. Iterate through the dictionary `student` and print all key-value pairs in the format `key: value`.  
9. Check if the key `grade` exists in the `student` dictionary and print `True` or `False`.  
10. Count the total number of keys in the `student` dictionary.  

---

### **Advanced Dictionary Usage**  
11. Merge the following two dictionaries and print the result:  
    ```python
    dict1 = {'a': 1, 'b': 2}  
    dict2 = {'c': 3, 'd': 4}  
    ```  
12. Create a dictionary from a list of tuples: `[('name', 'Alice'), ('age', 25), ('city', 'Paris')]`.  
13. Sort the keys of the dictionary `{'z': 1, 'a': 2, 'c': 3}` in ascending order and print the sorted dictionary.  
14. Reverse the dictionary `{'a': 1, 'b': 2, 'c': 3}` so that keys become values and values become keys.  
15. Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).  

---

### **Nested Dictionaries**  
16. Create a nested dictionary to represent the following data:  
    ```plaintext
    Person:  
      Name: John  
      Age: 30  
      Address:  
        Street: 123 Elm St  
        City: Boston  
    ```  
17. Access the value of the `City` key in the nested dictionary from the previous question.  
18. Add a new key `Phone` to the nested dictionary with the value `"123-456-7890"`.  
19. Delete the `Address` key from the nested dictionary.  
20. Iterate through all the keys in the outermost level of the nested dictionary and print them.  

---

### **Applications of Dictionaries**  
21. Use a dictionary to count the occurrences of each word in the string `"hello world hello python world"`.  
22. Write a Python program to find the key with the maximum value in the dictionary `{'a': 10, 'b': 15, 'c': 7}`.  
23. Create a dictionary to map numbers 1 to 5 to their squares (e.g., `{1: 1, 2: 4, 3: 9, ...}`).  
24. Write a Python program to remove duplicate values from the dictionary `{'a': 10, 'b': 15, 'c': 10, 'd': 15}`.  
25. Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return `"Key not found"`.  

---

### **Challenging Problems**  
26. Given two dictionaries `dict1 = {'a': 5, 'b': 10}` and `dict2 = {'a': 3, 'b': 7}`, write a Python program to add the values of matching keys and print the result.  
27. Write a Python program to create a dictionary where the keys are the first `n` positive integers, and the values are their cubes. Take `n` as user input.  
28. Flatten the following nested dictionary into a single-level dictionary:  
    ```python
    {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
    ```  
29. Write a Python program to split a dictionary into two based on whether the values are odd or even.  
30. Create a dictionary comprehension to filter out all keys in `{'a': 1, 'b': 2, 'c': 3, 'd': 4}` where the value is less than 3.  

---
