import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_words = random.choice(word_list)
print(chosen_words)

placeholder = ""
word_length = len(chosen_words)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letter = []

while not game_over:
    print(f"****************************** {lives}/6 LIVES LEFT ******************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_words:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    print("Word to guess: " + display)

    if guess not in chosen_words:
        lives -= 1
        print(f"You've guessed {guess}, that is not the word. You lose a life!")

        if lives == 0:
            game_over = True

            print(f"****************************** It was {chosen_words}. YOU LOSE! ******************************")

    if "_" not in display:
        game_over = True
        print("****************************** YOU WIN!! ******************************")

    print(stages[lives])