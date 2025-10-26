# This program calculates the total of all entered numbers until the user enters 0.

total = 0
number = None
while number !=0:
    number = int(input("Enter a number (0 to stop): "))
    total += number
print("The total sum is: ", total)