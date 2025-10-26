# This program calculates the factorial of the entered number.

number = int(input("Enter the number: "))
result = 1
count = 1

while count <= number:
    result *= count
    count +=1

print(f"The factorial of {number} is: {result}")