# number_guess_game.py

import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    print("Wrong guess, try again!")
    guess = int(input("Guess again: "))

print("Correct! You guessed it 🎉")