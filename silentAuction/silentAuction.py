# This program creates a dictionary of bidders/bids for a silent auction then prints the winner. 
# Author: Ray Bolin
# Date: 1/8/2022
# 100DaysOfCoding
 
import os

other_bidders = "yes"
auction = {}

print("Welcome to the secret auction program.")

# Get all the names/bids
while other_bidders == "yes":
    os.system("cls" if os.name == "nt" else "clear")
    name = input("What is your name: ")
    bid = input("What's your bid?:  $")

    auction[name] = bid

    other_bidders = ""
    while other_bidders != "yes" and other_bidders != "no":
        other_bidders = str.lower(input("Are there any other bidders? Type 'yes' or 'no':  "))

# Calculate the winner
highest_bid = 0
highest_bidder = ""

for name in auction:
    value = int(auction[name])

    # If bid is the same a previous bidder then previous bidder wins since value is not greater than the previous bidders value
    if  value > highest_bid:
        highest_bidder = name
        highest_bid = value

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
