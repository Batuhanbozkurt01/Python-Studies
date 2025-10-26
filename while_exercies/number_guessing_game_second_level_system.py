# This program is a number guessing game where the user has 3 attempts to guess a number between 1 and 10.

import random
secret_number = random.randint(1,10)
guess = 0
tries = 0
max_tries = 3
while guess != secret_number and tries < max_tries:
    guess = int(input("Enter your guess (1-10): "))
    tries += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {tries} tries.")
        break
if guess != secret_number:
    print("You lost! The correct number was: ", secret_number)