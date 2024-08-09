# Choose mode of transport on the basis of distance

distance = int(input("Enter your travel distance in km : "))

if distance < 3:
    print("You can go by walking")
elif distance >= 3 and distance <= 15:
    print("You can go by Bike")
else:
    print("You can go by Car")