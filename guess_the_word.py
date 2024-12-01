# Incomplete Solution

word = "Elephant"
hide_word = ""
for str in word:
    hide_word += (str.replace(str,'_'))
    # print(str.replace(str,'_'))
print("Guess the word: " + hide_word)

user_guess = input("Guess the letter: ")
if user_guess in word:
    print('Good Job! This letter is present in the word')
    guess_word_index = word.index(user_guess)
    hide_word = hide_word[guess_word_index].replace('_',user_guess)

    print(hide_word)
else:
    print("Sorry, This letter is not present. Please try again.")