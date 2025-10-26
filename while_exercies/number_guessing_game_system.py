# This program helps the system find a number between 1 and 100 by telling if the guess is too high or too low.

import random
secret_number = random.randint(1, 100)
guess = 0
while guess != secret_number:
    guess = int(input("Enter your guess (1-100): "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
print("Congratulations! You guessed it right!")