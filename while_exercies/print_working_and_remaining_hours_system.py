# This program calculates how many hours an employee has worked and how many hours are remaining.

total_working_hours = 0.00
target_time = 40.00
while total_working_hours < target_time:
    target_time = float(input("Enter your working hours: "))
    total_working_hours += target_time
    remaining_hours = 40.00 - total_working_hours
    print(f"Remaining Hours: {remaining_hours}")
print("You have completed the weekly hours.")

