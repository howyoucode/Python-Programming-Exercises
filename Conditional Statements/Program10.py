character = input("Enter a character to check if it's a vowel or consonant: ")
if len(character) == 1:
    if character.lower() in "aeiou":
        print("It's a vowel.")
    else:
        print("It's a consonant.")
else:
    print("Enter a single character.")