# ------------------ Set Problems (Beginner to Intermediate) ------------------

# 1. Create a set with 5 fruit names and print it.
fruits = {"apple", "banana", "cherry", "lychee", "mango", "mango"}  # duplicates ignored
print(fruits)

# 2. Add "kiwi" to the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("kiwi")
print(fruits)

# 3. Remove "banana" from the set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# 4. Try to remove "orange" using discard (no error if missing).
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")
print(fruits)

# 5. Clear the entire set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# 6. Print all elements of the set using a loop.
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# 7. Check if "blue" exists in the set.
colors = {"red", "green", "blue"}
print("Yes!" if "blue" in colors else "No!")

# 8. Count how many elements are in the set.
colors = {"red", "green", "blue"}
print(len(colors))

# 9. Loop through a set and print each item in uppercase.
colors = {"red", "green", "blue"}
colors = {color.upper() for color in colors}
print(colors)

# 10. Add user input into an existing set (example version without input).
colors = {"red", "green", "blue"}
# user_input = input("Enter a color: ").strip()
# colors.add(user_input)
print(colors)

# 11. Find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# 12. Find the intersection of two sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)

# 13. Find the difference (set1 - set2).
print(set1 - set2)

# 14. Find the symmetric difference.
print(set1 ^ set2)

# 15. Use `|` operator to join two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x | y)

# 16. Convert a list into a set (remove duplicates).
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))

# 17. Convert a string into a set of characters.
text = "banana"
print(set(text))

# 18. Copy a set and modify the copy.
original = {"a", "b", "c"}
copy = {*original}
copy.add("d")
print(copy)

# 19. Convert a set back to a list.
animals = {"cat", "dog", "fish"}
print(list(animals))

# 20. Convert two lists to sets and find common elements.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set(a) & set(b))

# 21. Remove all even numbers from a set.
nums = {1, 2, 3, 4, 5, 6, 7, 8}
nums = {n for n in nums if n % 2 != 0}
print(nums)

# 22. Keep only items that start with "A".
names = {"ali", "Ahmed", "Sara", "Adeel"}
names = {name for name in names if name.upper().startswith("A")}
print(names)

# 23. Find unique characters in a sentence.
text = "Set is a unique collection"
print(set(text))

# 24. Get common vowels from two strings using sets.
str1 = "education"
str2 = "foundation"
vowels = {"a", "e", "i", "o", "u"}
print(set(str1) & set(str2) & vowels)

# 25. Find letters that appear only in one string but not both.
a = "python"
b = "typhoon"
print(set(a) ^ set(b))

# 26. Check if one set is a subset of another.
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

# 27. Check if two sets are disjoint.
a = {1, 2}
b = {3, 4}
print("Disjoint" if a.isdisjoint(b) else "Not disjoint")

# 28. Check if one set is a superset of another.
a = {1, 2, 3, 4}
b = {2, 3}
print("Superset" if a.issuperset(b) else "Not superset")

# 29. Remove duplicates from a list using a set.
nums = [1, 2, 2, 3, 3, 4, 5]
print(set(nums))

# 30. Create a set from a sentence and count how many unique characters it contains.
sentence = "Practice makes perfect"
print(len(set(sentence)))