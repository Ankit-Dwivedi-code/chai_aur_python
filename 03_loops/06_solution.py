# Compute the factorial of a number using a while loop.

number = int(input("Enter any integer value to find its factorial: "))

fact = 1
while number >= 1:
    fact *= number
    number -= 1

print ("Factorial of the given input is: ", fact, "")