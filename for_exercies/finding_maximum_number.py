# Prints the largest number in the current list.
numbers = [56, 45, 77, 2, 10, 88, 11, 23, 44, 95, 12, 97]
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("The largest number is:", max_num)