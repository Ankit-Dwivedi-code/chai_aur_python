#  Keep asking the user for input until they enter a number between 1 and 10.

num = int(input("Enter a num: "))

while num > 10 or num < 1:
    num = int(input("Enter a num: "))
