import random
top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
     top_of_range = int(top_of_range)
else:
    print("Please enter a number next time")

random_number = random.randrange(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")

    if user_guess.isdigit():
     user_guess= int(user_guess)

    else:
        print("Please enter a number next time")
        continue

    if user_guess == random_number:
        print("Well done you got it!!")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were lower than the number!")

print("You got it in", guesses, "Quesses.")
