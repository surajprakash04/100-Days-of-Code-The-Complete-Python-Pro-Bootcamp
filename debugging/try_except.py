try:
    age = int(input("How old are you?"))
except ValueError or erro:
    print("Invalid input. Please try again!")
    age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print("You can't drive.")