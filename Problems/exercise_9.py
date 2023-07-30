#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

replay = ""

while replay != "n":
    print("Higher or lower...")
    random_number = random.randint(1, 9)
    #print(random_number)
    guess = 0
    counter = 0
    while guess != random_number:
        guess = int(input("Enter guess 1-9, integers only: "))
        counter += 1
        if guess < 1 or guess > 9:
            print("Invalid guess, try again.")
        elif guess < random_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
    print("You got it in", counter, "guesses!")
    replay = input("Type 'n' to stop: ")