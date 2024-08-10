# Check a number is prime

num = int(input("Enter a number: "))

if num == 1:
    print("This is not a prime number!")
elif num > 1 :
    for i in range(2, num):
        if(num % i) == 0:
            print("This is not a prime number!")
            break
    else:
        print("This is a prime number!")
else:
    print("Please enter an integer value!")
