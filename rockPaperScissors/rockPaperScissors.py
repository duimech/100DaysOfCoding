# This is the game of rock, paper, scissors
# Author: Ray Bolin
# Date: 1/2/2022
# 100DaysOfCoding

import random

rock = '''
    _______
---'    ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
          _______)
---.__________)
'''

scissors = '''
    _______
---'    ___)____
          ______)
       __________)
      (____)
---.__(___)
'''


# List with the ascii art
ascii_choices = [rock, paper, scissors]

# User goes first
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print(ascii_choices[user_choice])

# Computers turn
comp_choice = random.randint(0,2)

print("Computer chooses: \n")
print(ascii_choices[comp_choice])

if user_choice == comp_choice:
  print("Draw")
elif user_choice == 0 and comp_choice == 1:
  print("You lose")
elif user_choice == 0 and comp_choice == 2:
  print("You win")
elif user_choice == 1 and comp_choice == 0:
  print("You win")
elif user_choice == 1 and comp_choice == 2:
  print("You lose")
elif user_choice == 2 and comp_choice == 0:
  print("You lose")
elif user_choice == 2 and comp_choice == 1:
  print("You win")
