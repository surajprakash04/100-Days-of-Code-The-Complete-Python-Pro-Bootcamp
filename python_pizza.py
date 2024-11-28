print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pep = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You typed the wrong inputs.")

if pep == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 1

print(f"Your final bill is : ${bill}.")