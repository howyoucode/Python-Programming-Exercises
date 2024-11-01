# Write a program that continues to ask for a number until the correct number is guessed.


def number_guess(number_range, random_number):
    counter = 1
    while True:
        while True:
            guess_number = input("Enter your integer guess value: ")
            if not (guess_number.isdigit() and (int(guess_number) <= int(number_range))):
                continue
            else:
                guess_number = int(guess_number)
                break

        if guess_number > random_number:
            print("You're above the guess number.")
        elif guess_number < random_number:
            print("You're below the guess number.")
        elif guess_number == random_number:
            print("You guess it right in "+ str(counter) +" times.")
            break
        counter += 1

def rangee():
    while True:
        number_range = input("Enter integer number range: ")
        if not number_range.isdigit():
            continue
        else:
            number_range = int(number_range)
            import random
            random_number = random.randint(1, int(number_range))
            number_guess(number_range, random_number)
            break
while True:
    print("Welcome to number guessing game!")
    if input("Do you wanna play? (y / n): ").lower() != "y":
        print("Okay, Come again!")
        break 
    else:
        print("Lets jump to game.")
        rangee()