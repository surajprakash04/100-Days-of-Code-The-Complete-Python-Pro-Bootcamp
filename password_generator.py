import string
import random

letters = list(string.ascii_lowercase)

# numbers = str([num for num in range(0,10)])
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

random_symbols = string.punctuation
symbols = random.sample(random_symbols, 10)

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like to have in your password: "))
if nr_letters > len(letters):
    print("Please try with smaller number than 27!")
    nr_letters = int(input("How many letters would you like to have in your password: "))    

nr_symbols = int(input("How many symbols would you like to have? [Max: 9] : "))
nr_numbers = int(input("How many numbers would you like to have? [Max: 10] : "))

#Easy Level

your_pass = random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers, nr_numbers)
your_pass_str = ''.join(your_pass)
print("Your " + str(nr_letters+nr_symbols+nr_numbers) + " letters password is : " + your_pass_str)