# This program converts a word entered into a list of NATO words for each letter in the word.
# Author: Ray Bolin
# Date: 1/29/2022
# 100DaysOfCoding

import pandas

df = pandas.read_csv("100DaysOfCoding/natoConversion/nato_phonetic_alphabet.csv")

# df_dictionary = {}
# for (index,row) in df.iterrows():
#     key = row.letter
#     value = row.code
#     df_dictionary[key] = value

# Go through each row in the DataFrame. Add the columns "letter" and "code" to the new dictionary.
df_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

# Convert the word entered to upper case and make it a list. Make a new list to print containing the nato output.
user_input = list(input("Enter a word:  ").upper())
output = [df_dictionary[letter] for letter in user_input]

# for letter in user_input:
#     output.append(df_dictionary[letter])

print(output)