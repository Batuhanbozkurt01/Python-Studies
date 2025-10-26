# This program is a simple calculator that performs addition, subtraction, or exits based on the user's choice.

while True:
    print("\n----------------------------------")
    print("Select the action you want to perform:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Exit")
    print("----------------------------------")
    
    selection = int(input("Select an action between 1 and 3 according to the menu: "))
    if selection == 3:
        print("Exiting the program...")
        break

    elif selection == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        addition_result = num1 + num2 
        print(f"Addittion result: {addition_result}")
    
    elif selection == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        subtraction_result = num1 - num2
        print(f"Subtraction result: {subtraction_result}")
    
    else:
        print("Invalid selection. Try again.")