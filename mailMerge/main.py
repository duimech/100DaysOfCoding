# This program takes a list of names from a file and replaces them in a letter from another file then saves a new file in a new directory.
# Author: Ray Bolin
# Date: 1/27/2022
# 100DaysOfCoding

# Put names in a list without blank lines
with open("100DaysOfCoding/mailMerge/Input/Names/invited_names.txt") as invited_names:
    invited = []
    invited_names = invited_names.readlines()

    for name in invited_names:
        invited.append(name.strip("\n"))

# Make a dictionary with updated greetings for each name
with open("100DaysOfCoding/mailMerge/Input/Letters/starting_letter.txt") as starting_letter:
    greetings = {}
    starting_letter_contents = starting_letter.readlines()

    for name in invited:
        greetings[name] = starting_letter_contents[0].replace("[name]", name)

# Write the greetings and the contents to a file
for key in greetings:
    filename = "100DaysOfCoding/mailMerge/Output/ReadyToSend/letter_for_" + key + ".txt"
    with open(filename, mode="a") as invitation:
        invitation.write(greetings[key])
        for num in range(1, len(starting_letter_contents)):
            invitation.write(starting_letter_contents[num])