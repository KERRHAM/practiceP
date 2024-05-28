print("Welcome user")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Cool.... Lets get started")

score = 0

answer = input("What is the capital of ireland? ")
if answer == "Dublin":
    print("Correct!!")
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Scotland? ")
if answer == "Edinburgh":
    print("Correct!!")
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Wales? ")
if answer == "Cardiff":
    print("Correct!!")
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of England? ")
if answer == "London":
    print("Correct!!")
    score += 1
else: 
    print("Incorrect!!")

print("You answered " + str(score) + " Questions Correctly")
print("score " + str((score / 4) * 100) + "%.")