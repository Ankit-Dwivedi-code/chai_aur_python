# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order = input("Your order")
extra_Shot = True

if extra_Shot:
    print("You have ordered ", order, "coffee", "with extra shot")
else:
    print("You have ordered ", order, "coffee")