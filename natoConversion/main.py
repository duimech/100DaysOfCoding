# This program converts a word entered into a list of NATO words for each letter in the word.
# Author: Ray Bolin
# Date: 2/5/2022
# 100DaysOfCoding

import pandas
df = pandas.read_csv("100DaysOfCoding/natoConversion/nato_phonetic_alphabet.csv")

# Go through each row in the DataFrame. Add the columns "letter" and "code" to the new dictionary.
df_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

def convert():
    user_input = list(input("Enter a word:  ").upper())
    # Make a new list to print containing the nato output from the user input.
    try:        
        output = [df_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Only enter letters from the alphabet.")
        convert()
    else:
        print(output)

convert()