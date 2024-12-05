# Use a dictionary to count the occurrences of each word in the string "hello world hello python world".

text = "hello world hello python world"
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
