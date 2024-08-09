# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("What is your pet's species? ")
age = int(input("How old is your pet? "))

if species == "Dog" and age < 2:
    print("Your pet's type of food should be puppy food.")
elif species == "Cat" and age > 5:
    print("Your pet' s type of food should be senior cat food.")