# This project is the hangman game
# Author: Ray Bolin
# Date: 1/6/2022
# 100DaysOfCoding

import random
import hangman_art
import hangman_words

print(hangman_art.logo)

# Get a random word from the word list
word = random.choice(hangman_words.word_list)
display = []
guessed = []
wordlength = len(word)
end_of_game = False
wrong_guesses = 6


# Set the display to show blanks for each letter
for _ in range(wordlength):
    display.append("_")

print(word)

while end_of_game == False:

    print(hangman_art.stages[wrong_guesses])
    print(" ".join(display))

    guess = ""
    while guess == "":
        guess = input("Guess a letter: ")

        if guess not in guessed:
            guessed.append(guess)
        else:
            print(f"You already guessed {guess}")
            guess = ""

    
    for position in range(wordlength):
        if guess == word[position]:
            display[position] = guess
            

    if guess not in display:
        wrong_guesses -= 1
        print(f"The letter {guess} is not in the word")
        if wrong_guesses == 0:
            print(hangman_art.stages[wrong_guesses])
            print(f"The word was: {word}")
            print("You Lose")
            end_of_game = True

        
    if "_" not in display:
        print(hangman_art.stages[wrong_guesses])
        print(" ".join(display))
        print("You Win")
        end_of_game = True

    

