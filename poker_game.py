#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:53:20 2019

@author: gracepetrosini
"""

#%%
import sys
import random

playeramount = int(sys.argv[1])

print(playeramount)

class PokerGame:
    
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players #this is a class attribute
        self.namelist = []
        self.hand = []
        
    def names(self):
        for i in range(self.number_of_players):
            self.namelist.append(input("What is your name?"))
        print(self.namelist)

    def dealer(self):
        print("calling dealer method")
        self.card_choices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for player in self.namelist:
            self.hand = []
            for value in range(5):
                self.hand.append(random.choice(self.card_choices))
            print(player + ": " + " ".join(str(self.hand)))
        sort.self.hand
        #hand__gt__ index[4]
        
                
        
game1 = PokerGame(playeramount)
game1.names()
game1.dealer()

