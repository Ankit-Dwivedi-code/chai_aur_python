# Given a string, find the first non-repeated character.

string = input("Enter any String : ")

for char in string:
    if string.count(char) == 1:
        print("First Non Repeated Character : ",char)
        break