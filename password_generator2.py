import string
import random

letters = list(string.ascii_lowercase)

# numbers = str([num for num in range(0,10)])
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

random_symbols = string.punctuation
symbols = random.sample(random_symbols, 10)

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like to have in your password: "))
nr_symbols = int(input("How many symbols would you like to have? [Max: 9] : "))
nr_numbers = int(input("How many numbers would you like to have? [Max: 10] : "))

#Easy Level

# your_pass = ""
# for char in range(0, nr_letters):
#     your_pass += random.choice(letters)

# for char in range(0, nr_symbols):
#     your_pass += random.choice(symbols)

# for char in range(0, nr_numbers):
#     your_pass += random.choice(numbers)

# print(your_pass)

# Hard level

pass_list = []
for char in range(0,nr_letters):
    pass_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    pass_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    pass_list.append(random.choice(numbers))

print(pass_list)
random.shuffle(pass_list)
print(pass_list)

password = ""
for char in pass_list:
    password += char

print(password)