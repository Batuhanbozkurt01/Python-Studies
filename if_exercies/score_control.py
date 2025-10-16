# It receives the score information from the user and prints the score status on the screen.
print("Hello User :)")
print("Welcome to Score Control System...")
score = int(input("Please, enter the your score: "))
if score >= 90:
    print("Your letter grade: A")
    print(f"You passed with {score}.")
elif 80 <= score < 90:
    print("Your letter grade: B")
    print(f"You passed with {score}.")
elif 70 <= score < 80:
    print("Your letter grade: C")
    print(f"You passed with {score}.")
elif 60 <= score < 70:
    print("Your letter grade: D")
    print(f"You passed with {score}.")
else:
    print("Your letter grade: F")
    print(f"You couldn't pass with {score}.")
