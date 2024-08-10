num = int(input("Enter a number:"))
sum = 0

for i in range (1, num + 1):
    if i % 2 == 0:
        sum += 1
print("Sum of even numbers is:", sum)