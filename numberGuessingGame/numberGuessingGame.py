# This program picks a number and lets you guess it on two separate difficulty levels.
# Author: Ray Bolin
# Date: 1/12/2022
# 100DaysOfCoding

import random

def greeting():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def difficulty():
    gueses = 0
    difficulty = ""

    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = str.lower(input("Choose a difficulty. Type 'easy' or 'hard':  "))

    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5
    
    return guesses

def make_a_guess(guesses):
    guesses_left = guesses
    random_number = random.randint(0,100)
    user_guess = 500

    while guesses_left > 0 and user_guess != random_number:
        print(f"You have {guesses_left} attempts remaining to guess the number.\n")

        user_guess = int(input("Make a guess:  "))

        if user_guess > random_number:
            guesses_left -= 1
            print("Too high.")
        elif user_guess < random_number:
            guesses_left -= 1
            print("Too low.")
        else:
            print("Correct. You win.")
    
    if guesses_left == 0: 
        print("\nYou lose.")
        play_again = ""
        while play_again != "y" and play_again != "n":
            play_again = input("Would you like to play again? Type 'y' or 'n':  ")
        if play_again =="y":
            return True 
        else:
            return False


greeting()
play = True
while play:
    guesses = difficulty()
    play = make_a_guess(guesses)

