# This program is the "higher or lower" game. Two items are given and the user has to guess which item has more popularity based on numbers.   
# Author: Ray Bolin
# Date: 1/13/2022
# 100DaysOfCoding

import random
import game_data

# this is a list of dictionaries from game_data
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },

def intro():
    print("Welcome to Higher or Lower\n")

def get_entry():
    entry = random.choice(game_data.data)
    return entry

def get_new_entry(A_followers):
    num_followers = A_followers
    while num_followers == A_followers:
        new_entry = random.choice(game_data.data)
        num_followers = new_entry['follower_count']

    return new_entry

def print_compare(compareA, compareB):
    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}, {compareA['follower_count']}")
    print("vs")
    print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}, {compareB['follower_count']}")

score = 0
intro()

gameover = False
while gameover == False:

    # Only get account A the first time the game is ran. Account B become account A as game progresses. 
    if score == 0:
        A = get_entry()
        B = get_entry()
    else:
        B = get_entry()

    A_followers = A['follower_count']
    B_followers = B['follower_count']

    # Make sure the same accounts are not chosen.
    if A_followers == B_followers:
        B = get_new_entry(A_followers)
        B_followers = B['follower_count']

    # Show the two accounts to compare.
    print_compare(A,B)
    
    # Get user input.
    user_input = ""
    while user_input != "A" and user_input != "B":
        user_input = input("\nWho has more followers? Type 'A' or 'B':  ")
    
    # Compare the accounts. Make account B account A if B has more followers. 
    if user_input == "A":
        if A_followers > B_followers:
            score += 1 
            print(f"You're right! Current Score: {score} \n")
        else:
            gameover = True
            print(f"You lose. Score: {score} \n")
    else:
        if B_followers > A_followers:
            score += 1 
            print(f"You're right! Current Score: {score} \n")
            A = B
        else:
            gameover = True
            print(f"You lose. Score: {score} \n")



