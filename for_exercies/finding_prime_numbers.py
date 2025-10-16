# Finds and prints prime numbers between 2 and 101.
for primeNumber in range(2,101):
    prime = True
    for divisorNumber in range(2, primeNumber):
        if primeNumber % divisorNumber == 0:
            prime = False
    if prime: 
        print(primeNumber)