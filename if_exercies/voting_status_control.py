# It receives the voting age information from the user and prints the person's voting status on the screen.
print("Hello User :)")
print("Welcome to Voting Status Control System...")
voting_status_age = int(input("Please, enter the age: "))
if voting_status_age >= 18:
    print("You can vote.")
else:
    print("You can not vote.")
