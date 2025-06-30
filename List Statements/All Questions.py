# ------------------ Slicing Examples ------------------

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"1: {fruits[0:]}")               # All elements from start
print(f"2: {fruits[1:3]}")              # Index 1 to 2
print(f"3: {fruits[-1:]}")              # Last element
print(f"4: {fruits[-1:-4]}")            # Empty, invalid forward slice
print(f"5: {fruits[0::2]}")             # Every second element
print(f"6: {fruits[-1:-4:2]}")          # Empty, invalid forward step
print(f"7: {fruits[-4:-1:2]}")          # From -4 to -2, skipping every second
print(f"8: {fruits[-1:1]}")             # Empty
print(f"9: {fruits[0:-2]}")             # All except last two

# ------------------ Basic List Problems (Beginner) ------------------

# 1. Print the first element of the list.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])

# 2. Print the last element using negative indexing.
print(fruits[-1])

# 3. Print all elements using a loop.
for fruit in fruits:
    print(fruit)

# 4. Find the length of the list.
print(f"Length of the fruits list: {len(fruits)}")

# 5. Append a new element "orange" to the list.
fruits = ["apple", "banana", "cherry"]
print(f"Before append: {fruits}")
fruits.append("orange")
print(f"After append: {fruits}")

# 6. Insert "grape" at index 2.
fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "grape")
print(fruits)

# 7. Remove the element "banana".
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    fruits.remove("banana")
print(fruits)

# 8. Remove the last element using pop().
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

# 9. Check if "apple" exists in the list.
fruits = ["apple", "banana", "cherry"]
print("Yes, it's in the list" if "apple" in fruits else "Not in the list")

# 10. Count how many times "apple" appears.
fruits = ["apple", "banana", "apple", "cherry", "apple"]
print(fruits.count("apple"))

# ------------------ Indexing & Slicing ------------------

# 11. Print the first 3 elements.
fruits = ["apple", "banana", "cherry", "date", "orange"]
print(fruits[:3])

# 12. Print all elements except the last one.
print(fruits[:-1])

# 13. Reverse the list using slicing.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[::-1])

# 14. Print every second element.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[::2])

# 15. Print all elements from index 2 onward.
print(fruits[2:])

# 16. Get a sublist from index 1 to 3.
print(fruits[1:4])

# 17. Print the list in reverse using a loop.
fruits = ["apple", "banana", "cherry", "date"]
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# 18. Replace the second element with "kiwi".
fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits)

# 19. Swap the first and last elements.
fruits = ["apple", "banana", "cherry", "date"]
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)

# 20. Delete the first 3 elements using slicing.
fruits = ["apple", "banana", "cherry", "date", "orange"]
fruits = fruits[3:]
print(fruits)

# ------------------ Sorting & Math ------------------

# 21. Sort the list alphabetically.
words = ["grape", "apple", "banana", "cherry"]
words.sort()
print(words)

# 22. Sort a list of numbers in descending order.
numbers = [5, 2, 9, 1, 7]
length = len(numbers)
for i in range(length):
    for j in range(0, length - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

# 23. Find the maximum number in a list.
numbers = [45, 22, 89, 33, 67]
max_val = numbers[0]
for i in numbers:
    if i > max_val:
        max_val = i
print(max_val)
# OR
print(max(numbers))

# 24. Find the minimum number in a list.
numbers = [12, 3, 77, 45, 6]
min_val = numbers[0]
for i in numbers:
    if i < min_val:
        min_val = i
print(min_val)
# OR
print(min(numbers))

# 25. Find the average of numbers.
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) // len(numbers)
print(average)

# ------------------ List Comprehension & Filtering ------------------

# 26. List of squares from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print(squares)

# 27. Filter even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [i for i in numbers if i % 2 == 0]
print(evens)

# 28. Strings with more than 5 characters.
names = ["apple", "pineapple", "kiwi", "banana", "grapes"]
long_names = [i for i in names if len(i) > 5]
print(long_names)

# 29. Extract all vowels from a string.
text = "Programming is fun and educational"
vowels = [i for i in text if i.lower() in ["a", "e", "i", "o", "u"]]
print(vowels)

# 30. Find common elements in two lists.
list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "date", "cherry"]
common = [i for i in list1 if i in list2]
print(common)