items = ["apple", "banana", "orange", "apple", "mango"]

for fruit in items:
    if items.count(fruit) > 1:
        print("Duplicate", fruit)
        break
    else: print(fruit, "is not a duplicate")