from random import randint
from art import logo

def check_guess(guess, winning_number):
    if guess == winning_number:
        return "You got it right!"
    diff = abs(guess - winning_number)
    if diff > 10:
        return "Too high guess." if guess > winning_number else "Too low guess."
    if diff > 5:
        return "High guess." if guess > winning_number else "Low guess."
    if diff > 2:
        return "Near high guess." if guess > winning_number else "Near low guess."
    return "Almost there."

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ").lower()

no_of_attempts = 10 if level == 'e' else 5
print(f"You have {no_of_attempts} attempts to guess the number.")

winning_number = randint(1, 100)

while no_of_attempts > 0:
    guess = int(input("Make a guess: "))
    result = check_guess(guess, winning_number)
    print(result)
    if result == "You got it right!":
        break
    no_of_attempts = no_of_attempts - 1
    print(f"You have {no_of_attempts} attempts left.")

if no_of_attempts == 0:
    print(f"Sorry, you've ran out of attempts. The number was {winning_number}.")
