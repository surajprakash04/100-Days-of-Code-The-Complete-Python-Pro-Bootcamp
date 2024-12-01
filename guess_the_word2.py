import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["surajp", "abhina", "ajeetk", "amitku"]
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guessed = 1
guessed_letters = []
while guessed == 1:
    guess = input("Guess a letter: ").lower()
    # print(guess)
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessed_letters.append(guess)
            # print("Correct!")
            # guessed = 1
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"
            # print("Incorrect!")
            # guessed = 0
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            guessed = 0
            print("You Lose!")

    if "_" not in display:
        guessed = 0
        print("You Won!")

    print(stages[lives])
# print(guessed_letters)
