# Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter the Year: "))

if (year % 4 == 0) and (year % 400 == 0):
    print ("The year is a leap year.")
else:
    print ("The year is not a leap year.")

