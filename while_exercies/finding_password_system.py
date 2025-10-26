# This program checks if the entered password matches the correct password "python".

correct_password = "python"
password = ""
while password != correct_password:
    password = input("Enter the password: ")
    if password != correct_password:
        print("Wrong password! Try again.")
print("Access Granted!")