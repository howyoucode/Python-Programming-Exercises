value = []
while True:
    data = input("Enter a word to check if it's a palindrome or not (type 'x' to exit): ")
    if data.lower() == "x":
        break
    else:
        value.append(data)
 
result = []      
for val in value:
       reverse = val[::-1]
       result.append("It's Palindrome." if reverse == val else "It's not Palindrome.")