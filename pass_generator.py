# Name: Password Generator
# Author: Richard F Silva

import random
import string


letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("###### Welcome to the Password Generator! ######\n")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, num_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
