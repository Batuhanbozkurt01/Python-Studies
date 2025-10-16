# It receives the number information from the user and prints the number status as odd or even on the screen.
print("Hello User :)")
print("Welcome to Odd or Even Number Control System...")
number = int(input("Please, enter the your number: "))
if number % 2 == 0:
    print("Your number is an even number.")
    print(f"Remaining number: {number % 2}")
else:
    print("Your number is an odd number.")
    print(f"Remaining number: {number % 2}")