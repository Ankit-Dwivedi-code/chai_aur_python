age = int(input("Enter your age"))

if age < 13:
    print("You are a Child!")
elif age > 13 and age <= 19:
    print("You are an Teenager!")
elif age > 19 and age <= 59:
    print("You are an Adult!")
else:
    print("You are a Senior Citizen!")

