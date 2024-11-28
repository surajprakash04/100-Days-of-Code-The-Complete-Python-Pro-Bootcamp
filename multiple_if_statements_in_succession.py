print("Hi, Welcome to the RollerCoaster Ride")
height = int(input("Please enter your height: "))
bill = 0

if height >= 120:
    print("Congratulations!! You are eligible for the ride.")
    age = int(input("Please enter your age: "))
    if age <=12:
        bill = 5
        print("Children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry! You have to grow taller before you can ride.")
    