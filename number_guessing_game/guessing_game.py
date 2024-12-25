import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")

if level == 'e':
    no_of_attempts = 10
elif level == 'h':
    no_of_attempts = 5

print(f"You have {no_of_attempts} attempts to guess the number.")

winning_number = random.randint(1, 100)
print(winning_number)

while no_of_attempts > 0:
    guess = int(input("Make a guess: "))

    too_high = winning_number + 10
    high = winning_number + 5
    near_high = winning_number + 2
    near_low = winning_number - 2
    low = winning_number - 5
    too_low = winning_number - 10

    if guess == winning_number:
        print("You got it right!")
        break
    elif guess > too_high:
        print("Too high guess.")
    elif guess > high:
        print("High guess.")
    elif guess > near_high:
        print("Near high guess.")
    elif guess > near_low:
        print("Almost there.")
    elif guess < too_low:
        print("Too low guess.")
    elif guess < low:
        print("Low guess.")
    elif guess < near_low:
        print("Near low guess.")
    else:
        print("Almost there.")
    no_of_attempts -= 1
    print(f"You have {no_of_attempts} attempts to guess the number.")

if no_of_attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {winning_number}.")
