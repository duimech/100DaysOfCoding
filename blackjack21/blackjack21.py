# This program is a simulation of the blackjack / 21 game
# Author: Ray Bolin
# Date: 1/9/2022
# 100DaysOfCoding


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os 

def pullcard(turn):
    card = int(cards[random.randint(0,12)])
    total = get_total(turn)

    # Ace can be 11 or 1
    if card == 11:
        if total + 11 > 21:
            card = 1

    # Previous Ace that was 11 now needs to be a 1
    if total + card > 21:
        if turn == "Player":
            for position in player_cards:
                if position == 11:
                    index = player_cards.index(position)
                    player_cards[index] = 1
        else:
            for position in computer_cards:
                if position == 11:
                    index = computer_cards.index(position)
                    computer_cards[index] = 1

    if turn == "Player":
        player_cards.append(card)
    else:
        computer_cards.append(card)

def get_total(turn):
    total = 0
    if turn == "Player":
        for num in player_cards:
            total += num
        return total
    else:
        for num in computer_cards:
            total += num
        return total

def show_cards(turn):
    if turn == "Player":
        print(f"     Your cards: {player_cards} totals {player_total}")
        print(f"     Computer's first card: {computer_cards}")
    else:
        print(f"     Computer's cards: {computer_cards} total {computer_total}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
if play == 'y':
    # Clear screen and show initial cards
    os.system("cls" if os.name == "nt" else "clear")
    player_cards = []
    computer_cards = []
    turn = 'Player'
    another_card = 'y'
    player_total = 0
    computer_total = 0

    pullcard("Player")
    pullcard("Player")
    player_total = get_total("Player")
    pullcard("Computer")
    computer_total = get_total("Computer")

    show_cards(turn)    

    # Player pulls cards
    while another_card == 'y':
        if player_total <= 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass:  ")

        if another_card == 'y':
            pullcard(turn)
            player_total = get_total(turn)
            show_cards(turn)
            if player_total > 21:
                another_card = 'n'

    # Computer pulls cards.
    if player_total <= 21:
        turn = 'Computer'

        while computer_total < 17:
            pullcard(turn)
            computer_total = get_total(turn)
            show_cards(turn)

        if computer_total > 21:
            print("You Win")
        elif computer_total > player_total:
            print("Computer Wins")
        elif computer_total == player_total:
            print("Draw")
        else:
            print("You Win")
    else:
        print("You Lose")