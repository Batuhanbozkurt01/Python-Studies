# Counts the letters in the entered word.
word = input("Enter the word: ")
count = 0
for letter in word:
    count += 1
print("The word has", count, "letters.")