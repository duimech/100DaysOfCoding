# This is a Password Generator
# Author: Ray Bolin
# Date: 1/3/2022
# 100DaysOfCoding

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

i = 0
while i < num_letters:
    password += letters[random.randint(0,len(letters) - 1)]
    i += 1

i = 0
while i < num_symbols:
    password += symbols[random.randint(0,len(symbols) - 1)]
    i += 1

i = 0
while i < num_numbers:
    password += numbers[random.randint(0,len(numbers) - 1)]
    i += 1

# Password before random order
#print(password)

# Convert password to a list
pass_list = list(password)
pass_length = len(pass_list)

i = 0
random_pass = ""
while i < pass_length:
    i += 1
    ran_int = random.randint(0, len(pass_list) - 1)
    random_pass += pass_list[ran_int]
    pass_list.pop(ran_int)

print(f"Your password is: {random_pass}")
