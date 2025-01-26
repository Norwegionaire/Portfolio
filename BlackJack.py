# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:42:10 2024

@author: engeb
"""

import random

#simplified suggestion made by chatgpt
def deck():
    suits = ["s", "c", "h", "d"]
    values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, 
             "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}
    return {f"{value}{suit}": values[value] for value in values for suit in suits}


def blackjack():
    value_d = 0
    value_p = 0
    clean_deck = deck()
    
    #to make sure that the aces after 
    aces_p = 0
    aces_d = 0
    #player
    print("Player turn")
    
    for _ in range(2):
        card1_p = random.choice(list(clean_deck))
        value_p += clean_deck[card1_p]
        print(card1_p)
        del clean_deck[card1_p]
    
    print("You now have", value_p)
    while value_p < 21:
        if value_p >= 21:
            break
        choice_p = input("Would you like to hit?[y/n]: ")
        if choice_p != "y":
            break
        else:
            card2_p = random.choice(list(clean_deck))
            if value_p >= 11:
                clean_deck["As"] = 1
                clean_deck["Ac"] = 1
                clean_deck["Ah"] = 1
                clean_deck["Ad"] = 1
            print(card2_p)
            value_p += clean_deck[card2_p]
            print(value_p)
            del clean_deck[card2_p]
    #dealers turn
    print("Dealer Turn")
    for _ in range(2):
        card1_d = random.choice(list(clean_deck))
        value_d += clean_deck[card1_d]
        print(card1_d)
        del clean_deck[card1_d]
    
    print("Dealer has", value_d)
    
    while value_d > 21 and dealer_aces > 0:
        value_d -= 10
        dealer_aces -= 1
    
    while value_d < 17:
        if value_d >= 17 or value_p > 21:
            break
        else:
            card2_d = random.choice(list(clean_deck))
            print(card2_d)
            value_d += clean_deck[card2_d]
            print(value_d)
            del clean_deck[card2_d]

    print("Player:", value_p)
    print("Dealer:", value_d)
    if value_p <= 21 and value_p > value_d or value_d > 21 :
        print("Player wins")
    elif value_p == value_d:
        print("Draw")
    else:
        print("Player loses")

blackjack()
    