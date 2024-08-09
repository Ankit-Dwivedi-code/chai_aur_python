# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")

if len(password) < 6:
    print("Your password is weak")
elif len(password) >= 6 and len(password) <= 10:
    print("Your password is medium")
else:
    print("Your password is strong")
