import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissors]

you = int(input("What would you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if you == 0:
    print("You chose: Rock")
    print(images[0])
elif you == 1:
    print("You chose: Paper")
    print(images[1])
elif you == 2:
    print("You chose: Scissors")
    print(images[2])
else:
    print("Wrong Input!")

comp = random.randint(0,2)
if comp == 0:
    print("Computer chose: Rock")
    print(images[0])
elif comp == 1:
    print("Computer chose: Paper")
    print(images[1])
elif comp == 2:
    print("Computer chose: Scissors")
    print(images[2])
else:
    print("Computer mind is disturbed...")

# print(f"Computer chose: {comp}")

if you == 0 and comp == 0:
    print("Its a Draw!")
elif you == 0 and comp == 1:
    print("Computer Wins!")
elif you == 0 and comp == 2:
    print("You Win.. Congratulations!")
elif you == 1 and comp == 0:
    print("You Win.. Congratulations!")
elif you == 1 and comp == 1:
    print("Its a Draw!")
elif you == 1 and comp == 2:
    print("Computer Wins!")
elif you == 2 and comp == 0:
    print("Computer Wins!")
elif you == 2 and comp == 1:
    print("You Win.. Congratulations!")
elif you == 2 and comp == 2:
    print("Its a Draw!")
else:
    print("Computer Wins!")