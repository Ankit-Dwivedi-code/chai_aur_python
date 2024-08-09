age = int(input("Enter your age: "))
day = input("Enter day: ")

if age >= 18 and day == "Wednesday":
    print("Your ticket price is $10")
elif age < 18 and day == "Wednesday":
    print("Your ticket price is $6")
elif age < 18:
    print("Your ticket price is $8")
else:
    print("Your ticket price is $12")
